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
to the `X` braid action in every arity.  The examples not covered by this
theorem are genuinely degenerate, but the class of degenerate finite
bijective solutions is not a smaller problem: if `D` is a finite identity
solution with `|D|>1`, then `D x Z` is degenerate and has the same braid
kernels as any finite bijective solution `Z`.  Hence a theorem for all
degenerate finite bijective solutions is equivalent to the full Sawin problem.

## Pointwise rack detection

No individual braid can be a universal rack-invisible witness.

Theorem.  Let `beta in B_n` be nontrivial.  Then there is a finite
conjugation rack `Y` such that

```text
rho^Y_n(beta) != 1.
```

Proof.  Use the faithful Artin representation

```text
B_n -> Aut(F_n),        F_n=<x_1,...,x_n>,
```

with generator convention

```text
sigma_i:
  x_i     -> x_i x_{i+1} x_i^{-1},
  x_{i+1} -> x_i,
  x_j     -> x_j        for j != i,i+1.
```

Since the Artin representation is faithful, `beta(x_j) != x_j` for some
generator.  Free groups are residually finite, so there is a finite quotient
`q:F_n -> G` with

```text
q(beta(x_j)) != q(x_j).
```

Let `Y` be the conjugation rack of `G`,

```text
a*b = a b a^{-1}.
```

The rack braid action on `G^n` is exactly the Artin/Hurwitz action on the
tuple of quotient generators:

```text
sigma_i(g_1,...,g_n)
  =
(g_1,...,g_i g_{i+1} g_i^{-1},g_i,...,g_n).
```

Evaluating at `(q(x_1),...,q(x_n))`, the `j`-th coordinate after `beta` is
`q(beta(x_j))`, not `q(x_j)`.  Hence `beta` is detected by the finite rack
`Y`.

Consequently, if `rho^X_n(beta) != 1` for a finite YBE solution `X`, then
some finite rack detects the same braid in that same arity.  The obstruction
to Sawin's problem cannot be a single braid invisible to all finite racks; it
can only be failure of a uniform finite rack bound across all `X`-visible
braids.

## Uniform rack-size formulation

For fixed finite `X`, define

```text
d_X(n,beta) =
min { |Y| : Y is a finite rack and rho^Y_n(beta) != 1 }
```

for pairs with `rho^X_n(beta) != 1`.  The minimum is finite by pointwise rack
detection.  Let

```text
s_X = sup d_X(n,beta),
```

where the supremum ranges over all `n` and all `beta` with
`rho^X_n(beta) != 1`.

Theorem.  `X` is dominated by a finite rack if and only if `s_X` is finite.

Proof.  If a finite rack `Y` dominates `X`, then every `X`-visible braid is
also `Y`-visible, so `d_X(n,beta) <= |Y|` and `s_X <= |Y|`.

Conversely, if `s_X` is finite, take the finite product `Q_X` of one
representative of every finite rack of size at most `s_X`.  If
`rho^{Q_X}_n(beta)=1` but `rho^X_n(beta) != 1`, then the definition of `s_X`
supplies a rack of size at most `s_X` detecting `beta`, contradicting
triviality on the product.  Hence

```text
ker rho^{Q_X}_n <= ker rho^X_n
```

for every `n`.

Thus Sawin's question is equivalent to the uniform rack-size theorem:

```text
For every finite bijective YBE solution X, s_X < infinity.
```

## Fixed-arity rack cofinality

The following stronger fixed-arity theorem is recorded in
`proofs/fixed_arity_rack_cofinality_audit.md`.  Its external literature input
is the pure braid congruence subgroup property: for the Artin embedding
`P_n -> Aut(F_n)`, every finite-index subgroup of the pure braid group `P_n`
contains a principal congruence kernel

```text
ker(P_n -> Aut(F_n/K))
```

for some characteristic finite-index subgroup `K <= F_n`.  The passage from
`P_n` to full `B_n` is elementary: add the characteristic quotient
`F_n/[F_n,F_n]F_n^2`, whose Artin action records the strand permutation.

Theorem.  Fix `n>=2`.  For every finite quotient representation

