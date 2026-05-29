# Two-strand gate for known branches

Date: 2026-05-28

This note records symbolic branch-level consequences of the exact
two-strand symmetric detector gate from
`proofs/two_strand_symmetric_gate.md`.  It does not prove the all-`n`
direct `A_{Sym(X)}` theorem.  It shows that the first possible direct
symmetric-detector obstruction cannot come from two standard known branches.

The nondegenerate/guitar branch is recorded separately in
`proofs/two_strand_guitar_gate.md`.

## Permutation-form solutions

Suppose

```text
R(x,y) = (sigma(y), tau(x))
```

where `sigma,tau in Sym(X)`.  For a YBE table of this form, `sigma` and
`tau` commute.  Set

```text
h = sigma tau.
```

Then

```text
R^2(x,y) = (h(x), h(y)).
```

Therefore, if `|X|>1`,

```text
ord(R:X^2->X^2) = 2 ord(h),
```

and for the one-point solution the order is `1`.

Since `h` is a permutation of `X`, `ord(h)` divides
`exp(Sym(X)) = lcm(1,...,|X|)`.  Thus every finite permutation-form solution
satisfies the exact two-strand symmetric gate:

```text
ord(R) divides 2 lcm(1,...,|X|).
```

This matches the detector used in
`proofs/involutive_permutation_detector.md`: the pure part is cyclic of order
`ord(h)`, and the `T_2` factor records the Artin permutation.

## Rack-type solutions

If `X` is already rack-type, `R(a,b)=(a ▷ b,a)`, then the standard rack
longitude factorization computes the braid action through the finite inner
group

```text
Inn(X) <= Sym(X).
```

For `B_2`, the exact finite-G longitude kernel for `G=Sym(X)` is
`2 exp(Sym(X)) Z`.  Since `Inn(X)` is a subgroup of `Sym(X)`, its exponent
divides `exp(Sym(X))`.  Hence `sigma_1^(2 exp(Sym(X)))` acts trivially on
the rack, and the two-strand crossing order again divides
`2 lcm(1,...,|X|)`.

This is not a direct rack-cover shortcut for arbitrary `X`; it applies only
inside the rack-type branch.  The obstruction in
`proofs/rack_cover_obstruction.md` still rules out covering an arbitrary
non-rack solution by a rack as a braided set.

## What remains open

The exact two-strand symmetric gate remains open outside the branches above,
the nondegenerate/guitar branch, and the audited finite families.  In
particular, a degenerate non-rack, non-permutation-form solution with

```text
ord(R) not dividing 2 lcm(1,...,|X|)
```

would disprove the direct `A_{Sym(X)}` route, though it would still not be a
full Sawin counterexample without the normalized-law all-finite-group
sequence.

The global problem is harder: even if every finite bijective solution passes
this `B_2` gate, the direct symmetric detector still requires an all-`n`
factorization through `W_{Sym(X)}(n)` for `n>=3`, or else the local
Green/corridor master theorem.

## Executable layer

The helper

```text
permutation_solution_crossing_order_formula(X)
```

returns `2*ord(sigma tau)` for permutation-form solutions with more than one
point and `1` for the one-point solution.  Regression tests compare this
formula with the actual two-strand braid-action permutation order and verify
that these examples pass `two_strand_symmetric_detector_covers_solution(X)`.

The summary helper

```text
two_strand_symmetric_gate_summary(X)
```

records the point count, exact symmetric longitude period, crossing order,
gate pass/fail value, branch tags, and a current explanation label.  The
labels distinguish the proved two-strand explanations
`involutive_order_two`, `rack_inner_group_branch`,
`permutation_form_twist_order_m`, and
`nondegenerate_derived_rack_branch` from `passes_unclassified`.  The latter
is not a counterexample; it marks rows that pass the divisibility test but
whose passage has not been assigned to one of the symbolic branch formulas
above.

The generated `proofs/symmetric_detector_audit.md` and
`proofs/linear_f2_audit.json` include explanation-count histograms.  After
the derived-rack branch is included, the exhaustive size-`3` corpus has no
`passes_unclassified` rows.  Future rows with that label are the right place
to look for a proof of the general two-strand divisibility, or for a direct
`A_{Sym(X)}` two-strand failure in larger families.
