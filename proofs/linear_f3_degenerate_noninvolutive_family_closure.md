# Linear F3 Degenerate Non-Involutive Family Closure

Date: 2026-06-08

This note records the closure of the six-point linear skew-over-flip
degenerate non-involutive family

```text
X={0,1} x F_3,
R((a,i),(b,j))=((b,I),(a,J)),
(I,J)^T=M_ab(i,j)^T,
M_ab in GL_2(F_3).
```

It does not solve Sawin's problem in full.  It eliminates the first serious
six-point linear residual family used in the current search.

## Classification

The exhaustive classification audit is

```text
proofs/linear_f3_skew_flip_completion_audit.md
```

It checks `48^4` matrix choices and finds `1088` YBE solutions:

```text
816 nondegenerate non-involutive,
144 degenerate non-involutive,
96 degenerate involutive,
32 nondegenerate involutive.
```

The known nondegenerate and involutive theorems handle every row except the
`144` degenerate non-involutive rows.

## Degenerate Non-Involutive Rows

The monolith audit

```text
proofs/linear_f3_skew_flip_monolith_audit.md
```

splits the `144` rows as:

```text
80 non-subdirect rows,
32 subdirect monolith J-separating rows,
32 subdirect formal monolith J-collision rows.
```

Each branch is now closed.

### Non-Subdirect Rows

The audit

```text
proofs/linear_f3_nonsubdirect_quotient_factor_closure_audit.md
```

checks that all `80` non-subdirect rows are reconstructed by products of
proper quotient factors that are already known dominated: rack-form,
nondegenerate, or involutive quotients.  Hence all `80` are finite-rack
dominated.

### Monolith J-Separating Rows

The audit

```text
proofs/linear_f3_separating_quotient_closure_audit.md
```

checks that all `32` separating rows have involutive four-point monolith
quotients, contextual rack completions, and all-arity injectivity of

```text
(pi_mu^n,J_n).
```

The relative contextual theorem therefore dominates all `32` rows.

### Formal Monolith J-Collision Rows

The audit

```text
proofs/linear_f3_gap_corrected_invariant_audit.md
```

checks the gap-corrected hidden-fibre invariant for all `32` collision rows.
The proof note

```text
proofs/linear_f3_gap_corrected_invariant_closure.md
```

proves that every braid trivial on the nondegenerate four-point monolith
quotient is trivial on the six-point lift:

```text
ker rho^Z_n <= ker rho^X_n
```

for all `n`.  Hence all `32` collision rows are finite-rack dominated.

## Conclusion

Every degenerate non-involutive linear skew-over-flip solution on
`{0,1} x F_3` is finite-rack dominated.

Together with the known nondegenerate and involutive cases, every six-point
linear skew-over-flip YBE solution over `F_3` in this family is finite-rack
dominated.

A genuine counterexample must leave this linear `F_3` skew-over-flip family.
