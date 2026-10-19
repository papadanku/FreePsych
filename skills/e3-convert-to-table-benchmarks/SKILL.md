---
name: e3-convert-to-table-benchmarks
description: "Converts raw assessment data into a standardized Markdown table with benchmark names, seasons, bolded numeric scores and percentiles, and missing data handling. Use when the user asks to format assessment data or benchmark results into a table."
---

# Benchmark Table Formatter

Converts raw assessment data into a formatted Markdown table following strict structural, formatting, and missing data rules.

## When to Use

Use this skill when asked to format raw assessment data into a Markdown table with specific columns for Benchmark Name and Season, Score, Percentile, and Placement.

## Instructions

1. Accuracy: Do not alter benchmark names or descriptions.
2. Formatting:
    - Bold all numeric scores and percentile ranks (e.g., **95**).
    - Use the format "Benchmark Name (Season)" for the first column (where Season is Fall, Winter, or Spring).
3. Headers:
    - Include the header row: `| Benchmark Name (Season Name) | Score | Percentile | Placement |`
    - Include the alignment row: `| :--- | :---: | :---: | :---: |`
4. Missing Data: Fill every empty cell with a double dash `--`.
5. Structure & Order: Maintain the exact order of the data as provided by the user.
6. Style: Do not include additional conversational text; provide only the generated table.
