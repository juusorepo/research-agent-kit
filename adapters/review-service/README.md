# Manuscript review service (optional)

Tool setup only. Research rules live in `skills/review-the-manuscript/SKILL.md`. Do **not** copy this folder into a paper.

The kit talks to a review service only through the **operations** below. That contract is the product. One implementation is Coarse, on this computer or hosted later. The kit does **not** depend on one vendor command line, one model host, or one assistant product.

A review from this service is a **proposal**. It is not an audit of the research chain, not an approved result, and not a certificate.

## Now vs later

**Now (this version):** the same three operations against a **base URL** this paper names. `local_api` means the service can read a file path on this computer. `hosted_api` means the assistant uploads the named manuscript. Findings land in the contributions inbox.

**Later:** the same operations at a hosted URL for researchers who do not run a local service. Auth and quota stay with that host. The kit still only starts, polls, and fetches.

The review pipeline itself is **not** in this kit. Run it where that software lives; point this paper’s folder map at the URL.

To stand Coarse up as a container, copy [`coarse-docker-prompt.md`](coarse-docker-prompt.md) into the Coarse project (or paste it as the first message there) and implement it **there**.

## What RAK knows (operations)

Skills request **only** these. HTTP paths default as in `api-contract.yml`. Override them in `layout.yml` when a host uses other paths.

| Operation | For |
|---|---|
| `review_start` | Begin a review of the named manuscript. Must return a `review_id` before the review finishes. |
| `review_status` | Poll until `complete` or `failed`. |
| `review_result` | Fetch the report (`markdown` plus structured `comments` when the service provides them). |

## Explicit mapping (do not guess)

Read `review_service` in this paper’s `layout.yml` (see the commented block in the paper skeleton).

- `base_url` is required to call the service. Do not invent a host.
- `channel` is `local_api` or `hosted_api`.
- `capabilities` values are `METHOD /path` (for example `POST /reviews`). Replace `{id}` with the `review_id`. A host prefix on the same path is the same operation.
- If they asked for an external review (or **coarse-review**) but `base_url` is missing: **stop once**, ask them to set it. Do not guess. Until it is set, **Review the manuscript** is the assistant’s own reading.
- Do not call leftover vendor routes (studio, billing, model lists, raw pipeline steps).

## Channels

| Channel | When |
|---|---|
| *(none)* | Default. The assistant reads the manuscript itself. |
| `local_api` | This paper names a base URL. `review_start` sends a **path** the service can read. Do not upload the file unless the service rejects path. |
| `hosted_api` | This paper names a base URL. `review_start` **uploads** the named manuscript. The file leaves this machine. |

Classification when a channel is in use:

- provider: whatever implements this contract (Coarse is one)
- channel: `local_api` or `hosted_api`
- stability: experimental
- data_sensitivity: **non-restricted manuscripts only**

## When the assistant may send a manuscript

Read this paper’s `policies/what-is-on.md`, `policies/data-policy.md`, and `layout.yml` (`review_service` if present).

- **Restricted or confidential files:** do not send. Do not send row-level data, path-config that points at restricted data, or a manuscript that embeds those extracts.
- **Optional tick** “External manuscript review”: if ticked, `base_url` is set, and they asked **Review the manuscript** (full pass, not a prose scan), the assistant may call the three operations. Asking **coarse-review**, **external review**, or to use this paper’s review service **in this chat** is enough even if the box is off: do not ask for a second authorization.
- If the tick is off and they did not ask for an external review: do not call the service.
- **Scan for generic prose** / **Plain-language review:** never call the service.
- Tokens live in the environment named by `token_env` when that key is set (the commented folder map uses `REVIEW_SERVICE_TOKEN` as an example). Do not put secrets in `layout.yml` or in chat.

## What the skills need

| Skill | Role |
|---|---|
| Review the manuscript | Start, poll, fetch; split comments into inbox files; keep the full report beside them. Kit checks (tables/figures list, intellectual continuity) still run locally. |
| Contribute to the project | One file per atomic comment; `source: ai-review`; `external_id` so a later run does not duplicate |

## Must not

- Pin the kit to one vendor command line or one assistant product
- Hold `review_start` open until the review finishes
- Start a second review of the same file in this run unless they asked
- Treat the report as an independent audit or an approved result
- Send restricted or confidential files
- Store tokens in the paper folder
- Edit the manuscript in the review run
