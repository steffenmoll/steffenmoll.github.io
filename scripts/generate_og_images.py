#!/usr/bin/env python3
"""Generate per-note social share images into assets/og/<slug>.png.

Rerun after adding or editing a note so its preview image stays in sync:

    python3 scripts/generate_og_images.py

Uses San Francisco (/System/Library/Fonts/SFNS.ttf), so this only
produces pixel-correct output on macOS. Apple's font license doesn't
allow bundling SFNS.ttf into the repo, which is why this isn't wired
into the GitHub Actions build.
"""

import datetime
import glob
import os
import re

from PIL import Image, ImageDraw, ImageFont

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES_DIR = os.path.join(REPO_ROOT, "_notes")
OUT_DIR = os.path.join(REPO_ROOT, "assets", "og")

W, H = 1200, 630
BG = (255, 255, 255)
BORDER = (217, 217, 217)
PRIMARY = (26, 26, 26)
SUBTEXT = (77, 77, 77)
FAINT = (170, 170, 170)

SFNS = "/System/Library/Fonts/SFNS.ttf"


def font(size, variation="Regular"):
    f = ImageFont.truetype(SFNS, size)
    f.set_variation_by_name(variation)
    return f


eyebrow_font = font(28, "Semibold")
tag_font = font(24, "Medium")
date_font = font(28, "Regular")
url_font = font(28, "Regular")


def parse_front_matter(path):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    fm = re.match(r"^---\n(.*?)\n---\n", text, re.S).group(1)

    title_m = re.search(r'^title:\s*"(.*)"\s*$', fm, re.M) or re.search(
        r"^title:\s*(.*)\s*$", fm, re.M
    )
    date_m = re.search(r"^date:\s*(\S+)", fm, re.M)
    tags_m = re.search(r"^tags:\s*\[(.*)\]", fm, re.M)

    return {
        "title": title_m.group(1).strip() if title_m else "Untitled",
        "date": date_m.group(1).strip() if date_m else None,
        "tags": [t.strip() for t in tags_m.group(1).split(",")] if tags_m else [],
    }


def wrap_title(draw, title, max_width, sizes=(74, 62, 52)):
    lines = [title]
    chosen_font = font(sizes[-1], "Bold")
    for size in sizes:
        chosen_font = font(size, "Bold")
        words = title.split()
        lines, cur = [], ""
        for word in words:
            trial = (cur + " " + word).strip()
            if draw.textbbox((0, 0), trial, font=chosen_font)[2] <= max_width:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = word
        if cur:
            lines.append(cur)
        if len(lines) <= 3:
            break
    return chosen_font, lines[:3]


def render(path, out_path):
    data = parse_front_matter(path)
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    pad = 90
    content_width = W - 2 * pad

    draw.rectangle([40, 40, W - 40, H - 40], outline=BORDER, width=2)
    draw.text((pad, 70), "steffen novak mollestad", font=eyebrow_font, fill=SUBTEXT)

    title_font, lines = wrap_title(draw, data["title"], content_width)
    y = 150
    line_height = title_font.size + 16
    for line in lines:
        draw.text((pad, y), line, font=title_font, fill=PRIMARY)
        y += line_height
    y += 20

    if data["date"]:
        date_str = datetime.date.fromisoformat(data["date"]).strftime("%B %-d, %Y")
        draw.text((pad, y), date_str, font=date_font, fill=SUBTEXT)
        y += 46

    if data["tags"]:
        x, ty = pad, y
        for tag in data["tags"]:
            tw = draw.textbbox((0, 0), tag, font=tag_font)[2]
            pill_w, pill_h = tw + 34, 50
            if x + pill_w > W - pad:
                x, ty = pad, ty + pill_h + 14
            draw.rounded_rectangle(
                [x, ty, x + pill_w, ty + pill_h], radius=pill_h // 2, outline=BORDER, width=2
            )
            draw.text((x + 17, ty + 12), tag, font=tag_font, fill=SUBTEXT)
            x += pill_w + 14

    draw.line([pad, H - 110, W - pad, H - 110], fill=BORDER, width=2)
    draw.text((pad, H - 90), "steffenmoll.github.io", font=url_font, fill=FAINT)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    img.save(out_path, "PNG", optimize=True)


if __name__ == "__main__":
    for path in sorted(glob.glob(os.path.join(NOTES_DIR, "*.md"))):
        slug = os.path.splitext(os.path.basename(path))[0]
        out_path = os.path.join(OUT_DIR, slug + ".png")
        render(path, out_path)
        print("generated", os.path.relpath(out_path, REPO_ROOT))
