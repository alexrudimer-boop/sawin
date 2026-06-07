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

## Pairwise-core finite-image obstruction

The next theoretical response sharpened the previous pairwise-or-central
boundary; the detailed note is
`proofs/pairwise_core_finite_image_obstruction.md`.

Let `G` be a group and let

```text
N_1,...,N_r triangleleft G,        r>=2.
```

Put

```text
C=[N_1,...,N_r]_Sigma.
```

Then, for every distinct pair `a,b`,

```text
C <= [N_a,N_b].
```

Proof idea.  In a fully parenthesized all-variable commutator, fix `a,b` and
look at the lowest binary-tree vertex whose descendant leaves contain both
labels.  At that vertex the two child subcommutators lie in `N_a` and `N_b`;
their commutator lies in `[N_a,N_b]`, and normality keeps all further upper
commutators there.

In the finite-image boundary, set

```text
D_n = intersection_{1<=i<j<=n-1} [N_{i,n},N_{j,n}].
```

Then

```text
C_n <= D_n.
```

Thus a sufficient large-arity condition is the pairwise-core vanishing

```text
K_n cap D_n = 1.
```

This is weaker than requiring `K_n cap [N_{i,n},N_{j,n}]=1` for every pair:
only elements lying in all pairwise commutator subgroups simultaneously must
be killed.

Consequently, the central elementary abelian Type C obstruction is not
separate from pairwise commutators.  If a central chief factor is covered by
`C_n`, then it is covered by every pairwise commutator subgroup.  Since a
central chief factor has no proper nontrivial subgroup, it is cyclic of prime
order.

Relative commutator-injectivity criterion.  Let `Z` be a braided quotient of
`X` already dominated by a finite rack `Y_Z`, and set `Q=Y_Z^0 x T_2`.  With

```text
G^X_n = rho^X_n(F_{n-1}),
G^Z_n = rho^Z_n(F_{n-1}),
E_n = ker(G^X_n -> G^Z_n),
```

if

```text
E_n cap gamma_2(G^X_n)=1
```

for all sufficiently large `n`, then `X` is dominated by one finite rack.
Indeed, an element of `K_n cap D_n` projects to `E_n` because it is invisible
to the quotient detector, and it projects to `gamma_2(G^X_n)` because it lies
in every pairwise commutator.  Hence its `X`-projection is trivial; since
`K_n cap L_n=1`, the element itself is trivial.

This relative `gamma_2` condition is equivalently abelianization-injectivity
of the relative last-strand kernel:

```text
E_n -> (G^X_n)_ab
```

is injective.  It also forces `E_n` to be central in `G^X_n`, because

```text
[E_n,G^X_n] <= E_n cap gamma_2(G^X_n).
```

So the quotient route asks for a dominated braided quotient whose relative
last-strand kernel is abelianization-visible, or equivalently contains no
nontrivial element that is a commutator in the `X` last-strand image.

This pairwise-core target is useful but has now been sharpened by the
block-core hierarchy below.  It remains a valid sufficient condition, but it
is no longer the narrowest known formulation.

The pairwise-core positive target is:

```text
Find one finite detector Q=Y^0 x T_2 such that
K_n cap intersection_{i<j}[N_{i,n},N_{j,n}] = 1
for all sufficiently large n.
```

The current global negative target is a cofinal sequence of nontrivial
elements in

```text
K_n cap C_n
  <=
K_n cap intersection_{i<j}[N_{i,n},N_{j,n}].
```

A single nontrivial intersection `K_n cap [N_{i,n},N_{j,n}]` for one pair is
not enough; a genuine obstruction must be simultaneously pairwise-deep and
all-meridian.

## Block-core finite-image obstruction

The next theoretical response sharpened the pairwise-core target; the detailed
note is `proofs/block_core_finite_image_obstruction.md`.

For normal subgroups `N_1,...,N_r triangleleft G` and a nonempty subset
`S subset {1,...,r}`, write

```text
N_S = product_{i in S} N_i.
```

For `3<=s<=r`, define

```text
Theta_s(G;N_1,...,N_r)
  =
intersection_{P={S_1,...,S_s}}
  [N_{S_1},...,N_{S_s}]_Sigma,
```