```text
theta:B_n -> H,
```

there is a finite rack `Y` such that

```text
ker rho^Y_n <= ker theta.
```

Proof.  Let `N=ker theta`, and put `N_P=N cap P_n`.  By the pure braid
congruence subgroup theorem, choose a characteristic finite-index subgroup
`K_1 <= F_n` such that

```text
ker(P_n -> Aut(F_n/K_1)) <= N_P.
```

Let `K_0=[F_n,F_n]F_n^2`.  On `F_n/K_0=(Z/2)^n`, the Artin generators act by
permuting the basis, so

```text
ker(B_n -> Aut(F_n/K_0)) <= P_n.
```

Set `K=K_0 cap K_1`, still characteristic and finite-index.  If a braid acts
trivially on `F_n/K`, then it acts trivially on `F_n/K_0`, hence is pure, and
then acts trivially on `F_n/K_1`, hence lies in `N_P <= N`.

Now set `G=F_n/K`, and let `Y` be the conjugation rack of `G`.  Under the
standard Artin convention, the action of `B_n` on the tuple of quotient free
generators in `G^n` is the rack braid action of `Y`.  If a braid is trivial on
`Y^n`, it fixes every tuple in `G^n`, in particular the quotient generator
tuple.  Those generators generate `G`, so the braid acts trivially on `G`;
hence it lies in `ker(B_n -> Aut(F_n/K)) <= N`.

Consequence.  For every finite YBE solution `X` and every fixed arity `n`,
some finite rack `Y_n` satisfies

```text
ker rho^{Y_n}_n <= ker rho^X_n.
```

## Closed reductions and failed shortcuts

The GPT-5.5 Pro response received on 2026-06-06 correctly identified the
following proof-grade but already-known reductions.

Product closure.  If finite solutions `X_i` are dominated by finite racks
`Y_i`, then the Cartesian product solution `prod_i X_i` is dominated by the
product rack `prod_i Y_i`.  This is recorded in
`proofs/product_domination_closure.md`.

Quotient closure.  If `pi:X -> Z` is a surjective braided-set homomorphism and
`X` is dominated by `Y`, then the same `Y` dominates `Z`.  This is recorded in
`proofs/hereditary_domination_closure.md`.

Nondegenerate cover obstruction.  If `p:Y -> X` is a surjective braided-set
homomorphism of finite bijective solutions and `Y` is left nondegenerate, then
`X` is left nondegenerate; similarly on the right.  Therefore genuinely
degenerate `X` cannot be handled by first taking a finite nondegenerate
braided cover and pushing the derived-rack domination down.  This is recorded
in `proofs/nondegenerate_cover_obstruction.md`.

Coordinatewise rack-quotient obstruction.  A coordinatewise quotient map from
a rack switch `R_Y(a,b)=(a*b,a)` to a general YBE solution forces the copied
coordinate of the target to be unchanged.  With the workspace convention this
means `rho_y(x)=x` for all `x,y`; with the opposite convention it forces the
left action to be trivial.  Thus a positive proof for genuinely degenerate
solutions must use contextual readouts, finite-state decoders, or a
kernel-theoretic detector, not an ordinary coordinatewise rack quotient.  This
is recorded in `proofs/ybe_finite_state_rack_cover_criterion.md`.

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

The pointwise rack-detection theorem sharpens the expected shape of such a
sequence.  If a finite rack `P_m` dominates `X` in all arities above some
cutoff `N_0`, fixed-arity cofinality supplies finitely many additional racks
handling the bounded arities `2<=n<=N_0`; their product with `P_m` dominates
`X` in all arities.  Therefore a genuine no-rack counterexample must have
prefix failures arbitrarily far out:

```text
for every m and every N,
there exist n>N and beta in B_n with
rho^{P_m}_n(beta)=1 but rho^X_n(beta) != 1.
```

Equivalently, a negative solution must force the finite rack detector size
needed for `X`-visible braids to grow without bound along an unbounded arity
sequence.

## Transparent deletion-core criterion

The response reviewed on 2026-06-06 added a proof-grade conditional
narrowing, recorded in `proofs/transparent_deletion_core_criterion.md`.

