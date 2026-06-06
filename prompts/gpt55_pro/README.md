# GPT-5.5 Pro Prompts

This folder stores the self-contained prompts intended for GPT-5.5 Pro during
the Sawin finite-rack domination project.

Workflow:

1. Write each planned Pro query here before attempting to send it.
2. Use timestamped Markdown files so the prompt history is reproducible even
   if Chrome or ChatGPT is unavailable.
3. Mark each prompt status in the file header and filename.  For the current
   two-track Pro workflow, keep two active files named with the explicit
   suffixes `computational_asknow.md` and `theoretical_asknow.md`, and label
   their prompt bodies exactly `computational_asknow` and `theoretical_asknow`.
   Use `_answered.md` and `_partially_answered.md` once a response or local
   computation has settled that prompt.  Use `_superseded.md` for stale prompts
   that should not be answered now.
4. Do not keep a stale combined `_ask_now.md` handoff once the separate
   computational/theoretical asknow files exist.
5. Keep prompts self-contained: assume GPT-5.5 Pro has no access to this repo.
6. After a Pro answer is acted on, record any resulting code/proof artifact in
   the normal `proofs/`, `src/`, `tests/`, or `tools/` locations.

These files are prompts only.  They are not proof artifacts unless separately
promoted into the proof ledger.
