#!/usr/bin/env python3
"""Short DP-4 narrative builder: loads JSON chunks, replaces placeholders, fills classifications."""

import argparse, json, re, sys
from pathlib import Path


def name_case(s: str) -> str:
    return re.sub(r"[A-Za-z]+(?:'[A-Za-z]+)?", lambda m: m.group(0) if m.group(0).upper() == "DP" else m.group(0)[0].upper() + m.group(0)[1:].lower(), s.strip())


def build(inp: dict) -> str:
    data = json.loads((Path(__file__).resolve().parent / "data-dp4.json").read_text(encoding="utf-8"))
    text = "\n\n".join(data["Chunks"])

    text = re.sub(r"_firstname", f"**{name_case(inp['firstname'])}**", text)
    lines = []
    for idx, chunk in enumerate(text.split("\n\n")):
        if 1 <= idx <= 5 and ":" in chunk:
            area, rest = chunk.split(":", 1)
            area_nc = name_case(area)
            val = inp.get("domains", {}).get(area.strip()) or inp.get("domains", {}).get(area_nc)
            if val:
                rest = rest.replace("??", name_case(str(val)), 1)
            chunk = f"{area_nc}: {rest.strip()}"
        elif idx == 7 and "overall_classification" in inp:
            chunk = chunk.replace("??", name_case(inp["overall_classification"]), 1)
        lines.append(chunk)

    out = re.sub(r"\bt-?score\b", "T-Score", "\n\n".join(lines), flags=re.IGNORECASE)
    return re.sub(r" {2,}", " ", out).strip()


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("-i", "--input", help="Input JSON path (reads stdin if omitted)")
    a = p.parse_args()
    data = json.loads(Path(a.input).read_text(encoding="utf-8")) if a.input else json.load(sys.stdin)
    print(build(data))