where the intersection ranges over partitions of `{1,...,r}` into `s`
nonempty blocks.  The all-meridian commutator is `Theta_r`, while the
pairwise core is `D=intersection_{i<j}[N_i,N_j]`.

Block-core interpolation theorem:

```text
[N_1,...,N_r]_Sigma
  = Theta_r
  <= Theta_{r-1} <= ... <= Theta_3
  <= intersection_{i<j}[N_i,N_j].
```

The proof uses the standard fat-commutator theorem: fully parenthesized
commutators in normal subgroups where every block appears at least once
generate the same subgroup as the symmetric commutator with one input from
each block.  Therefore every all-meridian commutator is a fat commutator for
every block partition.

The inclusion `Theta_3<=D` can be strict.  A class-two `p`-group with
`[a,b]=[a,c]=[b,c]=z` has nontrivial pairwise core `<z>` for
`N_1=<a,z>`, `N_2=<b,z>`, `N_3=<c,z>`, but its triple commutator core is
trivial.  Thus the pairwise core contains class-two noise that is not an
all-meridian Brunnian obstruction.

In the finite-image boundary, set

```text
Theta_{n,s}
  =
Theta_s(Gamma_n;N_{1,n},...,N_{n-1,n}).
```

Then

```text
C_n <= Theta_{n,s} <= Theta_{n,3} <= D_n.
```

So the sharper current global positive target is:

```text
Find one finite detector Q=Y^0 x T_2 such that
K_n cap Theta_{n,3} = 1
for all sufficiently large n.
```

There is also a sharper quotient criterion.  Let `Z` be a braided quotient of
`X` already dominated by a finite rack, and write

```text
G^X_n = rho^X_n(F_{n-1}),
E_n = ker(G^X_n -> G^Z_n),
M_{i,n}=<<rho^X_n(x_i)>>_{G^X_n}.
```

If, for one fixed `s>=3`,

```text
E_n cap Theta_s(G^X_n;M_{1,n},...,M_{n-1,n}) = 1
```

for all sufficiently large `n`, then `X` is dominated by one finite rack.
In particular, triple-block vanishing suffices:

```text
E_n cap Theta^X_{n,3}=1.
```

This is weaker than the previous relative `gamma_2` criterion because

```text
Theta^X_{n,3} <= gamma_3(G^X_n) <= gamma_2(G^X_n).
```

The current global negative target is therefore cofinal production of
nontrivial elements in `K_n cap C_n`.  Such elements automatically lie in
`K_n cap Theta_{n,s}` for every fixed block depth `3<=s<=n-1`; producing
pairwise commutator noise outside the all-meridian subgroup is insufficient.

## Weighted block-core finite-image obstruction

The next theoretical response sharpened the block-core target again; the
detailed note is `proofs/weighted_block_core_finite_image_obstruction.md`.

For normal subgroups `H_1,...,H_s triangleleft G` and positive integers
`m=(m_1,...,m_s)`, define

```text
[H_1^(m_1),...,H_s^(m_s)]_Sigma^wt
```

to be the subgroup generated by fully parenthesized commutators with exactly
`m_j` entries from `H_j`.  For a partition `P={S_1,...,S_s}` of
`{1,...,r}`, define

```text
Omega_s(G;N_1,...,N_r)
  =
intersection_P
[N_{S_1}^(|S_1|),...,N_{S_s}^(|S_s|)]_Sigma^wt.
```

This is the multiplicity-preserving block core.  It retains the original
number of meridians inside each collapsed block.

Weighted block-core theorem:

```text
[N_1,...,N_r]_Sigma <= Omega_s(G;N_1,...,N_r)
```

for every `2<=s<=r`, and

```text
Omega_s(G;N_1,...,N_r) <= Theta_s(G;N_1,...,N_r),
Omega_s(G;N_1,...,N_r) <= gamma_r(G).
```

Consequently,

```text
[N_1,...,N_r]_Sigma
  <= Omega_3(G;N_1,...,N_r)
  <= Theta_3(G;N_1,...,N_r) cap gamma_r(G).
```

The refinement is strict.  For `G=UT_4(F_p)` and
`N_1=N_2=N_3=N_4=G`, the unweighted triple core is `gamma_3(G)`, but the
weighted triple core is `gamma_4(G)=1`.

