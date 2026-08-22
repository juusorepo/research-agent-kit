# Local Stata run helper (Windows first).
# Rewrite for the Research Agent Kit. Not a job queue and not a copy of another project's runner.
# Does not change analysis code, data, the plan, or result files. Updates only the named sidecar's
# technical provenance fields. Never sets status: approved.

param(
    [Parameter(Mandatory = $true)]
    [string]$DoFile,

    [Parameter(Mandatory = $true)]
    [string]$SidecarPath,

    [string]$LogPath = "",

    [string]$WorkDir = "",

    [string]$StataBin = ""
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Resolve-WorkDir([string]$dir) {
    if ([string]::IsNullOrWhiteSpace($dir)) {
        return (Get-Location).Path
    }
    return (Resolve-Path -LiteralPath $dir).Path
}

function Read-StataBinFromYaml([string]$path) {
    if (-not (Test-Path -LiteralPath $path)) {
        return ""
    }
    foreach ($line in Get-Content -LiteralPath $path) {
        if ($line -match '^\s*stata_bin:\s*(.*)\s*$') {
            $raw = $Matches[1].Trim().Trim('"').Trim("'")
            return $raw
        }
    }
    return ""
}

function Resolve-StataBin([string]$workDir, [string]$override) {
    if (-not [string]::IsNullOrWhiteSpace($override)) {
        return $override.Trim()
    }
    if (-not [string]::IsNullOrWhiteSpace($env:STATA_BIN)) {
        return $env:STATA_BIN.Trim()
    }
    foreach ($rel in @("stata_bin.local.yml", (Join-Path "02-scripts" "stata_bin.local.yml"))) {
        $candidate = Join-Path $workDir $rel
        $fromFile = Read-StataBinFromYaml $candidate
        if (-not [string]::IsNullOrWhiteSpace($fromFile)) {
            return $fromFile
        }
    }
    return ""
}

function Get-ScriptsDir([string]$workDir) {
    $rel = "02-scripts"
    $layout = Join-Path $workDir "layout.yml"
    if (Test-Path -LiteralPath $layout) {
        $inPaths = $false
        foreach ($line in Get-Content -LiteralPath $layout) {
            if ($line -match '^\s*paths:\s*$') {
                $inPaths = $true
                continue
            }
            if ($inPaths) {
                if ($line -match '^\S') {
                    break
                }
                if ($line -match '^\s*scripts:\s*(.+)\s*$') {
                    $rel = $Matches[1].Trim().Trim('"').Trim("'")
                    break
                }
            }
        }
    }
    return [System.IO.Path]::GetFullPath((Join-Path $workDir $rel))
}

function Test-PathIsUnder([string]$child, [string]$parent) {
    $childFull = [System.IO.Path]::GetFullPath($child).TrimEnd('\', '/')
    $parentFull = [System.IO.Path]::GetFullPath($parent).TrimEnd('\', '/')
    if ([string]::Equals($childFull, $parentFull, [System.StringComparison]::OrdinalIgnoreCase)) {
        return $true
    }
    $prefix = $parentFull + [System.IO.Path]::DirectorySeparatorChar
    return $childFull.StartsWith($prefix, [System.StringComparison]::OrdinalIgnoreCase)
}

function Get-Sha256Lower([string]$path) {
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try {
        $stream = [System.IO.File]::OpenRead($path)
        try {
            $bytes = $sha.ComputeHash($stream)
            return (([System.BitConverter]::ToString($bytes)) -replace '-', '').ToLowerInvariant()
        }
        finally {
            $stream.Dispose()
        }
    }
    finally {
        $sha.Dispose()
    }
}

function Get-LogStatus([string]$path) {
    if (-not (Test-Path -LiteralPath $path)) {
        return "failed"
    }
    $text = Get-Content -LiteralPath $path -Raw -ErrorAction SilentlyContinue
    if ([string]::IsNullOrWhiteSpace($text)) {
        return "failed"
    }
    if ($text -match '(?m)^r\(\d+\);') {
        return "failed"
    }
    if ($text -match 'end of do-file') {
        return "completed"
    }
    return "failed"
}

function Get-StataVersionFromLog([string]$path) {
    if (-not (Test-Path -LiteralPath $path)) {
        return ""
    }
    $text = Get-Content -LiteralPath $path -Raw -ErrorAction SilentlyContinue
    if ([string]::IsNullOrWhiteSpace($text)) {
        return ""
    }
    if ($text -match 'Stata/(?:MP|SE|BE|IC)\s+[0-9]+(?:\.[0-9]+)*') {
        return $Matches[0].Trim()
    }
    if ($text -match '(?im)^[ \t]*Version:\s*([0-9]+(?:\.[0-9]+)*)') {
        return $Matches[1].Trim()
    }
    return ""
}

function Format-YamlScalar([string]$value) {
    if ($null -eq $value) {
        $value = ""
    }
    $escaped = $value.Replace("'", "''")
    return "'" + $escaped + "'"
}

function Update-SidecarProvenance {
    param(
        [string]$Path,
        [hashtable]$Fields
    )
    $protected = @('status', 'approved_by', 'approved_at')
    $lines = New-Object System.Collections.Generic.List[string]
    if (Test-Path -LiteralPath $Path) {
        foreach ($line in Get-Content -LiteralPath $Path) {
            [void]$lines.Add($line)
        }
    }
    $found = @{}
    for ($i = 0; $i -lt $lines.Count; $i++) {
        if ($lines[$i] -match '^(?<indent>\s*)(?<key>[A-Za-z0-9_]+)\s*:') {
            $key = $Matches.key
            if ($Fields.ContainsKey($key) -and ($protected -notcontains $key)) {
                $lines[$i] = '{0}{1}: {2}' -f $Matches.indent, $key, (Format-YamlScalar ([string]$Fields[$key]))
                $found[$key] = $true
            }
        }
    }
    foreach ($key in $Fields.Keys) {
        if (-not $found.ContainsKey($key) -and ($protected -notcontains $key)) {
            [void]$lines.Add(('{0}: {1}' -f $key, (Format-YamlScalar ([string]$Fields[$key]))))
        }
    }
    $hasStatus = $false
    foreach ($line in $lines) {
        if ($line -match '^\s*status\s*:') {
            $hasStatus = $true
            break
        }
    }
    if (-not $hasStatus) {
        $lines.Insert(0, 'status: provisional')
    }
    [System.IO.File]::WriteAllLines($Path, $lines.ToArray())
}

function Write-Report {
    param(
        [string]$Bin,
        [string]$Command,
        [string]$Do,
        [string]$Hash,
        [string]$Started,
        [string]$Ended,
        [string]$Exit,
        [string]$Status,
        [string]$Log,
        [string]$Version
    )
    Write-Output "stata_bin=$Bin"
    Write-Output "command=$Command"
    Write-Output "do_file=$Do"
    Write-Output "script_hash=$Hash"
    Write-Output "started_at=$Started"
    Write-Output "ended_at=$Ended"
    Write-Output "exit_code=$Exit"
    Write-Output "run_status=$Status"
    Write-Output "log_path=$Log"
    Write-Output "stata_version=$Version"
}

$workDir = Resolve-WorkDir $WorkDir
$scriptsDir = Get-ScriptsDir $workDir

if (-not [System.IO.Path]::IsPathRooted($DoFile)) {
    $DoFile = Join-Path $workDir $DoFile
}
$DoFile = [System.IO.Path]::GetFullPath($DoFile)

if (-not [System.IO.Path]::IsPathRooted($SidecarPath)) {
    $SidecarPath = Join-Path $workDir $SidecarPath
}
$SidecarPath = [System.IO.Path]::GetFullPath($SidecarPath)

$extension = [System.IO.Path]::GetExtension($DoFile)
if ([string]::IsNullOrWhiteSpace($extension) -or -not $extension.Equals('.do', [System.StringComparison]::OrdinalIgnoreCase)) {
    Write-Error "Do-file must be a .do script: $DoFile"
    exit 1
}
if (-not (Test-Path -LiteralPath $DoFile)) {
    Write-Error "Do-file not found: $DoFile"
    exit 1
}
if (-not (Test-PathIsUnder -child $DoFile -parent $scriptsDir)) {
    Write-Error "Do-file must live under the project scripts path ($scriptsDir): $DoFile"
    exit 1
}
if (-not (Test-Path -LiteralPath $SidecarPath)) {
    Write-Error "Named output sidecar is required before a run and was not found: $SidecarPath"
    exit 1
}

if ([string]::IsNullOrWhiteSpace($LogPath)) {
    $stem = [System.IO.Path]::GetFileNameWithoutExtension($DoFile)
    $LogPath = Join-Path $scriptsDir "logs\$stem.log"
}
elseif (-not [System.IO.Path]::IsPathRooted($LogPath)) {
    $LogPath = Join-Path $workDir $LogPath
}
$LogPath = [System.IO.Path]::GetFullPath($LogPath)
$logParent = [System.IO.Path]::GetDirectoryName($LogPath)
if (-not [string]::IsNullOrWhiteSpace($logParent) -and -not (Test-Path -LiteralPath $logParent)) {
    New-Item -ItemType Directory -Path $logParent | Out-Null
}

$bin = Resolve-StataBin -workDir $workDir -override $StataBin
if ([string]::IsNullOrWhiteSpace($bin) -or -not (Test-Path -LiteralPath $bin)) {
    Write-Error @"
No Stata executable configured.
Set STATA_BIN to the full path, or add stata_bin.local.yml in the paper folder (see templates/analysis/stata/stata_bin.local.yml.example).
Do not assume an install path.
"@
    exit 1
}

$scriptHash = Get-Sha256Lower $DoFile
$startedAt = [DateTime]::UtcNow.ToString("yyyy-MM-ddTHH:mm:ssZ")

$isWindows = ($env:OS -eq "Windows_NT")
if ($isWindows) {
    $argList = @("/e", "do", "`"$DoFile`"")
}
else {
    $argList = @("-b", "do", $DoFile)
}

$command = "$bin $($argList -join ' ')"
$exitCode = 1
Push-Location $workDir
try {
    $proc = Start-Process -FilePath $bin -ArgumentList $argList -WorkingDirectory $workDir -Wait -PassThru -NoNewWindow
    if ($null -eq $proc.ExitCode) {
        $exitCode = 1
    }
    else {
        $exitCode = [int]$proc.ExitCode
    }
}
finally {
    Pop-Location
}

$endedAt = [DateTime]::UtcNow.ToString("yyyy-MM-ddTHH:mm:ssZ")
$stataVersion = Get-StataVersionFromLog $LogPath
$logStatus = Get-LogStatus $LogPath
if ($exitCode -ne 0) {
    $runStatus = "failed"
}
elseif ($logStatus -ne "completed") {
    $runStatus = "failed"
}
else {
    $runStatus = "completed"
}

Write-Report -Bin $bin -Command $command -Do $DoFile -Hash $scriptHash -Started $startedAt -Ended $endedAt -Exit "$exitCode" -Status $runStatus -Log $LogPath -Version $stataVersion

Update-SidecarProvenance -Path $SidecarPath -Fields @{
    command        = $command
    script_hash    = $scriptHash
    started_at     = $startedAt
    ended_at       = $endedAt
    run_status     = $runStatus
    log_path       = $LogPath
    stata_version  = $stataVersion
}

if ($runStatus -ne "completed") {
    exit 1
}
exit 0
