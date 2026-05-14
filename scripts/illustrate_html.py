#!/usr/bin/env python3
"""Inject local article images into wechat-viral-content HTML files.

The script is intentionally dependency-free. It targets the HTML structure
created by assets/template.html: optional media-slot blocks plus caption
paragraphs, with a single in-file <style> block.
"""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path
from typing import Any


IMAGE_CSS = """

    .article-image {
      margin: 30px 0;
      padding: 0;
    }

    .article-image img {
      display: block;
      width: 100%;
      height: auto;
      border: 1px solid var(--rule);
      background: var(--panel);
    }

    .hero-visual {
      margin: 34px 0 0;
    }
"""


MEDIA_SLOT_RE = re.compile(
    r'(?P<indent>[ \t]*)<div class="media-slot">(?P<body>.*?)</div>\s*'
    r'<p class="caption">(?P<caption>.*?)</p>',
    re.DOTALL,
)

LEAD_RE = re.compile(r'(?P<indent>[ \t]*)<p class="lead">', re.DOTALL)


def clean_text(value: str) -> str:
    value = re.sub(r"<br\s*/?>", " ", value)
    value = re.sub(r"<.*?>", " ", value)
    value = html.unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def ensure_image_css(document: str) -> str:
    if ".article-image" in document:
        return document
    if "</style>" not in document:
        raise SystemExit("No </style> tag found; cannot inject image CSS.")
    return document.replace("\n  </style>", IMAGE_CSS + "\n  </style>", 1)


def figure_markup(item: dict[str, Any], indent: str, hero: bool = False) -> str:
    src = item.get("src")
    if not src:
        raise SystemExit("Every image item needs a non-empty 'src'.")

    alt = html.escape(item.get("alt") or clean_text(item.get("caption", "")) or "公众号文章配图", quote=True)
    caption = html.escape(item.get("caption", ""), quote=False)
    class_name = "article-image hero-visual" if hero else "article-image"

    lines = [
        f'{indent}<figure class="{class_name}">',
        f'{indent}  <img src="{html.escape(src, quote=True)}" alt="{alt}">',
        f"{indent}</figure>",
    ]
    if caption:
        lines.append(f'{indent}<p class="caption">{caption}</p>')
    return "\n".join(lines)


def build_plan(document: str) -> dict[str, Any]:
    slots = []
    for index, match in enumerate(MEDIA_SLOT_RE.finditer(document), start=1):
        slots.append(
            {
                "slot": index,
                "placeholder": clean_text(match.group("body")),
                "src": "",
                "alt": "",
                "caption": clean_text(match.group("caption")),
            }
        )
    return {
        "hero": {
            "src": "",
            "alt": "",
            "caption": "",
            "insert_before_lead": True,
        },
        "slots": slots,
    }


def apply_config(document: str, config: dict[str, Any]) -> str:
    document = ensure_image_css(document)

    hero = config.get("hero") or {}
    if hero.get("src") and hero.get("insert_before_lead", True) and "hero-visual" not in document:
        lead_match = LEAD_RE.search(document)
        if not lead_match:
            raise SystemExit("No lead paragraph found; cannot insert hero image.")
        indent = lead_match.group("indent")
        hero_html = figure_markup(hero, indent, hero=True) + "\n\n"
        document = document[: lead_match.start()] + hero_html + document[lead_match.start() :]

    images = list(config.get("slots") or [])
    image_iter = iter(images)

    def replace_slot(match: re.Match[str]) -> str:
        try:
            item = next(image_iter)
        except StopIteration:
            return match.group(0)
        if not item.get("src"):
            return match.group(0)
        if not item.get("caption"):
            item["caption"] = clean_text(match.group("caption"))
        return figure_markup(item, match.group("indent"))

    return MEDIA_SLOT_RE.sub(replace_slot, document)


def main() -> None:
    parser = argparse.ArgumentParser(description="Inject local images into a WeChat article HTML file.")
    parser.add_argument("--html", required=True, type=Path, help="Input HTML file.")
    parser.add_argument("--plan", action="store_true", help="Print a JSON image plan for existing media slots.")
    parser.add_argument("--config", type=Path, help="JSON config with hero and slots image paths.")
    parser.add_argument("--output", type=Path, help="Output HTML path. Defaults to stdout unless --apply is used.")
    parser.add_argument("--apply", action="store_true", help="Write changes back to --html.")
    args = parser.parse_args()

    document = args.html.read_text(encoding="utf-8")

    if args.plan:
        print(json.dumps(build_plan(document), ensure_ascii=False, indent=2))
        return

    if not args.config:
        raise SystemExit("Use --plan or provide --config.")

    config = json.loads(args.config.read_text(encoding="utf-8"))
    updated = apply_config(document, config)

    if args.apply:
        args.html.write_text(updated, encoding="utf-8")
    elif args.output:
        args.output.write_text(updated, encoding="utf-8")
    else:
        print(updated)


if __name__ == "__main__":
    main()