In the finite-image boundary, define

```text
Omega_{n,s}^wt
  =
Omega_s(Gamma_n;N_{1,n},...,N_{n-1,n}).
```

Then

```text
C_n <= Omega_{n,s}^wt <= Theta_{n,s},
Omega_{n,s}^wt <= gamma_{n-1}(Gamma_n).
```

The sharper current positive target is therefore:

```text
Find one finite detector Q=Y^0 x T_2 such that
K_n cap Omega_{n,3}^wt = 1
for all sufficiently large n.
```

An even sharper sufficient target is:

```text
K_n cap (Omega_{n,2}^wt cap Omega_{n,3}^wt) = 1.
```

The quotient version is similarly sharpened.  With

```text
M_{i,n}=<<rho^X_n(x_i)>>_{G^X_n},
E_n=ker(G^X_n -> G^Z_n),
```

define

```text
Omega_{n,s}^{X,wt}
  =
Omega_s(G^X_n;M_{1,n},...,M_{n-1,n}).
```

If, for one fixed `s>=2`,

```text
E_n cap Omega_{n,s}^{X,wt}=1
```

for all sufficiently large `n`, then `X` is dominated by one finite rack.

This is weaker than the unweighted triple-core target and weaker than the
lower-central `gamma_{n-1}` target.  A genuine cofinal obstruction must still
produce elements in the all-meridian subgroup `K_n cap C_n`; membership in a
weighted core alone is not enough unless the all-meridian source is proved.

## Recursive root-core finite-image obstruction

The next theoretical response sharpened the weighted block-core target again;
the detailed note is `proofs/recursive_root_core_finite_image_obstruction.md`.

For every nonempty `S subset {1,...,r}`, define

```text
C_S=[N_i | i in S]_Sigma,
C_{ {i} }=N_i.
```

Let `Bip(S)` be the set of unordered bipartitions `S=A sqcup B` with both
parts nonempty.  The root-split factorization theorem says:

```text
C_S =
product_{ {A,B} in Bip(S) } [C_A,C_B].
```

Thus a true all-meridian commutator has a coherent binary root split into
smaller all-support commutators.

Define recursive root cores by:

```text
R_S^(0)=Omega_2(G;(N_i)_{i in S}) cap Omega_3(G;(N_i)_{i in S})
```

for `|S|>=3`, with the exact conventions `R_{ {i} }^(d)=N_i` and
`R_{ {i,j} }^(0)=[N_i,N_j]`.  For `d>=0`,

```text
R_S^(d+1)
  =
R_S^(d) cap
product_{ {A,B} in Bip(S) } [R_A^(d),R_B^(d)].
```

Then:

```text
C_S <= R_S^(d+1) <= R_S^(d),
R_S^(d)=C_S whenever d>=|S|-3.
```

In the finite-image boundary, with `R_n={1,...,n-1}`, write

```text
R_n^(d)=R_{R_n}^(d)(Gamma_n;(N_{i,n})_{i in R_n}).
```

Then

```text
C_n <= R_n^(d)
  <= Omega_{n,2}^wt cap Omega_{n,3}^wt,
R_n^(d)=C_n for d>=n-4.
```

The sharper current positive target is therefore:

```text
Find one finite detector Q=Y^0 x T_2 and one fixed d>=0 such that
K_n cap R_n^(d)=1
for all sufficiently large n.
```

The quotient target is similarly sharpened.  Define `R_n^{X,(d)}` by applying
the same recursive construction inside `G^X_n` to the normal closures
`M_{i,n}=<<rho^X_n(x_i)>>`.  If there is a dominated quotient `Z` and fixed
`d` such that

```text
E_n cap R_n^{X,(d)}=1
```

for all sufficiently large `n`, then `X` is dominated by one finite rack.

A cofinal counterexample must still produce elements in `K_n cap C_n`.  Such
elements survive every fixed-depth recursive root core, but membership in a
root-core approximation alone is not enough unless exact all-meridian
membership is also proved.

## Q-skeletal root-core finite-image obstruction

The next theoretical response sharpened the recursive root-core target by
adding exact small-support tests; the detailed note is
`proofs/q_skeletal_root_core_finite_image_obstruction.md`.

Exact support monotonicity says that if `empty != T subset S`, then

