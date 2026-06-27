# Interview Talking Points

> Verbal walkthrough scripts for recruiters, hiring managers, clients, and technical interviews.  
> Pair with [CASE_STUDY.md](../CASE_STUDY.md) and [docs/architecture.md](architecture.md).

---

## 2-Minute Explanation

> Use for: recruiter screens, Upwork intro calls, LinkedIn conversations

"I built an AI Voice Receptionist for hotel front-desk operations. Guests call and speak naturally ù the system handles room availability, policy questions, and booking requests.

The key design choice is that the voice agent doesn't guess operational data. It uses MCP-style tool calls to check live inventory in Google Sheets, retrieve policy answers through a RAG pipeline, and trigger booking workflows in n8n.

So when a guest asks about a room, the agent checks real availability, handles guest count, suggests alternatives if needed, and can create a reservation end-to-end.

It's a production-style architecture ù voice layer, tool orchestration, live data, knowledge retrieval, and workflow automation ù documented as a public portfolio repo without exposing proprietary prompts or credentials."

---

## 5-Minute Explanation

> Use for: hiring manager calls, client discovery, portfolio walkthroughs

### 1. Problem (45 sec)

"Hotel front desks handle repetitive, time-sensitive work ù availability checks, policy questions, bookings. Static chatbots fail because inventory changes and policies update. I designed a system that automates voice interactions while staying grounded in live operational data."

### 2. Architecture (90 sec)

"The architecture has five layers:

1. **Vapi** handles voice ù natural guest conversation.
2. **MCP-style tools** route intent to backend capabilities with structured contracts.
3. **Availability engine** reads Google Sheets, validates dates, checks conflicts.
4. **RAG pipeline** answers policy questions from maintained documents.
5. **n8n workflows** record bookings and trigger downstream actions ù confirmations, CRM updates.

The voice agent never computes availability itself. It calls tools and narrates structured results."

### 3. Demo highlights (60 sec)

"In the demo you'll see: room discovery, live availability checks, guest count handling, alternative room suggestions when the preferred type is limited, reservation creation, and the full workflow automation chain."

### 4. Why it matters (45 sec)

"This isn't a chatbot demo. It shows how to build AI automation for operations ù tool orchestration, live data, maintainable knowledge, integration depth. The public repo documents architecture and decisions; production workflows and prompts stay private."

### 5. Close (30 sec)

"I'd point you to the README architecture diagram, the case study, and the demo video. Happy to go deeper on any layer ù RAG, tool design, or workflow automation."

---

## Technical Deep Dive

> Use for: engineering interviews, architecture reviews

### System boundaries

| Layer | Responsibility | Failure mode if blurred |
|-------|----------------|-------------------------|
| Voice (Vapi) | Dialogue, intent, tool invocation | Agent hallucinates operational state |
| Tools | Structured I/O contracts | Untestable, fragile integrations |
| Availability engine | Inventory truth | Stale or incorrect bookings |
| RAG | Policy retrieval | Outdated or invented policies |
| n8n / APIs | Side effects and integrations | Bookings without downstream sync |

### Key flows to whiteboard

1. **Availability check:** Guest ? Vapi ? `check_room_availability` tool ? Sheets read ? conflict validation ? structured response ? voice narration
2. **Booking:** Guest confirms ? re-validate availability ? `create_reservation` tool ? Sheets write ? n8n workflow ? confirmation + CRM
3. **Policy Q&A:** Guest question ? `lookup_hotel_policy` tool ? RAG retrieval ? grounded answer with source reference

### Design decisions to articulate

- **Why tools, not end-to-end LLM?** Operational accuracy requires validated backend logic.
- **Why MCP-style pattern?** Industry-aligned agent architecture; swappable backends; clear contracts.
- **Why RAG for policies?** Documents are the pageable by ops teams; no retraining on policy change.
- **Why re-validate before booking?** Inventory state can change between inquiry and confirmation.
- **Why portfolio-only public repo?** Demonstrate engineering depth without security or IP risk.

### Example artifacts to reference

- [examples/tool-contract-example.md](../examples/tool-contract-example.md) ù fictional tool schemas
- [docs/architecture.md](architecture.md) ù Mermaid diagrams for whiteboarding

---

## Common Recruiter Questions

| Question | Suggested answer |
|----------|------------------|
| **What did you build?** | AI voice receptionist for hotels ù availability, policies, bookings via tool-orchestrated backend. |
| **What technologies?** | Vapi, n8n, Google Sheets, RAG, MCP-style tools, API integrations. |
| **Is this production?** | Production-style architecture and patterns; public repo is documentation portfolio; implementation details are private. |
| **What's your role?** | End-to-end AI automation ù agent design, tool contracts, workflow automation, integration architecture. |
| **Can I see it work?** | Yes ù [LinkedIn demo](https://www.linkedin.com/feed/update/urn:li:activity:7476686387690455043/) and [README](../README.md#demo). |
| **Why not open-source the code?** | Proprietary workflows and business logic; architecture and case study demonstrate capability without IP exposure. |
| **What makes this different from a chatbot?** | Live inventory, tool orchestration, RAG maintainability, downstream workflow automation. |

---

## Common Engineering Questions

| Question | Suggested answer |
|----------|------------------|
| **How do you prevent double-booking?** | Availability engine validates against live inventory and pending reservations; re-check immediately before write. |
| **How does the agent know when to call tools?** | Tool definitions with descriptions; agent routes operational intents to structured tools. |
| **What happens if a tool fails?** | Structured error responses; agent can apologize and offer retry or human handoff (future enhancement). |
| **How is knowledge updated?** | Update source documents ? re-index vector store ? RAG answers reflect changes without redeployment. |
| **Why Google Sheets?** | Fast to demonstrate and inspect; architecture supports PMS/database migration without redesigning voice layer. |
| **How would you scale this?** | Migrate inventory to PMS API; cache frequent RAG queries; horizontal n8n scaling; per-property knowledge partitioning. |
| **Security approach?** | No credentials in repo; scoped service accounts; sanitized portfolio materials; see SECURITY.md. |

---

## Why Architectural Decisions Were Made

| Decision | Rationale | Trade-off accepted |
|----------|-----------|-------------------|
| Tool orchestration over monolithic agent | Accuracy and testability for operational actions | Higher initial design effort |
| MCP-style contracts | Clear agent-backend boundary; industry pattern | Requires disciplined tool design |
| RAG over fine-tuning | Maintainable policy updates via documents | Depends on document quality |
| Sheets for demo inventory | Speed and visibility for portfolio | Not ideal at very high volume |
| n8n for automation | Rapid integration workflows | Platform ops at scale |
| Portfolio-only public repo | Share architecture; protect IP | Reviewers can't inspect live implementation |

---

## Quick Links for Screen Share

1. [README](../README.md) - entry point and demo
2. [CASE_STUDY.md](../CASE_STUDY.md) - narrative for non-technical stakeholders
3. [docs/architecture.md](architecture.md) - diagrams for technical audience
4. [LinkedIn demo](https://www.linkedin.com/feed/update/urn:li:activity:7476686387690455043/) - primary walkthrough
5. [demo/AI-Voice-Receptionist-Demo.mp4](../demo/AI-Voice-Receptionist-Demo.mp4) - archival download

---

*Practice the 2-minute version until fluent. Expand to 5-minute or deep dive based on interviewer signals.*
