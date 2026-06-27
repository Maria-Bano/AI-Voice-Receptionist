# Assets

Visual assets for the AI Voice Receptionist portfolio repository.

---

## Portfolio Assets

| File | Size | Purpose |
|------|------|---------|
| `banner.png` | 1280×400 | README hero banner |
| `github-social-preview.png` | 1280×640 | GitHub social preview image |
| `architecture-overview.png` | 1200×800 | Architecture section visual |
| `workflow-overview.png` | 1200×500 | Demo / workflow section visual |
| `demo-thumbnail.png` | 1280×720 | LinkedIn demo thumbnail (README) |

All assets are PNG for reliable rendering on GitHub, LinkedIn, and mobile.

---

## Regenerating Assets

Run the asset generator from the repository root:

```bash
python scripts/generate_assets.py
```

Requires Python 3 and Pillow (`pip install Pillow`).

---

## GitHub Social Preview

1. Open `assets/github-social-preview.png`
2. Go to **Repository → Settings → General → Social preview**
3. Upload the image

This image appears when the repository link is shared on LinkedIn, Slack, and email.

---

## Optional Upgrades

| Asset | Upgrade path |
|-------|--------------|
| `banner.png` | Replace with Canva/Figma design using the same palette |
| `architecture-overview.png` | Export from Mermaid Live Editor for higher fidelity |
| `workflow-overview.png` | Replace with sanitized n8n workflow screenshot |
| `demo-thumbnail.png` | Capture a frame from the LinkedIn demo video |

See [docs/demo-checklist.md](../docs/demo-checklist.md) for sanitization rules.

---

## Related

- [Demo checklist](../docs/demo-checklist.md)
- [GitHub profile setup](../docs/github-profile-setup.md)
- [screenshots/](../screenshots/) — sanitized production UI captures
