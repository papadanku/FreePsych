---
name: psy-6a-draft-interpretation-gars-3
description: "Generate professional autism assessment interpretation narratives for the Gilliam Autism Rating Scale, Third Edition (GARS-3). Use when drafting psychoeducational evaluation reports requiring GARS-3 subscale and Autism Index narratives."
---

# Gilliam Autism Rating Scale, Third Edition (GARS-3) Narrative Generator

Use this skill to generate a formal, technical narrative for the "Autism Assessment" section of a psychoeducational report using `scripts/generate_gars3.py` and `scripts/data-gars-3.json`.

## Workflow

1. **Extract Context & Scores**: Gather the student's first name, rater names, subscale Scaled Scores and Percentile Ranks, and Autism Index scores.
2. **Run the Generator Script**: Pass a JSON payload matching the schema below via `--input <file.json>` or `stdin`:

    ```bash
    python3 scripts/generate_gars3.py --input <input_json_path>
    ```

    The script loads chunks from `scripts/data-gars-3.json` (with a blank line between chunks), performs regex find-and-replace for `_firstname` and rater placeholders, fills in scores and Autism Index classifications, and applies Name Case formatting.

3. **LLM Output Revisions**: Review the script output and revise as needed:
    - Adjust rater lists and sentences if fewer or different raters were provided.
    - Ensure consistency checks reflect differing rater Autism Index levels accurately.
    - Enforce **Name Case** for Raters' names, Classification Names (`Unlikely`, `Probable`, `Very Likely`), `T-Score`, and Area Names.

## Input JSON Schema

```json
{
    "firstname": "<student_firstname>",
    "raters": {
        "rater1": "<rater1_name>",
        "rater2": "<rater2_name>",
        "rater3": "<rater3_name>"
    },
    "scores": {
        "<Subscale Name>": {
        "rater1": {"ss": "<scaled_score>", "percentile": "<percentile>"},
        "rater2": {"ss": "<scaled_score>", "percentile": "<percentile>"},
        "rater3": {"ss": "<scaled_score>", "percentile": "<percentile>"}
        }
    },
    "autism_index": {
        "rater1": "<index_score>",
        "rater2": "<index_score>",
        "rater3": "<index_score>"
    }
}
```
