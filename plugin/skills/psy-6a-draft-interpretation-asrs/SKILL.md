---
name: psy-6a-draft-interpretation-asrs
description: Generate professional autism assessment interpretation narratives for the Autism Spectrum Rating Scales (ASRS). Use when drafting psychoeducational evaluation reports requiring ASRS domain narratives.
---

# Autism Spectrum Rating Scales (ASRS) Narrative Generator

Use this skill to generate a formal, technical narrative for the "Autism Assessment" section of a psychoeducational report using `scripts/generate_asrs.py` and `scripts/data-asrs.json`.

## Workflow

1. **Extract Context & Scores**: Gather the student's first name, gender/pronouns, rater names, and T-Scores for each ASRS scale from the evaluation context.
2. **Run the Generator Script**: Pass a JSON payload matching the schema below via `--input <file.json>` or `stdin`:

    ```bash
    python3 scripts/generate_asrs.py --input <input_json_path>
    ```

    The script loads chunks from `scripts/data-asrs.json` (with a blank line between chunks), performs regex find-and-replace for `_firstname`, pronouns, and rater placeholders, fills in T-Scores and classifications, and applies Name Case formatting.

3. **LLM Output Revisions**: Review the script output and revise as needed:
    - Adjust rater lists and sentences if fewer or different raters were provided.
    - Ensure consistency checks reflect differing rater classifications accurately.
    - Enforce **Name Case** for Raters' names, Classification Names (`Low`, `Average`, `Slightly Elevated (*)`, `Elevated (**)`, `Very Elevated (***)`), `T-Score`, and Area Names.

## Input JSON Schema

```json
{
    "firstname": "<student_firstname>",
    "gender": "<male|female|they>",
    "raters": {
        "rater1": "<rater1_name>",
        "rater2": "<rater2_name>",
        "rater3": "<rater3_name>"
    },
    "scores": {
        "<Area Name>": {"rater1": "<t_score>", "rater2": "<t_score>", "rater3": "<t_score>"}
    }
}
```
