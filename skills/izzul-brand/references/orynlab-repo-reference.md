# OrynLab repository as a STRUCTURE reference

Reviewed 2026-10-14: [OrynGithub](https://github.com/Amjadh23/OrynGithub), `main` commit `2ea84f2133f58314c7d1c6436ebf55d095ac6a3a`.

- It packages a Claude Code plugin marketplace with `jira-buddy` and a brand skill `orynlab-brand`.
- The brand skill stores instructions under `skills/.../SKILL.md`, optional CSS design tokens and SVG assets; `.claude-plugin/*.json` provide metadata/install plumbing.
- Here we mirror **modular capability packaging**: root plugin manifest, optional marketplace manifest, self-contained skill, `references`, `assets` and `templates`.
- **We do not reproduce** OrynLab's copyrighted design, specific Poppins-based monochrome identity, its brand dots, its wordmark or its Jira integration.
- This repo targets **one personal skill** (a full plugin marketplace is not a prerequisite). Including a one-plugin marketplace manifest is optional convenience.
- Re-check Claude Code commands/API against your installed version. A static repository read does not prove installing or executing a plugin.
