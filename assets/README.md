# Assets

Visual assets for the AI Voice Receptionist portfolio repository.

---

## Current Assets

| File | Type | Purpose | Status |
|------|------|---------|--------|
| `banner.svg` | SVG placeholder | README hero banner | ✅ In repo — replace with PNG when ready |
| `github-social-preview.svg` | SVG placeholder | GitHub social preview (1280×640) | ✅ In repo — export to PNG & upload to Settings |
| `architecture-overview.svg` | SVG placeholder | Architecture section visual | ✅ In repo — replace with Mermaid export PNG |
| `workflow-overview.svg` | SVG placeholder | Demo / workflow section visual | ✅ In repo — replace with sanitized n8n screenshot |
| `demo-thumbnail.svg` | SVG placeholder | Demo video thumbnail | ✅ In repo — replace with video frame capture |
| `banner.png` | PNG target | Final hero banner | ⬜ Generate from SVG or Canva |
| `github-social-preview.png` | PNG target | GitHub link preview image | ⬜ Export from SVG (1280×640) |
| `architecture-overview.png` | PNG target | Standalone architecture diagram | ⬜ Export from Mermaid Live Editor |
| `workflow-overview.png` | PNG target | Sanitized workflow screenshot | ⬜ Capture from n8n (no credentials) |
| `demo-thumbnail.png` | PNG target | Video thumbnail (1280×720) | ⬜ Capture frame from demo video |

> **Note:** README currently references SVG placeholders. When PNG versions are ready, update README image paths from `.svg` to `.png` for sharper rendering on some platforms.

---

## How to Replace Each Placeholder

### `banner.png` ← replace `banner.svg`

**Target size:** 1280×400 px

1. Open `banner.svg` in browser or Figma for reference
2. Create in Canva: dark background (#0F172A), project title, tech badges (Vapi · n8n · RAG · MCP)
3. Export PNG → save as `assets/banner.png`
4. Update README: `![Architecture Banner](assets/banner.png)`

---

### `github-social-preview.png` ← replace `github-social-preview.svg`

**Target size:** 1280×640 px (required by GitHub)

1. Export SVG at exact dimensions (browser screenshot or Figma)
2. Save as `assets/github-social-preview.png`
3. Upload: **GitHub → Repository → Settings → General → Social preview**

---

### `architecture-overview.png` ← replace `architecture-overview.svg`

**Target size:** 1200×800 px

1. Copy High-Level Architecture Mermaid block from [docs/architecture.md](../docs/architecture.md)
2. Paste into [Mermaid Live Editor](https://mermaid.live) → export PNG
3. Save as `assets/architecture-overview.png`
4. Update README architecture image path

---

### `workflow-overview.png` ← replace `workflow-overview.svg`

**Target size:** 1200×500 px (or match screenshot aspect ratio)

1. Open n8n workflow canvas (sanitized — no credential panels)
2. Screenshot booking workflow overview
3. Blur/redact any URLs, keys, or PII
4. Save as `assets/workflow-overview.png`

See [docs/demo-checklist.md](../docs/demo-checklist.md) for sanitization rules.

---

### `demo-thumbnail.png` ← replace `demo-thumbnail.svg`

**Target size:** 1280×720 px

1. Play [demo/AI-Voice-Receptionist-Demo.mp4](../demo/AI-Voice-Receptionist-Demo.mp4)
2. Capture a compelling frame (voice UI or workflow moment — sanitized)
3. Optionally add play-button overlay in Canva
4. Save as `assets/demo-thumbnail.png`
5. Update README demo thumbnail link

---

## Brand Consistency

- Dark background palette: `#0F172A`, `#1A1A2E`
- Accent colors matching README badges: orange `#FF6B35`, purple `#5B4FFF`, pink `#EA4B71`, blue `#2D9CDB`, green `#00C896`
- No credentials, real data, or proprietary UI details in any asset

---

## Related

- [Demo checklist](../docs/demo-checklist.md) — full screenshot, video, and GIF tracking
- [GitHub profile setup](../docs/github-profile-setup.md) — social preview upload instructions
- [screenshots/](../screenshots/) — sanitized production UI captures
