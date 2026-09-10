#!/usr/bin/env python3
"""Generate social share images: assets/og-default.png and
assets/og/<slug>.png for each note.

Runs automatically in the Pages build (see .github/workflows/pages.yml),
so new notes get a matching image on deploy without any manual step.
Rerun locally if you want to preview the result before pushing:

    python3 scripts/generate_og_images.py

Uses Inter, Source Serif 4 and JetBrains Mono (bundled under
scripts/fonts/, all OFL-licensed) so the cards match the site's own
type system, plus assets/grain.png for the same paper texture as the
page background.
"""

import datetime
import glob
import os
import re

from PIL import Image, ImageDraw, ImageFont

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES_DIR = os.path.join(REPO_ROOT, "_notes")
OUT_DIR = os.path.join(REPO_ROOT, "assets", "og")
FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
GRAIN_PATH = os.path.join(REPO_ROOT, "assets", "grain.png")

W, H = 1200, 630
BG = (250, 249, 247)
BORDER = (231, 229, 228)
PRIMARY = (28, 25, 23)
MUTED = (168, 162, 158)
FAINT = (194, 189, 185)

SITE_TITLE = "steffen novak mollestad"
SITE_TAGLINE = "a place for where thoughts turns into writing"
SITE_URL = "steffenmoll.github.io"


def font(path, size, variation="Regular"):
    f = ImageFont.truetype(path, size)
    f.set_variation_by_name(variation)
    return f


def inter(size, variation="Regular"):
    return font(os.path.join(FONT_DIR, "Inter.ttf"), size, variation)


def mono(size, variation="Regular"):
    return font(os.path.join(FONT_DIR, "JetBrainsMono.ttf"), size, variation)


def serif(size, variation="Regular"):
    return font(os.path.join(FONT_DIR, "SourceSerif4.ttf"), size, variation)


def new_canvas():
    bg = Image.new("RGB", (W, H), BG)

    grain_tile = Image.open(GRAIN_PATH).convert("L")
    tile_size = grain_tile.width
    grain_l = Image.new("L", (W, H))
    for y in range(0, H, tile_size):
        for x in range(0, W, tile_size):
            grain_l.paste(grain_tile, (x, y))
    grain_rgb = Image.merge("RGB", (grain_l, grain_l, grain_l))

    img = Image.blend(bg, grain_rgb, 0.05)
    draw = ImageDraw.Draw(img)
    draw.rectangle([40, 40, W - 40, H - 40], outline=BORDER, width=2)
    return img, draw


def draw_footer(draw, y_rule):
    draw.line([90, y_rule, W - 90, y_rule], fill=BORDER, width=2)
    draw.text((90, y_rule + 20), SITE_URL, font=mono(28), fill=FAINT)


def wrap_text(draw, text, font_fn, max_width, sizes, max_lines=3):
    chosen_font, lines = font_fn(sizes[-1]), [text]
    for size in sizes:
        chosen_font = font_fn(size)
        words = text.split()
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
        if len(lines) <= max_lines:
            break
    return chosen_font, lines[:max_lines]


def render_default(out_path):
    img, draw = new_canvas()
    pad = 90

    draw.text((pad, 170), "steffen novak", font=inter(74, "Bold"), fill=PRIMARY)
    draw.text((pad, 254), "mollestad", font=inter(74, "Bold"), fill=PRIMARY)
    draw.text((pad, 358), SITE_TAGLINE, font=serif(38), fill=MUTED)

    draw_footer(draw, H - 110)
    img.save(out_path, "PNG", optimize=True)


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


def render_note(path, out_path):
    data = parse_front_matter(path)
    img, draw = new_canvas()
    pad = 90
    content_width = W - 2 * pad

    draw.text((pad, 70), SITE_TITLE, font=mono(26, "Medium"), fill=MUTED)

    title_font, lines = wrap_text(
        draw, data["title"], lambda s: inter(s, "Bold"), content_width, (72, 60, 50)
    )
    y = 150
    line_height = title_font.size + 16
    for line in lines:
        draw.text((pad, y), line, font=title_font, fill=PRIMARY)
        y += line_height
    y += 20

    if data["date"]:
        date_str = datetime.date.fromisoformat(data["date"]).strftime("%B %-d, %Y")
        draw.text((pad, y), date_str, font=mono(26), fill=MUTED)
        y += 44

    if data["tags"]:
        tag_font = mono(24, "Medium")
        x, ty = pad, y
        for tag in data["tags"]:
            tw = draw.textbbox((0, 0), tag, font=tag_font)[2]
            pill_w, pill_h = tw + 34, 50
            if x + pill_w > W - pad:
                x, ty = pad, ty + pill_h + 14
            draw.rounded_rectangle(
                [x, ty, x + pill_w, ty + pill_h], radius=pill_h // 2, outline=BORDER, width=2
            )
            draw.text((x + 17, ty + 12), tag, font=tag_font, fill=MUTED)
            x += pill_w + 14

    draw_footer(draw, H - 110)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    img.save(out_path, "PNG", optimize=True)


if __name__ == "__main__":
    default_out = os.path.join(REPO_ROOT, "assets", "og-default.png")
    render_default(default_out)
    print("generated", os.path.relpath(default_out, REPO_ROOT))

    for path in sorted(glob.glob(os.path.join(NOTES_DIR, "*.md"))):
        slug = os.path.splitext(os.path.basename(path))[0]
        out_path = os.path.join(OUT_DIR, slug + ".png")
        render_note(path, out_path)
        print("generated", os.path.relpath(out_path, REPO_ROOT))