```text
C_S <= C_T.
```

One proof is by induction on the commutator tree: if all selected labels lie
on one child, normality keeps upper commutators inside `C_T`; if selected
labels split across the two children, the root-split/fat-commutator
containment sends `[C_{T_a},C_{T_b}]` into `C_T`.

For fixed `q>=3`, define

```text
J_{S,q}
  =
intersection_{empty != T subset S, |T|<=q} C_T.
```

Then `C_S<=J_{S,q}`.  Define q-skeletal recursive root cores by

```text
Sk_{S,q}^{(0)} = R_S^(0) cap J_{S,q},
Sk_{S,q}^{(d+1)}
  =
Sk_{S,q}^{(d)} cap
product_{ {A,B} in Bip(S) } [Sk_{A,q}^{(d)},Sk_{B,q}^{(d)}].
```

They satisfy:

```text
C_S <= Sk_{S,q}^{(d+1)} <= Sk_{S,q}^{(d)} <= R_S^(d),
Sk_{S,q'}^{(d)} <= Sk_{S,q}^{(d)} for q' >= q,
Sk_{S,q}^{(d)}=C_S whenever d>=max(0, |S|-q).
```

In the finite-image boundary, with full support `R_n={1,...,n-1}`, write

```text
Sk_{n,q}^{(d)}
  =
Sk_{R_n,q}^{(d)}(Gamma_n;(N_{i,n})_{i in R_n}).
```

The sharper current positive target is now:

```text
Find one finite detector Q=Y^0 x T_2 and fixed q>=3,d>=0 such that
K_n cap Sk_{n,q}^{(d)}=1
for all sufficiently large n.
```

The quotient target is similarly:

```text
Find a dominated quotient Z and fixed q>=3,d>=0 such that
E_n cap Sk_{n,q}^{X,(d)}=1
for all sufficiently large n.
```

A cofinal counterexample must still produce exact all-meridian elements in
`K_n cap C_n`.  Such elements lie in every fixed `q,d` skeletal root core for
large enough `n`; membership in `Sk_{n,q}^{(d)}` alone is not enough.

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

Arity-5 product audit for the detector product `Y_X`:

```text
55 non-permutation size-three rows certified
43 direct full-product stabilizer rows
12 q=5 rows certified by [2,3] detector subproducts
0 truncated rows
full_product_kernel_image_size distribution {1: 55}
full_product_quotient_size distribution {1: 55}
```

The twelve q=5 rows have full detector component sizes `[2,3,5]`.  The full
stabilizer calculation for detector-index row 5 timed out after ten minutes,
but the `[2,3]` detector subproduct alone has trivial realized kernel image on
`X^5` for all twelve such rows.  This proves the full-product conclusion by
the inclusion

```text
K^{Y' x Y''}_5 <= K^{Y'}_5.
```

The independent verifier
`tools/verify_nonperm3_subproduct_trivial_kernel_audit.py` recomputes all
twelve subproduct kernels and checks the full-product conclusion.  This is
proof-grade fixed-arity evidence that there is no arity-5 realized
cross-effect obstruction for the current detector product.  It is not an
all-arity theorem.

The consolidated arity-5 certificate

```text
proofs/nonperm3_width3_arity5_certified_trivial_kernel_combined.json
```

packages the fixed-arity conclusion as:

```text
row_count 55
certification_method_counts {
  "direct_full_product_stabilizer": 43,
  "subproduct_trivial_kernel": 12
}
full_product_kernel_image_size_distribution {"1": 55}
full_product_quotient_size_distribution {"1": 55}
```

and is checked by
`tools/verify_nonperm3_certified_trivial_kernel_audit.py`.

Arity-6 initial probe for the detector product `Y_X`:

```text
13 non-permutation size-three rows certified
1 identity/no-detector row
12 one-component q=2 rows
0 truncated rows
kernel_image_size distribution {1: 13}
quotient_size distribution {1: 13}
```

The independent stabilizer-row verifier recomputes the twelve non-empty rows.
This is fixed-arity evidence for only the low-component arity-6 slice; the
remaining arity-6 rows are not certified.

Arity-6 no-q5 component-count <= 3 stabilizer probe:

