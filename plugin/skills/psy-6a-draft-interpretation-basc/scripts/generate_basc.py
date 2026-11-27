#!/usr/bin/env python3
"""Short BASC-3 narrative builder: loads JSON chunks, replaces placeholders, fills scores/classifications."""

import argparse, json, re, sys
from pathlib import Path


def name_case(s: str) -> str:
    return re.sub(r"[A-Za-z]+(?:'[A-Za-z]+)?", lambda m: m.group(0) if m.group(0).upper() in {"BASC", "BSI", "ESI", "SRP", "TRS", "PRS"} else m.group(0)[0].upper() + m.group(0)[1:].lower(), s.strip())


def classify(score: float, table: dict) -> str:
    for label, rule in table.items():
        if (rule.startswith("<=") and score <= float(rule[2:])) or (rule.startswith(">=") and score >= float(rule[2:])) or ("-" in rule and float(rule.split("-")[0]) <= score <= float(rule.split("-")[1])):
            return name_case(label)
    return "Unclassified"


def build(inp: dict) -> str:
    mode = inp.get("mode", "multi-rater").lower()
    fname = "data-basc-self-rater-scale.json" if mode in {"self", "self-rater", "srp"} else "data-basc-multi-rater-scale.json"
    data = json.loads((Path(__file__).resolve().parent / fname).read_text(encoding="utf-8"))
    text = "\n\n".join(data["Chunks"])

    pronouns = {"male": ("He", "he", "Him", "him", "His", "his"), "female": ("She", "she", "Her", "her", "Her", "her")}.get(
        inp.get("gender", "").lower(), ("They", "they", "Them", "them", "Their", "their")
    )
    repls = {
        "_firstname": f"**{name_case(inp['firstname'])}**",
        "_He/She": pronouns[0], "_he/she": pronouns[1],
        "_Him/Her": pronouns[2], "_him/her": pronouns[3],
        "_His/Her": pronouns[4], "_his/her": pronouns[5],
        "_rater1": name_case(inp.get("raters", {}).get("rater1", "Rater 1")),
        "_rater2": name_case(inp.get("raters", {}).get("rater2", "Rater 2")),
    }
    for k, v in repls.items():
        text = re.sub(re.escape(k), v, text)

    cls_tables = data["Classifications"]
    clin_tbl = cls_tables["Clinical & Composite Scales"]
    adap_tbl = cls_tables.get("Adaptive Scales & Composites") or cls_tables.get("Personal Adjustment Scales & Composites")
    adap_names = {"adaptive behavior", "adaptability", "social skills", "leadership", "activities of daily living", "functional communication", "study skills", "personal adjustment", "relations with parents", "interpersonal relations", "self-esteem", "self-reliance"}

    lines = []
    for chunk in text.split("\n\n"):
        if ":" in chunk:
            area, rest = chunk.split(":", 1)
            area_nc = name_case(area)
            tbl = adap_tbl if area.strip().lower() in adap_names else clin_tbl
            scores = inp.get("scores", {})
            val = scores.get(area.strip()) or scores.get(area_nc)
            if isinstance(val, dict):
                for key in ["rater1", "rater2"]:
                    if key in val:
                        sc = val[key]
                        rest = rest.replace("[Classification]", classify(float(sc), tbl), 1).replace("[??]", f"**{sc}**", 1)
            elif val is not None:
                rest = rest.replace("[Classification]", classify(float(val), tbl), 1).replace("[??]", f"**{val}**", 1)
            if area.strip().lower() in {"adaptive behavior", "personal adjustment"}:
                for sub in ["Adaptability", "Social Skills", "Leadership", "Activities of Daily Living", "Functional Communication", "Study Skills", "Relations With Parents", "Interpersonal Relations", "Self-Esteem", "Self-Reliance"]:
                    sv = scores.get(sub)
                    if isinstance(sv, dict):
                        for key in ["rater1", "rater2"]:
                            if key in sv:
                                rest = rest.replace("[Classification]", classify(float(sv[key]), adap_tbl), 1).replace("[??]", f"**{sv[key]}**", 1)
                    elif sv is not None:
                        rest = rest.replace("[Classification]", classify(float(sv), adap_tbl), 1).replace("[??]", f"**{sv}**", 1)
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
