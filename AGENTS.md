
# FreePsych: Agent Instructions

This repository contains tools for school psychologists to automate repetitive tasks in drafting psychological evaluations and date calculations.

---

### Key Directories and Workflows

- **`/skills`**
    - Contains **Markdown-based narrative drafting templates** for standardized psychoeducational evaluation reports.
    - Each skill folder (e.g., `e6-8-draft-recommendations`) includes a `SKILL.md` file with instructions for agents.
    - **Installation for Agents**:
        - Copy the `/skills` folder to the platform-specific skills directory (e.g., `~/.config/opencode/skills/` for OpenCode).
        - Ensure the `SKILL.md` file is properly formatted for the platform (e.g., Claude, OpenCode).
- **`/apps/date-calculator`**
    - A **self-contained HTML application** for calculating durations between dates and performing date arithmetic.
    - **Usage**: Open `date-calculator.html` directly in any modern browser. No installation or dependencies required.

---

### Agent-Specific Notes

- **Platform-Specific Installation**:
    - For **OpenCode**, copy the `/skills` folder to `~/.config/opencode/skills/`.
    - For **Claude Code**, copy the `/skills` folder to `~/.claude/skills/`.
    - For **Vibe**, copy the `/skills` folder to `~/.vibe/skills/`.
- **Skill Usage**:
    - Each skill folder contains a `SKILL.md` file with **strict filtering criteria** (e.g., developmental appropriateness, feasibility).
    - **Do not modify the wording** of the recommendations in the templates. Use them **verbatim** as provided.
- **Date Calculator**:
    - Works **offline** and requires no setup beyond opening the HTML file.
    - Supports **duration calculation** and **date arithmetic** with intuitive UI.

---

### Execution Flow

- **For Skills**:
    1. Copy the `/skills` folder to the platform-specific skills directory.
    2. Ensure the `SKILL.md` file is correctly formatted for the platform.
    3. Use the skill by referencing the `name:` and `description:` fields in `SKILL.md`.

- **For Date Calculator**:
    1. Open `date-calculator.html` directly in a browser.
    2. No additional setup is required.

---

### Constraints and Gotchas

- **Skills**:
  - Adhere strictly to the **filtering criteria** in `SKILL.md` (e.g., developmental appropriateness, practicality).
  - Do not alter the **wording** of recommendations.
- **Date Calculator**:
  - Works **without internet** or external dependencies.

---

### References

- For **OpenCode-specific instructions**, refer to the `README.md` in the `/skills` directory.
- For **platform-specific installation**, refer to the `README.md` in this repository.
