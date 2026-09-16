# Prompt for the Coarse Docker review service

Copy this whole file into the **Coarse** project (or paste it as the first message there). Implement it there. Do **not** put this service in the Research Agent Kit. Do **not** edit RAK from Coarse.

The client is any assistant that can send HTTP. One client is the Research Agent Kit (`review_service` in a paper’s folder map). The service must not assume Cursor, Claude Code, Codex, or RAK.

---

You are implementing a **small HTTP service** that wraps the existing Coarse / `coarse-ink` review pipeline and exposes **exactly** the contract below. Run it as a **Docker container**.

## Goal

A container that:

1. Accepts a manuscript (`path` on a mounted volume, or an upload).
2. Starts a Coarse review **in the background** and returns a `review_id` immediately.
3. Lets the client poll until `complete` or `failed`.
4. Returns structured comments plus the full markdown report.

A full review takes about 10–25 minutes. The HTTP start call must not wait for that.

## Use Coarse as a library, not as a host CLI

Inside Docker, call the Python API (or the non-interactive CLI with confirmation skipped):

```python
from coarse import review_paper
from pathlib import Path

review, markdown, paper_text = review_paper(pdf_path=Path("paper.pdf"), ...)
```

Package: `coarse-ink` on PyPI (import name `coarse`). Pin a version (1.9.x or newer). Python 3.12+.

**Default LLM path in the container:** provider keys (`OPENROUTER_API_KEY` is enough). This image must run **non-interactively**.

**Skip the cost prompt.** Coarse prints `Proceed with estimated cost $X? [Y/n]:` and waits. In Docker nobody can type `Y`, so the review dies after OCR with `review pipeline failed`. You **must** disable that prompt on every run:

- CLI: `coarse-ink review … --yes` (or the documented skip-confirm flag)
- Python: the `review_paper(…)` argument that skips confirmation (often `yes=True` / `skip_confirm=True` — use whatever this `coarse-ink` version actually exports; if unsure, read the function signature)
- Also set `stdin` to `/dev/null` (or `DEVNULL`) so a missed flag cannot hang on the prompt

A log line that contains `Proceed with estimated cost` is a **bug in this service**, not a client error. Do not mark the review `complete` until the pipeline has finished without that prompt.

**Do not** use `claude -p`, `codex exec`, or `gemini -p` as the default backend. Those need a logged-in desktop CLI and will not work for a hosted container. A later optional extra may mount a host CLI; it is out of scope for v1.

Non-PDF sources extract locally. PDFs still need OpenRouter for OCR unless the client sends pre-extracted markdown.

## HTTP contract (do not invent extra client operations)

Listen on `0.0.0.0:8787` (map host `8787:8787`). JSON only. UTF-8.

If `REVIEW_SERVICE_TOKEN` is set, every route except `GET /health` requires:

```
Authorization: Bearer <REVIEW_SERVICE_TOKEN>
```

Mismatch → `401`. If the token env is **unset**, bind only to `127.0.0.1` (local docker-compose default) and log a warning. Never log the token.

### `GET /health`

No auth. `{ "ok": true }`. For Docker healthchecks only. RAK will not call this.

### `POST /reviews` → `review_start`

Return **immediately** (`200` or `202`) with:

```json
{ "review_id": "<uuid>", "status": "queued" }
```

Then run the pipeline on a worker. Status becomes `running`, then `complete` or `failed`.

Request body:

```json
{
  "channel": "local_api | hosted_api",
  "filename": "paper.pdf",
  "media_type": "application/pdf",
  "path": "/absolute/or/windows/path",
  "content_base64": null
}
```

Rules:

- `hosted_api`: `content_base64` required. Decode to a working file named from `filename` (sanitize). Ignore `path`.
- `local_api`: `path` required. Resolve it to a file the container can read (see **Path mapping**). If the file is missing, `400` with a short error telling the client to upload (`hosted_api`) instead. Do not scan the host filesystem.
- Supported files: PDF, Markdown, TeX, TXT, DOCX, HTML, EPUB (whatever `review_paper` already accepts).
- Reject empty bodies, missing filename, and oversized uploads (cap, e.g. 50 MB).

Do **not** keep this request open until the review finishes.

### `GET /reviews/{id}` → `review_status`

```json
{
  "review_id": "<uuid>",
  "status": "queued | running | complete | failed",
  "error": null
}
```

Unknown id → `404`. On failure, `error` is a short string (no stack traces, no keys).

### `GET /reviews/{id}/result` → `review_result`

Only when `status` is `complete`. Otherwise `409` with the status payload.

