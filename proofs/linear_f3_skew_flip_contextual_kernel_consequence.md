# Linear F3 Contextual Kernel Consequence

This generated verifier cross-checks the linear F3 completion,
orbit-injectivity, monolith, and pure-kernel monodromy audit artifacts.
It records the low-arity consequence used by the current theoretical
prompt.

## Source Artifacts

- `proofs\linear_f3_skew_flip_completion_audit.json`
- `proofs\linear_f3_skew_flip_orbit_audit.json`
- `proofs\linear_f3_skew_flip_monolith_audit.json`
- `proofs\linear_f3_skew_flip_pure_kernel_monodromy_audit.json`

## Summary

- completion audit passed: `True`;
- orbit audit passed: `True`;
- monolith audit passed: `True`;
- pure-kernel audit passed: `True`;
- degenerate non-involutive rows: `144`;
- subdirect rows: `64`;
- contextual orbit-injectivity all rows through arity: `5`;
- derived contextual-kernel X-motion exclusion through arity: `5`;
- explicit two-strand pure-kernel X-motion count: `0`;
- explicit three-strand pure-kernel checked rows: `4`;
- explicit three-strand pure-kernel X-motion count: `0`;
- all claimed checks passed: `True`.

## Consequence

For the 64 subdirectly irreducible rows in this family, the existing
contextual rack completion and orbit-injectivity audit imply that
any braid in the contextual-rack kernel acts trivially on `X^n` for
`n <= 5`.  Therefore the pure detector-kernel monodromy obstruction
is excluded through arity 5 for these rows, independently of the
monolith quotient detector.

This remains finite evidence.  It does not prove all-arity
contextual pure-loop faithfulness and does not resolve A or B.
