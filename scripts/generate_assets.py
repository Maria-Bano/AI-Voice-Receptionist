# -*- coding: utf-8 -*-
"""Generate portfolio PNG assets for AI-Voice-Receptionist."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ASSETS = Path(__file__).resolve().parent.parent / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

BG = (15, 23, 42)
BG2 = (26, 26, 46)
PANEL = (30, 41, 59)
TEXT = (248, 250, 252)
MUTED = (148, 163, 184)
DIM = (100, 116, 139)
ORANGE = (255, 107, 53)
PURPLE = (91, 79, 255)
PINK = (234, 75, 113)
BLUE = (45, 156, 219)
GREEN = (0, 200, 150)


def font(size: int, bold: bool = False):
    candidates = [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def gradient_bg(w: int, h: int) -> Image.Image:
    img = Image.new("RGB", (w, h), BG)
    draw = ImageDraw.Draw(img)
    for y in range(h):
        t = y / max(h - 1, 1)
        r = int(BG[0] + (BG2[0] - BG[0]) * t)
        g = int(BG[1] + (BG2[1] - BG[1]) * t)
        b = int(BG[2] + (BG2[2] - BG[2]) * t)
        draw.line([(0, y), (w, y)], fill=(r, g, b))
    return img


def centered_text(draw, y, text, fnt, fill=TEXT):
    bbox = draw.textbbox((0, 0), text, font=fnt)
    x = (draw.im.size[0] - (bbox[2] - bbox[0])) // 2
    draw.text((x, y), text, font=fnt, fill=fill)


def rounded_box(draw, xy, fill, outline=None, radius=12):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=2)


def arrow(draw, start, end, color=MUTED):
    draw.line([start, end], fill=color, width=3)
    ex, ey = end
    sx, sy = start
    if abs(ex - sx) >= abs(ey - sy):
        tip = (ex - 10, ey) if ex > sx else (ex + 10, ey)
        draw.polygon([(ex, ey), (tip[0], ey - 6), (tip[0], ey + 6)], fill=color)
    else:
        tip = (ex, ey - 10) if ey > sy else (ex, ey + 10)
        draw.polygon([(ex, ey), (ex - 6, tip[1]), (ex + 6, tip[1])], fill=color)


def make_banner():
    w, h = 1280, 400
    img = gradient_bg(w, h)
    draw = ImageDraw.Draw(img)
    rounded_box(draw, (40, 40, w - 40, h - 40), fill=None, outline=PANEL, radius=16)
    centered_text(draw, 120, "AI Voice Receptionist", font(48, True))
    centered_text(draw, 185, "Hotel Operations | Voice AI | Workflow Automation", font(22), MUTED)
    badges = [("Vapi", PURPLE), ("n8n", PINK), ("RAG", BLUE), ("MCP Tools", ORANGE)]
    x = 360
    for label, color in badges:
        rounded_box(draw, (x, 260, x + 130, 300), fill=color, radius=20)
        bbox = draw.textbbox((0, 0), label, font=font(16, True))
        tx = x + (130 - (bbox[2] - bbox[0])) // 2
        draw.text((tx, 272), label, font=font(16, True), fill=(255, 255, 255))
        x += 150
    img.save(ASSETS / "banner.png", optimize=True)


def make_social_preview():
    w, h = 1280, 640
    img = gradient_bg(w, h)
    draw = ImageDraw.Draw(img)
    centered_text(draw, 210, "AI Voice Receptionist", font(54, True))
    centered_text(draw, 290, "Production AI Automation | Portfolio Project", font(26), MUTED)
    badges = [("AI Agents", ORANGE), ("Vapi", PURPLE), ("n8n", PINK), ("RAG", BLUE)]
    x = 300
    for label, color in badges:
        rounded_box(draw, (x, 380, x + 160, 430), fill=color, radius=24)
        bbox = draw.textbbox((0, 0), label, font=font(18, True))
        tx = x + (160 - (bbox[2] - bbox[0])) // 2
        draw.text((tx, 394), label, font=font(18, True), fill=(255, 255, 255))
        x += 180
    centered_text(draw, 520, "Voice agent | Live inventory | RAG | Workflow orchestration", font(18), DIM)
    img.save(ASSETS / "github-social-preview.png", optimize=True)


def make_architecture_overview():
    w, h = 1200, 800
    img = Image.new("RGB", (w, h), BG)
    draw = ImageDraw.Draw(img)
    centered_text(draw, 30, "System Architecture Overview", font(30, True))

    nodes = [
        (430, 90, 770, 140, "Guest (Voice)", PANEL, TEXT),
        (410, 170, 790, 220, "Vapi Agent", PURPLE, (255, 255, 255)),
        (380, 250, 820, 300, "MCP-Style Tools", ORANGE, (255, 255, 255)),
        (80, 380, 320, 450, "RAG Pipeline", BLUE, (255, 255, 255)),
        (430, 380, 770, 450, "Availability Engine + Google Sheets", GREEN, (255, 255, 255)),
        (880, 380, 1120, 450, "n8n / API Workflows", PINK, (255, 255, 255)),
        (880, 500, 1120, 550, "Confirmations | CRM Updates", PANEL, MUTED),
    ]
    for x1, y1, x2, y2, label, fill, color in nodes:
        rounded_box(draw, (x1, y1, x2, y2), fill=fill, radius=10)
        bbox = draw.textbbox((0, 0), label, font=font(16, True))
        tx = x1 + ((x2 - x1) - (bbox[2] - bbox[0])) // 2
        ty = y1 + ((y2 - y1) - (bbox[3] - bbox[1])) // 2
        draw.text((tx, ty), label, font=font(16, True), fill=color)

    arrow(draw, (600, 140), (600, 170))
    arrow(draw, (600, 220), (600, 250))
    arrow(draw, (600, 300), (600, 340))
    arrow(draw, (600, 340), (200, 380))
    arrow(draw, (600, 340), (600, 380))
    arrow(draw, (600, 340), (1000, 380))
    arrow(draw, (1000, 450), (1000, 500))
    img.save(ASSETS / "architecture-overview.png", optimize=True)


def make_workflow_overview():
    w, h = 1200, 500
    img = Image.new("RGB", (w, h), BG)
    draw = ImageDraw.Draw(img)
    centered_text(draw, 25, "End-to-End Booking Workflow", font(28, True))
    steps = [
        ("Guest Inquiry", PANEL),
        ("Voice Agent", PURPLE),
        ("Check Availability", ORANGE),
        ("Validate Dates", GREEN),
        ("Suggest Alternatives", BLUE),
        ("Book Room", PINK),
    ]
    x = 40
    for i, (label, color) in enumerate(steps):
        rounded_box(draw, (x, 110, x + 170, 166), fill=color, radius=10)
        bbox = draw.textbbox((0, 0), label, font=font(14, True))
        tx = x + (170 - (bbox[2] - bbox[0])) // 2
        draw.text((tx, 132), label, font=font(14, True), fill=(255, 255, 255))
        if i < len(steps) - 1:
            draw.text((x + 178, 132), "->", font=font(18, True), fill=MUTED)
        x += 190
    rounded_box(draw, (80, 220, 1120, 390), fill=PANEL, outline=(51, 65, 85), radius=14)
    centered_text(draw, 250, "Demo highlights", font(20, True), MUTED)
    centered_text(draw, 295, "Room discovery | Availability checks | Guest count handling", font(17), TEXT)
    centered_text(draw, 330, "Alternative suggestions | Reservation creation | Workflow automation", font(17), TEXT)
    img.save(ASSETS / "workflow-overview.png", optimize=True)


def make_demo_thumbnail():
    w, h = 1280, 720
    img = gradient_bg(w, h)
    draw = ImageDraw.Draw(img)
    cx, cy = w // 2, 300
    draw.ellipse((cx - 80, cy - 80, cx + 80, cy + 80), fill=ORANGE)
    draw.polygon([(cx - 25, cy - 45), (cx - 25, cy + 45), (cx + 45, cy)], fill=(255, 255, 255))
    centered_text(draw, 430, "Watch Demo on LinkedIn", font(42, True))
    centered_text(draw, 500, "AI Voice Receptionist | End-to-End Walkthrough", font(24), MUTED)
    centered_text(draw, 620, "Click to open the full demo", font(18), DIM)
    img.save(ASSETS / "demo-thumbnail.png", optimize=True)


if __name__ == "__main__":
    make_banner()
    make_social_preview()
    make_architecture_overview()
    make_workflow_overview()
    make_demo_thumbnail()
    print("Generated PNG assets in", ASSETS)
