---
name: psy-6a-draft-interpretation-basc
description: Generate professional BASC-3 social-emotional interpretation narratives for psychoeducational reports. Use when drafting psychoeducational evaluation reports requiring BASC-3 interpretation.
---

# BASC-3 Interpretation Narrative Generator

Use this skill to generate a formal, technical narrative for the "Social-Emotional" section of a psychoeducational report using `scripts/generate_basc.py`.

## Workflow

1. **Select Mode & Extract Data**: Choose `"multi-rater"` (`scripts/data-basc-multi-rater-scale.json`) or `"self-rater"` (`scripts/data-basc-self-rater-scale.json`). Gather the student's first name, gender/pronouns, rater names, and T-Scores.
2. **Run the Generator Script**: Pass a JSON payload matching the schema below via `--input <file.json>` or `stdin`:

    ```bash
    python3 scripts/generate_basc.py --input <input_json_path>
    ```

    The script loads chunks from the `.json` file (with a blank line between chunks), performs regex find-and-replace for `_firstname`, pronouns, and rater placeholders, fills in T-Scores and classifications, and applies Name Case formatting.

3. **LLM Output Revisions**: Review the script output and revise as needed:
    - Adjust rater references and validity statements to match the actual raters and validity results.
    - Remove or adapt any unadministered scales (e.g., `Sensation Seeking` and `Somatization` for adolescent SRP).
    - Enforce **Name Case** for Raters' names, Classification Names (`Average`, `At-Risk (*)`, `Clinically Significant (**)`), `T-Score`, and Area Names.

## Input JSON Schema

```json
{
    "mode": "<multi-rater|self-rater>",
    "firstname": "<student_firstname>",
    "gender": "<male|female|they>",
    "raters": {
        "rater1": "<rater1_name>",
        "rater2": "<rater2_name>"
    },
    "scores": {
        "<Area Name>": {"rater1": "<t_score>", "rater2": "<t_score>"}
    }
}
```

*(In `self-rater` mode, map each `<Area Name>` directly to `<t_score>`.)*
