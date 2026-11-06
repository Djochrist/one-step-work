# One Step Work

**One Step Work** is an instruction-only Agent Skill that encourages AI agents to collaborate with users by completing work in meaningful steps.

It is designed for **any type of task or project**, from a small edit to a multi-stage project: software development, writing, research, data analysis, document creation, design, planning, organization and troubleshooting.

The aim is not to make an agent slower. It is to make its work easier to follow, review and redirect.

## How it works

For each request, the agent should:

1. Understand the expected result and use the context already available.
2. Decide what counts as the next meaningful unit of work.
3. Complete that unit without splitting it into unnecessary micro-steps.
4. Verify the result when practical.
5. Explain what was done and pause before the next independent stage.

A simple request is treated as one complete step. A larger task is divided into logical stages. The agent should not ask for approval for every small operation inside the current step.

Users can change the workflow at any time. For example, they can ask the agent to continue, revise the result, skip a step or complete the whole task at once.

## Skill structure

```text
one-step-work/
├── SKILL.md
├── README.md
└── LICENSE
```

- `SKILL.md` contains the metadata and instructions used by the agent.
- `README.md` explains the project, installation and usage.
- `LICENSE` contains the MIT License terms.

This is an instruction-only skill. It does not require scripts, packages or external services.

## Installation in Codex

### Personal installation (available across your projects)

Copy the `one-step-work` folder into:

```text
~/.agents/skills/one-step-work/
```

On Windows PowerShell, from the directory containing this repository, run:

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse -Force ".\one-step-work" "$HOME\.agents\skills\one-step-work"
```

If the repository itself is already the `one-step-work` folder, use:

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills\one-step-work" | Out-Null
Copy-Item -Force ".\SKILL.md" "$HOME\.agents\skills\one-step-work\SKILL.md"
```

### Project installation (for one repository)

Copy the skill folder into the project where you want to use it:

```text
your-project/
└── .agents/
    └── skills/
        └── one-step-work/
            └── SKILL.md
```

The `.agents/skills/` location is Codex's repository-level skill location. The personal location is `~/.agents/skills/`.

After installing, open or restart Codex if the skill does not appear. Codex can discover a skill from its metadata and may select it when the request matches the description. You can also invoke it explicitly by mentioning `$one-step-work` in Codex.

## Example requests

```text
Use one-step-work to help me plan a small research project.
```

```text
Use one-step-work. Help me update this document, one meaningful step at a time.
```

```text
Use one-step-work to build this feature. Complete one stage, explain the result, and wait for my direction.
```

## Testing checklist

Try the skill with different kinds and sizes of requests:

- **Small task:** correct one paragraph or rename one file. The agent should complete the request as one step, report it and stop.
- **Medium task:** add one small feature. The agent should complete a coherent unit and pause before unrelated follow-up work.
- **Large task:** plan a multi-stage project. The agent should give a short roadmap, complete the first stage and wait.
- **User changes direction:** ask for a revision. The agent should revise the current result before proceeding.
- **User requests full execution:** ask the agent to complete everything at once. The agent should respect that instruction, subject to applicable safety and authorization requirements.

A skill provides instructions; it does not technically enforce agent behavior. Results can vary by model, host and task. Test it in your target environment and adjust the instructions when needed.

## References

- [Agent Skills specification](https://agentskills.io/specification) — the open format for skill folders and `SKILL.md` metadata.
- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills) — creating, discovering and using skills with ChatGPT and Codex.
- [OpenAI: Skills concepts](https://developers.openai.com/plugins/concepts/skills) — how skills package reusable workflows and resources.
- [OpenAI Skills catalog](https://github.com/openai/skills) — examples of skills published for Codex.

## License

This project is released under the [MIT License](LICENSE).
