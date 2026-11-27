#!/usr/bin/env python3
"""Short Vineland-3 narrative builder: loads JSON chunks, replaces placeholders, fills scores/classifications."""

import argparse, json, re, sys
from pathlib import Path


def name_case(s: str) -> str:
    return re.sub(r"[A-Za-z]+(?:'[A-Za-z]+)?", lambda m: m.group(0) if m.group(0).upper() == "SS" else m.group(0)[0].upper() + m.group(0)[1:].lower(), s.strip())


def classify(score: float, table: dict) -> str:
    for label, rule in table.items():
        if ("-" in rule and float(rule.split("-")[0]) <= score <= float(rule.split("-")[1])) or (rule.startswith("<=") and score <= float(rule[2:])) or (rule.startswith(">=") and score >= float(rule[2:])):
            return name_case(label)
    return "Unclassified"


def build(inp: dict) -> str:
    data = json.loads((Path(__file__).resolve().parent / "data-vineland.json").read_text(encoding="utf-8"))
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
    repls["[Raters 2 and 3]"] = f"{repls['[Rater 2]']} and {repls['[Rater 3]']}"
    for k, v in repls.items():
        text = re.sub(re.escape(k), v, text)

    ss_tbl = data["Classifications"]["Standard Scores (Domains)"]
    v_tbl = data["Classifications"]["v-Scale Scores (Subdomains)"]
    dom_subs = {"Communication": ["Receptive", "Expressive", "Written"], "Socialization": ["Interpersonal", "Play", "Coping"], "Daily Living Skills": ["Personal", "Domestic", "Community"], "Motor Skills": ["Gross Motor", "Fine Motor"]}

    lines = []
    for chunk in text.split("\n\n"):
        if ":" in chunk:
            area, rest = chunk.split(":", 1)
            area_nc = name_case(area)
            dscores = inp.get("domains", {}).get(area.strip()) or inp.get("domains", {}).get(area_nc, {})
            for key in ["rater1", "rater2", "rater3"]:
                if key in dscores:
                    sc = dscores[key]
                    rest = rest.replace("[Classification]", classify(float(sc), ss_tbl), 1).replace("??", f"**{sc}**", 1)
            for sub in dom_subs.get(area_nc, []):
                sv = inp.get("subdomains", {}).get(sub, {}).get("rater1")
                if sv is not None:
                    rest = rest.replace("[Classification]", classify(float(sv), v_tbl), 1).replace("??", f"**{sv}**", 1)
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
