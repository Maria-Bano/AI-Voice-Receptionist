# Demo & Portfolio Asset Checklist

> Track screenshots, videos, and GIFs for the AI Voice Receptionist portfolio repository.  
> All assets must be **sanitized** — no credentials, webhook URLs, customer data, or proprietary prompts.

**Related:** [README](../README.md) · [assets/README.md](../assets/README.md)

---

## Status Legend

| Symbol | Meaning |
|--------|---------|
| ⬜ | Not started |
| 🔄 | In progress |
| ✅ | Complete |
| 🔒 | Intentionally excluded (proprietary) |

---

## Screenshots

### Vapi Dashboard (Sanitized)

| # | Asset | Filename | Status | Notes |
|---|-------|----------|--------|-------|
| 1 | Agent overview — name, status, high-level config | `screenshots/vapi-agent-overview.png` | ⬜ | Blur or crop any API keys, assistant IDs, or account details |
| 2 | Tool configuration view (sanitized) | `screenshots/vapi-tools-overview.png` | ⬜ | Show tool names and structure only — no endpoint URLs or secrets |
| 3 | Call log / conversation summary (redacted) | `screenshots/vapi-call-summary.png` | ⬜ | Redact guest PII, phone numbers, and transcript content |

**Sanitization checklist before publish:**

- [ ] No API keys or tokens visible
- [ ] No webhook URLs visible
- [ ] No real guest names, phone numbers, or emails
- [ ] No proprietary prompt text visible
- [ ] No account-specific identifiers that could be misused

---

### n8n Workflow Screenshots (Sanitized)

| # | Asset | Filename | Status | Notes |
|---|-------|----------|--------|-------|
| 4 | High-level workflow canvas (overview) | `screenshots/n8n-workflow-overview.png` | ⬜ | Show node structure and flow — not credential panels |
| 5 | Booking workflow segment | `screenshots/n8n-booking-flow.png` | ⬜ | Crop credential and HTTP header configuration |
| 6 | Integration node example (sanitized) | `screenshots/n8n-integration-node.png` | ⬜ | Replace real URLs with `[REDACTED]` if visible |

**Important:** Do **not** export or commit production n8n workflow JSON. Screenshots only.

**Sanitization checklist before publish:**

- [ ] No credential fields visible in any node
- [ ] No webhook URLs or API endpoints with tokens
- [ ] No real customer or reservation data in node previews
- [ ] Workflow JSON files are NOT committed to the repository

---

### Google Sheets Inventory View

| # | Asset | Filename | Status | Notes |
|---|-------|----------|--------|-------|
| 7 | Room inventory sheet (sample data) | `screenshots/sheets-inventory.png` | ⬜ | Use fictional room types, dates, and guest names |
| 8 | Reservation log (sample data) | `screenshots/sheets-reservations.png` | ⬜ | No real guest PII |
| 9 | Availability columns / status view | `screenshots/sheets-availability.png` | ⬜ | Demonstrate structure, not live production data |

**Sanitization checklist before publish:**

- [ ] All data is fictional or anonymized
- [ ] No service account emails or sharing links visible
- [ ] No links to live production spreadsheets

---

### Architecture Diagrams

| # | Asset | Filename | Status | Notes |
|---|-------|----------|--------|-------|
| 10 | High-level architecture (rendered) | `assets/architecture-overview.png` | ⬜ | Export from Mermaid or design tool |
| 11 | Booking sequence diagram (rendered) | `screenshots/diagram-booking-sequence.png` | ⬜ | Optional — Mermaid in docs may suffice |
| 12 | RAG workflow diagram (rendered) | `screenshots/diagram-rag-workflow.png` | ⬜ | Optional |
| 13 | Data flow diagram (rendered) | `screenshots/diagram-data-flow.png` | ⬜ | Optional |

**Source:** Diagrams are defined in [docs/architecture.md](architecture.md). Export PNGs for README banner and social preview use.

---

## Videos

### End-to-End Walkthrough