```json
{
  "review_id": "<uuid>",
  "status": "complete",
  "recommendation": "accept | minor_revision | major_revision | reject | other",
  "summary": "short overall feedback",
  "comments": [
    {
      "id": "1",
      "quote": "verbatim from the paper",
      "body": "actionable feedback",
      "section": "optional",
      "severity": "major | minor | editorial | other"
    }
  ],
  "markdown": "# full coarse report ..."
}
```

Map Coarse’s structured `Review` into `comments` (`id`, quote, feedback → `body`, section if present). Map recommendation language:

| Coarse wording | `recommendation` |
|---|---|
| accept | `accept` |
| minor revision | `minor_revision` |
| major revision / revise and resubmit | `major_revision` |
| reject | `reject` |
| anything else | `other` |

`summary` = overall feedback, truncated if huge; full text stays in `markdown`.

If Coarse returns markdown but no structured comments, still return `markdown` and an empty `comments` list. Do not fail the review for that.

## Path mapping (Docker `local_api`)

Windows host paths (`C:\Users\...`) are not Linux container paths.

Env (optional):

```
REVIEW_SERVICE_HOST_ROOT=C:\Users\juuso
REVIEW_SERVICE_CONTAINER_ROOT=/host
```

Replace the host prefix with the container prefix. Example compose mount:

```yaml
volumes:
  - C:/Users/juuso:/host
```

If mapping is unset and `path` is not readable inside the container, `400` and tell the client to use `hosted_api` (upload). **Prefer upload for Docker and for any hosted deployment.** `local_api` is a convenience when the same tree is mounted.

Working files and results live under `/data` in the container (named volume or bind). Persist `review_id` → status + result so a container restart can still answer polls for in-flight or finished jobs if you already wrote the result; v1 may drop in-flight jobs on restart (document that).

## Docker deliverables

In the Coarse project (not RAK):

- `Dockerfile` — Python 3.12, `coarse-ink`, this HTTP app, non-root user.
- `compose.yaml` — service `review-service`, port `8787:8787`, env from `.env`, volume `./data:/data`.
- `.env.example` — `REVIEW_SERVICE_TOKEN=`, `OPENROUTER_API_KEY=`, optional `COARSE_MODEL=`, optional path-mapping vars. No real secrets.
- `.dockerignore`
- Short `README` in that project: how to `docker compose up --build`, how to curl start/poll/result, that RAK points `review_service.base_url` at `http://127.0.0.1:8787` with `channel: hosted_api` (upload) unless they set up path mapping.

Example local run:

```bash
docker compose up --build
```

Example RAK folder map (paper, not this container):

```yaml
review_service:
  enabled: true
  channel: hosted_api
  base_url: http://127.0.0.1:8787
  token_env: REVIEW_SERVICE_TOKEN
  capabilities:
    review_start: POST /reviews
    review_status: GET /reviews/{id}
    review_result: GET /reviews/{id}/result
```

Same image later: put it on a URL, keep `hosted_api`, require `REVIEW_SERVICE_TOKEN`. Do not mount researchers’ disks on a public host.

## Concurrency and runtime

- v1: one review **running** at a time is fine. Further `POST /reviews` may return `status: queued` and wait their turn. Do not reject a second start unless you must (disk/memory).
- Cap wall time (e.g. 60 minutes) then `failed`.
- If `review_paper` raises, mark `failed` with a short error.
- Do not start a duplicate worker because the client polls again. Poll is read-only.

## Must not

- Block `POST /reviews` until Coarse finishes
- Require RAK, Cursor, Claude Code, or a desktop CLI login
- Put API keys in the image, in git, or in response bodies
- Echo `REVIEW_SERVICE_TOKEN` or provider keys in logs
- Expose Coarse’s interactive CLI, web UI, or extra REST surface as something RAK should call (internal extras are fine if undocumented for the client)
- Treat the report as an audit or as an approved scientific result
- Wait on `Proceed with estimated cost` (or any other interactive prompt)
- Fetch papers from arbitrary URLs in v1 (no SSRF). Only `path` (mapped) or `content_base64`

## Done when

1. `docker compose up --build` serves `/health`.
2. `POST /reviews` with a small markdown upload returns a `review_id` in under two seconds.
3. Polling `/reviews/{id}` moves `queued` → `running` → `complete` (or `failed`).
4. `/reviews/{id}/result` has `markdown` and, when Coarse provides them, `comments`.
5. Wrong bearer token → `401`.
6. README in the Coarse project explains env vars and the RAK `base_url`.

Implement now. Pin `coarse-ink`. Keep the HTTP layer thin.
