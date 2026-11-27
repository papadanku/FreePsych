---
name: psy-6a-draft-interpretation-dp4
description: Generate professional developmental interpretation narratives for the Developmental Profile 4 (DP-4) assessment. Use when drafting psychoeducational evaluation reports requiring DP-4 developmental domain narratives.
---

# Developmental Profile 4 (DP-4) Interpretation Drafting

Use this skill to generate a formal, technical narrative for the DP-4 assessment using `scripts/generate_dp4.py` and `scripts/data-dp4.json`.

## Workflow

1. **Extract Context & Domain Ratings**: Gather the student's first name, domain classifications (`Physical`, `Adaptive`, `Social-Emotional`, `Cognitive`, `Communication`), overall classification, and observed parent-reported skills.
2. **Run the Generator Script**: Pass a JSON payload matching the schema below via `--input <file.json>` or `stdin`:

    ```bash
    python3 scripts/generate_dp4.py --input <input_json_path>
    ```

    The script loads chunks from `scripts/data-dp4.json` (with a blank line between chunks), performs regex find-and-replace for `_firstname`, fills in domain and overall classifications, and applies Name Case formatting.

3. **LLM Output Revisions**: Review the script output and revise as needed:
    - Update the parent-reported strengths/challenges and qualitative descriptions to match the student's actual evaluation data.
    - Enforce **Name Case** for Raters' names, Classification Names, `T-Score`, and Area Names (`Physical`, `Adaptive`, `Social-Emotional`, `Cognitive`, `Communication`).

## Input JSON Schema

```json
{
    "firstname": "<student_firstname>",
    "overall_classification": "<classification>",
    "domains": {
        "Physical": "<classification>",
        "Adaptive": "<classification>",
        "Social-Emotional": "<classification>",
        "Cognitive": "<classification>",
        "Communication": "<classification>"
    }
}
```