For a rack `Y`, define the transparent extension

```text
Y^0 = Y sqcup {0}
```

by

```text
a*b = old a*b for a,b in Y,
0*b = b,
a*0 = 0,
0*0 = 0.
```

This is a rack: left translations are bijective, and the rack
self-distributivity identity follows by cases.  Equivalently, `Y^0` is the
flip-across disjoint union of `Y` with the one-point trivial rack.

Deletion lemma.  Let `beta in P_n` be pure and let `partial_I beta` be the
braid obtained by deleting all strands outside `I`.  If all strands outside
`I` are colored by the transparent color, the retained color history under
`beta` is exactly the `Y`-rack action of `partial_I beta`.  Hence

```text
beta in ker rho^{Y^0}_n  =>  partial_I beta in ker rho^Y_|I|.
```

Relative bounded-deletion core theorem.  Suppose there are a finite rack
`Y_0` and an integer `N` such that for every `n` and every

```text
beta in ker rho^{Y_0^0 x T_2}_n,
```

where `T_2` is the two-element trivial rack, the implication

```text
rho^X_n(beta) != 1
  =>
there is I with 2 <= |I| <= N and rho^X_|I|(partial_I beta) != 1
```

holds.  Then `X` is dominated by a finite rack.  Indeed, fixed-arity rack
cofinality supplies finite racks `Z_k` for `2<=k<=N` with

```text
ker rho^{Z_k}_k <= ker rho^X_k,
```

and then

```text
Y = Y_0^0 x T_2 x prod_{k=2}^N Z_k^0
```

dominates `X`.

Contrapositive.  If a finite degenerate `X` is not dominated by any finite
rack, then for every rack prefix `P_m` and every deletion cutoff `N`, there
must be some pure braid `beta in P_n` such that

```text
rho^{P_m^0 x T_2}_n(beta)=1,
rho^X_n(beta) != 1,
```

while every bounded deletion shadow is already `X`-invisible:

```text
rho^X_|I|(partial_I beta)=1
for every I with 2 <= |I| <= N.
```

Thus the negative target is not merely a Brunnian braid missed by one
detector.  It is a cofinal sequence of rack-prefix-invisible, `X`-visible
pure braids with unbounded `X`-deletion support.

## Fully Brunnian core reduction

The response reviewed later on 2026-06-06 strengthened the bounded-deletion
criterion to a minimal-arity Brunnian-core criterion, recorded in
`proofs/fully_brunnian_core_reduction.md`.

Let `Y` be a finite rack and set

```text
Q = Y^0 x T_2,
```

where `T_2` is the two-element trivial rack.  The transparent extension has an
exact support formula.  If `iota_I:Y^I -> (Y^0)^n` colors strands in `I` by
`Y` and all other strands by the transparent color, then for every braid
`beta in B_n`,

```text
rho^{Y^0}_n(beta) iota_I(c)
 =
iota_{pi_beta(I)}(rho^Y_|I|(partial_I beta)c).
```

For pure `beta`, this gives the if-and-only-if

```text
beta in ker rho^{Y^0}_n
  <=>
partial_I beta in ker rho^Y_|I| for every I.
```

Define the fully deletion-minimal `X`-Brunnian `Q`-invisible core by

```text
B_{X,Y}(n) =
{
  beta in ker rho^Q_n :
  rho^X_|I|(partial_I beta)=1
  for every proper I subsetneq {1,...,n}
}.
```

Theorem.  `Q` dominates `X` if and only if every element of `B_{X,Y}(n)` is
`X`-trivial for every `n`.

Proof.  If `Q` dominates `X`, this is immediate.  Conversely, if `Q` fails,
choose a `Q`-invisible, `X`-visible witness of minimal arity.  Since `Q`
contains `T_2`, the witness is pure.  The support formula makes every proper
deletion `Q`-invisible, and minimality forces every proper deletion to be
`X`-trivial.  Hence a failure is witnessed in `B_{X,Y}(n)`.

Consequently, if no finite rack dominates `X`, then for every finite rack
prefix `P_m`, with `Q_m=P_m^0 x T_2`, there is a witness