```text
25 non-permutation size-three rows certified
1 identity/no-detector row
12 one-component q=2 rows
12 q=2/q=3/q=3 component rows
0 truncated rows
kernel_image_size distribution {1: 25}
quotient_size distribution {1: 25}
```

The independent stabilizer-row verifier recomputes the 24 non-empty rows and
finds trivial kernel image in each.  This is still a partial arity-6 result:
rows with q=4 or q=5 detector components are not certified by this probe.

Arity-6 complete certified trivial-kernel certificate:

```text
proofs/nonperm3_width3_arity6_certified_trivial_kernel_combined.json

55 non-permutation size-three rows certified
31 direct full-product stabilizer rows
24 subproduct-trivial rows
full_product_kernel_image_size distribution {1: 55}
full_product_quotient_size distribution {1: 55}
```

The 31 direct rows cover the identity row, all q=2 one-component rows, all
q=2/q=3/q=3 rows, and all q=2/q=3/q=3/q=3 rows.  The 24 subproduct rows cover
the q=4/q=5 profiles: `(3,4)` is certified by the q=3 subproduct, and
`(2,3,5)` is certified by the `(2,3)` subproduct.  The combined verifier
checks all 55 rows with `--require-trivial-full-product`.

This proves the fixed-arity statement

```text
rho^X_6(K^{Y_X}_6)=1
```

for the current detector product `Y_X` and every non-permutation size-three
table `X`.  It is still not an all-arity theorem.

Arity-7 complete certified trivial-kernel certificate:

```text
proofs/nonperm3_width3_arity7_certified_trivial_kernel_combined.json

55 non-permutation size-three rows certified
31 direct full-product stabilizer rows
24 subproduct-trivial rows
full_product_kernel_image_size distribution {1: 55}
full_product_quotient_size distribution {1: 55}
```

The direct rows again cover the identity row, all q=2 one-component rows, all
q=2/q=3/q=3 rows, and all q=2/q=3/q=3/q=3 rows.  The q=4/q=5 profiles are
certified by q<=3 subproducts.  The combined verifier checks all 55 rows with
`--require-trivial-full-product`.

This proves the fixed-arity statement

```text
rho^X_7(K^{Y_X}_7)=1
```

for the current detector product `Y_X` and every non-permutation size-three
table `X`.  It is still not an all-arity theorem.

Arity-8 partial certified trivial-kernel certificate:

```text
proofs/nonperm3_width3_arity8_partial_certified_trivial_kernel_combined.json

25 non-permutation size-three rows certified
13 direct full-product stabilizer rows
12 subproduct-trivial rows
full_product_kernel_image_size distribution {1: 25}
full_product_quotient_size distribution {1: 25}
```

The direct rows cover the identity row and all q=2 one-component rows.  The
subproduct partial covers four `(3,4)` rows by their q=3 subproduct and eight
`(2,3,5)` rows by their `(2,3)` subproducts.  This is partial arity-8
evidence: 30 of the 55 arity-8 rows remain uncertified by this probe, and the
full q=4/q=5 subproduct batch is now a multi-hour computation.

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
sequence from the criteria above, now sharpened to nontrivial elements in the
all-meridian finite-image intersection, which automatically lies in every
fixed `q,d` q-skeletal recursive root core:

```text
K_n cap [N_{1,n},...,N_{n-1,n}]_Sigma
  <=
K_n cap MSk_{n,q,a}^{(d)}    for every fixed q>=3,d>=0,a>=1
  <=
K_n cap Sk_{n,q}^{(d)}       for every fixed q>=3,d>=0
  <=
K_n cap R_n^(d)       for every fixed d
  <=
K_n cap Omega_{n,3}^wt
  <=
K_n cap Theta_{n,3}
  <=
K_n cap intersection_{i<j}[N_{i,n},N_{j,n}].
```

after adding transparent rack colors and a `T_2` purity factor.  A single
high-arity miss against one detector product, even the current `Y_X`, is not
enough.  Pairwise, unweighted triple-block, weighted block-core, or
fixed-depth root-core noise is also not enough unless it comes from the
all-meridian symmetric commutator.  The same warning applies to q-skeletal
and Moore-coherent root-core noise: the obstruction must be in the exact
all-meridian subgroup and must have a single lift whose deletion evaluations
vanish in the same finite image.

