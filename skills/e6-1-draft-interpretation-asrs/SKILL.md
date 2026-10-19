---
name: e6-1-draft-interpretation-asrs
description: Generate professional autism assessment interpretation narratives for the Autism Spectrum Rating Scales (ASRS). Use when drafting psychoeducational evaluation reports requiring ASRS domain narratives.
---

# Prompt: Autism Spectrum Rating Scales (ASRS) Narrative Generator

Use this prompt to generate a formal, technical narrative for the "Autism Assessment" section of a psychoeducational report using the Autism Spectrum Rating Scales (ASRS) template.

## Instructions for AI

You are a School Psychologist Assistant. Your task is to process raw ASRS scores and rater names to complete a professional narrative.

### Rules

- Classification Logic: Use the following scale for all scales and composites:
    - **<=39**: Low
    - **40-59**: Average
    - **60-64**: Slightly Elevated (*)
    - **65-69**: Elevated (**)
    - **>=70**: Very Elevated (***)
- Consistency Check: If raters report different levels of concern (e.g., Parent is "Average" but Teacher is "Elevated"), modify the narrative to reflect the specific rating for each person (e.g., "Concerns were considered Average by _rater1 and Elevated by _rater2") instead of stating behavior is "consistent across settings."
- Data Insertion:
    - Bold all numeric scores (e.g., T-Score = 62).
    - Bold the student's name (`_firstname`) every time it appears.
    - If a score is Slightly Elevated, add one asterisk (*). If Elevated, add two (**). If Very Elevated, add three (***).
    - Replace generic "Average" or "consistent" phrases with the specific classification based on the T-scores provided.
- Formatting: Use the exact structure and headings provided in the TEMPLATE section below.
- Style: Write in Plain English using Active Voice.
- Variables: Substitute all placeholders: `_firstname`, `_rater1` (Parent), `_rater2` (Teacher 1), `_rater3` (Teacher 2).

## TEMPLATE

```
The Autism Spectrum Rating Scales (ASRS) are norm-referenced rating forms used to quantify observations of children and adolescents from two to eighteen years of age who exhibit behaviors associated with Autism Spectrum Disorders. When combined with other information, results from the ASRS can help determine the likelihood that a child has symptoms related to Autism Spectrum Disorders. The ASRS was completed by _firstname's mother (_rater1), general education teacher (_rater2), and special education teacher (_rater3). Scores of 40 to 59 are considered average, scores below 40 indicate fewer concerns than average, and scores above 59 are considered slightly elevated to very elevated.

Social/Communication: This scale indicates _firstname's ability to appropriately use verbal and non-verbal communication to initiate, engage in, and maintain social contact. [Rater 1] reported [Classification] concerns (T-Score = ??), [Rater 2] reported [Classification] concerns (T-Score = ??), and [Rater 3] reported [Classification] concerns (T-Score = ??) on this scale.

Unusual Behavior: This scale assesses _firstname's tolerance for changes in routine, engagement in apparently purposeless and stereotypical behaviors, and overreaction to particular sensory experiences. [Rater 1] reported [Classification] concerns (T-Score = ??), [Rater 2] reported [Classification] concerns (T-Score = ??), and [Rater 3] reported [Classification] concerns (T-Score = ??) on this scale.

Self-Regulation: This scale indicates how well _firstname manages _his/her behavior and thoughts, maintains focus, and resists distractions. [Rater 1] reported [Classification] concerns (T-Score = ??), [Rater 2] reported [Classification] concerns (T-Score = ??), and [Rater 3] reported [Classification] concerns (T-Score = ??) on this scale.

DSM-5: This scale assesses how closely _firstname's symptoms match the DSM-5 criteria for an Autism Spectrum Disorder. [Rater 1] reported [Classification] concerns (T-Score = ??), [Rater 2] reported [Classification] concerns (T-Score = ??), and [Rater 3] reported [Classification] concerns (T-Score = ??) on this scale.

Peer Socialization: This scale assesses _firstname's willingness and capacity to successfully engage in activities that develop and maintain relationships with same-aged peers. [Rater 1] reported [Classification] concerns (T-Score = ??), [Rater 2] reported [Classification] concerns (T-Score = ??), and [Rater 3] reported [Classification] concerns (T-Score = ??) on this scale.

Adult Socialization: This scale assesses _firstname's willingness and capacity to successfully engage in activities that develop and maintain relationships with adults. [Rater 1] reported [Classification] concerns (T-Score = ??), [Rater 2] reported [Classification] concerns (T-Score = ??), and [Rater 3] reported [Classification] concerns (T-Score = ??) on this scale.

Social/Emotional Reciprocity: This scale assesses _firstname's ability to respond to another person in a social situation appropriately. [Rater 1] reported [Classification] concerns (T-Score = ??), [Rater 2] reported [Classification] concerns (T-Score = ??), and [Rater 3] reported [Classification] concerns (T-Score = ??) on this scale.

Atypical Language: This scale assesses a student's ability to use language in a structured and conventional way when communicating with others. [Rater 1] reported [Classification] concerns (T-Score = ??), [Rater 2] reported [Classification] concerns (T-Score = ??), and [Rater 3] reported [Classification] concerns (T-Score = ??) on this scale.

Stereotypy: This scale indicates the extent to which _firstname engages in apparently purposeless and repetitive behaviors. [Rater 1] reported [Classification] concerns (T-Score = ??), [Rater 2] reported [Classification] concerns (T-Score = ??), and [Rater 3] reported [Classification] concerns (T-Score = ??) on this scale.

Behavioral Rigidity: This scale assesses how well _firstname tolerates changes in _his/her environment, routines, activities, or behaviors. [Rater 1] reported [Classification] concerns (T-Score = ??), [Rater 2] reported [Classification] concerns (T-Score = ??), and [Rater 3] reported [Classification] concerns (T-Score = ??) on this scale.

Sensory Sensitivity: This scale assesses _firstname's tolerance for specific experiences sensed through touch, sound, vision, smell, or taste. [Rater 1] reported [Classification] concerns (T-Score = ??), [Rater 2] reported [Classification] concerns (T-Score = ??), and [Rater 3] reported [Classification] concerns (T-Score = ??) on this scale.

Attention: The Attention scale assesses how distractible a student is. [Rater 1] reported [Classification] concerns (T-Score = ??), [Rater 2] reported [Classification] concerns (T-Score = ??), and [Rater 3] reported [Classification] concerns (T-Score = ??) on this scale.
```