```text
beta_m in ker rho^{Q_m}_{n_m},
rho^X_{n_m}(beta_m) != 1,
rho^X_|I|(partial_I beta_m)=1
  for every proper I subsetneq {1,...,n_m}.
```

The arities `n_m` must go to infinity by fixed-arity rack cofinality.

Thus the exact global positive target can be sharpened to Brunnian-core
annihilation: find one finite rack `Y_0` such that every fully
deletion-minimal element of `ker rho^{Y_0^0 x T_2}_n` is `X`-trivial in every
arity.  The exact global negative target is an explicit finite degenerate `X`
with a cofinal prefix sequence of such fully deletion-minimal witnesses.

## Ordinary Brunnian sharpening

The response reviewed after the fully Brunnian-core reduction sharpened the
target again, recorded in `proofs/ordinary_brunnian_sharpening.md`.

For a finite rack `Y`, put `Q=Y^0 x T_2`, and let

```text
Brun_n = {
  beta in P_n :
  partial_I beta = 1 for every proper I subsetneq {1,...,n}
}
```

be the ordinary Brunnian subgroup.

Theorem.  `Q` dominates `X` if and only if

```text
Brun_n cap ker rho^Q_n <= ker rho^X_n
```

for every `n`.

Proof idea.  Starting from a fully deletion-minimal `Q`-invisible,
`X`-visible witness, set

```text
K_m = ker rho^Q_m cap ker rho^X_m.
```

Use deletion maps `d_i:P_n->P_{n-1}` and trivial-strand insertion sections
`s_i:P_{n-1}->P_n`.  Kill one-strand deletions from right to left by replacing
the current witness by

```text
beta <- beta s_i(d_i beta)^-1.
```

The standard face-section identities preserve already killed faces.  Insertion
preserves `K`, and the induction uses the maintained fact that all proper
deletions of the current witness lie in the appropriate `K_m`.  It does not
assume arbitrary deletion-closure of `ker rho^X`, which would be false for a
general YBE solution.  The final witness is ordinary Brunnian and has the same
`X`- and `Q`-actions.

Cofinal consequence.  If no finite rack dominates `X`, then for every finite
rack prefix `P_m`, with `Q_m=P_m^0 x T_2`, there exist `n_m -> infinity` and

```text
beta_m in Brun_{n_m}
```

such that

```text
rho^{Q_m}_{n_m}(beta_m)=1,
rho^X_{n_m}(beta_m) != 1.
```

Uniform nilpotent-image closed class.  Let

```text
F_{n-1} = ker(d_n:P_n -> P_{n-1}),
```

the free group generated by `A_{1n},...,A_{n-1,n}`.  If there is a constant
`c` such that every `rho^X_n(F_{n-1})` is nilpotent of class at most `c`, then
`X` is dominated by a finite rack.  Fixed-arity cofinality handles
`n<=c+1`; for `n>c+1`, ordinary Brunnian elements lie in
`gamma_{n-1}(F_{n-1})` because

```text
intersection_i <<A_{in}>> <= gamma_{n-1}(F_{n-1})
```

by the Magnus expansion.  The nilpotent-class bound kills their `X`-image.
The constructed dominator is `Y_0^0 x T_2`, not necessarily the unextended
product `Y_0`.

Thus any counterexample must have unbounded ordinary-Brunnian visibility in
the last-strand free groups, beyond any uniformly nilpotent last-strand image
bound.

## Finite-image symmetric-commutator obstruction

The response reviewed after the ordinary-Brunnian sharpening reformulated the
remaining obstruction inside a finite combined image.  The detailed note is
`proofs/finite_image_symmetric_commutator_obstruction.md`.

Fix a finite rack `Y`, put `Q=Y^0 x T_2`, and let

```text
F_{n-1} = ker(d_n:P_n -> P_{n-1})
```

with free generators `x_i=A_{in}`.  Let

```text
Phi_n:F_{n-1}->Gamma_n<=Sym(Q^n) x Sym(X^n)
```

be the combined finite image, and define

