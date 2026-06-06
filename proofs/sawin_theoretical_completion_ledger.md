# Sawin theoretical completion ledger

Date: 2026-06-06

This note records the current self-contained mathematical boundary for Will
Sawin's finite-rack domination question.  It is intended as a proof-review
ledger: theorem/proof claims are separated from finite evidence, heuristics,
and the exact remaining obligations.

## Problem

Let `X` be a finite bijective set-theoretic solution of the Yang-Baxter
equation, so each braid group `B_n` acts on `X^n`:

```text
rho^X_n : B_n -> Sym(X^n).
```

A finite rack `Y` is viewed as the set-theoretic solution

```text
R_Y(a,b) = (a*b, a).
```

Sawin's question asks whether every finite `X` admits one finite rack `Y`,
independent of `n`, such that

```text
ker rho^Y_n <= ker rho^X_n
```

for every `n`.

## Exact positive target

A positive solution must give, for every finite `X`, a finite rack `Y_X` and a
proof that every braid invisible to `Y_X` in every arity is also invisible to
`X`:

```text
for all n and beta in B_n,
rho^{Y_X}_n(beta)=1 => rho^X_n(beta)=1.
```

Finite checks at bounded arity, even with complete certificates, do not prove
this unless they are tied to an all-arity theorem.

Known positive theorem: if `X` is one-sided nondegenerate, the guitar or
derived-rack construction gives a finite rack whose braid action is conjugate
to the `X` braid action in every arity.  Thus the remaining difficulty is in
degenerate finite bijective solutions.

## Exact negative target

Fix an enumeration `R_1,R_2,...` of one labelled representative of every
finite rack isomorphism class, and set

```text
P_m = R_1 x R_2 x ... x R_m.
```

Each `P_m` is a finite rack and

```text
ker rho^{P_m}_n = intersection_{i<=m} ker rho^{R_i}_n.
```

The following criterion is the normalized obstruction required for a negative
answer.

```text
Theorem.
For a fixed finite YBE solution X, no finite rack dominates X if and only if
for every m there exist n_m and beta_m in B_{n_m} such that

  rho^{P_m}_{n_m}(beta_m)=1
  but
  rho^X_{n_m}(beta_m) != 1.
```

Proof.  If such witnesses exist for every `m`, then no finite rack `R_j`
dominates `X`: for `m>=j`, `ker rho^{P_m}_n <= ker rho^{R_j}_n`, so the
prefix witness `beta_m` is also in `ker rho^{R_j}_{n_m}` while still moving
`X^{n_m}`.

Conversely, suppose there is no such witness for some `m`.  Then for every
`n`,

```text
ker rho^{P_m}_n <= ker rho^X_n,
```

so the finite rack `P_m` dominates `X`.  Therefore, if no finite rack
dominates `X`, every prefix `P_m` must admit a witness.

This is why a miss against one chosen detector product is not a Sawin
counterexample.  A genuine negative answer needs the cofinal prefix sequence.

## Route-specific compactness gap

Many partial approaches construct finite contextual rack detector schemas
rather than arbitrary finite rack dominators.  The following compactness
statement records the exact uniformity gap for that route.

Let `B_X` be the class of actual bad arrows for a chosen base detector `P_X`:

```text
B_X = {
  (n, beta, x) :
  beta in ker rho^{P_X}_n,
  rho^X_n(beta)x != x
}.
```

For a finite contextual rack detector `D`, let `S_D subset B_X` be the bad
arrows separated by `D`, and `U_D = B_X \ S_D`.  Products of detectors satisfy

```text
S_{D_1 x D_2} = S_{D_1} union S_{D_2},
U_{D_1 x D_2} = U_{D_1} intersection U_{D_2}.
```

Theorem.  The following are equivalent for the chosen contextual detector
route.

```text
1. Some finite product of contextual rack detectors separates every bad arrow
   in B_X.

2. There is no ultrafilter U on B_X such that U_D belongs to U for every
   finite contextual rack detector D.
```

Proof.  If a finite product `D` separates every bad arrow, then `U_D` is
empty, so no ultrafilter can contain all `U_D`.

Conversely, if no finite product separates every bad arrow, then every finite
intersection of sets `U_D` is nonempty, because that intersection is the
unseparated set for the finite product of those detectors.  Hence the family
`{U_D}` has the finite intersection property.  By the ultrafilter lemma it
extends to an ultrafilter on `B_X` containing every `U_D`.

Thus pointwise detector separation

```text
for every bad arrow h, exists D_h separating h
```

is not enough.  One must rule out a harmful ultrafilter of bad arrows escaping
every fixed finite detector, or else construct a finite product detector that
separates all bad arrows uniformly.

This compactness theorem is route-specific.  It does not itself prove or
disprove Sawin's problem for arbitrary finite rack dominators; it explains the
uniformity obligation inside the contextual endpoint strategy.

