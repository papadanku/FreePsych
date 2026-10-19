---
name: e3-convert-to-table-grades-quarter-progress
description: "Convert raw grade data into a professional Markdown table. Use when the user wants to format grade data, report cards, or quarterly academic marks into a standard Markdown table with center-aligned grade columns, bolded grades, and missing data handled by double dashes."
---

# Format Grade Table

Convert raw grade data into a professional Markdown table following specific structural, formatting, and stylistic rules.

## Formatting Rules

1. Alignment: Center-align all grade columns (QTR 1 through QTR 4).
2. Course Structure: Keep the courses in the exact order provided in the data. Do not alter or shorten area descriptions.
3. Grade Highlighting: Bold every letter grade or completion status (e.g., **A**, **B**, **P**, **NM**).
4. Headers:
    - Include the header: `| Area | QTR 1 | QTR 2 | QTR 3 | QTR 4 |`
    - Include the alignment row: `| :--- | :---: | :---: | :---: | :---: |`
    - Separate major subject areas (e.g., Language Arts, Math, Specials) with a dedicated header row within the table if applicable.
5. Missing Data: Fill every empty cell with a double dash (`--`).
6. Style Output: Provide only the Markdown table. Do not include introductory or concluding conversational text.

