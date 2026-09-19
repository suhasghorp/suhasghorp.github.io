# suhasghorp.github.io

Source of the article series *Building a Fixed Income Risk Engine*, published at
<https://suhasghorp.github.io/fixed-income-risk/>. The engine itself lives at
<https://github.com/suhasghorp/fixed-income-risk-engine>.

Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) on MkDocs 1.6 (pinned: MkDocs 2.0 is
incompatible with Material, so do not upgrade `mkdocs` past 1.x) and deployed by GitHub Actions
on every push to `main` (repository settings: Pages → Source → GitHub Actions).

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve          # http://127.0.0.1:8000
.venv/bin/mkdocs build --strict
```

- `docs/fixed-income-risk/_template.md`: the skeleton every article follows (built, not in the navigation).
- `docs/fixed-income-risk/glossary.md` and `includes/abbreviations.md`: generated from the engine's glossary by
  `scripts/glossary.py`.
