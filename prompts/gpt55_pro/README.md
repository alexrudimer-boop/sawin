# GPT-5.5 Pro Prompts

This folder stores the self-contained prompts intended for GPT-5.5 Pro during
the Sawin finite-rack domination project.

Workflow:

1. Write each planned Pro query here before attempting to send it.
2. Use timestamped Markdown files so the prompt history is reproducible even
   if Chrome or ChatGPT is unavailable.
3. Mark each prompt status in the file header (`queued`, `sent`, or
   `answered`); if the desktop UI is locked, leave it as `queued`.
4. Keep prompts self-contained: assume GPT-5.5 Pro has no access to this repo.
5. After a Pro answer is acted on, record any resulting code/proof artifact in
   the normal `proofs/`, `src/`, `tests/`, or `tools/` locations.

These files are prompts only.  They are not proof artifacts unless separately
promoted into the proof ledger.
