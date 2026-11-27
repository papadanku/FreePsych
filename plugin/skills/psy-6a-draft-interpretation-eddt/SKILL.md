---
name: psy-6a-draft-interpretation-eddt
description: Generate professional social-emotional interpretation narratives for the Emotional Disturbance Decision Tree (EDDT) assessment. Use when drafting psychoeducational evaluation reports requiring EDDT domain narratives.
---

# EDDT Social-Emotional Narrative Generator

Use this skill to generate a formal, technical narrative for the "Emotional Disturbance Decision Tree (EDDT)" section of a psychoeducational report using `scripts/generate_eddt.py` and `scripts/data-eddt.json`.

## Workflow

1. **Extract Context & Scores**: Gather the student's first name, gender/pronouns, Parent/Teacher validity ratings, Motivation Cluster (`TC`, `IE`, `PA`), Characteristic Scale T-Scores (`REL`, `IBF`, `PM/DEP`, `FEARS`, `TOTAL`), and Cluster Raw Scores (`ADHD`, `POSSIBLE PSYCHOSIS`, `SM`, `SEVERITY`, `IMPACT`).
2. **Run the Generator Script**: Pass a JSON payload matching the schema below via `--input <file.json>` or `stdin`:

    ```bash
    python3 scripts/generate_eddt.py --input <input_json_path>
    ```

    The script loads chunks from `scripts/data-eddt.json` (with a blank line between chunks), performs regex find-and-replace for `_firstname` and pronouns, fills in scores and classifications, and applies Name Case formatting.

3. **LLM Output Revisions**: Review the script output and revise as needed:
    - Adjust by rater count if only one rater was administered.
    - Refine qualitative descriptions (e.g., `SM` differences regarding rules, authority, and empathy).
    - Enforce **Name Case** for Raters' names, Classification Names (`Normal`, `Mild At-Risk`, `Moderate Clinical`, `High Clinical`, `Very High Clinical`), `T-Score`, and Area Names.

## Input JSON Schema

```json
{
    "firstname": "<student_firstname>",
    "gender": "<male|female|they>",
    "validity": {"parent": "<Acceptable|Caution>", "teacher": "<Acceptable|Caution>"},
    "motivation": {
        "TC": {"score": "<score>", "range": "<range_label>"},
        "IE": {"score": "<score>", "range": "<range_label>"},
        "PA": {"score": "<score>", "range": "<range_label>"}
    },
    "characteristic_scales": {
        "REL": {"parent": "<t_score>", "teacher": "<t_score>"}
    },
    "clusters": {
        "ADHD": {"raw_score": "<raw_score>", "present": "<true|false>"},
        "SM": {"raw_score": "<raw_score>", "description": "<sm_summary>"}
    }
}
```
