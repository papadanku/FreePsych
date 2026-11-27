---
name: psy-6a-draft-interpretation-vineland
description: "Generate professional adaptive behavior interpretation narratives for the Vineland Adaptive Behavior Scales, Third Edition (Vineland-3). Use when drafting psychoeducational evaluation reports requiring Vineland-3 domain and subdomain narratives."
---

# Vineland-3 Adaptive Behavior Narrative Generator

Use this skill to generate a formal, technical narrative for the "Adaptive Behavior" section of a psychoeducational report using `scripts/generate_vineland.py` and `scripts/data-vineland.json`.

## Workflow

1. **Extract Context & Scores**: Gather the student's first name, gender/pronouns, rater names, Domain Standard Scores, and Subdomain v-Scale Scores.
2. **Run the Generator Script**: Pass a JSON payload matching the schema below via `--input <file.json>` or `stdin`:

    ```bash
    python3 scripts/generate_vineland.py --input <input_json_path>
    ```

    The script loads chunks from `scripts/data-vineland.json` (with a blank line between chunks), performs regex find-and-replace for `_firstname`, pronouns, and rater placeholders, fills in Domain and Subdomain scores and classifications, and applies Name Case formatting.

3. **LLM Output Revisions**: Review the script output and revise as needed:
    - Adjust rater lists and subdomain summaries if raters differ in functioning levels or if fewer raters were administered.
    - Enforce **Name Case** for Raters' names, Classification Names (`High`, `Moderately High`, `Adequate`, `Moderately Low (*)`, `Low (**)`), `T-Score`, and Area Names.

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
    "domains": {
        "<Domain Name>": {"rater1": "<std_score>", "rater2": "<std_score>", "rater3": "<std_score>"}
    },
    "subdomains": {
        "<Subdomain Name>": {"rater1": "<v_scale_score>"}
    }
}
```
