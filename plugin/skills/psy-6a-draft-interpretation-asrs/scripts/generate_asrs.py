#!/usr/bin/env python3
"""Short ASRS narrative builder: loads JSON chunks, replaces placeholders, fills scores/classifications."""

import argparse, json, re, sys
from pathlib import Path


def name_case(s: str) -> str:
    return re.sub(r"[A-Za-z]+(?:'[A-Za-z]+)?", lambda m: m.group(0) if m.group(0).upper() in {"ASRS", "DSM", "ASD"} else m.group(0)[0].upper() + m.group(0)[1:].lower(), s.strip())


def classify(score: float, table: dict) -> str:
    for label, rule in table.items():
        if (rule.startswith("<=") and score <= float(rule[2:])) or (rule.startswith(">=") and score >= float(rule[2:])) or ("-" in rule and float(rule.split("-")[0]) <= score <= float(rule.split("-")[1])):
            return name_case(label)
    return "Unclassified"


def build(inp: dict) -> str:
    data = json.loads((Path(__file__).resolve().parent / "data-asrs.json").read_text(encoding="utf-8"))
    text = "\n\n".join(data["Chunks"])

    pronouns = {"male": ("He", "he", "Him", "him", "His", "his"), "female": ("She", "she", "Her", "her", "Her", "her")}.get(
        inp.get("gender", "").lower(), ("They", "they", "Them", "them", "Their", "their")
    )
    repls = {
        "_firstname": f"**{name_case(inp['firstname'])}**",
        "_He/She": pronouns[0], "_he/she": pronouns[1],
        "_Him/Her": pronouns[2], "_him/her": pronouns[3],
        "_His/Her": pronouns[4], "_his/her": pronouns[5],
    }
    for i, key in enumerate(["rater1", "rater2", "rater3"], 1):
        rname = name_case(inp.get("raters", {}).get(key, f"Rater {i}"))
        repls[f"_rater{i}"] = rname
        repls[f"[Rater {i}]"] = rname

    for k, v in repls.items():
        text = re.sub(re.escape(k), v, text)

    lines = []
    for chunk in text.split("\n\n"):
        if ":" in chunk:
            area, rest = chunk.split(":", 1)
            area_nc = name_case(area)
            scores = inp.get("scores", {}).get(area.strip()) or inp.get("scores", {}).get(area_nc, {})
            for key in ["rater1", "rater2", "rater3"]:
                if key in scores:
                    sc = scores[key]
                    cls = classify(float(sc), data["Classifications"])
                    rest = rest.replace("[Classification]", cls, 1).replace("??", f"**{sc}**", 1)
            chunk = f"{area_nc}: {rest.strip()}"
        lines.append(chunk)

    out = re.sub(r"\bt-?score\b", "T-Score", "\n\n".join(lines), flags=re.IGNORECASE)
    return re.sub(r" {2,}", " ", out).strip()


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("-i", "--input", help="Input JSON path (reads stdin if omitted)")
    a = p.parse_args()
    data = json.loads(Path(a.input).read_text(encoding="utf-8")) if a.input else json.load(sys.stdin)
    print(build(data))
