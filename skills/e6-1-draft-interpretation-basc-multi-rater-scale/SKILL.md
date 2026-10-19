---
name: e6-1-draft-interpretation-basc-multi-rater-scale
description: Generate professional BASC-3 multi-rater social-emotional interpretation narratives for psychoeducational reports. Use when drafting psychoeducational evaluation reports requiring BASC-3 multi-rater scale interpretation.
---

# BASC-3 Multi-Rater Scale Narrative Generator

Use this skill to generate a formal, technical narrative for the "Social-Emotional" section of a psychoeducational report using the Behavior Assessment System for Children, Third Edition (BASC-3) multi-rater template.

## Instructions for AI

You are a School Psychologist Assistant. Your task is to process raw BASC-3 scores and rater names to complete a professional narrative.

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
Social-emotional development includes an individual's experience, expression, and management of emotions and behaviors. It consists of the ability to establish positive and rewarding relationships with others and encompasses how well we manage ourselves and our interactions with others. To obtain information regarding _firstname's behavior at school and home, the Behavior Assessment System for Children, Third Edition (BASC-3) was completed by their mother, _rater1, and general education teacher, _rater2. The BASC-3 is a multidimensional approach to evaluating the behavior of children and adolescents. It measures numerous aspects of behavior and personality. _firstname's functioning was assessed through three broad Composites: Externalizing Problems, Internalizing Problems, and School Problems.

Externalizing Problems: This composite is characterized by under-control of emotions/behaviors that result in disruptive behaviors, such as aggression, hyperactivity, and conduct problems. _firstname's overall level of Externalizing Problems was rated to be in the [Classification] range (T-Score = [??]) by _rater1 and the [Classification] range (T-Score = [??]) by _rater2.

Hyperactivity: This scale assesses a student's activity levels. Typical hyperactive behaviors may include fidgeting, constant movement, and wandering. _firstname received ratings within the [Classification] range (T-Score = [??]) by _rater1 and the [Classification] range (T-Score = [??]) by _rater2.

Aggression: This scale measures a student's tendency to act hostilely. This may include verbal (threatening others) and physical (hitting/kicking) behaviors. _firstname's levels of aggression were rated in the [Classification] range (T-Score = [??]) by _rater1 and the [Classification] range (T-Score = [??]) by _rater2.

Conduct Problems: This scale measures how often _firstname gets in trouble. It is characterized by anti-social behavior and marked impairments in relationships. _firstname received scores within the [Classification] range (T-Score = [??]) by _rater1 and the [Classification] range (T-Score = [??]) by _rater2.

Internalizing Problems: This composite is characterized by over-control of emotions/behaviors and is not usually marked by acting out behavior. Instead, internalizing behaviors are often described as social withdrawal and/or feelings of nervousness and sadness. _firstname's overall level of Internalizing Problems was rated within the [Classification] range (T-Score = [??]) by _rater1 and the [Classification] range (T-Score = [??]) by _rater2.

Anxiety: This scale measures worry, nervousness, and/or unease. _firstname received scores within the [Classification] range (T-Score = [??]) by _rater1 and the [Classification] range (T-Score = [??]) by _rater2.

Depression: Depression is a common and serious medical illness that negatively affects how one feels, thinks, and acts. This scale measures observable behaviors associated with depression, such as loss of interest and energy, verbalizations of sadness, and pervasive sad moods. _firstname received ratings within the [Classification] range (T-Score = [??]) by _rater1 and the [Classification] range (T-Score = [??]) by _rater2.

Somatization: This scale assesses complaints of physical ailments or oversensitivity to seemingly normal physical problems. _firstname received scores within the [Classification] range (T-Score = [??]) by _rater1 and the [Classification] range (T-Score = [??]) by _rater2.

School Problems: This composite reflects academic difficulties, including problems of motivation, attention, learning, and cognition. A high score on this composite indicates that _firstname displays behaviors likely to interfere with achievement. An overall composite for school problems is only obtained when the BASC-3 is completed by a teacher/educator. _firstname's general education teacher reported concerns within the [Classification] range (T-Score = [??]) for overall school problems.

Attention Problems: This scale measures distractibility and focus. _firstname's attention was rated within the [Classification] range (T-Score = [??]) by _rater1 and the [Classification] range (T-Score = [??]) by _rater2.

Learning Problems: This scale measures aspects related to academic achievement, such as getting poor grades and having trouble keeping up in class. A score for learning problems is only obtained when the BASC-3 is completed by a teacher/educator. _firstname's general education teacher reported concerns within the [Classification] range (T-Score = [??]) for learning problems.

Behavioral Symptoms Index (BSI): This composite is a total score of Hyperactivity, Aggression, Depression, Attention, Atypicality, and Withdrawal. _firstname received scores within the [Classification] range (T-Score = [??]) by _rater1 and the [Classification] range (T-Score = [??]) by _rater2.

Atypicality: This scale measures the tendency to behave in ways considered immature, odd, or seemingly disconnected. _firstname received scores within the [Classification] range (T-Score = [??]) by _rater1 and the [Classification] range (T-Score = [??]) by _rater2.

Withdrawal: This scale measures the tendency to avoid social interactions or shy away in social situations. _firstname received scores within the [Classification] range (T-Score = [??]) by _rater1 and the [Classification] range (T-Score = [??]) by _rater2.

Adaptive Behavior: Adaptive behavior includes the age-appropriate behaviors necessary to live independently and function safely and appropriately in daily life. Adaptive scales measure positive behaviors; higher scores indicate more adaptive behaviors and better adjustment. _firstname's overall Adaptive skills were rated to be in the [Classification] range (T-Score = [??]) by _rater1 and the [Classification] range (T-Score = [??]) by _rater2. More specifically, _firstname's mother rated the area of Adaptability as [Classification] (T-Score = [??]), Social Skills as [Classification] (T-Score = [??]), Leadership as [Classification] (T-Score = [??]), Activities of Daily Living as [Classification] (T-Score = [??]), and Functional Communication as [Classification] (T-Score = [??]). _firstname's general education teacher rated the area of Adaptability as [Classification] (T-Score = [??]), Social Skills as [Classification] (T-Score = [??]), Leadership as [Classification] (T-Score = [??]), Study Skills as [Classification] (T-Score = [??]), and Functional Communication as [Classification] (T-Score = [??]).

The BASC-3 Rating Scales assess a rater's response pattern to determine how results should be interpreted. _rater1's rating consistency, response pattern, and F-Index were acceptable, indicating that these ratings are likely a valid representation of _firstname's current behavior/social-emotional functioning. Likewise, _rater2's rating consistency, response pattern, and F-Index were acceptable.
```
