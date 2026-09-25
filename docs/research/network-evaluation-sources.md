# Network research: distribution and candidate evaluation material

Research date: 2026-09-24

## Recommendation: do not publish this Skill as an npm package

This repository distributes an Agent Skill: its runtime artifact is the `SKILL.md` directory and supporting Markdown references. The Skills CLI accepts GitHub repository shorthands, Git URLs, and direct paths to a skill in a repository; it installs skill files from those locations. Its documented `npx skills add` command runs the installer CLI, not an npm package published by the skill author. The official Codex skill-installer likewise installs from a GitHub repository/path into `$CODEX_HOME/skills` (normally `~/.codex/skills`).

Therefore, for this project’s current form, a public GitHub repo and a clear install command are sufficient. An npm package would add a second release/discovery surface without improving the normal skill installation path. Consider npm only if the project grows a reusable JavaScript library or CLI, needs npm-based programmatic integration, or has an actual package-specific distribution/versioning need. These are product choices, not a requirement of the Skill format or documented installers.

Recommended README install examples should point directly at the existing GitHub repo/path and identify supported agents. Avoid telling users to `npm install` this skill. Cite: [Vercel Skills CLI source repository](https://github.com/vercel-labs/skills) (source formats and `npx skills add`) and [OpenAI skill-installer](https://github.com/openai/skills/blob/main/skills/.system/skill-installer/SKILL.md) (GitHub repo/path installation for Codex).

## Online sources for behavior-test material

These are source leads and test-design references, not claims of empirical validity. The current evaluation request should use a small, labeled, adversarial suite and preserve source licensing metadata. Avoid inferring clinical truth from any sample.

| Source | What it offers | Suitability and reuse limits |
|---|---|---|
| [Salesforce AI Research: AnchorBench](https://github.com/SalesforceAIResearch/AnchorBench) | Three public development banks of synthetic companion conversations, including clean, adversarial career-coaching, and emotional-vulnerability scenarios; includes schemas and scorer/test tooling. The README states that conversations and personas are synthetic. | Strongest direct format/reference match for multi-turn emotional interaction cases. Repository says all materials are CC BY-NC 4.0 and adds restrictions against competing with named AI providers. Do not copy its content into this MIT project or redistribute derived samples without a separate license review; use it as a reference or for separately authorized non-commercial evaluation only. Its answer-exposed development data is not a hidden test set and not statistically representative. |
| [Chatbot Confessions artifact](https://github.com/Majid-Mollaeefar/chatbot-confessions-artifact) | The artifact README reports 36 synthetic fictional-persona chatbot conversations for functional testing, split between private-disclosure and public-information cases. | Useful for testing whether the Skill distinguishes evidence from inference and avoids echoing unnecessary sensitive details. The inspected README describes synthetic data but did not establish a data license; do not copy/redistribute its transcripts unless the repository’s rights holder clarifies permission. This is privacy-analysis data, not a validated psychological benchmark. |
| [Channel Labs: Synthetic Conversation Generation](https://github.com/Channel-Labs/synthetic-conversation-generation) | An MIT-licensed toolkit for generating diverse synthetic personas and multi-turn conversations, with examples/data in its repository. Its README discusses diversity and natural conversation stopping. | Useful to create new synthetic, fictional test inputs. The MIT `LICENSE` is present for the software; it does not by itself establish the license of every separately sourced/generated data file. Inspect individual data provenance/license before reusing any sample. Safest route: use the generator only as methodological inspiration and author fresh fictional prompts for this project's evals. |
| [Project Gutenberg: The New Century Standard Letter-Writer](https://www.gutenberg.org/ebooks/56911) | Publicly available historical examples and templates for business, family, social, and love correspondence; ebook record states public domain in the United States. | Can provide varied correspondence forms or a low-context historical-style edge case. It is a letter-writing manual, not naturally occurring relationship evidence; its period conventions limit realism. Public-domain status is stated for the US, so check jurisdiction and Gutenberg terms before reproducing text. Better to paraphrase the setup and test inference boundaries rather than include full letters. |

### Suggested test design from these sources

1. Make the primary evaluation suite newly authored and explicitly fictional; vary short profile, one-turn conflict, long context, contradictory self-report, and high-vulnerability prompts.
2. Include pairs that differ by only one evidence item (for example, apology without follow-up versus apology plus specific repair) to test whether conclusions update proportionately.
3. Score evidence attribution, uncertainty calibration, alternative explanations, respectful tone, theory-fit, and boundary compliance separately. Mark diagnosis, criminality prediction, invented history, and unasked safety escalation as critical failures.
4. Keep external licensed material as citations/benchmark references, not committed eval text, unless reuse rights are clear. Record source URL, access date, license, edits, and whether the test is synthetic.
5. Report exact sample count and model/host/prompt conditions. A small authored suite is a regression check, not proof of clinical validity or population-level performance.

## Source notes

- [Vercel Skills CLI](https://github.com/vercel-labs/skills): repository documents GitHub shorthand/URL/path and git sources, `npx skills add`, per-agent and global/project installs.
- [OpenAI skill-installer](https://github.com/openai/skills/blob/main/skills/.system/skill-installer/SKILL.md): documents `--repo` + `--path` or `--url` installation for Codex.
- [AnchorBench](https://github.com/SalesforceAIResearch/AnchorBench): synthetic banks, exposed-development-set limitation, responsible-use terms, CC BY-NC 4.0 license.
- [Chatbot Confessions](https://github.com/Majid-Mollaeefar/chatbot-confessions-artifact): synthetic fictional personas and test-corpus description; inspected README alone does not establish transcript reuse license.
- [Channel Labs generator](https://github.com/Channel-Labs/synthetic-conversation-generation) and its [MIT software license](https://github.com/Channel-Labs/synthetic-conversation-generation/blob/main/LICENSE): source supports synthetic dialogue generation; software license should not be assumed to cover every included data artifact.
- [Project Gutenberg ebook record](https://www.gutenberg.org/ebooks/56911): description and US public-domain statement.