## Contextual detector theorem

A contextual rack detector schema consists of a finite quotient `M` of the
structure monoid, a finite rack `Q`, and a map

```text
alpha : M x X x M -> Q
```

satisfying the contextual `T` and rack `R` crossing relations for every
`p,s in M` and `x,y in X`.

For every arity define

```text
Phi^alpha_n(x_1,...,x_n)_i =
  alpha([x_1...x_{i-1}], x_i, [x_{i+1}...x_n]).
```

The checked local relations imply

```text
Phi^alpha_n : X^n -> Q^n
```

is braid-equivariant for every `n`.  This is an all-arity theorem about a
verified schema, not a bounded-arity extrapolation: braid equivariance follows
generator by generator because the only local change is at two adjacent
coordinates, and the contextual `T` and `R` identities are exactly the two
identities needed to match the rack crossing on those readout coordinates.

Consequently, if finitely many contextual schemas separate every actual
nontrivial detector-kernel motion of `X^n` in every arity, then the product of
their finite rack targets dominates `X`.

## H3 sufficient theorem

For the non-permutation size-three route, let `S_X` be the verified arity-2
and arity-3 contextual detector schemas, and let `Y_X` be the product of the
distinct rack targets appearing in them.

Hypothesis H3, or 3-coskeletal endpoint completeness:

```text
For every n, every beta in ker rho^{Y_X}_n, and every x in X^n with
rho^X_n(beta)x != x, the pair (x, rho^X_n(beta)x) contains a transported
principal endpoint obstruction whose core has arity at most 3 and is separated
by one of the schemas in S_X.
```

Theorem.  H3 implies direct domination:

```text
ker rho^{Y_X}_n <= ker rho^X_n
```

for every `n`.

Proof.  Let `beta in ker rho^{Y_X}_n`.  Since `Y_X` contains every target rack
`Q` used by every schema, `beta` acts trivially on each `Q^n`.  By the
equivariance theorem,

```text
Phi^alpha_n(beta x) = beta Phi^alpha_n(x) = Phi^alpha_n(x)
```

for every verified schema.  If `beta` moved some `x in X^n`, H3 would give a
transported arity-at-most-3 endpoint core separated by one of these schemas,
contradicting equality of the corresponding readout values.  Hence `beta`
fixes every `x`, so `beta in ker rho^X_n`.

Thus H3 is more than enough: it proves direct domination, not merely width-3
realized parabolic propagation.

## Finite evidence

The current size-three non-permutation evidence is proof-grade only in fixed
arity.

Arity-2 endpoint gate:

```text
2064 principal bad endpoint pairs
2064 finite-rack-separated
0 unresolved
```

Arity-3 endpoint gate:

```text
37692 principal bad endpoint pairs
37476 separated by q<=4 detectors
216 additional separated by q=5 detectors
0 unresolved
```

Arity-4 product audit for the detector product `Y_X`:

```text
55 non-permutation size-three rows
0 truncated rows
quotient_size distribution {1: 55}
kernel_image_size distribution {1: 55}
```

The arity-4 stabilizer result proves the stronger fixed-arity statement

```text
rho^X_4(ker rho^{Y_X}_4) = 1
```

for every one of the 55 non-permutation size-three tables.  It does not prove
the same statement for `n>=5`.

Arity-5 has only partial probes so far.  The current two partial stabilizer
certificates cover 37 of the 55 rows, all with trivial detector-kernel image.
The remaining 18 rows, including all `[2,3,5]` q=5-component rows, are
unresolved.  A timeout on one q=5-component row is not negative evidence.

## Exact open implications

The current material does not prove Sawin's problem and does not provide a
counterexample.  The exact missing positive implication in the size-three route
is:

```text
beta in ker rho^{Y_X}_n and rho^X_n(beta) != 1
  =>
there is an arity <= 3 detector-separated endpoint core.
```

Equivalently, Brunnian or high-context detector-kernel monodromy must be
excluded.

The exact missing global positive theorem is a finite endpoint-change cover,
finite contextual rack absorption, or a different construction that produces
one finite rack detector for every finite `X` in all arities.

The exact missing global negative theorem is the cofinal prefix obstruction
sequence from the criterion above.  A single high-arity miss against one
detector product, even the current `Y_X`, is not enough.

## Review rubric

A future response should be classified as follows.

Theorem/proof: a construction or obstruction with quantified all-arity
statements and proofs of the required kernel inclusions or exclusions.

Finite evidence: any verified fixed-arity endpoint or stabilizer audit.

Heuristic: structural plausibility, expected arity-5 behavior, or analogies
with Brunnian pure braids without a complete kernel argument.

Unsupported claim: any statement that the problem is solved from bounded
arity evidence, that q<=4 misses matter after q=5 closure, or that one-detector
failure is a Sawin counterexample without the cofinal prefix sequence.
