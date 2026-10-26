---
name: e6-1-draft-interpretation-basc
description: Generate professional BASC-3 social-emotional interpretation narratives for psychoeducational reports. Use when drafting psychoeducational evaluation reports requiring BASC-3 interpretation.
---

# BASC-3 Interpretation Narrative Generator

Use this skill to generate a formal, technical narrative for the "Social-Emotional" section of a psychoeducational report using the Behavior Assessment System for Children, Third Edition (BASC-3) assessment templates.

## Available Template Files

This skill includes three template files in its resource directory:

1. `assets/template-interpretation-basc-multi-rater-scale.md`: Multi-rater (Parent & Teacher) evaluation narrative template.
2. `assets/template-interpretation-basc-self-rater-scale.md`: Self-Report of Personality (SRP) template for adolescents/older examinees.
3. `assets/template-interpretation-basc-self-rater-scale-child.md`: Self-Report of Personality (SRP) template for children.

Refer to these template files to select and populate the appropriate structure based on the raters provided (Multi-Rater vs. Self-Report Child vs. Self-Report Adolescent).

## Instructions for AI

You are a School Psychologist Assistant. Your task is to process raw BASC-3 scores and rater information to complete a professional, report-ready narrative using the appropriate template file structure.

## Classification & Formatting Rules

- **Classification Ranges**:
    - **Clinical & Composite Scales** (Externalizing Problems, Internalizing Problems, School Problems, Inattention/Hyperactivity, Behavioral Symptoms Index, Aggression, Conduct Problems, Anxiety, Depression, Somatization, Attention Problems, Learning Problems, Atypicality, Withdrawal):
        - **<= 59**: Average
        - **60–69**: At-Risk (\*)
        - **>= 70**: Clinically Significant (\*\*)
    - **Adaptive Scales & Composites** (Adaptive Behavior, Personal Adjustment, Adaptability, Social Skills, Leadership, Activities of Daily Living, Functional Communication, Study Skills):
        - **>= 41**: Average
        - **31–40**: At-Risk (\*)
        - **<= 30**: Clinically Significant (\*\*)
- **Data Insertion Rules**:
    - **Bold** all numeric scores (e.g., T-Score = **65**).
    - **Bold** the student's name (`_firstname`) every time it appears in narrative text.
    - Append an asterisk (`*`) for **At-Risk** scores and double asterisks (`**`) for **Clinically Significant** scores next to classifications or scores as dictated by template format.
    - Dynamically replace all template placeholders (`_firstname`, `_boy/girl`, `_he/she`, `_He/She`, `_him/her`, `_His/Her`, `_rater1`, `_rater2`, `[Classification]`, `[??]`, bracketed qualitative descriptions).
- **Multi-Rater Dynamic Handling**:
    - Adjust narrative sections to match the actual number and identity of raters (e.g., single parent, single teacher, or multi-rater).
    - Ensure all pronoun and gender references match the student's profile.
