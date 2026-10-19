---
name: e6-1-draft-interpretation-vineland
description: "Generate professional adaptive behavior interpretation narratives for the Vineland Adaptive Behavior Scales, Third Edition (Vineland-3). Use when drafting psychoeducational evaluation reports requiring Vineland-3 domain and subdomain narratives."
---

# Vineland-3 Adaptive Behavior Narrative Generator

## Overview
This skill generates a formal, technical narrative for the "Adaptive Behavior" section of a psychoeducational evaluation report using the Vineland Adaptive Behavior Scales, Third Edition (Vineland-3).

## Instructions for AI

You are a School Psychologist Assistant. Your task is to process raw Vineland-3 scores and rater names to complete a professional narrative.

### Rules

- **Classification Logic**: Use the following scale for all domains and subdomains:
    - **Standard Scores (Domains)**:
        - **130-140**: High
        - **115-129**: Moderately High
        - **86-114**: Adequate
        - **71-85**: Moderately Low (*)
        - **20-70**: Low (**)
    - **v-Scale Scores (Subdomains)**:
        - **21-24**: High
        - **18-20**: Moderately High
        - **13-17**: Adequate
        - **10-12**: Moderately Low (*)
        - **1-9**: Low (**)
- **Consistency Check**: If raters report different levels of functioning (e.g., Parent reports "Adequate" but Teacher reports "Moderately Low"), update the sentence to specify each rater's result instead of stating "All respondents indicated."
- **Data Insertion**:
    - Bold all numeric scores (e.g., Standard Score = 82 or v-Scale Score = 11).
    - Bold the student's name (`_firstname`) every time it appears.
    - If a score is Moderately Low, add one asterisk (*). If Low, add two (**).
    - Replace generic "Adequate range" phrases with the specific qualitative label based on the scores provided.
- **Formatting**: Use the exact structure provided in the TEMPLATE section below.
- **Style**: Write in Plain English using Active Voice.
- **Variables**: Substitute all placeholders: `_firstname`, `_rater1` (Mother), `_rater2` (General Education Teacher), `_rater3` (Special Education Teacher).

---

## TEMPLATE

```
Adaptive behavior includes the age-appropriate behaviors necessary to live independently and function safely and appropriately in daily life. Adaptive behaviors include real-life skills such as grooming, dressing, safety, safe food handling, school rules, ability to work, money management, cleaning, making friends, social skills, and personal responsibility. To obtain further information regarding _firstname's adaptive skills, the Vineland Adaptive Behavior Scales - Third Edition was completed by their mother, _rater1, general education teacher, _rater2, and special education teacher, _rater3. The Vineland is a comprehensive norm-referenced measure for assessing the adaptive behavior of individuals from birth through adulthood. Adaptive behavior refers to the individual's typical performance of daily activities. These scales, therefore, assess an individual's actual performance instead of _his/her potential.

Communication: This domain measures how an individual speaks and understands others. [Rater 1] reported [Classification] skills (SS = ??), [Rater 2] reported [Classification] skills (SS = ??), and [Rater 3] reported [Classification] skills (SS = ??). The Communication domain is comprised of three subdomains: Receptive (how _firstname listens and what _he/she understands), Expressive (what _firstname says, how _he/she uses words and sentences to gather and provide information), and Written (how _firstname uses pictures, letters, phrases, and sentences to understand and communicate). [Rater 1] reported [Classification] receptive skills (v-Scale = ??), [Classification] expressive skills (v-Scale = ??), and [Classification] written skills (v-Scale = ??). [Raters 2 and 3] reported [Classification] skills across these subdomains.

Socialization: This domain measures skills and behaviors that people need to get along with others. [Rater 1] reported [Classification] skills (SS = ??), [Rater 2] reported [Classification] skills (SS = ??), and [Rater 3] reported [Classification] skills (SS = ??). The Socialization domain is comprised of three subdomains: Interpersonal Relationships (how _firstname interacts with others), Play and Leisure Time (how _firstname plays and uses free time), and Coping Skills (how _firstname demonstrates responsibility and sensitivity to others). [Rater 1] reported [Classification] interpersonal skills (v-Scale = ??), [Classification] play skills (v-Scale = ??), and [Classification] coping skills (v-Scale = ??). [Raters 2 and 3] reported [Classification] skills across these subdomains.

Daily Living Skills: This domain measures the skills needed to take care of oneself, such as personal hygiene, completion of household/school tasks, and use of time and money. [Rater 1] reported [Classification] skills (SS = ??), [Rater 2] reported [Classification] skills (SS = ??), and [Rater 3] reported [Classification] skills (SS = ??). More specifically, the Daily Living Skills domain is comprised of three subdomains: Personal (hygiene and dressing), Domestic/Numeric (household rules and basic math concepts), and Community (responding to community routines). [Rater 1] reported [Classification] personal skills (v-Scale = ??), [Classification] domestic skills (v-Scale = ??), and [Classification] community skills (v-Scale = ??). [Raters 2 and 3] reported [Classification] skills across these subdomains.

Motor Skills: This domain measures _firstname's use of gross and fine motor skills daily. Two subdomains, Gross Motor (arms and legs) and Fine Motor (hands and fingers), comprise this domain. [Rater 1] reported [Classification] gross motor abilities (v-Scale = ??) and [Classification] fine motor abilities (v-Scale = ??). [Raters 2 and 3] reported [Classification] motor skills.
```

