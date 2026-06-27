# MCP-Style Tool Contract Example (Fictional)

> Sanitized illustration of how backend tools are defined for the AI Voice Receptionist.  
> **Not production code.** No proprietary logic, endpoints, or credentials.

---

## Purpose

This example shows the **contract pattern** between the Vapi voice agent and backend systems. Each tool has:

- A clear name and description (for agent routing)
- Structured input parameters
- Structured output schema
- No embedded business secrets

Production tool definitions and validation rules remain private.

---

## Tool: `check_room_availability`

### Description

Checks live room availability for requested dates, guest count, and optional room type preference.

### Input Schema (Fictional)

```json
{
  "check_in_date": "2026-07-15",
  "check_out_date": "2026-07-18",
  "guest_count": 2,
  "room_type_preference": "deluxe_king"
}
```

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `check_in_date` | string (ISO date) | Yes | Arrival date |
| `check_out_date` | string (ISO date) | Yes | Departure date |
| `guest_count` | integer | Yes | Total guests |
| `room_type_preference` | string | No | Preferred room category |

### Output Schema (Fictional)

```json
{
  "status": "available",
  "available_rooms": [
    {
      "room_type": "deluxe_king",
      "display_name": "Deluxe King Room",
      "nightly_rate": 189.00,
      "max_occupancy": 2,
      "available_count": 3
    }
  ],
  "alternatives": [
    {
      "room_type": "standard_queen",
      "display_name": "Standard Queen Room",
      "nightly_rate": 149.00,
      "max_occupancy": 2,
      "available_count": 5,
      "reason": "Requested type limited; lower rate alternative"
    }
  ],
  "message": "Deluxe King available for requested dates."
}
```

| Field | Type | Description |
|-------|------|-------------|
| `status` | string | `available`, `unavailable`, or `partial` |
| `available_rooms` | array | Matching rooms with rates and counts |
| `alternatives` | array | Suggested alternatives when preference unavailable |
| `message` | string | Human-readable summary for agent narration |

---

## Tool: `create_reservation`

### Description

Creates a reservation after re-validating availability. Triggers downstream workflow automation.

### Input Schema (Fictional)

```json
{
  "room_type": "deluxe_king",
  "check_in_date": "2026-07-15",
  "check_out_date": "2026-07-18",
  "guest_count": 2,
  "guest_name": "Alex Morgan",
  "contact_phone": "+1-555-0100"
}
```

### Output Schema (Fictional)

```json
{
  "status": "confirmed",
  "reservation_id": "RES-2026-00482",
  "confirmation_message": "Your Deluxe King room is confirmed for July 15–18, 2026.",
  "workflow_triggered": true
}
```

---

## Tool: `lookup_hotel_policy`

### Description

Retrieves hotel policy information via the RAG knowledge pipeline.

### Input Schema (Fictional)

```json
{
  "query": "What is the pet policy?"
}
```

### Output Schema (Fictional)

```json
{
  "status": "found",
  "answer": "Pets under 25 lbs are welcome with a nightly pet fee. Service animals are exempt.",
  "source_documents": ["pet-policy-v2.pdf"],
  "confidence": "high"
}
```

---

## Design Principles Illustrated

| Principle | How the contract supports it |
|-----------|-------------------------------|
| **Structured I/O** | Agent receives predictable JSON, not free-form generation |
| **Separation of concerns** | Voice layer narrates; tools compute and validate |
| **Alternative suggestions** | Availability tool returns structured alternatives for agent dialogue |
| **Re-validation** | Booking tool re-checks availability before write |
| **RAG grounding** | Policy tool returns source document references |

---

## Related

- [sample-api-request.json](sample-api-request.json) — fictional API request body
- [sample-api-response.json](sample-api-response.json) — fictional API response body
- [docs/architecture.md](../docs/architecture.md) — full system design
