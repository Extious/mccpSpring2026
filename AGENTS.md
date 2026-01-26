# Agent Notes (mccpSpring2026)

This repository is primarily course material plus a handful of Python utilities (PDF/Word processing and an archived RAG chatbot demo). It is not a single packaged application.

Working assumptions for agentic coding:
- Prefer minimal, targeted edits; keep scripts runnable as standalone files.
- Do not commit secrets (API keys, `.env`, `LLM/` contents). See `.gitignore`.
- Many scripts are "one-off"; avoid repo-wide refactors or formatting sweeps unless asked.

## Repo Map

- `scripts/`: PDF/Word processing utilities.
- Repo root `process_*.py`, `convert_*.py`, `format_*.py`: convenience entrypoints.
- `writing/_archive/activity 1.5 build a chatbot/`: archived RAG chatbot demo + ad-hoc test scripts.
- `literature/`: papers/notes (often large / non-code).

## Setup

No top-level `pyproject.toml`/`package.json`/`Makefile` is present.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
```

Chatbot demo deps (only pinned requirements in the repo):

```bash
python -m pip install -r "writing/_archive/activity 1.5 build a chatbot/requirements.txt"
```

System deps (macOS):

```bash
brew install poppler  # for pdf2image (pdftoppm)
```

## Build / Lint / Test Commands

There is no unified build system; use targeted commands.

Sanity checks:

```bash
python -m compileall .
python -m pip check
```

Lint/format (optional; not configured repo-wide):

```bash
python -m ruff check .
python -m black .
```

### Tests (Ad-hoc Script Style)

Most "tests" are standalone scripts under `writing/_archive/activity 1.5 build a chatbot/`.

Run a single test (preferred approach in this repo):

```bash
python "writing/_archive/activity 1.5 build a chatbot/test_poe_api.py"
```

Other common test scripts:

```bash
python "writing/_archive/activity 1.5 build a chatbot/test_zai_api.py"
python "writing/_archive/activity 1.5 build a chatbot/test_hkbu_api.py"
python "writing/_archive/activity 1.5 build a chatbot/test_hkbu_embeddings.py"
```

If you need to run "a single test" via pytest (only if pytest is installed):

```bash
python -m pytest "writing/_archive/activity 1.5 build a chatbot/test_hkbu_embeddings.py" -k hkbu
```

## Common Run Commands

RAG chatbot (CLI):

```bash
python "writing/_archive/activity 1.5 build a chatbot/rag_chatbot.py" literature/HXChen --api poe
python "writing/_archive/activity 1.5 build a chatbot/rag_chatbot.py" literature/HXChen --api demo
```

RAG chatbot (Streamlit UI):

```bash
streamlit run "writing/_archive/activity 1.5 build a chatbot/rag_chatbot_ui.py"
```

PDF/Word utilities (note: several scripts embed absolute paths; inspect before running):

```bash
python scripts/process_pdfs_with_ai.py
python scripts/process_word_docs.py
python scripts/format_markdown_files.py
```

## Secrets / Keys / Safety

`.gitignore` excludes `.env`, `*.key`, and the `LLM/` folder. Keep it that way.

Keys may be stored (locally) in:
- `LLM/poe.md`
- `LLM/zai.md`
- `LLM/HKBUAPIkey.md`

Guidelines:
- Never print full keys; redact to a short prefix if needed.
- Prefer env vars when adding new code paths:
  `POE_API_KEY`, `ZAI_API_KEY`, `HKBU_API_KEY` (fallback to files is OK).

## Code Style Guidelines (Python)

This repo is script-heavy; optimize for clarity and CLI usability.

Formatting:
- 4 spaces, no tabs; keep existing style.
- Line length ~88-100; do not reflow large text blocks.
- Prefer f-strings.
- Prefer `pathlib.Path` for new code.

Imports:
- Order with blank lines: stdlib, third-party, local.
- Avoid `import *`.
- If a dependency is optional/heavy, import inside the function and raise a helpful error.

Types:
- Add type hints where they clarify inputs/outputs of reusable helpers.
- Prefer built-in generics (`list[str]`, `dict[str, str]`) when Python version allows.
- Use `Optional[T]` only when `None` is a meaningful value.

Naming:
- Files/modules: `snake_case.py`.
- Functions/variables: `snake_case`.
- Classes: `PascalCase`.
- Constants: `UPPER_SNAKE_CASE`.
- CLI args: use consistent names (`--api`, `--provider`, `--output-dir`).

Error handling and logging:
- Avoid bare `except:`; catch specific exceptions when reasonable.
- For user-facing scripts: print a concise message and exit non-zero (`sys.exit(1)`) on failure.
- For helper functions: raise exceptions; let the caller decide.
- Network calls: always set timeouts; include status code + short response snippet on errors; consider simple retries.

I/O and encoding:
- Use `encoding="utf-8"` for text files.
- Only use `ensure_ascii=False` in JSON when you intentionally want Unicode preserved.
- Avoid writing outside the repo unless explicitly part of the script's purpose.

Absolute paths:
- Some existing scripts contain hardcoded absolute paths. Do not add new ones.
- Prefer `argparse`, env vars, or paths relative to `Path(__file__)`/repo root.

## Cursor / Copilot Rules

No Cursor rules were found in `.cursor/rules/` or `.cursorrules`.
No Copilot instructions were found in `.github/copilot-instructions.md`.
