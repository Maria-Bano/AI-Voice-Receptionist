# Assets

Visual assets for the AI Voice Receptionist portfolio repository.

## Placeholder Files

| File | Purpose | Status |
|------|---------|--------|
| `banner.png` | README hero banner | ⬜ Placeholder — generate before publish |
| `architecture-overview.png` | Architecture section visual | ⬜ Placeholder — generate before publish |
| `demo-thumbnail.png` | Video thumbnail and README demo section | ⬜ Placeholder — generate before publish |
| `github-social-preview.png` | GitHub repository social preview (1280×640) | ⬜ Placeholder — generate before publish |

> **Note:** Binary image files are not committed as placeholders. Add generated PNGs to this folder when ready. Until then, README references serve as placement markers.

---

## How to Generate Each Asset

### `banner.png` — README Hero Banner

**Recommended size:** 1280×400 px (or 1200×300 px)

**Purpose:** First visual impression on the GitHub README. Should communicate voice AI + hotel operations + system architecture.

**How to create:**

1. **Option A — Canva (fastest)**
   - Template: GitHub README banner or LinkedIn banner
   - Include: project title, subtitle ("AI Voice Receptionist · Hotel Operations"), tech icons (Vapi, n8n, RAG)
   - Color palette: dark professional background (#1A1A2E or #0F172A) with accent colors matching README badges
   - Export as PNG

2. **Option B — Figma**
   - Frame: 1280×400
   - Add architecture mini-diagram (Guest → Vapi → Tools → Backend)
   - Export 2× PNG for retina clarity

3. **Option C — Mermaid export**
   - Render high-level architecture from [docs/architecture.md](../docs/architecture.md)
   - Use [Mermaid Live Editor](https://mermaid.live) → Export PNG
   - Add title bar in Canva/Figma overlay

**Save to:** `assets/banner.png`

---

### `architecture-overview.png` — Architecture Diagram

**Recommended size:** 1200×800 px

**Purpose:** Standalone architecture visual for README, CASE_STUDY, and LinkedIn posts.

**How to create:**

1. Open [docs/architecture.md](../docs/architecture.md)
2. Copy the **High-Level Architecture** Mermaid block
3. Paste into [Mermaid Live Editor](https://mermaid.live)
4. Adjust theme (dark or neutral professional)
5. Export PNG at 2× scale
6. Optionally annotate layers in Figma (Voice · Orchestration · Backend · Downstream)

**Save to:** `assets/architecture-overview.png`

---

### `demo-thumbnail.png` — Demo Video Thumbnail

**Recommended size:** 1280×720 px (16:9)

**Purpose:** YouTube/Loom thumbnail and README demo section preview.

**How to create:**

1. Canva → YouTube Thumbnail template
2. Include: "AI Voice Receptionist Demo", subtitle "Live Availability · RAG Policies · Booking Automation"
3. Add play-button overlay icon (visual cue only)
4. Match banner color palette for brand consistency
5. Export PNG

**Save to:** `assets/demo-thumbnail.png`

---

### `github-social-preview.png` — GitHub Social Preview

**Recommended size:** 1280×640 px (GitHub required dimensions)

**Purpose:** Image shown when the repository link is shared on social media, Slack, or LinkedIn.

**How to create:**

1. Canva → Custom size 1280×640
2. Include: project title, one-line value prop, 3–4 tech badges (Vapi · n8n · RAG · MCP Tools)
3. Keep text large — image renders small in link previews
4. Export PNG

**Upload to:** GitHub → Repository → Settings → General → Social preview image  
**Also save to:** `assets/github-social-preview.png`

---

## Brand Consistency Tips

- Use the same dark background and accent colors across all assets
- Keep typography consistent (one heading font, one body font)
- Do not include credentials, real data, or proprietary UI details in any asset
- Prefer diagrams and icons over raw production screenshots for banner/social assets

---

## Related

- [Demo checklist](../docs/demo-checklist.md) — full screenshot, video, and GIF tracking
- [Screenshots folder](../screenshots/README.md) — sanitized production UI captures
- [Demo folder](../demo/README.md) — video and GIF files
