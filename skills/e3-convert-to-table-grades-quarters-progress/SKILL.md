---
name: e3-convert-to-table-grades-quarters-progress
description: "Convert raw grade data into a professional Markdown table. Use when the user wants to format grade data, report cards, or quarterly academic marks into a standard Markdown table with center-aligned grade columns, bolded grades, and missing data handled by double dashes."
---

# Student Grade Table Formatter

Convert raw grade data into a structured Markdown table using the specified format, formatting rules, and consistency guidelines.

## When to Use

Use this skill when the user provides raw grade data, report card data, or quarterly marks and asks to format them into a structured Markdown table.

## Rules & Formatting

1. Categorization:
    - If the data includes specific grade levels or subject headers, keep them as part of the "Course" description.
2. Consistency:
    - Keep the courses in the exact order they appear in the raw data.
    - Do not alter course titles or descriptions.
3. Formatting Grades:
    - Bold every letter grade or completion status (e.g., **A**, **F**, **P**, **In Progress**).
4. Missing Data:
    - Fill every empty cell with a double dash `--`.
5. Table Structure & Header:
    - Include the exact header: `| Course | QTR 1 | PRG 1 | QTR 2 | PRG 2 | QTR 3 | PRG 3 | QTR 4 | PRG 4 |`
    - Include the alignment row: `| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |`

