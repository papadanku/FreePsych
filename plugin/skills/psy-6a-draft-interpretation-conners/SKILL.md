---
name: psy-6a-draft-interpretation-conners
description: Generate professional ADHD and behavioral interpretation narratives for the Conners 4th Edition (Conners-4) assessment. Use when drafting psychoeducational evaluation reports requiring Conners-4 domain narratives.
---

# Conners-4 ADHD Narrative Generator

Use this skill to generate a formal, technical narrative for the "ADHD/Behavioral" section of a psychoeducational report using `scripts/generate_conners.py` and `scripts/data-conners.json`.

## Workflow

1. **Extract Context & Scores**: Gather the student's first name, gender/pronouns, rater names, and T-Scores for each Conners-4 scale from the evaluation context.
2. **Run the Generator Script**: Pass a JSON payload matching the schema below via `--input <file.json>` or `stdin`:

    ```bash
    python3 scripts/generate_conners.py --input <input_json_path>
    ```

    The script loads chunks from `scripts/data-conners.json` (with a blank line between chunks), performs regex find-and-replace for `_firstname`, pronouns, and rater placeholders, fills in T-Scores and classifications, and applies Name Case formatting.

3. **LLM Output Revisions**: Review the script output and revise as needed:
    - Adjust rater lists and scale sentences if fewer or different raters were provided.
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
