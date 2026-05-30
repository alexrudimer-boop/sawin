# Point-Pushing Base-Free Thresholds

Date: 2026-05-30

This note rewrites the remaining point-pushing fork as boundedness of
base-free extension thresholds.  The arity-`1` gate is already closed by
`proofs/point_pushing_base_arity_gate.md`, so the only thresholds that matter
are the one-new-strand Brunnian extension gates.

It does not prove outcome A or B.  It gives the current clean growth invariant
after removing the base gate.

## Definition

Let `X` be a finite bijective YBE solution and set

```text
s_X = ord(rho_{X,2}(A_{1,2})).
```

For `K>=1`, define the base-free prefix threshold

```text
epsilon_X(K)
```

to be the least integer `m>=s_X` such that the Brunnian gate induction for
`S_m` passes through arity `K`; equivalently:

1. the base arity passes, which is automatic from `m>=s_X`; and
2. every extension row with `2<=k<=K` has

   ```text
   failure_kind="none".
   ```

If `K=1`, this says only that `m>=s_X`.

## Theorem

For a finite solution `X`, the following are equivalent:

1. `X` is finite-rack dominated through the symmetric derivative-detector fork.
2. The sequence `epsilon_X(K)` is bounded.
3. There exists one integer `m>=s_X` such that every one-new-strand Brunnian
   extension row for `S_m` has `failure_kind="none"`.

If these conditions fail, then `epsilon_X(K)->infinity` along a subsequence,
and the first failures of the corresponding base-free prefixes give an
infinite certified non-base Brunnian tail after passing to a homogeneous
subsequence.

## Proof

If one fixed `m>=s_X` passes every Brunnian extension row, then by
`proofs/point_pushing_brunnian_gate_induction.md` all marked quotients

```text
D_k(S_m) -> P_k(X)
```

exist.  The sharp detector rack `A_{S_m}` therefore dominates `X`.

Conversely, if `X` is finite-rack dominated in the symmetric derivative fork,
then by `proofs/symmetric_derivative_quotient_fork.md` some `S_m` supplies all
marked quotients.  Enlarging `m` if necessary to satisfy `m>=s_X` preserves the
marked quotients by symmetric tower monotonicity.  Hence every extension row
passes for that one `m`, so `epsilon_X(K)<=m` for all `K`.

The equivalence between boundedness of `epsilon_X(K)` and existence of one
global `m` is immediate because `epsilon_X(K)` is nondecreasing in `K`: a
detector passing arity prefix `K+1` also passes prefix `K`.

If the sequence is unbounded, choose finite prefix lengths `K_j` such that
`epsilon_X(K_j)>j`.  For every large `j>=s_X`, `S_j` passes the base gate but
fails some extension row before or at `K_j`.  Choosing the first such row gives
a non-base failure kind

```text
stabilizer,
orbit_label,
or orbit_relation.
```

Fixed-arity cofinality forces these first failing arities to escape to
infinity after passing to a subsequence, and the finite set of non-base
failure kinds lets us pass to a homogeneous subsequence.  The finite row
certificates and normalized-prefix bridge then give the standard B-row format,
provided a symbolic infinite family is actually constructed.  QED.

## Relation To `mu_X(k)`

The original growth sequence

```text
mu_X(k)=min {m : D_k(S_m)->P_k(X)}
```

and the base-free threshold sequence `epsilon_X(K)` have the same boundedness
content.  The latter simply separates the always-finite base cutoff `s_X` from
the real extension problem.

Thus the remaining Sawin point-pushing target is:

```text
sup_K epsilon_X(K) < infinity.
```

## Audit Hook

The helper

```text
point_pushing_base_free_threshold_audit(...)
```

computes a finite rectangle approximation to `epsilon_X(K)`: it starts at the
base cutoff `s_X`, checks symmetric degrees up to a supplied bound, and
returns the first degree in that range whose base-free prefix is detected.

The fields

```text
minimal_detecting_degree
detected_within_bound
bound_below_base_cutoff
unresolved_degrees
```

are finite-prefix diagnostics.  They do not prove boundedness or unboundedness
without a symbolic all-`K` argument.
