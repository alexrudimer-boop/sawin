# Progress summary

Date: 2026-05-29

This file is the compact state of the Sawin finite-rack domination workspace.
It is a rigorous progress summary, not a final resolution.  As of this
snapshot, neither final outcome A nor final outcome B has been proved.

## Problem

For every finite bijective set-theoretic Yang-Baxter solution `X`, decide
whether there is a finite rack `Y`, independent of braid index `n`, such that

```text
ker rho_{Y,n} subset ker rho_{X,n}   for all n.
```

The permitted final answers are:

- A. a complete all-`n` proof of finite-rack domination; or
- B. an explicit finite bijective YBE counterexample together with a
  normalized-law obstruction sequence defeating every finite rack.

Finite search, bounded detector misses, and timeout evidence are guardrails
only.  They cannot close either outcome.

## Established reductions

The quotient/residual setup is fixed.  For a quotient `pi:X->Z`, if `Z` is
already dominated by a rack `Q`, set `N_n=ker rho_{Q,n}`.  For each
`z in Z^n`, the fibre product is `X_z=prod_i pi^{-1}(z_i)`, and the residual
action is

```text
delta_{n,z}: N_n -> Sym(X_z).
```

The bundled residual map is `Delta_n(beta)=(delta_{n,z}(beta))_z`.

The sharp obstruction theorem is now the central reduction.  For a finite
group `G`, the rack

```text
A_G = T_2 x (G x G),
(a,u) triangleright (b,v) = (aba^{-1}, av)
```

detects finite-`G` recursive Artin-longitude data
`Lambda_{G,n}(beta)`.  For an interval over `Q`, it is enough to find one
finite group `G=G(pi,Q)`, independent of `n`, such that for all `n` and
`beta in N_n`,

```text
Lambda_{G,n}(beta)=Lambda_{G,n}(1) => Delta_n(beta)=1.
```

Then `Q x A_G` dominates the interval.  The repository contains the executable
rack constructor `sharp_obstruction_rack(Q,G)`.

The congruence-chain induction is reduced to local-minimal intervals.  Given
a maximal congruence chain

```text
Delta_X=kappa_0 < ... < kappa_m=Nabla_X,
```

it is enough to prove the local theorem for every interval
`X/kappa_i -> X/kappa_{i+1}`.  If the local detector is `G_i`, the racks are
assembled by `Q_i=Q_{i+1} x A_{G_i}`.  This preserves finiteness and
independence from `n` provided every `G_i` is fixed at the interval level.

## Local-minimality and semisplit handling

The local table has colours `a,b`, fibres `A_a`, and bijections

```text
T_{a,b}: A_a x A_b -> A_{a dot b} x A_{a*b}
```

satisfying the coloured YBE.  Local-minimality means the only admissible
families of fibre congruences `theta_a` are all equality and all universal,
where

```text
T_{a,b}(theta_a x theta_b) =
theta_{a dot b} x theta_{a*b}.
```

The old full partition enumeration is no longer needed for this question.
The exact criterion is:

```text
the interval is local-minimal
iff every distinct pair p,q in every fibre A_a
generates the all-universal admissible congruence family.
```

The helper `LocalInterval.pair_generated_local_minimality_audits()` computes
the least admissible closure of each single pair by transporting product
relations through every local bijection and inverse.  This is an exact
finite certificate for the supplied interval and works for arbitrary finite
fibre sizes; it is not Bell-number partition enumeration.
The generated closure audit now records first-derivation rows for every
nontrivial relation edge, including the depth, seed/forward/inverse source,
crossing colour pair, and source product pairs.  Thus local-minimality rows
are no longer only Boolean or counter-based: a proof critic can inspect how
each universal fibre edge was forced, or where a proper mixed closure stops.

Semisplit families are fully visible.  For a subset of colours `S`, the
equality/universal family

```text
theta^S_a = universal on A_a if a in S,
theta^S_a = equality on A_a otherwise
```

is tested at the relation level, not by a colour-graph shortcut.
`LocalInterval.semisplit_audits()` records every admissible semisplit family
or a concrete failed transport witness.  The Boolean-CSP view
`semisplit_constraint_rows()` and `semisplit_boolean_assignments()` is an
independent tabular presentation of the same exact relation test, including
singleton-fibre canonicalization.

Thus any final proof or counterexample must pass this gate: a semisplit leak
is simply non-local-minimal and must be refined before invoking the master
local theorem.

## Known closed branches

The following branches have finite-`G` measurable routes recorded in the
proof notes and tests:

- rack-type, involutive, permutation-form, and nondegenerate/guitar branches;
- affine and fibre-size-two affine over `F_2` branches in the audited form;
- pairwise-linking and one-colour product holonomy branches;
- coboundary/product-label telescope branches;
- finite semidirect affine and finite product detector branches already
  reduced to fixed finite groups;
- direct `Sym(X)` detection for the known symbolic subbranches.

The notes also close several false shortcuts:

- a direct rack cover of `X` exists only in the rack-type case;
- nondegenerate covers cannot solve arbitrary degenerate intervals by
  quotienting;
- fixed finite braid-action image laws vanish on that fixed image and do not
  produce B;
- pure two-strand crossing-order mismatch cannot be outcome B, since for
  `r=ord(R_X)` the cyclic group `C_r` detects the `B_2` action.

## Longitude subgroup calculus

The longitude-value subgroup

```text
V_beta(G) <= G
```