The next theoretical response gave a sharp detector-independent boundary for
the exact same-image deletion ghost quotient; the detailed review is recorded
in
`proofs/2026_06_07_theoretical_full_deletion_ghost_response_review.md`.
The full-deletion collapse is:

```text
M_{S,|S|-1}(phi)=C_S
```

for every surjection `phi:F_S -> G`, equivalently

```text
A_{|S|-1}(phi) <= D_S ker(phi).
```

For bounded deletion depth `a`, one only gets face confinement:

```text
M_{S,a}(phi)
  <=
intersection_{U subset S, 1 <= |U| <= a}
[N_i | i in U]_Sigma.
```

The same response proves that this bounded-depth confinement does not collapse
detector-independently: for every fixed `a`, finite p-group images exist
cofinally with `C_S=1` but `M_{S,a}(phi) != 1`.

The active theoretical prompt now asks for a direct detector-specific attack
on the exact same-image deletion ghost quotient.  The previous Moore-coherent
review is
`proofs/2026_06_07_theoretical_moore_coherent_response_review.md`.
For `phi:F_S -> G`, with `R=ker phi`,
`epsilon_T=iota_T d_T`, and

```text
A_a(phi)
  =
intersection_{T proper subset S, 1 <= |S\T| <= a}
epsilon_T^{-1}(R),
```

the detector target is:

```text
K cap MSk_{S,q,a}^{(d)}=1
  iff
A_a(phi) cap phi^{-1}(K cap Sk_{S,q}^{(d)}) <= R.
```

So a positive proof must exclude nontrivial same-image deletion ghosts

```text
w in A_a(Phi_n) cap Phi_n^{-1}(K_n cap Sk_{n,q}^{(d)})
but w notin ker Phi_n.
```

The prompt now asks for detector-specific annihilation of these ghosts, or a
cofinal rack-prefix construction where such ghosts survive.  Moore coherence,
finite image, bounded skeletal depth, exact small-support face confinement,
and bounded deletion depth are known to be insufficient.  The conjugation rack
`A_5` also has cofinal perfect point-pushing ghosts against the weak detector
`T_2`, although it is not a Sawin counterexample because it dominates itself
as a rack.

The next theoretical response gave a stronger varying-target detector-specific
survival theorem; the detailed review is recorded in
`proofs/2026_06_07_theoretical_detector_specific_survival_response_review.md`.
For every finite rack detector `Q`, if

```text
e(Q)=ord(rho^Q_2(sigma_1^2)),
```

then choosing an odd prime `ell` not dividing `e(Q)` and

```text
X_Q=Conj(A_ell)
```

gives unbounded-index powered Brunnian words

```text
w_r=[...[ [x_1^{e(Q)},x_2^{e(Q)}],x_3^{e(Q)}],...,x_r^{e(Q)}]
```

with

```text
rho^Q_{r+1}(w_r)=1,
rho^{X_Q}_{r+1}(w_r) != 1.
```

Every proper deletion of `w_r` is already trivial in the free group, so the
combined image lies nontrivially in `K_n cap C_n`, the full symmetric
commutator layer.  This proves that no fixed finite rack detector annihilates
full-Brunnian ghosts for all finite rack targets.

This is still not a Sawin counterexample.  The target varies with the detector
or rack prefix, and each `X_Q` is itself a rack.  The remaining negative route
still requires one fixed finite YBE solution `X` missed cofinally by every
finite rack prefix.  The remaining positive route still allows the detector
to depend on the fixed target `X`.

The latest strict A/B attempt is recorded in
`proofs/2026_06_07_theoretical_strict_ab_attempt_review.md`.  It did not prove
either side.  It identified the two active fatal blockers:

```text
Positive blocker:
prove an all-arity non-coordinatewise contextual/guitar endpoint encoding
theorem for arbitrary finite degenerate X.  The coordinatewise
left-nondegenerate-cover shortcut cannot work except when X is already
left-nondegenerate, because finite fiber-weight preservation forces the
target first-coordinate maps to be surjective.

Negative blocker:
replace the varying Conj(A_ell) rack targets in the detector-survival theorem
by one fixed finite bijective YBE target X missed cofinally by every finite
rack prefix.
```

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
