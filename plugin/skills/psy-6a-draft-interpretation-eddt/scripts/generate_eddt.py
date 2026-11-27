#!/usr/bin/env python3
"""Short EDDT narrative builder: loads JSON chunks, replaces placeholders, fills scores/classifications."""

import argparse, json, re, sys
from pathlib import Path


def name_case(s: str) -> str:
    return re.sub(r"[A-Za-z]+(?:'[A-Za-z]+)?", lambda m: m.group(0) if m.group(0).upper() in {"EDDT", "ED", "IDEA", "MOT", "TC", "IE", "PA", "REL", "IBF", "PM", "DEP", "FEARS", "TOTAL", "ADHD", "SM", "SEVERITY", "IMPACT"} else m.group(0)[0].upper() + m.group(0)[1:].lower(), s.strip())


def classify(score: float, table: dict) -> str:
    for label, rule in table.items():
        if (rule.startswith("<=") and score <= float(rule[2:])) or (rule.startswith(">=") and score >= float(rule[2:])) or ("-" in rule and float(rule.split("-")[0]) <= score <= float(rule.split("-")[1])):
            return name_case(label)
    return "Unclassified"


def build(inp: dict) -> str:
    data = json.loads((Path(__file__).resolve().parent / "data-eddt.json").read_text(encoding="utf-8"))
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
    for k, v in repls.items():
        text = re.sub(re.escape(k), v, text)

    char_tbl = data["Classifications"]["Characteristic Scales (REL, IBF, PM/DEP, FEARS, TOTAL)"]
    res_tbl = data["Classifications"]["Resilience Scales T-Score Range: Qualitative Label"]

    lines = []
    for idx, chunk in enumerate(text.split("\n\n")):
        if idx == 2:
            val = inp.get("validity", {})
            chunk = chunk.replace("[Acceptable/Caution]", name_case(val.get("parent", "Acceptable")), 1).replace("[Acceptable/Caution]", name_case(val.get("teacher", "Acceptable")), 1)
        elif idx == 3:
            for k in ["TC", "IE", "PA"]:
                mv = inp.get("motivation", {}).get(k, {})
                if "score" in mv:
                    rng = name_case(mv["range"]) if "range" in mv else classify(float(mv["score"]), res_tbl)
                    chunk = chunk.replace("??", f"**{mv['score']}**", 1).replace("??", rng, 1)
        elif 4 <= idx <= 8 and ":" in chunk:
            area, rest = chunk.split(":", 1)
            code = re.search(r"\(([^)]+)\)", area).group(1)
            sv = inp.get("characteristic_scales", {}).get(code, {})
            if "parent" in sv and "teacher" in sv:
                p_cls, t_cls = classify(float(sv["parent"]), char_tbl), classify(float(sv["teacher"]), char_tbl)
                cls_str = p_cls if p_cls == t_cls else f"{p_cls} (Parent) and {t_cls} (Teacher)"
                rest = rest.replace("??", f"**{sv['parent']}**", 1).replace("??", f"**{sv['teacher']}**", 1).replace("[Classification]", cls_str, 1)
            chunk = f"{name_case(area)}: {rest.strip()}"
        elif idx >= 9 and ":" in chunk:
            area, rest = chunk.split(":", 1)
            code = re.search(r"\(([^)]+)\)", area).group(1)
            cv = inp.get("clusters", {}).get(code, {})
            if "raw_score" in cv:
                rest = rest.replace("??", f"**{cv['raw_score']}**", 1)
            if "present" in cv:
                rest = rest.replace("[possible presence/absence]", "possible presence" if cv["present"] else "absence").replace("[are/are not]", "are" if cv["present"] else "are not")
            if "description" in cv:
                rest = re.sub(r"\[Describe Parent/Teacher .*?\]", cv["description"], rest)
            chunk = f"{name_case(area)}: {rest.strip()}"
        lines.append(chunk)

    out = re.sub(r"\bt-?score\b", "T-Score", "\n\n".join(lines), flags=re.IGNORECASE)
    return re.sub(r" {2,}", " ", out).strip()


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("-i", "--input", help="Input JSON path (reads stdin if omitted)")
    a = p.parse_args()
    data = json.loads(Path(a.input).read_text(encoding="utf-8")) if a.input else json.load(sys.stdin)
    print(build(data))