is now functorial under fixed finite group homomorphisms and multiplicative
over fixed direct products:

```text
V_beta(prod_i G_i) = prod_i V_beta(G_i).
```

The code includes explicit witness operations:

- `pushforward_longitude_subgroup_witness(...)`;
- `direct_product_longitude_subgroup_witness(...)`;
- product endpoint witnesses in `prod_i U(M_i)`.

This matters because a proof may use finitely many branch detector groups,
but the sharp obstruction theorem requires one finite product group
independent of `n`.  The witness calculus prevents an informal factor list
from hiding an `n`-dependent detector.

## Semigroup, unit, and endpoint progress

The semigroup holonomy layer has been sharpened to a group problem.  If a
word in total transformations of a finite set has a final residual action
that is a permutation, every total-transformation factor in that word is a
unit/permutation.  Reset-like nonunit labels cannot be the final B
obstruction.

For one finite transformation monoid `M`, the preferred A-side endpoint
certificate is:

```text
final residual unit composite lies in V_beta(U(M)).
```

It is enough to display this endpoint as a finite product of evaluated
recursive longitudes under an input-dependent assignment into the fixed unit
group `U(M)`.  For several fixed monoids, the product endpoint audit packages
the certificates into one direct product group.  The current code records
literal product witnesses and checks that their values match the residual
endpoint.

This is an important reduction but not the missing theorem.  The missing
theorem must produce these endpoint expressions uniformly for all braid
indices in the remaining branch.

## Green and corridor progress

The current final local branch is named
`bi_free_universal_corridor_bottleneck`.  An interval reaches it only after:

- coloured YBE holds;
- no semisplit family survives;
- pair-closure local-minimality is exact;
- no product-permutation witness routes it to a closed product branch;
- the local coordinate-kernel closure is universal rather than equality;
- no known whole-solution finite-`G` branch applies.

The finite detector candidate for this branch is a product of:

- symmetric groups on left and right Green kernel-block quotients;
- left and right Schutzenberger action groups of regular Green classes;
- left and right atom quotient inner groups when the atom layer is rack-like;
- already proved quotient or branch detector factors.

This product is finite and depends only on the interval and the quotient
detector, not on `n`.
The executable factor helper now includes these atom inner groups directly,
with duplicate concrete group tables removed, so the code-level detector
candidate matches the atom-rack lift criterion.

The Green atom layer is now explicit.  Retained edge-germs in a regular Green
`R`-class have a saturated atom relation generated by `q^a ~ q`.  The helper
`atom_action_summary(...)` checks whether completed rows descend to

```text
p(a) triangleright p(q) = p(a^q)
p(a^q) triangleleft p(q) = p(a).
```

If total and well-defined, `atom_quotient_solution(...)` constructs a finite
right-rack-like YBE layer, and `atom_quotient_rack_audit(...)` checks
bijective right translations and right self-distributivity directly.

The descent-closure helper `atom_descent_closure_summary(...)` records the
least coarsening needed for descent.  In all current tiny exhaustive audits
and named stress rows this closure is trivial, but this is diagnostic only.
The new `atom_descent_quotient_rack_audit(...)` checks whether a nontrivial
closed quotient is nevertheless a total finite rack layer.  Thus the symbolic
theorem must prove either trivial descent, controlled descent-closed rack
quotients plus endpoint/unit detection for the lost lower information, or a
real normalized-law counterexample.

## Counterexample route status

The B route has been reduced to normalized-law behavior.  It is not enough to
miss one finite detector group.  To defeat every finite rack, a candidate must
provide:

- an explicit finite bijective YBE solution `X`;
- a symbolic YBE proof;
- braid words `beta_j in B_{q_j}` with `q_j -> infinity`;
- eventual finite-`G` longitude invisibility for every finite group `G`;
- explicit moved tuples under `rho_{X,q_j}`;
- a proof that the sharp obstruction theorem converts this into failure
  against every finite rack.

The diagonal product lemma says that if one explicit local residual interval
has no finite detector group at all, then products of the first `j` finite
groups and right-strand stabilization yield the required normalized-law
sequence.  No such explicit interval has been found.

## Current bottleneck

The unresolved mathematical task is the Master Local-Minimal Residual
Theorem, now concentrated in the bi-free universal-corridor branch:

```text
For every local-minimal interval pi:X->Z with Z dominated by Q,
construct one finite group G(pi,Q), independent of n, such that
Lambda_{G(pi,Q),n}(beta)=Lambda_{G(pi,Q),n}(1)
implies Delta_n(beta)=1 for all n and beta in ker rho_{Q,n}.
```

The current best A route is to prove that all residual Green/corridor
endpoint units are explicit products of recursive Artin-longitude evaluations
in the fixed product of the finite groups above.

The current best B route is to construct a finite local-minimal interval in
this exact bottleneck branch whose unit/group-like residual holonomy admits a
normalized-law sequence invisible to every finite group but moving an explicit
tuple.

Until one of these is done, the archive supports neither final A nor final B.

## Verification snapshot

At the latest verified snapshot:

- `python -m unittest discover -s tests` passed with 261 tests;
- `python -m compileall -q src tests tools` passed;
- `node --check tools/build_reduction_audit_workbook.mjs` passed;
- the proof log DOCX and reduction audit workbook were regenerated;
- LibreOffice/`soffice` was unavailable, so DOCX visual render QA could not
  be completed;
- the Desktop zip was overwritten rather than versioned separately.
