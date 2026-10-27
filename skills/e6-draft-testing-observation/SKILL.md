---
name: e6-draft-testing-observation
description: Converts testing observation notes, behavioral metrics, and subtest observations into narrative paragraph-form summaries for psychoeducational evaluation reports (Section E6 C: Observations During Testing). Use when drafting or formatting testing observation summaries for school psychologists or special education teachers.
---

# E6 Draft Testing Observation

## Summary

This skill takes raw testing observation notes or behavioral metric inputs and generates professional, objective, plain-English narrative paragraph templates for psychoeducational evaluation reports (Section E6 Part C: Observations During Testing). Templates are stored as modular files inside the `assets/` folder.

## Inputs & Requirements

The input expected by this skill includes testing observation variables such as:

- **General Behavioral Factors**: Level of conversational proficiency, Level of cooperation, Level of activity, Attention and concentration, Self-confidence, Care in responding, Response to difficult tasks.
- **Academic Subtest Observations**: Letter-Word Identification, Applied Problems, Spelling, Passage Comprehension, Calculation, Writing Samples, Word Attack, Oral Reading, Sentence Reading Fluency, Math Facts Fluency, Sentence Writing Fluency, Reading Recall, Number Matrices, or any other administered subtests.

## Key Rules

1. **Plain English & Active Voice**: Write clearly, directly, and objectively using active voice.
2. **Zero Data Omission**: Do not omit any observed area, subtest behavior, or behavioral metric provided in the input.
3. **Structured Paragraph Summaries**: Format the output into structured narrative paragraph-form templates by loading the corresponding templates from the `assets/` directory:
    - **School Psychologist**: `assets/template-school-psychologist.md`
    - **Special Education Teacher (Initial Evaluation)**: `assets/template-special-education-teacher-initial.md`
    - **Special Education Teacher (Re-Evaluation)**: `assets/template-special-education-teacher-triennial.md`

## Instructions for Execution

1. Receive raw observation metrics or placeholder values for the student's testing session.
2. Read the appropriate template file(s) from the `assets/` folder based on the required evaluator role(s).
3. Draft plain-English narrative paragraphs for each required evaluator role incorporating all observed metrics and subtest details.