| # | Asset | Filename | Status | Notes |
|---|-------|----------|--------|-------|
| 14 | Full system demo (voice → availability → booking) | `demo/AI-Voice-Receptionist-Demo.mp4` | ✅ | ~37 MB; in-repo; optional YouTube/Loom for external sharing |
| 15 | Demo thumbnail | `assets/demo-thumbnail.png` | ⬜ | Used for video embed and README |

**Content outline:**

1. Intro — problem and solution (15 sec)
2. Architecture overview — quick visual (30 sec)
3. Live voice demo — availability inquiry (45 sec)
4. Policy Q&A via RAG (30 sec)
5. Booking confirmation flow (45 sec)
6. Closing — skills and contact (15 sec)

**Sanitization checklist before publish:**

- [ ] No credentials shown on screen
- [ ] No real guest data in voice interaction
- [ ] No proprietary prompt content visible
- [ ] Link added to README Contact section when live

---

### Booking Flow

| # | Asset | Filename | Status | Notes |
|---|-------|----------|--------|-------|
| 16 | Booking flow focused demo | `demo/booking-flow.mp4` | ⬜ | 60–90 seconds; availability check through confirmation |

**Content outline:**

1. Guest asks for specific dates and room type
2. Agent checks live availability
3. Guest confirms
4. Workflow records reservation (show sanitized Sheets update or n8n execution log)

---

### Policy Q&A Flow

| # | Asset | Filename | Status | Notes |
|---|-------|----------|--------|-------|
| 17 | RAG policy Q&A demo | `demo/policy-qa.mp4` | ⬜ | 60–90 seconds; demonstrate document-driven answer |

**Content outline:**

1. Guest asks a policy question (e.g., check-in time, pet policy)
2. Agent retrieves answer via RAG
3. Brief note that policy docs can be updated without retraining

---

## GIFs

### Guest Interaction Sequence

| # | Asset | Filename | Status | Notes |
|---|-------|----------|--------|-------|
| 18 | Voice interaction loop | `demo/guest-interaction.gif` | ⬜ | 10–20 sec loop; show Vapi or call interface with sanitized UI |
| 19 | Tool call indicator (optional) | `demo/tool-orchestration.gif` | ⬜ | Visual showing agent triggering backend tool |

**Recommended specs:** 1280×720 or 800×450, under 5 MB, 10–15 fps

---

### Workflow Execution

| # | Asset | Filename | Status | Notes |
|---|-------|----------|--------|-------|
| 20 | n8n workflow running (sanitized) | `demo/workflow-execution.gif` | ⬜ | Show nodes activating in sequence — no credential panels |
| 21 | Sheets update on booking (optional) | `demo/sheets-update.gif` | ⬜ | Fictional data row appearing after booking |

---

## README Integration Checklist

Once assets are ready, update these locations:

| Asset | Update location |
|-------|-----------------|
| `assets/banner.png` | README hero banner |
| `assets/architecture-overview.png` | README, CASE_STUDY.md (optional) |
| `assets/demo-thumbnail.png` | README Demo section |
| `assets/github-social-preview.png` | GitHub repo Settings → Social preview |
| `demo/walkthrough.mp4` (or YouTube link) | README Demo section, Contact section |
| `demo/guest-interaction.gif` | README Demo section |
| `demo/workflow-execution.gif` | README Demo section |
| Screenshots | README Demo section, CASE_STUDY.md (optional) |

---

## Publishing Order (Recommended)

1. Architecture diagram PNGs (from Mermaid exports)
2. GitHub social preview image
3. README banner
4. Sanitized Vapi and Sheets screenshots
5. Sanitized n8n workflow screenshot
6. GIFs (guest interaction, workflow execution)
7. Demo videos (booking flow → policy Q&A → full walkthrough)
8. Update README placeholders with live links

---

## What Never Goes in This Repository

- Production n8n workflow JSON exports
- API keys, credentials, or `.env` files
- Webhook URLs with tokens
- Proprietary prompts or system instructions
- Real customer, guest, or reservation data
- Unredacted production dashboard screenshots

---

*Use this checklist to track portfolio media progress. Mark items ✅ as they are completed and linked from the README.*
