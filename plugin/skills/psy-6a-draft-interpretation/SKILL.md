---
name: psy-6a-draft-interpretation
description: Draft professional psychoeducational evaluation report interpretation narratives across 15 assessment batteries: ASRS, BASC-3, Conners-4, CTONI-2, DP-4, EDDT, GARS-3, KABC-II NU, Vineland-3, WISC-V, WJ-IV ACH, WJ-IV Cog, WJ-IV OL, X-BASS 3.0, and YCAT-2. Use when drafting psychoeducational reports, converting raw, standard, scaled, or T-scores into domain narratives, or writing cognitive, academic, adaptive, autism, ADHD, developmental, oral language, or social-emotional interpretation sections.
---

# Psychoeducational Interpretation Drafting

Generate formal, report-ready psychoeducational interpretation narratives across 15 standardized assessment batteries by pairing each battery's classification rules with its narrative template.

## When to Use

Use this skill when drafting psychoeducational evaluation report sections for any of the following batteries:

- **Autism & Social-Emotional / Behavioral**: ASRS, BASC-3, Conners-4, EDDT, GARS-3
- **Cognitive & Nonverbal Intelligence**: CTONI-2, KABC-II NU, WISC-V, WJ-IV Cog, X-BASS 3.0
- **Academic & Oral Language**: WJ-IV ACH, WJ-IV OL, YCAT-2
- **Adaptive & Developmental**: DP-4, Vineland-3

## Directory Structure

Locate the matching battery's details file in `references/` and its template file(s) in `assets/` using this tree:

- **`references/`**
    - `references/details-asrs.md`: ASRS classification ranges, consistency & formatting rules
    - `references/details-basc.md`: BASC-3 clinical/adaptive ranges & multi-rater rules
    - `references/details-conners.md`: Conners-4 classification ranges & ADHD narrative rules
    - `references/details-ctoni.md`: CTONI-2 summary, steps & nonverbal composite guidance
    - `references/details-dp4.md`: DP-4 summary, steps & 5 developmental domain rules
    - `references/details-eddt.md`: EDDT characteristic/resilience ranges & rater rules
    - `references/details-gars-3.md`: GARS-3 subscale metrics, Autism Index & DSM-5 severity
    - `references/details-kabc.md`: KABC-II NU FCI/NVI & CHC domain guidance
    - `references/details-vineland.md`: Vineland-3 domain Standard & subdomain v-Scale ranges
    - `references/details-wisc.md`: WISC-V primary index & composite guidance
    - `references/details-wj-ach.md`: WJ-IV Tests of Achievement cluster/subtest guidance
    - `references/details-wj-cog.md`: WJ-IV Tests of Cognitive Abilities CHC guidance
    - `references/details-wj-ol.md`: WJ-IV Tests of Oral Language cluster/subtest guidance
    - `references/details-xbass.md`: X-BASS 3.0 Cross-Battery CHC domain guidance
    - `references/details-ycat.md`: YCAT-2 early academic achievement guidance
- **`assets/`**
    - `assets/templates-asrs.md`
    - `assets/template-interpretation-basc-multi-rater-scale.md`
    - `assets/template-interpretation-basc-self-rater-scale.md`
    - `assets/template-interpretation-basc-self-rater-scale-child.md`
    - `assets/templates-conners.md`
    - `assets/templates-ctoni.md`
    - `assets/templates-dp4.md`
    - `assets/templates-eddt.md`
    - `assets/templates-gars-3.md`
    - `assets/templates-kabc.md`
    - `assets/templates-vineland.md`
    - `assets/templates-wisc.md`
    - `assets/templates-wj-ach.md`
    - `assets/templates-wj-cog.md`
    - `assets/templates-wj-ol.md`
    - `assets/templates-xbass.md`
    - `assets/templates-ycat.md`

## Steps

1. **Identify the battery (or batteries)** from the user's score report, data table, or prompt.
2. **Load the battery's rules and template** by reading the corresponding `references/details-<battery>.md` and `assets/templates-<battery>.md` files (for BASC-3, select the matching `assets/template-interpretation-basc-*.md` file based on whether the administration is Multi-Rater, Self-Report Adolescent, or Self-Report Child).
3. **Apply classification logic and consistency checks** from the `references/` file before filling text:
    - Map every raw, standard, scaled, v-Scale, or T-score to its exact qualitative classification and severity marker (e.g., `*`, `**`, `***` where specified).
    - When multiple raters disagree (e.g., Parent vs. Teacher), adjust the narrative to state each rater's specific rating instead of claiming consistency across settings.
4. **Populate all template placeholders** (`_firstname`, `_he/she`, `_his/her`, `_rater1`, `_rater2`, `_rater3`, `??`, `[Classification]`, `[Range]`, `[Score]`), bolding numeric scores and the student's name where required by the battery's rules.
5. **Verify completeness** so no unreplaced placeholders, mismatched pronouns, or incorrect classification labels remain.

## Gotchas

- **BASC-3 uses three separate asset templates**: Always check whether the data is Multi-Rater (Parent/Teacher), Self-Report Adolescent, or Self-Report Child before choosing the BASC-3 template file.
- **Scale direction differs across batteries**: On BASC-3, Clinical scales classify higher T-scores as elevated, whereas Adaptive scales classify lower T-scores (`<= 40`) as At-Risk or Clinically Significant. Similarly, Vineland-3 classifies lower Standard/v-Scale scores as Moderately Low or Low. Always verify against `references/details-<battery>.md`.
- **Rater count varies**: Templates with three raters (`_rater1`, `_rater2`, `_rater3`) must be adapted cleanly when only one or two raters are provided.
