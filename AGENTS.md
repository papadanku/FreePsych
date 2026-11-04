
# FreePsych Agent Instructions

## Overview

FreePsych is a repository of tools designed to assist school psychologists in automating clerical tasks related to drafting psychological evaluations and managing psychometric data. The project includes:

- **Psychologist Assistant Skills**: Markdown-based narrative drafting templates for standardized psychoeducational evaluation reports.
- **Date Calculator**: A self-contained HTML application for calculating durations between dates and performing date arithmetic.

## Key Directories and Files

### Psychologist Assistant Skills

- **Location**: `plugin/skills/`
- **Purpose**: Contains narrative drafting templates for standardized psychoeducational evaluation reports.
- **Installation**: Copy the `plugin/skills` folder to the appropriate platform-specific directory (e.g., `~/.config/opencode/skills/` for OpenCode).

### Date Calculator

- **Location**: `apps/date-calculator/date-calculator.html`
- **Purpose**: A self-contained HTML application for date calculations.
- **Usage**: Open the `date-calculator.html` file directly in any modern browser. No installation required.

## Agent-Specific Guidance

### Skill Templates

- **Template Structure**: Each skill folder contains a `SKILL.md` file with instructions and a template file (e.g., `e6-1-draft-interpretation-wj-cog.md`).
- **Usage**: Copy the relevant `.md` file into your preferred text editor or document tool and populate placeholders with assessment data.

### Recommendations and Narratives

- **Recommendations**: Use the `psy-draft-recommendations` skill to generate tailored educational recommendations for students. Ensure you adhere to the filtering criteria:
  - **Developmental Appropriateness**: Remove items suited for early childhood.
  - **Feasibility**: Avoid recommendations requiring specialized equipment or training.
  - **Practicality**: Prioritize low-tech strategies.
  - **Quantity**: Limit each section to a maximum of 8 items.
- **Narrative Templates**: Use the provided narrative templates for cognitive interpretations, summaries, and other sections of psychoeducational reports. Ensure you populate placeholders with accurate and relevant data.

### Testing and Observations

- **Observation Templates**: Use the templates in `psy-draft-testing-observation/assets/` to document observations from teachers and psychologists. Customize placeholders like `[Insert Level of conversational proficiency]` with relevant details.

### Communication Templates

- **Email Templates**: Use the `psy-notify-teacher-input` and `psy-notify-parent-input` skills to generate professional email templates for requesting updates and information from teachers and parents.

## Platform-Specific Instructions

### OpenCode

- **Skill Installation**: Copy the `plugin/skills` folder to `~/.config/opencode/skills/` for global use or to `./.opencode/skills/` for workspace-specific use.

### Other Platforms

- **Antigravity (Google)**: Copy the `plugin/skills` folder to `~/.gemini/config/skills/` or `<workspace-root>/.agents/skills/`.
- **Claude Code (Anthropic)**: Copy the `plugin/skills` folder to `~/.claude/skills/` or `<workspace-root>/.claude/skills/`.
- **Codex (OpenAI)**: Copy the `plugin/skills` folder to `~/.agents/skills/` or `<workspace-root>/.agents/skills/`.
- **Vibe (Mistral AI)**: Copy the `plugin/skills` folder to `~/.vibe/skills/` or `<workspace-root>/.vibe/skills/`.

## Workflow Tips

- **Review and Populate**: Always review the templates and populate placeholders with accurate data before using them.
- **Consistency**: Ensure consistency in terminology and formatting across all generated documents.
- **Validation**: Validate the generated narratives and recommendations with clinical standards and guidelines.

## Additional Notes

- **Zero Dependencies**: All tools are designed to be lightweight and portable with no external dependencies.
- **Privacy-First**: Data processing happens locally or within secure environments.
- **Professional Standards**: Narrative templates and scoring rules are based on established clinical practices.
