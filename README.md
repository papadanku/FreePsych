# FreePsych

A repository of tools to help school psychologists automate repetitive tasks in drafting psychological evaluations.

This repository includes:

- **Psychologist Assistant Skills**: Narrative drafting templates for standardized psychoeducational evaluation reports.
- **Date Calculator**: A self-contained HTML application for calculating durations between dates and performing date arithmetic.

## Philosophy

* **Zero External Dependencies:** All tools are designed to be lightweight, portable, and independent of external libraries or frameworks.
* **Privacy-First:** Data processing happens locally or within your own secure Google/CLI environment.
* **Professional Standards:** Narrative templates and scoring rules are based on established clinical practices and classification tables.

## Psychologist Assistant Skills: */skills*

The **Psychologist Assistant Skills** directory contains **narrative drafting templates** for standardized psychoeducational evaluation reports. These templates are designed to assist school psychologists in generating professional, consistent, and clinically accurate narratives for assessments like cognitive interpretations, IEP eligibility determinations, and educational planning.

### Installation Instructions (Agents)

FrIEP's skills are supported in the following products:

* Antigravity (Google): https://antigravity.google/
* Claude Code (Anthropic): https://claude.com/product/claude-code
* Codex (OpenAI): https://openai.com/codex/
* Vibe (Mistral AI): https://mistral.ai/products/vibe/
* OpenCode: https://opencode.ai/
* And more... https://agentskills.io/clients

To use the **Psychologist Assistant Skills** templates, follow these platform-specific instructions:

#### Global Installation (All Workspaces)

* **Antigravity (Google)**: Copy FrIEP's `/skills` folder to `~/.gemini/config/skills/`.
* **Claude Code (Anthropic)**: Copy FrIEP's `/skills` folder to `~/.claude/skills/`.
* **Codex (OpenAI)**: Copy FrIEP's `/skills` folder to `~/.agents/skills/`.
* **OpenCode**: Copy FrIEP's `/skills` folder to `~/.config/opencode/skills/`.
* **Vibe (Mistral AI)**: Copy FrIEP's `/skills` folder to `~/.vibe/skills/`.

#### Workspace-Specific Installation

* **Antigravity (Google)**: Copy FrIEP's `/skills` folder to `<workspace-root>/.agents/skills/`.
* **Claude Code (Anthropic)**: Copy FrIEP's `/skills` folder to `<workspace-root>/.claude/skills/`.
* **Codex (OpenAI)**: Copy FrIEP's `/skills` folder to `<workspace-root>/.agents/skills/`.
* **OpenCode**: Copy FrIEP's `/skills` folder to `<workspace-root>/.opencode/skills/`.
* **Vibe (Mistral AI)**: Copy FrIEP's `/skills` folder to `<workspace-root>/.vibe/skills/`.

### Installation Instructions (Regular)

* Claude (Anthropic): https://claude.ai/
* Gemini (Google): https://gemini.google.com/app
* Vibe (Mistral AI): https://chat.mistral.ai/chat

#### Claude (Anthropic)

1. Open https://claude.ai/.
1. Click your profile icon in the bottom-left corner.
1. Select **Skills** from the dropdown menu.
1. Click the **Add** button in the top-right corner.
1. Choose **Upload Skill** from the options.
1. Drag and drop the `SKILL.md` file from your desired skill folder (e.g., `skills/e6-8-draft-recommendations/SKILL.md`) into the upload box.
1. Click **Upload** to add the skill to your Claude interface.

#### Gemini (Google)

1. Open https://gemini.google.com/app.
1. Click the settings gear icon in the bottom-left corner.
1. In the settings menu, select **Skills**.
1. Click the **Create** button in the top-right corner.
1. Choose **Upload** from the options.
1. Drag and drop the entire skill folder (e.g., `skills/e6-8-draft-recommendations/`) into the upload box.
1. Once the upload completes, click **Create** to add the skill.

#### Vibe (Mistral AI)

1. Open https://chat.mistral.ai/chat.
1. Click the box in the top-right corner and select **Studio**. This will redirect you to https://console.mistral.ai/.
1. Navigate to the **Skills** section under **Context**.
1. Click the **Create Skill** button in the top-left corner.
1. Open the `SKILL.md` file from your desired skill folder (e.g., `skills/e6-8-draft-recommendations/SKILL.md`).
1. Copy and paste the following content into the appropriate boxes:
    - Paste the `name:` field content into the **new-skill** placeholder.
    - Paste the `description:` field content into the **Required. Use this skill when the user asks to...** placeholder.
    - Paste the content below the `---` line into the **Write your skill instructions here** placeholder.
1. Click **Create** to finalize the skill setup.

#### General Usage

* The templates are **Markdown-based** and **platform-agnostic**. Simply copy the relevant `.md` file (e.g., `e6-1-draft-interpretation-wj-cog.md`) into your preferred text editor or document tool.
* Populate the placeholders with assessment data to generate a polished narrative.

No installation is required beyond copying the files to your desired location.

## Date Calculator: */apps/date-calculator*

The **Date Calculator** is a **self-contained HTML application** designed for calculating durations between dates and performing date arithmetic. It is ideal for school psychologists needing to track timelines for assessments, IEP eligibility, or other administrative tasks.

### Features

- **Duration Calculation**: Calculate the time between two dates (years, months, days).
- **Date Arithmetic**: Add or subtract days, weeks, months, or years from a base date.
- **Offline Capability**: Works without an internet connection.
- **Responsive Design**: Compatible with mobile and desktop devices.

### Install Instructions

The **Date Calculator** requires **no installation** and is designed to be **offline-friendly**. Simply follow these steps:

1. Locate the `date-calculator.html` file in the `/apps/date-calculator` directory.
1. Open the file in any modern browser (Chrome, Firefox, Safari, or Edge).
1. No additional setup or dependencies are required.

### Usage

1. Open the `date-calculator.html` file directly from your local machine or a shared drive.
1. Use the intuitive interface to input dates and perform calculations.
