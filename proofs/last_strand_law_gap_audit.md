# Last-strand law gap audit

Date: 2026-05-30

This note supersedes the strongest form of
`proofs/sawin_last_strand_law_reduction.md` and
`proofs/point_pushing_fixed_variety_domination.md`.  It records a convention
failure in the tempting last-strand law criterion.

The failure is useful: it prevents the branch from replacing finite-longitude
identity by ordinary group-law identity too aggressively.

## Naive Claim That Fails

The false implication is:

```text
w in Law_k(G)  =>  iota_{k+1}(w) in K_G(k+1).
```

The last recursive longitude of `iota_{k+1}(w)` is a triangular Nielsen
transform of `w`, so the reverse implication

```text
iota_{k+1}(w) in K_G(k+1)  =>  w in Law_k(G)
```

remains a valid necessary condition.  The forward implication fails because
the other recursive Artin longitudes of a point-pushing word need not be
substitution/conjugate instances of `w`.

Thus ordinary law identity is necessary for last-strand finite-longitude
identity, but not sufficient.

## Explicit Guardrail Row

Let `X` be the three-element dihedral rack in the repository convention:

```text
R(a,b)=(2a-b mod 3, a).
```

Let `G=S_3` and let

```text
w=(x_1 x_2^{-1})^6 in F_2.
```

The word `w` is a law on `S_3`, because every element of `S_3` has order
dividing `6`.

However the last-strand point-pushing braid

```text
iota_3(w)
```

moves `X^3`.  The executable row

```text
point_pushing_exponent_escape_audit(
    X,
    law_bound=3,
    point_pushing_arity=2,
)
```

records an element of the marked point-pushing image of order `4`, represented
by `x_1 x_2^{-1}`.  Raising that representative to `lcm(1,2,3)=6` gives the
word above, and direct braid action agrees with the evaluated point-pushing
permutation.

The same row also computes finite-longitude identity in `S_3` by streaming the
Artin recursion without expanding the huge free words.  It records:

```text
symmetric_identity_longitude_signature = False.
```

So the moving braid is not a normalized-law obstruction row; it is a witness
that the naive law-to-`K_G` implication was too strong.

## Consequences

The exact global fork cannot be justified merely by replacing finite-longitude
identity with:

```text
S_m-law point-pushing words act trivially on X.
```

For a particular large `m` such a condition might still hold for separate
reasons, but ordinary law membership alone does not imply finite-longitude
invisibility.  Therefore this condition is not an equivalent reformulation of
the sharp detector kernel without an additional theorem controlling the other
point-pushing longitudes.

The safe statements are:

1. If `iota_{k+1}(w) in K_G(k+1)`, then `w` is a law on `G`.
2. A B certificate may use last-strand point-pushing words only after proving
   identity finite-longitude data, not merely ordinary law identity.
3. Any fixed-variety reformulation based on the false forward implication is
   a search heuristic or necessary-condition filter, not an equivalent
   theorem.

This returns the final A-route burden to the finite-longitude problem:
construct fixed interval-level detector groups and prove actual recursive
Artin-longitude identity kills residual motion, or produce a sequence whose
braids truly lie in every finite `K_G` eventually.

## Executable Support

Two helpers now support this guardrail.

```text
evaluate_artin_longitudes_streamed(...)
has_identity_longitude_signature_streamed(...)
```

evaluate finite-group longitude data by updating the Artin recursion directly
inside the finite group, avoiding exponential free-word expansion.

```text
point_pushing_exponent_escape_audit(...)
```

keeps the finite action-image mover and records whether the corresponding
symmetric finite-longitude signature is actually identity.  The regression
test checks the dihedral-rack row above and requires
`exposes_naive_law_gap`.
