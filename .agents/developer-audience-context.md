# Developer audience context (pointer)

Some third-party skills in `.claude/skills/ext-*` look for this file. In this repo the source of truth is `knowledge/`.
Read `.agents/product-marketing.md` first, then:

- `knowledge/market/channels.csv`: communities we scored, whether self-promotion is allowed, effort. Run `python tools/kb.py cham-diem` for the ranking.
- `knowledge/playbooks/content.md`: topics and formats that fit our developers.
- `knowledge/market/trends-log.md`: recent pain points quoted from Reddit, Hacker News, GitHub issues, with links.

Audience in one paragraph (the files above win if they differ): developers, DevOps engineers and sysadmins who live in the
terminal and manage many SSH hosts (Vutty), and Mac users who want to free disk space without a subscription or a black box
(Vutidy). They distrust hype, value local-first and open source, read the code, and react badly to marketing that hides that
the apps are free to build from source or that the builds are unsigned.
