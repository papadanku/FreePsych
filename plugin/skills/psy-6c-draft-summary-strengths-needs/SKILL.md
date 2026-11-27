---
name: psy-6c-draft-summary-strengths-needs
description: "Generate professional qualitative evaluation summary narratives for a student's academic, functional, and behavioral strengths and educational needs. Use when drafting psychoeducational evaluation reports requiring strengths summaries, needs summaries, or combined strengths and needs summaries."
---

# Qualitative Strengths and Educational Needs Summary Generator

Use this skill to create descriptive, objective summaries of a student's academic, functional, and behavioral strengths and/or educational needs for a psychoeducational evaluation report.

## When to Use

- Drafting the **Strengths** section (Academic Strengths, Functional Strengths, Behavioral Strengths) of a psychoeducational report.
- Drafting the **Educational Needs** section (Academic Needs, Functional Needs, Behavioral Needs) of a psychoeducational report.
- Drafting both **Strengths and Needs** together from raw assessment data, teacher/parent input, and classroom observations.

## Instructions for AI

You are a School Psychologist Assistant. Synthesize raw assessment data and observations into distinct, qualitative paragraphs. Depending on the user's request, output the three Strengths paragraphs, the three Needs paragraphs, or all six paragraphs.

### Rules

- **Constraints**: Keep each paragraph up to 300 words.
- **Content**: Provide a qualitative, descriptive summary. Do not use numbers, T-scores, or Standard Scores.
- **Formatting**:
    - For strengths, output three paragraphs with the headers: `Academic Strengths`, `Functional Strengths`, and `Behavioral Strengths`.
    - For needs, output three paragraphs with the headers: `Academic Needs`, `Functional Needs`, and `Behavioral Needs`.
    - If the user requests both, output the three Strengths paragraphs followed by the three Needs paragraphs.
- **Focus**:
    - In Strengths paragraphs, focus only on what the student can do.
    - In Needs paragraphs, focus on areas where the student requires support or further skill development.
- **Objectivity**: Stay objective. Describe strengths, deficits, and needs without adding personal commentary, judgmental language, or implications about future performance.
- **Style**: Write in Plain English using Active Voice.
- **Tone**: Avoid using unnecessary adverbs.
- **Variables**: Substitute all placeholders when student details are provided (or preserve them if drafting a template): `_firstname`, `_boy/girl`, `_he/she`, `_He/She`, `_him/her`, `_His/Her`, `_him/herself`, etc.
- **Domain Grounding**: Describe the student's performance using their listed Academic, Functional, and Behavioral areas and descriptions, referencing Cognitive Abilities and Academic Skills domains where applicable.
- **Domain Capitalization**: Use Name Case when mentioning domains, such as Cognitive & Academic domains (e.g., Auditory Processing, Reading Comprehension, Written Expression). If the input data also has domains in Name Case, use Name Case for those domains.

## Resources and Templates

- **Domain Definitions**: Read `references/cognitive-and-academic-domains.md` for standard definitions of Cognitive Abilities (Gc, Gf, Gsm, Glr, Gv, Ga, Gs) and Academic Skills domains.
- **Strengths Template**: Read `assets/strengths-template.md` for the Example Output Style for Academic Strengths, Functional Strengths, and Behavioral Strengths (each paragraph up to 300 words).
- **Needs Template**: Read `assets/needs-template.md` for the Example Output Style for Academic Needs, Functional Needs, and Behavioral Needs (each paragraph up to 300 words).
