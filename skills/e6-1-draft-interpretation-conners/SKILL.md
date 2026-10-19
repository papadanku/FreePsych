---
name: e6-1-draft-interpretation-conners
description: Generate professional ADHD and behavioral interpretation narratives for the Conners 4th Edition (Conners-4) assessment. Use when drafting psychoeducational evaluation reports requiring Conners-4 domain narratives.
---

# Prompt: Conners 4 ADHD Narrative Generator

Use this prompt to generate a formal, technical narrative for the "ADHD/Behavioral" section of a psychoeducational report using the Conners, Fourth Edition (Conners-4) template.

## Instructions for AI

You are a School Psychologist Assistant. Your task is to process raw Conners-4 scores and rater names to complete a professional narrative.

### Rules

- Classification Logic: Use the following scale for all scales and composites:
    - **<=39**: Low
    - **40-59**: Average
    - **60-64**: Slightly Elevated (*)
    - **65-69**: Elevated (**)
    - **>=70**: Very Elevated (***)
- Consistency Check: If raters report different levels of concern (e.g., Parent is "Average" but Teacher is "Elevated"), modify the sentence to reflect the discrepancy (e.g., "...was rated in the Average range by _rater1 and the Elevated range by _rater2.") instead of stating behavior is "consistent across settings."
- Data Insertion:
    - Bold all numeric scores (e.g., T-Score = 67).
    - Bold the student's name (`_firstname`) every time it appears.
    - If a score is Slightly Elevated, add one asterisk (*). If Elevated, add two (**). If Very Elevated, add three (***).
    - Replace generic "Average concerns" or "Average range" phrases with the specific classification based on the T-scores provided.
- Formatting: Use the exact structure provided in the TEMPLATE section below.
- Style: Write in Plain English using Active Voice.
- Variables: Substitute all placeholders: `_firstname`, `_rater1` (Parent), `_rater2` (Teacher 1), `_rater3` (Teacher 2).

## TEMPLATE

```
Attention Deficit Hyperactive Disorder (ADHD) is one of the most common neurodevelopmental disorders of childhood. It is usually first diagnosed in childhood and often lasts into adulthood. Children with ADHD may have trouble paying attention, controlling impulsive behaviors (may act without thinking about what the result will be), or be overly active. To obtain information regarding how closely related _firstname's behavior is to ADHD across settings, the Conners, Fourth Edition (Conners-4) was completed by their mother (_rater1), general education teacher (_rater2), and special education teacher(_rater3). Further details about _firstname's observed behaviors across settings are discussed below.

Inattention/Executive Dysfunction: The Inattention/ Executive Dysfunction scale measures how distractible and detail/ plan-oriented _firstname is. Attention and executive functioning problems can affect one's ability to remain focused on the task, follow directions, and complete multi-step problems. Additionally, planning skills can aid in organization, task completion, and assignment prioritization. [Rater 1] reported [Classification] concerns (T-Score = ??), [Rater 2] reported [Classification] concerns (T-Score = ??), and [Rater 3] reported [Classification] concerns (T-Score = ??) on this scale.

Hyperactivity: The Hyperactivity scale measures how active, restless, and impulsive _firstname is. Students with high levels of hyperactivity tend to have trouble sitting still and being quiet. [Rater 1] reported [Classification] concerns (T-Score = ??), [Rater 2] reported [Classification] concerns (T-Score = ??), and [Rater 3] reported [Classification] concerns (T-Score = ??) on this scale.

Impulsivity: The Impulsivity scale measures how well _firstname can control their initial reactions to an event or stimuli. This includes the ability to have a thought and not act upon that thought. [Rater 1] reported [Classification] concerns (T-Score = ??), [Rater 2] reported [Classification] concerns (T-Score = ??), and [Rater 3] reported [Classification] concerns (T-Score = ??) on this scale.

Emotional Dysregulation: The Emotional Dysregulation scale measures how well _firstname can control their emotions. [Rater 1] reported [Classification] concerns (T-Score = ??), [Rater 2] reported [Classification] concerns (T-Score = ??), and [Rater 3] reported [Classification] concerns (T-Score = ??) on this scale.

Depressed Mood: The Depressed Mood scale measures _firstname's overall mood and feelings of sadness. [Rater 1] reported [Classification] concerns (T-Score = ??), [Rater 2] reported [Classification] concerns (T-Score = ??), and [Rater 3] reported [Classification] concerns (T-Score = ??) on this scale.

Anxious Thoughts: The Anxious Thoughts scale measures _firstname's fears and worries. [Rater 1] reported [Classification] concerns (T-Score = ??), [Rater 2] reported [Classification] concerns (T-Score = ??), and [Rater 3] reported [Classification] concerns (T-Score = ??) on this scale.

Schoolwork: This measures how well _firstname can keep up with the academic demands of the classroom. [Rater 1] reported [Classification] concerns (T-Score = ??), [Rater 2] reported [Classification] concerns (T-Score = ??), and [Rater 3] reported [Classification] concerns (T-Score = ??) on this scale.

Peer Interaction: This measures how well _firstname gets along with others their age. [Rater 1] reported [Classification] concerns (T-Score = ??), [Rater 2] reported [Classification] concerns (T-Score = ??), and [Rater 3] reported [Classification] concerns (T-Score = ??) on this scale.

Family Life: This measures how _firstname feels about home life. _rater1 reported [Classification] concerns (T-Score = ??) on this scale.

ADHD Inattention Symptoms (DSM): The DSM criteria for ADHD Inattentive Type requires the presence of symptoms such as poor listening, losing items, and lack of ability to complete work. [Rater 1] reported concerns in the [Classification] range (T-Score = ??), [Rater 2] reported concerns in the [Classification] range (T-Score = ??), and [Rater 3] reported concerns in the [Classification] range (T-Score = ??) on this scale.

ADHD Hyperactive/Impulsive Symptoms (DSM): This scale measures symptoms like fidgeting, restlessness, and interrupting. [Rater 1] reported concerns in the [Classification] range (T-Score = ??), [Rater 2] reported concerns in the [Classification] range (T-Score = ??), and [Rater 3] reported concerns in the [Classification] range (T-Score = ??) on this scale.

Total ADHD Symptoms: This scale examines combined inattentive and hyperactive symptoms. [Rater 1] reported concerns in the [Classification] range (T-Score = ??), [Rater 2] reported concerns in the [Classification] range (T-Score = ??), and [Rater 3] reported concerns in the [Classification] range (T-Score = ??) on this scale.

Oppositional Defiant Disorder (DSM): This scale measures angry/irritable moods and argumentative behavior. [Rater 1] reported concerns in the [Classification] range (T-Score = ??), [Rater 2] reported concerns in the [Classification] range (T-Score = ??), and [Rater 3] reported concerns in the [Classification] range (T-Score = ??) on this scale.

Conduct Disorder (DSM): This measures persistent patterns of violating rules or the rights of others. [Rater 1] reported concerns in the [Classification] range (T-Score = ??), [Rater 2] reported concerns in the [Classification] range (T-Score = ??), and [Rater 3] reported concerns in the [Classification] range (T-Score = ??) on this scale.
```