```text
K_n = ker(Gamma_n -> rho^Q_n(F_{n-1})),
L_n = ker(Gamma_n -> rho^X_n(F_{n-1})).
```

For each meridian set

```text
N_{i,n}=<<Phi_n(x_i)>>_{Gamma_n}.
```

Then

```text
Phi_n(Brun_n cap ker rho^Q_n)
 =
K_n cap [N_{1,n},...,N_{n-1,n}]_Sigma.
```

The free-group input is the standard projection-kernel symmetric commutator
theorem: in a free group, the intersection of the kernels of the coordinate
projections killing the basis elements equals the symmetric commutator of the
corresponding normal closures.

Consequently `Q` dominates `X` if and only if

```text
K_n cap [N_{1,n},...,N_{n-1,n}]_Sigma <= L_n
```

for every `n`.

Relative lower-central criterion.  If there is a constant `c` such that for
all `n>c+1`,

```text
K_n cap gamma_{c+1}(Gamma_n) <= L_n,
```

then `X` is dominated by one finite rack.  The all-meridian symmetric
commutator lies in `gamma_{n-1}(Gamma_n)`, hence in `gamma_{c+1}(Gamma_n)` in
large arity, and the bounded arities are handled by fixed-arity cofinality.

Redundant-meridian criterion.  If, for all sufficiently large `n`, one image
of `N_{i,n}` in `Gamma_n/L_n` centralizes the subgroup generated by all the
other meridian normal closures, then the all-meridian symmetric commutator is
contained in `L_n`.  Again fixed-arity cofinality handles the finitely many
small arities.

Thus the remaining obstruction is not just an ordinary Brunnian element in a
deep lower central subgroup.  It is a genuinely all-meridian symmetric
commutator in the finite combined image, lying in the detector kernel and
surviving modulo the `X`-kernel.

## Chief-factor finite-image obstruction

The next theoretical response refined the finite-image obstruction by chief
factors; the detailed note is
`proofs/chief_factor_finite_image_obstruction.md`.

First, it corrected the global framing.  Let `D` be a finite identity
solution with `|D|>1`:

```text
R_D(a,b)=(a,b).
```

For any finite bijective solution `Z`, the product `X=D x Z` is degenerate
and satisfies

```text
ker rho^X_n = ker rho^Z_n
```

for every `n`.  Therefore proving domination for all finite degenerate
solutions would prove the full problem.

Now fix `Q=Y^0 x T_2` and keep the finite-image notation

```text
Gamma_n <= Sym(Q^n) x Sym(X^n),
K_n = ker(Gamma_n -> rho^Q_n(F_{n-1})),
L_n = ker(Gamma_n -> rho^X_n(F_{n-1})),
N_{i,n}=<<Phi_n(A_{in})>>_{Gamma_n},
C_n=[N_{1,n},...,N_{n-1,n}]_Sigma.
```

Since `Gamma_n` is a subgroup of a direct product of permutation groups, the
two projection kernels intersect trivially:

```text
K_n cap L_n = 1.
```

Thus the containment from the symmetric-commutator boundary,

```text
K_n cap C_n <= L_n,
```

is equivalent to

```text
K_n cap C_n = 1.
```

Chief-factor theorem.  Let `G` be finite, `K,N_1,...,N_r` normal in `G`, and
`C=[N_1,...,N_r]_Sigma`.  Then

```text
K cap C != 1
```

if and only if some chief factor `A/B` lying inside `K` is covered by `C`,
where `U` covers `A/B` means `A<=UB`.

For nonabelian chief factors, `C` covers `A/B` if and only if every `N_i`
covers `A/B`.  For abelian chief factors, coverage by `C` implies coverage by
every `N_i` and by `gamma_r(G)`.

Applied to `Gamma_n`, every finite-image failure is therefore one of two
types:

```text
Type I:
  a nonabelian chief factor inside K_n covered by every meridian normal
  closure N_{i,n};

Type II:
  an abelian chief factor inside K_n covered by C_n, hence necessarily by
  every N_{i,n} and by gamma_{n-1}(Gamma_n).
```

