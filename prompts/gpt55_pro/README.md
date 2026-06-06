# GPT-5.5 Pro Prompts

This folder stores the self-contained prompts intended for GPT-5.5 Pro during
the Sawin finite-rack domination project.

Workflow:

1. Write each planned Pro query here before attempting to send it.
2. Use timestamped Markdown files so the prompt history is reproducible even
   if Chrome or ChatGPT is unavailable.
3. Mark each prompt status in the file header and filename.  Use at most one
   `_ask_now.md` suffix for the prompt that should be sent or answered next.
   Use `_answered.md` and `_partially_answered.md` once a response or local
   computation has settled that prompt.  Use `_superseded.md` for stale prompts
   that should not be answered now.
4. When the next handoff contains the two-track Pro workflow, label the two
   prompt bodies exactly `computational_asknow` and `theoretical_asknow`.
5. Keep prompts self-contained: assume GPT-5.5 Pro has no access to this repo.
6. After a Pro answer is acted on, record any resulting code/proof artifact in
   the normal `proofs/`, `src/`, `tests/`, or `tools/` locations.

These files are prompts only.  They are not proof artifacts unless separately
promoted into the proof ledger.
