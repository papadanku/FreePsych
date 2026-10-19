---
name: e6-1-draft-interpretation-basc-self-rater-scale
description: Generate professional BASC-3 self-report scale interpretation narratives for psychoeducational reports. Use when drafting psychoeducational evaluation reports requiring BASC-3 self-rater scale interpretation.
---

# BASC-3 Self-Report (SRP) Narrative Generator

Use this skill to generate a formal, technical narrative for the "Social-Emotional Self-Report" section of a psychoeducational report using the BASC-3 SRP template.

## Instructions for AI

You are a School Psychologist Assistant. Your task is to process raw BASC-3 Self-Report (SRP) scores to complete a professional narrative.

### Rules

- Classification Logic: Use the following scale for all clinical and adaptive composites:
    - Adaptive Scales/Composites (Personal Adjustment):
        - **>=41**: Average
        - **31-40**: At-Risk (*)
        - **<=30**: Clinically Significant (**)
    - Clinical Scales/Composites (School Problems, Internalizing, Inattention/Hyperactivity):
        - **<=59**: Average
        - **60-69**: At-Risk (*)
        - **>=70**: Clinically Significant (**)
- Data Insertion:
    - Bold all numeric scores (e.g., T-Score = 65).
    - Bold the student's name (`_firstname`) every time it appears.
    - If a score is At-Risk, add a single asterisk (*). If it is Clinically Significant, add two asterisks (**).
- Formatting: Use the structure provided in the TEMPLATE section below. Adjust by rater amount.
- Style: Write in Plain English using Active Voice.
- Variables: Substitute all placeholders: `_firstname`, `_boy/girl`, `_he/she`, `_He/She`, `_him/her`, `_His/Her`, etc.

## TEMPLATE

```
To obtain information regarding _firstname's interpretation of _his/her social/emotional and behavioral functioning, the Behavior Assessment System for Children, Third Edition Self Report of Personality (BASC-3 SRP) was completed by _firstname. The BASC-3 is a multidimensional approach to evaluating the behavior of children and adolescents. It measures numerous aspects of behavior and personality, including positive (adaptive) and negative (clinical) dimensions. Scores in the clinically significant range suggest a high level of maladjustment. In contrast, scores in the at-risk range identify either a critical problem that may not be severe enough to require formal treatment or the potential of developing an issue that needs careful monitoring.

School Problems: This composite measures attitudes and behaviors that may be problematic for school success. _firstname reported [Classification] functioning on this composite (T-Score = [??]). _firstname's ratings indicate that _he/she [likes/dislikes] school. Additionally, _firstname described _him/herself as having [age-appropriate/concerning] attitudes towards _his/her teachers. Additionally, _firstname reported engaging in risky behaviors as often as others _his/her age.

Internalizing Problems: This composite measures depression, anxiety, and similar difficulties that are not usually marked by acting out behaviors. _firstname reported [Classification] functioning on this composite (T-Score = [??]). More specifically, _firstname reported that _he/she [has/does not have] appropriate thoughts and perceptions, [feels/does not feel] that _he/she has control over events that occur in _his/her life, and reported that _he/she [does/does not] often experience feelings of loneliness. _firstname indicated that _he/she [tends/tends not] to experience an odd amount of health-related problems. Additionally, _firstname [did/did not] report significant anxiety-based feelings or feelings of depression. Furthermore, _firstname reported being [satisfied/dissatisfied] with _his/her ability to perform various tasks.

Inattention/Hyperactivity: This composite measures problems with attention, hyperactivity, and impulsivity. _firstname's Inattention/Hyperactivity composite was reported to be within the [Classification] range of functioning (T-Score = [??]). Specifically, _firstname [did/did not] report significant concerns for attention or hyperactivity.

Personal Adjustment: This composite measures problems with interpersonal relations and self-perception. _firstname rated _his/her overall personal adjustment to be within the [Classification] range (T-Score = [??]). More specifically, _firstname reported that _he/she [has/lacks] a positive relationship with _his/her parents, [feels/does not feel] liked and respected by _his/her peers, generally reports [liking/disliking] _him/herself, and often [feels/lacks] confidence in _his/her abilities.

The BASC-3 Rating Scales assess a rater's response pattern to determine how results should be interpreted. _firstname's rating consistency, response pattern, and F-Index were considered to be [acceptable/cautionary], indicating that these ratings are likely a valid representation of _his/her current behavior/social-emotional functioning. Additionally, _his/her ratings were in the [Classification] range for the L-Index, and within the [Classification] range for the V-Index.
```