Sufficient criterion.  If one finite rack detector `Q=Y^0 x T_2` can be
chosen so that neither Type I nor Type II occurs in all sufficiently large
arities, then fixed-arity rack cofinality handles the finitely many small
arities and a finite rack dominates `X`.

Thus the remaining all-arity obstruction has been narrowed again: it must
survive as a chief factor inside the detector-invisible finite image.  The
semisimple part is a common-chief-factor obstruction; the abelian part is a
common-coverage obstruction at unbounded lower-central depth.

## Pairwise-or-central finite-image obstruction

The next theoretical response sharpened the chief-factor obstruction; the
detailed note is
`proofs/pairwise_or_central_finite_image_obstruction.md`.

Let `G` be finite and generated by normal subgroups

```text
N_1,...,N_r,        r>=2,
```

let `K triangleleft G`, and put

```text
C=[N_1,...,N_r]_Sigma.
```

If

```text
K cap C != 1,
```

then there is a chief factor `A/B` inside `K` with one of two forms:

```text
Pairwise obstruction:
  [N_i,N_j] covers A/B for some i!=j.

Central abelian obstruction:
  A/B is elementary abelian, A/B <= Z(G/B), and C covers A/B.
```

More sharply, if `A/B` is nonabelian then every pair `[N_i,N_j]` covers it.
If `A/B` is abelian but noncentral, then some `N_j` acts nontrivially on
`A/B`, and `[N_i,N_j]` covers `A/B` for every `i!=j`.

Applied to the finite-image boundary, the normal closures `N_{i,n}` generate
`Gamma_n`, so every obstruction for `n>=3` is either:

```text
K_n cap [N_{i,n},N_{j,n}] != 1
```

for some pair, or a central elementary abelian chief factor inside `K_n`
covered by the all-meridian symmetric commutator.

Sufficient criterion.  For a fixed detector `Q=Y^0 x T_2`, if all
sufficiently large arities have no pairwise obstruction

```text
K_n cap [N_{i,n},N_{j,n}] = 1        for every i!=j,
```

and no central elementary abelian chief factor inside `K_n` covered by
`[N_{1,n},...,N_{n-1,n}]_Sigma`, then fixed-arity cofinality handles the small
arities and a finite rack dominates `X`.

The same response also gave a relative lower-central criterion.  Let `Z` be a
braided quotient of `X` already dominated by a finite rack, and write

```text
G^X_n = rho^X_n(F_{n-1}),
G^Z_n = rho^Z_n(F_{n-1}),
E_n = ker(G^X_n -> G^Z_n).
```

If

```text
E_n cap gamma_{n-1}(G^X_n)=1
```

for all sufficiently large `n`, then `X` is dominated by one finite rack.
Indeed, using a detector of the form `Q=Y_Z^0 x T_2` containing a rack
dominating `Z`, any detector-invisible element projects into `E_n`, while the
all-meridian commutator projects into `gamma_{n-1}(G^X_n)`.  Trivial
intersection kills the finite-image obstruction in large arity, and
fixed-arity cofinality handles the rest.

Thus the remaining obstruction has been narrowed once more:

```text
pairwise invisible chief factors
or
central elementary abelian high-Brunnian chief factors.
```

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

For a fixed finite monoid quotient `M`, one can package all contextual
detectors over `M` into a universal presented rack `U_M(X)` with generators

```text
e_{a,x,b}        (a,b in M, x in X)
```

and with the contextual transport and rack-crossing relations imposed.  A
finite contextual detector over `M` is exactly a finite rack quotient of this
presented rack.  This formulation is proof-grade but not yet a solution: one
still needs finitely many finite quotients whose product readout is
orbit-separating in every arity.

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
finite contextual rack absorption, a finite bounded-deletion core, or a
different construction that produces one finite rack detector for every finite
`X` in all arities.

The exact missing global negative theorem is the cofinal prefix obstruction
sequence from the criteria above, now sharpened to either pairwise
finite-image chief-factor witnesses or central elementary abelian
high-Brunnian chief-factor witnesses after adding transparent rack colors and
a `T_2` purity factor.  A single high-arity miss against one detector product,
even the current `Y_X`, is not enough.

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
