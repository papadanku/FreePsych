---
name: psy-3-convert-grades-to-table
description: Convert raw grade data into a structured Markdown table supporting both quarters-only and quarters-with-progress formats. Use when the user wants to format grade data, report cards, quarterly academic marks, or progress report marks into a standard Markdown table with center-aligned grade columns, bolded grades, and double dashes for missing data.
---

# psy-3-convert-grades-to-table

Convert raw grade data or report card marks into a structured Markdown table, automatically selecting either the quarters-only format or the quarters-with-progress format based on the input data.

## When to Use

- The user provides raw grade data, report card exports, or quarterly academic marks and asks to format them into a Markdown table.
- The data contains quarterly marks (`QTR 1` through `QTR 4`) with or without progress report marks (`PRG 1` through `PRG 4`).

## Steps

1. **Detect the Table Format**
    - **Quarters Only**: Use `assets/quarters-template.md` (`Area` + `QTR 1` to `QTR 4`) when the raw data only contains quarterly marks.
    - **Quarters and Progress**: Use `assets/quarters-progress-template.md` (`Course` + `QTR 1`/`PRG 1` through `QTR 4`/`PRG 4`) when the raw data includes progress report (`PRG`) marks alongside quarterly marks.
2. **Preserve Order and Course Descriptions**
    - Keep all courses or areas in the exact order they appear in the raw data.
    - Do not alter, abbreviate, or shorten course titles or area descriptions.
    - For **Quarters Only**, separate major subject areas (e.g., Language Arts, Math, Specials) with a dedicated header row within the table when applicable.
    - For **Quarters and Progress**, keep specific grade levels or subject headers as part of the `Course` description if present in the source data.
3. **Format Grades and Missing Cells**
    - Bold every letter grade or completion status (e.g., **A**, **B**, **F**, **P**, **NM**, **In Progress**).
    - Fill every empty or missing cell with a double dash (`--`).
    - Left-align the first column (`:---`) and center-align all grade and progress columns (`:---:`).
4. **Output Only the Table**
    - Return only the formatted Markdown table without introductory or concluding conversational text.

## Gotchas

- Do not mix up the first-column header: use `Area` for quarters-only tables and `Course` for quarters-with-progress tables.
- Never leave blank cells or `N/A`; always use `--` for missing marks.
- Do not bold `--` in empty cells; only bold actual grades or completion statuses.
