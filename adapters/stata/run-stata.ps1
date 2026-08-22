# Local Stata run helper (Windows first).
# Rewrite for the Research Agent Kit. Not a job queue and not a copy of another project's runner.

param(
    [Parameter(Mandatory = $true)]
    [string]$DoFile,

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

function Get-LogStatus([string]$logPath) {
    if (-not (Test-Path -LiteralPath $logPath)) {
        return "failed"
    }
    $text = Get-Content -LiteralPath $logPath -Raw -ErrorAction SilentlyContinue
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

$workDir = Resolve-WorkDir $WorkDir
if (-not [System.IO.Path]::IsPathRooted($DoFile)) {
    $DoFile = Join-Path $workDir $DoFile
}
if (-not (Test-Path -LiteralPath $DoFile)) {
    Write-Error "Do-file not found: $DoFile"
    exit 1
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

$stem = [System.IO.Path]::GetFileNameWithoutExtension($DoFile)
$logDir = Join-Path $workDir "02-scripts\logs"
if (-not (Test-Path -LiteralPath $logDir)) {
    New-Item -ItemType Directory -Path $logDir | Out-Null
}
$preferredLog = Join-Path $logDir "$stem.log"
$cwdLog = Join-Path $workDir "$stem.log"

$isWindows = ($env:OS -eq "Windows_NT")
if ($isWindows) {
    $argList = @("/e", "do", "`"$DoFile`"")
}
else {
    $argList = @("-b", "do", $DoFile)
}

$command = "$bin $($argList -join ' ')"
Push-Location $workDir
try {
    $proc = Start-Process -FilePath $bin -ArgumentList $argList -WorkingDirectory $workDir -Wait -PassThru -NoNewWindow
    $exitCode = $proc.ExitCode
}
finally {
    Pop-Location
}

$logPath = $preferredLog
if (-not (Test-Path -LiteralPath $logPath) -and (Test-Path -LiteralPath $cwdLog)) {
    $logPath = $cwdLog
}

$runStatus = Get-LogStatus $logPath
if ($runStatus -ne "completed") {
    $runStatus = "failed"
}

Write-Output "stata_bin=$bin"
Write-Output "command=$command"
Write-Output "do_file=$DoFile"
Write-Output "log_path=$logPath"
Write-Output "run_status=$runStatus"
Write-Output "exit_code=$exitCode"

if ($runStatus -ne "completed") {
    exit 1
}
exit 0
