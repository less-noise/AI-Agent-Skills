"""Render structured resume JSON into a print-friendly HTML file.

Usage:
    python generate_resume.py input.json output.html

Input JSON fields:
    basics: {name, phone, email, city, target}
    summary: optional list[str]
    sections: list[{title, items}]

Each section item may contain heading, subheading, period, and bullets.
The script uses pathlib only, performs no network access, and writes one HTML
file that can be opened in a browser or printed to PDF.
"""

from __future__ import annotations

import argparse
import html
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "assets" / "resume-template.html"


def fail(message: str) -> None:
    print(f"Error: {message}", file=sys.stderr)
    sys.exit(1)


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def esc(value: Any) -> str:
    return html.escape(str(value or "").strip())


def render_bullets(values: list[Any]) -> str:
    bullets = [esc(value) for value in values if str(value or "").strip()]
    if not bullets:
        return ""
    return "<ul>" + "".join(f"<li>{value}</li>" for value in bullets) + "</ul>"


def render_section(section: dict[str, Any]) -> str:
    title = esc(section.get("title", "Section"))
    output = [f"<section><h2>{title}</h2>"]
    for item in as_list(section.get("items")):
        if isinstance(item, str):
            output.append(f"<p>{esc(item)}</p>")
            continue
        if not isinstance(item, dict):
            continue
        heading = esc(item.get("heading"))
        meta = " | ".join(
            part for part in [esc(item.get("subheading")), esc(item.get("period"))] if part
        )
        output.append('<div class="entry">')
        if heading:
            output.append(f'<div class="entry-head"><strong>{heading}</strong><span>{meta}</span></div>')
        elif meta:
            output.append(f'<p class="muted">{meta}</p>')
        output.append(render_bullets(as_list(item.get("bullets"))))
        output.append("</div>")
    output.append("</section>")
    return "\n".join(output)


def render_content(data: dict[str, Any]) -> tuple[str, str, str]:
    basics = data.get("basics")
    sections = data.get("sections")
    if not isinstance(basics, dict):
        fail("input JSON must contain object field: basics")
    if not isinstance(sections, list):
        fail("input JSON must contain list field: sections")

    name = esc(basics.get("name", "姓名"))
    contact = " · ".join(
        part
        for part in [
            esc(basics.get("phone")),
            esc(basics.get("email")),
            esc(basics.get("city")),
            esc(basics.get("target")),
        ]
        if part
    )

    content: list[str] = []
    summary = as_list(data.get("summary"))
    if summary:
        content.append("<section><h2>核心摘要</h2>")
        content.append(render_bullets(summary))
        content.append("</section>")
    content.extend(render_section(section) for section in sections if isinstance(section, dict))
    return name, contact, "\n".join(content)


def main() -> None:
    parser = argparse.ArgumentParser(description="Render resume JSON into HTML.")
    parser.add_argument("input_json", type=Path)
    parser.add_argument("output_html", type=Path)
    args = parser.parse_args()

    try:
        data = json.loads(args.input_json.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"input file not found: {args.input_json}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON: {exc}")
    if not isinstance(data, dict):
        fail("input JSON root must be an object")

    try:
        template = TEMPLATE.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"template not found: {TEMPLATE}")

    name, contact, content = render_content(data)
    html_output = (
        template.replace("{{NAME}}", name)
        .replace("{{CONTACT}}", contact)
        .replace("{{CONTENT}}", content)
    )

    args.output_html.parent.mkdir(parents=True, exist_ok=True)
    args.output_html.write_text(html_output, encoding="utf-8")
    print(args.output_html)


if __name__ == "__main__":
    main()
