# Welcome to FreePsych!

FreePsych is a repository of tools to help school psychologists automate repetitive tasks in drafting psychological evaluations.

- **Who is FreePsych for?**

    FreePsych was created and is maintained for psychologists and professionals administering psychometrics.

- **What is FreePsych**

    FreePsych is a repository of tools designed to help psychologists and professionals automate clerical tasks in drafting psychological evaluations and managing psychometric data.

- **Where was FreePsych created?**

    FreePsych originated in the confines of an elementary school in Arizona.

- **When was FreePsych created?**

    FreePsych was developed in **Fall 2025** to address evolving needs in the field.

- **Why FreePsych?**

    FreePsych aims to provide a **free, open-source framework** to help create **streamlined, efficient, modern psychometric evaluations** accessible to all professionals in the field.

## Features

- **Psychologist Assistant Skills**

    Narrative drafting templates for standardized psychoeducational evaluation reports. These templates are designed to assist school psychologists in generating professional, consistent, and clinically accurate narratives for assessments like cognitive interpretations, IEP eligibility determinations, and educational planning.

- **Date Calculator**

    A self-contained HTML application for calculating durations between dates and performing date arithmetic. It is ideal for school psychologists needing to track timelines for assessments, IEP eligibility, or other administrative tasks.

## Supported Platforms

FreePsych is supported in the following products:

- **ChatGPT (OpenAI)**:
    - Download ChatGPT: https://chatgpt.com/download/
    - Download Codex: https://openai.com/codex/
    - Docs (Skills): https://developers.openai.com/plugins/concepts/skills
    - Docs (Plugins): https://developers.openai.com/plugins/concepts/plugins
- **Claude (Anthropic)**:
    - Download Claude: https://claude.com/download
    - Download Claude Code CLI: https://code.claude.com/docs/en/overview
    - Docs (Skills): https://support.claude.com/en/articles/12512180-use-skills-in-claude
    - Docs (Plugins): https://support.claude.com/en/articles/13837440-use-plugins-in-claude
- **Gemini (Google)**:
    - Download Gemini: https://gemini.google/desktop/
    - Download Antigravity: https://antigravity.google/
    - Docs (Skills): https://docs.cloud.google.com/gemini/enterprise/docs/skills
- **Vibe (Mistral AI)**:
    - Download Vibe: https://mistral.ai/products/vibe/
    - Download Vibe CLI: https://docs.mistral.ai/vibe/code/cli/install-setup
    - Docs (Skills): https://docs.mistral.ai/getting-started/quickstarts/vibe-work/create-first-skill
- **OpenCode**: https://opencode.ai/
- And more... https://agentskills.io/clients

# FreePsych-Skills: *plugin/skills*

## Installation Instructions - Plugin

### Prerequisite: Download Plugin

You need to download the repository as a `.zip` file using the following steps:

1. Click the **Code** button.
1. In the **Code** dropdown, click the **zip** button under the **Download source code** section.

### ChatGPT (OpenAI)

1. **Install the Plugin in ChatGPT Desktop App**:
    1. Open the ChatGPT desktop app.
    1. Click on the plugin icon on the top-left corner.
    1. Click the **Add** button on the top-right corner.
    1. On the **Add** menu, select the **Upload plugin archive** option.
    1. Drag and drop the downloaded `.zip` file into the upload box.
    1. Click the **Install plugin** button.
1. **Enable the Plugin**:
    1. Once installed, the plugin will appear in your list of available plugins.
    1. Enable the plugin to make the skills available for use in ChatGPT.

### Claude (Anthropic)

1. **Install the Plugin in Claude Desktop App**:
    1. Open the Claude desktop app.
    1. Click on the **Plugins** icon on the top-left corner.
    1. Click the **Add** button in the top-right corner.
    1. Choose the **Upload plugin** option.
    1. Drag the `.zip` file you created from the `/plugin` folder into the **Plugin file** box.
    1. Click the **Upload** button.
    1. Wait for the installation to complete.
1. **Enable the Plugin**:
    1. Once installed, the plugin will appear in your list of available plugins.
    1. Enable the plugin to make the skills available for use in Claude.

## Installation Instructions - Skills

### Gemini (Google)

1. Open the Gemini desktop app.
1. Click the settings gear icon in the bottom-left corner.
1. In the settings menu, select **Skills**.
1. Click the **Create** button in the top-right corner.
1. Choose **Upload** from the options.
1. Drag and drop the entire skill folder (e.g., `skills/psy-draft-recommendations/`) into the upload box.
1. Once the upload completes, click **Create** to add the skill.

### Vibe (Mistral AI)

1. Open the Vibe desktop app.
1. Click the **Context** icon in the top-left corner.
1. In the Context menu, select **Skills**.
1. Click the **Import** button in the top-right corner (next to the **+ New skill** button).
1. Choose **Upload skill folder** from the options.
1. Select an entire skill folder (e.g., `skills/psy-draft-recommendations/`).
1. Click the **Upload** button.
1. Once the upload completes, click the **Create skill** button on the top-left corner to add the skill.

## Installation Instructions - CLI Agents

**Copy** FreePsych' `skills` folder into the following paths:

- **Antigravity (Google)**
    - `~/.gemini/config/skills/` (global)
    - `<workspace-root>/.agents/skills/` (workspace)
- **Claude Code (Anthropic)**
    - `~/.claude/skills/` (global)
    - `<workspace-root>/.claude/skills/` (workspace)
- **Codex (OpenAI)**
    - `~/.agents/skills/` (global)
    - `<workspace-root>/.agents/skills/` (workspace)
- **OpenCode**
    - `~/.config/opencode/skills/` (global)
    - `<workspace-root>/.opencode/skills/` (workspace)
- **Vibe (Mistral AI)**
    - `~/.vibe/skills/` (global)
    - `<workspace-root>/.vibe/skills/` (workspace)

# FreePsych-Time: */apps/date-calculator*

## Features

- **Duration Calculation**: Calculate the time between two dates (years, months, days).
- **Date Arithmetic**: Add or subtract days, weeks, months, or years from a base date.
- **Offline Capability**: Works without an internet connection.
- **Responsive Design**: Compatible with mobile and desktop devices.

## Install Instructions

The **Date Calculator** requires **no installation** and is designed to be **offline-friendly**. Simply follow these steps:

1. Locate the `date-calculator.html` file in the `/apps/date-calculator` directory.
1. Open the file in any modern browser (Chrome, Firefox, Safari, or Edge).
1. No additional setup or dependencies are required.

## Usage

1. Open the `date-calculator.html` file directly from your local machine or a shared drive.
1. Use the intuitive interface to input dates and perform calculations.

# AI Diligence Statement

While developing and maintaining FreePsych, I used AI models as tools to streamline documentation, version control, and technical research. **Mistral AI's Ministral** model helped draft commit messages and write project documentation. **Google's Gemini Flash-Lite** served as a skill creator, helping me build and structure the skills FreePsych relies on.

I affirm that all AI-assisted content, documentation, and frameworks have undergone human review, evaluation, and adaptation. The final implementation, architecture, and output reflect my decisions, expertise, and intended design. While these AI models provided valuable assistance throughout development, I remain responsible for the project's codebase, accuracy, and overall direction. This disclosure is provided in the spirit of transparency, open-source integrity, and a commitment to acknowledging the collaborative tools utilized in FreePsych's creation.
