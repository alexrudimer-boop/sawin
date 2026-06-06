# Width-3 cross-effect propagation response review

Date: 2026-06-06

This note records the review of the GPT-5.5 Pro response to
`prompts/gpt55_pro/2026-06-06-width3-cross-effect-propagation_answered.md`.

## Verdict

The response returned outcome `C`.

It does not provide a proof of the width-3 propagation lemma and does not
produce an arity-4 witness.  It correctly identifies the present blocker: the
full q=5 detector schema certificate is not local, so the intended detector
product `Y_X` is not locally defined for all 55 non-permutation size-three
tables.

## Valid mathematical content

For a fixed detector product `Y`, the response correctly records the tautological
inclusion:

```text
J^Y_{3,n} <= K^Y_n
```

and hence:

```text
rho^X_n(J^Y_{3,n}) <= rho^X_n(K^Y_n).
```

The missing theorem is the reverse inclusion on the realized `X`-image:

```text
rho^X_n(K^Y_n) <= rho^X_n(J^Y_{3,n}).
```

No current proof note supplies an induction or parabolic-generation argument
for this reverse inclusion.  The existing bounded-width theorem in
`proofs/parabolic_kernel_generation_bounded_width.md` is conditional: it
propagates domination after one has already proved the required bounded-width
kernel generation statement.  It does not prove that the current detector
product has width `3`.

The response also correctly isolates arity `4` as the first non-tautological
test.  For `n <= 3`, `J^Y_{3,n}` contains `K^Y_n` itself among the allowed
parabolic widths.  At `n=4`, the first realized cross-effect is:

```text
C^{X,Y_X}_{3,4}
  =
rho^X_4(K^{Y_X}_4) / rho^X_4(J^{Y_X}_{3,4}).
```

A nontrivial quotient here disproves the proposed width-3 propagation lemma
for that detector product.  It is not a Sawin counterexample unless promoted
to a cofinal rack-prefix obstruction sequence.

## Artifact status

The response correctly distinguishes the reported q=5 arity-3 closure from the
missing local artifact:

```text
reported q=5 closure:
  new_positive_detector_coverages 216
  combined_positive_detector_coverages 37692
  remaining_unresolved_candidates 0

local missing artifact:
  proofs/nonperm3_arity3_q5_resolution_certificate.json
  proofs/nonperm3_arity3_q5_resolution_verifier.py
```

The local importer audit now records the same blocker more concretely:

```text
schema_like_detector_records: 1
nonpermutation_ybe_tables: 55
tables_with_detector_components: 1
missing_table_count: 54
incomplete_detector_basis: true
```

This is an artifact/import gap, not finite negative evidence.

## Code consequence

The response noted that `tools/run_componentwise_cross_effect_audit.py`
emitted the dataclass field `n` rather than the requested row field `arity`.
The script now adds an `arity` alias to each output row while retaining `n`.
The full-table wrapper
`tools/run_nonperm3_detector_product_cross_effect_audit.py` does the same.

## Next prompt

The next prompt is now:

```text
prompts/gpt55_pro/2026-06-06-import-q5-detector-index-and-run-width3-audit_ask_now.md
```

It asks for the exact import/reconstruction path for the full q=5 detector
schema basis and the subsequent 55-row arity-4 componentwise cross-effect
audit.
