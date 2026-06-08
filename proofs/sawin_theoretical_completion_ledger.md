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

31 non-permutation size-three rows certified
13 direct full-product stabilizer rows
18 subproduct-trivial rows
full_product_kernel_image_size distribution {1: 31}
full_product_quotient_size distribution {1: 31}
```

The direct rows cover the identity row and all q=2 one-component rows.  The
subproduct partial covers eight `(3,4)` rows by their q=3 subproduct and ten
`(2,3,5)` rows by their `(2,3)` subproducts.  This is partial arity-8
evidence: 24 of the 55 arity-8 rows remain uncertified by this probe, and the
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

The following strict A/B attempt is recorded in
`proofs/2026_06_07_theoretical_strict_ab_context_depth_failure_review.md`.
It also did not prove either side.  It restated the same gap in sharper
language:

```text
Positive restatement:
the non-coordinatewise contextual/endpoint readout appears to require history
depth growing with arity, but no proof of unavoidable growth and no
target-specific finite invariant bounding that depth was given.

Negative restatement:
racks self-dominate, identity padding preserves braid kernels, and the known
powered-Brunnian alternating-group engine varies the target with the detector;
no fixed finite coupled degenerate target was constructed.
```

The active prompt now forbids merely repeating those two blockers.  A future
answer must either produce a concrete finite complexity bound/readout for
fixed `X` or give one explicit fixed finite degenerate target with cofinal
prefix-invisible witnesses.

The latest strict A/B attempt is recorded in
`proofs/2026_06_07_theoretical_endpoint_rackification_failure_review.md`.
It gave a more concrete formulation of the positive endpoint-rackification
blocker.  For `R_X(x,y)=(u,v)` and suffix `w`, a desired endpoint readout
would satisfy

```text
c(x,yw)=c(v,w),
c(u,vw)=c(v,w)*c(y,w).
```

After quotienting endpoint profiles, the induced operation must be a finite
rack operation and the readouts

```text
J_n(x_1,...,x_n)=(c(x_1,x_2...x_n),...,c(x_n,empty))
```

must be orbit-separating in every arity.  The response did not prove that such
a finite quotient exists; the obstruction is that the identifications needed
for well-definedness, bijective translations, and self-distributivity may
collapse points in a braid orbit.

The same response sharpened the negative failure: once one fixed target `X` is
chosen, the two-strand pure order

```text
d=ord(rho^X_2(sigma_1^2))
```

is fixed, so the powered-commutator family from the varying `Conj(A_ell)`
construction cannot be reused without a new mechanism.  A rack prefix can
include detectors whose relevant pure orders are divisible by `d`.  No fixed
finite degenerate target with a replacement cofinal witness family was
constructed.

The next response is recorded in
`proofs/2026_06_07_theoretical_fiber_monodromy_quotient_failure_review.md`.
It did not prove A or B, but it gave a locally checked four-point example
showing that a nondegenerate quotient can lose fiber pure-braid monodromy.
For

```text
X={0,1} x {0,1}
```

and

```text
R((a,i),(b,j))=((b,I),(a,J)),
```

where

```text
(I,J)=(i,j)     if (a,b)=(0,0),
(I,J)=(j,i)     if (a,b)=(0,1) or (1,0),
(I,J)=(j,1-i)   if (a,b)=(1,1),
```

the workspace check found:

```text
bijective True
YBE True
sigma1sq_moved_count 4
```

The projection to the first coordinate is the two-point flip solution, but
`sigma_1^2` moves every point in the fiber over base pair `(1,1)`.  Thus a
positive proof cannot simply pass to a nondegenerate quotient and use the
derived rack unless it also records degenerate fiber monodromy uniformly.

The latest response is recorded in
`proofs/2026_06_07_theoretical_two_sided_contextual_blocker_review.md`.
It proposed the strongest finite target-specific construction so far.  For
`R(x,y)=(u,v)`, define

```text
r_y(x)=pr_2 R(x,y),
m_u(v)=pr_1 R^{-1}(u,v),
M_R=<r_y:y in X>,
M_L=<m_u:u in X>.
```

The finite two-sided contextual state is

```text
(A,x,B) in M_L x X x M_R.
```

Same-strand transport forces

```text
(A,x,B r_y) ~ (A m_u,v,B),
```

and the proposed rack operation is

```text
[(A,x,B r_y)] * [(A m_x,y,B)] = [(A,u,B r_v)].
```

The proof fails exactly at representative independence: the response did not
prove that if the two inputs are replaced by equivalent representatives, then
the output representatives are equivalent.  Adding this as a congruence may
collapse orbit-separating contextual states.  The active prompt now asks the
next theoretical pass to prove this implication from YBE and bijectivity,
find a finite counterexample to it, or replace the construction with a working
finite rackification.

The next response is recorded in
`proofs/2026_06_07_theoretical_partial_rack_totalization_blocker_review.md`.
It claims the representative-independence implication is true by the
diagrammatic Yang-Baxter move: representative changes are marked-strand slides,
and changing before crossing versus crossing before changing is exactly

```text
R_12 R_23 R_12 = R_23 R_12 R_23.
```

The fatal positive obstruction is therefore shifted to the next step.  The
two-sided contextual construction gives a finite compatible-pair partial rack,
not a total finite rack.  A positive proof now needs a finite completion of
this partial operation that preserves all forced compatible translations,
makes all left translations bijective, satisfies global self-distributivity

```text
L_{a*b} L_a = L_a L_b
```

for all class pairs, and keeps the all-arity readout orbit-separating.  YBE
only proves the identities on jointly realizable contextual triples.  The
active prompt now asks for a finite rack completion theorem or an explicit
finite YBE solution whose contextual partial rack cannot be completed without
breaking the forced operation or collapsing orbit separation.

The next response is recorded in
`proofs/2026_06_07_theoretical_augmented_rack_completion_blocker_review.md`.
It sharpened the totalization problem to finite augmented-rack completion.
The desired finite data are

```text
G, Omega, iota:P -> Omega, ell:P -> G,
```

with `G` acting on `Omega`, such that every forced compatible product satisfies

```text
iota(a*b) = ell(a) iota(b),
ell(a*b)  = ell(a) ell(b) ell(a)^(-1).
```

The response notes that YBE gives these identities only on realizable
compatible triples.  It does not supply a finite global `G`-action extending
all partial translations, nor prove that any quotient required by completion
preserves the all-arity orbit-separating readout.  The active prompt now asks
for a proof that such finite augmented-rack completions always exist, or for
an explicit finite YBE solution whose partial augmented rack has no finite
completion with those properties.

The next response is recorded in
`proofs/2026_06_07_theoretical_contextual_wirtinger_separability_blocker_review.md`.
It sharpened finite augmented-rack completion into a contextual Wirtinger
separability problem.  For the two-sided contextual partial rack `P_X`, define

```text
G_X =
< g_p (p in P_X) |
  g_{p*q}=g_p g_q g_p^(-1) for every forced compatible product p*q >.
```

A finite rack completion preserving forced products and the all-arity readout
would require a finite quotient

```text
G_X -> Gbar_X
```

whose induced conjugation rack does not identify two contextual readout tuples
lying in the same braid orbit unless they already represent the same `X`-state.
Thus the missing theorem is a residual-finiteness or separability statement
for this contextual Wirtinger group, with preservation of the contextual
readout.  The active prompt now asks for this separability theorem or for a
finite `X` where separability fails and yields a fixed-target counterexample.

The next response is recorded in
`proofs/2026_06_07_theoretical_general_completion_false_review.md`.  It
clarified that a general finite augmented-rack completion theorem is false.
An arbitrary finite partial augmented rack can encode a finitely presented
group

```text
G=<s_i | r_j>
```

and a word `w`, with partial translations forcing a composite to send a
marked point `p` to a marked point `q`.  Any finite rack completion separating
`p != q` would give a finite quotient of `G` where `w != 1`.  A finitely
presented non-residually finite group with a nontrivial element killed in
every finite quotient therefore gives a finite partial augmented rack with no
finite separating completion.

Thus the remaining positive route cannot be a general completion theorem.  It
must prove a special contextual Wirtinger separability theorem for the partial
augmented racks that actually arise from finite bijective YBE solutions, or
else find a finite YBE solution whose contextual Wirtinger group realizes the
non-residual-finiteness obstruction and yields a fixed-target counterexample.

The next response is recorded in
`proofs/2026_06_07_theoretical_virtual_context_state_blocker_review.md`.  It
identified the current obstruction inside the special YBE-origin separability
route.  A contextual generator can be realized as a finite braid-image
monodromy operator for every realizable compatible product, because YBE
identifies the corresponding local braid diagrams.  But an arbitrary word in
the contextual Wirtinger generators may pass through virtual intermediate
contextual states that do not occur simultaneously in any single `X`-colored
word with one common left and right context.  Hence the natural map from
`G_X` to finite braid-image monodromies is not automatically a well-defined
separating representation of the whole group.  The active prompt now asks for
a proof that virtual contextual states can always be represented or eliminated
without losing all-arity readout distinctions, or for a finite `X` where such
virtual states force nonseparability and produce a fixed-target obstruction.

The next response is recorded in
`proofs/2026_06_07_theoretical_joint_fillability_gap_review.md`.  It gave a
concrete claimed joint-fillability gap in the checked four-point YBE example.
With elements ordered as `00,01,10,11`, the contextual monoids contain

```text
alpha=(01,01,10,11),
beta =(00,00,10,11).
```

In the two-sided contextual quotient, the classes represented by

```text
p=(alpha,00,alpha),
q=(alpha,00,beta)
```

are claimed to be individually realizable but not jointly fillable: no
representatives can be put into adjacent compatible form

```text
(A,x,B r_y), (A m_x,y,B)
```

with common `A,B,x,y`.  This blocks the simple realization strategy for
virtual contextual states.  A positive proof must either show that non-fillable
products can be assigned harmlessly in a finite completion while preserving
the all-arity readout, or avoid the completion problem by a different
target-specific rack construction.

The next response is recorded in
`proofs/2026_06_07_theoretical_nonfillable_closure_blocker_review.md`.  It
corrected the interpretation of the non-fillable contextual pair.  Since

```text
p=(alpha,00,alpha),  q=(alpha,00,beta)
```

are not jointly fillable, YBE imposes no local value for `p*q`; this alone is
not a contradiction.  A finite completion could introduce a new value for
`p*q` with left translation

```text
L_{p*q}=L_p L_q L_p^(-1).
```

The unresolved positive step is to prove that iterating this closure process
has a finite quotient preserving injectivity of the realizable contextual
readout, or else to prove that it must become infinite or collapse two
`X`-distinct realizable states.  The unresolved negative step is stronger:
even a closure/readout obstruction must be converted into an actual Brunnian
detector-kernel braid witness.  A non-fillable contextual pair is not itself
such a witness.

The next response is recorded in
`proofs/2026_06_07_theoretical_inverse_semigroup_totalization_blocker_review.md`.
It sharpened the obstruction again: the forced contextual partial translations
have a finite inverse-semigroup closure, but this is not yet a rack.  The
missing step is replacing partial bijections, with their domain and idempotent
data, by total permutations or genuine group conjugations while preserving
forced products on realizable states and enforcing

```text
L_{a*b}=L_a L_b L_a^(-1)
```

for newly created non-fillable products.  No proof was given that this
totalization remains finite without collapsing two `X`-distinct realizable
readout tuples, nor that failure of totalization yields an actual Brunnian
detector-kernel braid witness.

The next response is recorded in
`proofs/2026_06_07_theoretical_partial_bijection_globalization_blocker_review.md`.
It explains why standard finite globalization of partial bijections is
insufficient.  One can extend finite contextual partial translations to total
permutations on a finite enlargement and then define an augmented rack by

```text
(omega,g) * (eta,h) = (g eta, g h g^(-1)).
```

However, finite globalization preserves coherent partial compositions, not
arbitrary quotient-group relations of the contextual Wirtinger group.  For
non-fillable contextual states, the relevant relation words are partially
undefined; passing to total permutations erases the domain idempotents that
record where those words were valid.  Thus the missing theorem is still a
YBE-origin finite quotient/separability statement ensuring the contextual
Wirtinger relations survive totalization without collapsing realizable
readouts.

The next response is recorded in
`proofs/2026_06_07_theoretical_augmented_rack_domain_condition_blocker_review.md`.
It isolates the exact failed implication in the natural augmented-rack
workaround.  Taking total extensions in a finite permutation group and forming

```text
Y = Omega x G,
(omega,g) * (eta,h) = (g eta, g h g^(-1))
```

would still require, for every forced compatible crossing,

```text
h extends L_p,  k extends L_q
  =>  h k h^(-1) extends L_{p*q}.
```

For a point `r in dom(L_{p*q})`, this needs

```text
h^(-1)(r) in dom(L_q),
k h^(-1)(r) in dom(L_p).
```

These are precisely the missing joint-fillability conditions.  They are
guaranteed by YBE only on jointly realizable triples, not for arbitrary
virtual or non-fillable contextual states.  Thus arbitrary finite total
extensions of the partial translations may break the next crossing, and the
unresolved positive step remains a YBE-origin finite totalization/separability
theorem preserving realizable readouts.

The next response is recorded in
`proofs/2026_06_07_theoretical_four_point_contextual_completion_review.md`.
It changes the status of the four-point degenerate test case from candidate
obstruction to positive evidence.  For the four-point solution on
`00,01,10,11`, the two-sided contextual quotient `(M x X x M)/~` has 20
classes, and the forced compatible products extend to a total 20-element rack.

The result was locally audited by:

```text
tools/run_four_point_contextual_completion_audit.py
proofs/four_point_contextual_completion_audit.json
proofs/four_point_contextual_completion_audit.md
```

The audit verifies:

```text
source YBE: true
contextual monoid size: 6
contextual quotient classes: 20
forced product conflicts: 0
rack size: 20
rack YBE: true
rack-form check: true
forced partial translations extend to permutations: true
equivariance checked arities: 1..8
orbit-injectivity checked arities: 1..8
```

The response also gives a specific all-arity orbit-separation proof for this
four-point example by classifying braid orbits according to the number of
base-`1` letters and the ordered zero-fibre string.  Thus the earlier
non-fillable contextual pair is not a counterexample: it can be filled
harmlessly in this example without adding points or collapsing contextual
classes.

The current positive target is now to generalize this 20-class completion
mechanism to arbitrary finite YBE-origin contextual partial racks.  The current
negative target is to find a new finite YBE-origin example where finite
orbit-separating rack completion fails and to convert that failure into an
actual Brunnian detector-kernel braid witness.

The next response is recorded in
`proofs/2026_06_07_theoretical_binary_skew_flip_family_completion_review.md`.
It stress-tests the four-point contextual completion against the whole binary
skew-over-flip family:

```text
X={0,1} x {0,1},
R((a,i),(b,j))=((b,I_ab(i,j)),(a,J_ab(i,j))),
```

where each fibre map `(i,j)->(I_ab(i,j),J_ab(i,j))` is an arbitrary
permutation of `{0,1}^2`.  The local exhaustive audit is:

```text
tools/run_binary_skew_flip_contextual_family_audit.py
proofs/binary_skew_flip_contextual_family_audit.json
proofs/binary_skew_flip_contextual_family_audit.md
```

It checks all `24^4=331776` tables and reproduces:

```text
YBE solutions: 520
nondegenerate: 384
degenerate involutive: 64
degenerate non-involutive: 72
```

For all 72 degenerate non-involutive rows, the contextual completion succeeds:

```text
M_L and M_R have the same underlying maps;
|M| is in {3,4,5,6};
|P| is in {10,14,16,20};
forced products have no conflicts;
every forced partial left translation is injective;
the identity fill is a rack.
```

The completion is especially structured.  Closing each nontrivial partial
two-cycle and fixing all other points gives total permutations `L_p` with:

```text
L_p^2 = 1,
L_p L_q = L_q L_p,
L_{L_p(q)} = L_q.
```

Thus `p*q=L_p(q)` defines a finite rack on the same contextual quotient `P`,
with no extra points.  The four-point non-fillable obstruction neighborhood is
therefore exhausted positively.  The next target is a general theorem forcing
this commuting-involution completion for YBE-origin contextual partial racks,
or a larger finite YBE solution where this property fails and can be converted
into a genuine cofinal braid witness.

The next response is recorded in
`proofs/2026_06_07_theoretical_identity_extension_completion_lemma_review.md`.
It abstracts the successful finite completions into a clean identity-extension
lemma.

Let `P` be the finite two-sided contextual quotient and let

```text
lambda_p : D_p -> P
```

be the forced partial left translation.  Define the identity-outside extension

```text
L_p(q)=lambda_p(q)  if q in D_p,
L_p(q)=q            otherwise.
```

If:

```text
lambda_p : D_p -> D_p is bijective for every p,
L_{L_p(q)} = L_p L_q L_p^(-1) for every p,q,
```

then `p*q=L_p(q)` defines a finite rack on `P`, extending the forced
contextual products.  The proof is direct: the first identity makes each `L_p`
a permutation, and the second is exactly the rack left-translation identity
after substituting `p*q=L_p(q)`.

Therefore the positive route is now reduced to:

```text
balanced domains: lambda_p(D_p)=D_p;
conjugacy covariance: L_{L_p(q)}=L_p L_q L_p^(-1);
all-arity orbit separation for J_n:X^n -> P^n.
```

If all three hold for a fixed finite `X`, then the rack `P` dominates `X` in
all arities.  A negative obstruction should now explicitly fail one of the two
finite identities, or pass them but fail all-arity orbit separation in a way
that yields an actual Brunnian detector-kernel braid witness.

The next response is recorded in
`proofs/2026_06_07_theoretical_linear_f3_skew_flip_completion_review.md`.
It moves the finite-completion tests beyond the four-point binary family to
the six-point linear skew-over-flip family:

```text
X={0,1} x F_3,
R((a,i),(b,j))=((b,I),(a,J)),
(I,J)^T=M_ab(i,j)^T,  M_ab in GL_2(F_3).
```

The local audit is:

```text
tools/run_linear_f3_skew_flip_completion_audit.py
proofs/linear_f3_skew_flip_completion_audit.json
proofs/linear_f3_skew_flip_completion_audit.md
```

It checks all `48^4=5308416` choices and verifies:

```text
YBE solutions: 1088
nondegenerate non-involutive: 816
degenerate non-involutive: 144
degenerate involutive: 96
nondegenerate involutive: 32
```

For all 144 degenerate non-involutive rows:

```text
forced products have no conflicts;
forced partial translations are injective;
lambda_p(D_p)=D_p for every p;
identity-outside L_p are total permutations;
L_{L_p(q)}=L_p L_q L_p^(-1) for every p,q.
```

There are 8 rows where `M_L` and `M_R` differ as sets of maps.  This is
diagnostic only, not a completion failure.  The finite identity-extension
completion still succeeds.  This audit does not check all-arity orbit
separation.

The next response is recorded in
`proofs/2026_06_07_theoretical_multicopy_augmented_rack_lift_reduction_review.md`.
It removes algebraic finite rack totalization as the final blocker by allowing
multiple copies.  For any finite contextual quotient `P=P_X`, define:

```text
Y_X = P x Sym(P),
(p,g)*(q,h) = (g(q), g h g^(-1)).
```

This is always a finite rack and locally realizes forced contextual crossings
because any injective forced partial map `lambda_p:D_p -> I_p` can be extended
to a permutation of `P`.

The remaining positive theorem is coherent lift separation:

```text
For every n, construct a braid-equivariant relation
Pi_n subseteq Y_X^n x X^n
such that every x has a lift y, Pi_n is B_n-invariant, and y determines x.
```

If such `Pi_n` exists for every `n`, then `Y_X` dominates `X`.  A negative
route should now find a fixed finite `X` where no such coherent single-valued
lift relation can exist and convert that failure into an actual Brunnian
detector-kernel braid witness.

The next response is recorded in
`proofs/2026_06_07_theoretical_transport_stable_lift_fibers_review.md`.
It corrects the multi-copy rack reduction: `P x Sym(P)` is always a rack, but
not every copy `(p,g)` should be considered a legitimate contextual lift.

For each contextual class `p`, the required finite datum is a nonempty set

```text
E_p subseteq Sym(P)
```

such that:

```text
Extension:
g(q)=lambda_p(q) for every g in E_p and q in D_p.

Transport:
if q in D_p and r=lambda_p(q), then
g E_q g^(-1)=E_r for every g in E_p.
```

Given such `E_p`, define `Pi_n subseteq (P x Sym(P))^n x X^n` by allowing
exactly lifts `(p_i,g_i)` with `g_i in E_{p_i}` over the contextual readout
`J_n(x)=(p_i)`.  The extension and transport conditions make `Pi_n`
braid-equivariant.  If `J_n` is also injective on every braid orbit, then
`P x Sym(P)` dominates `X`.

The current positive theorem is therefore:

```text
For every finite bijective YBE solution X, construct nonempty
transport-stable extension fibres E_p over P_X, and prove all-arity
orbit-injectivity of J_n.
```

The current negative target is a fixed finite `X` with no such `E_p`, or with
such `E_p` but an all-arity orbit-separation failure that can be converted into
actual Brunnian detector-kernel witnesses.

The next response is recorded in
`proofs/2026_06_07_theoretical_active_lift_forced_pair_criterion_review.md`.
It weakens the lift-fibre condition to the actual condition needed along
real braid trajectories.  The equality condition

```text
g E_q g^(-1)=E_{lambda_p(q)}
```

controls non-fillable and virtual products that do not appear in actual
adjacent contextual braid moves.  The correct finite datum is a nonempty
active set

```text
C_p subseteq Sym(P)
```

for each contextual class `p`, satisfying:

```text
Forced extension:
g(q)=lambda_p(q) for every g in C_p and q in D_p.

Forced-pair closure only:
if q in D_p, r=lambda_p(q), g in C_p, and h in C_q,
then g h g^(-1) in C_r.
```

No condition is imposed for `q notin D_p`.  These conditions make the lift
relation `Pi_n subseteq (P x Sym(P))^n x X^n` braid-equivariant for every `n`.
If the contextual readout `J_n` is braid-orbit-injective for every `n`, then
`P x Sym(P)` dominates `X`.

The current positive theorem is therefore:

```text
For every finite bijective YBE solution X, construct nonempty active lift sets
C_p satisfying forced extension and forced-pair closure, and prove all-arity
orbit-injectivity of J_n.
```

The current negative target is a fixed finite `X` with no such `C_p`, or with
such `C_p` but an orbit-separation failure that yields actual Brunnian
detector-kernel witnesses.

The next local audit is recorded in
`proofs/2026_06_07_theoretical_linear_f3_skew_flip_orbit_review.md`.
It checks orbit separation for the same six-point linear skew-over-flip family
where completion was verified.  The generated audit is:

```text
tools/run_linear_f3_skew_flip_orbit_audit.py
proofs/linear_f3_skew_flip_orbit_audit.json
proofs/linear_f3_skew_flip_orbit_audit.md
```

It verifies:

```text
degenerate non-involutive rows: 144
all rows checked through arity: 5
representative contextual types checked through arity: 6
representative contextual type count: 16
orbit-injectivity failure count: 0
```

This is finite evidence only.  It supports the orbit-separation side of the
positive route but does not prove all-arity orbit-injectivity.

The next response is recorded in
`proofs/2026_06_07_theoretical_active_lift_greatest_fixed_point_review.md`.
It makes active-lift existence canonical.  For each `p`, let

```text
V_p={g in Sym(P): g extends lambda_p}.
```

Define the monotone pruning operator

```text
T(C)_p =
  { g in C_p :
      for every q in D_p and every h in C_q,
      g h g^(-1) in C_{lambda_p(q)}
  }.
```

Starting from `C^(0)=V`, iterate `C^(k+1)=T(C^(k))`.  Since everything is
finite, this stabilizes to a greatest fixed point `C^(infty)`.  There exists
an active lift system iff

```text
C^(infty)_p != empty
```

for every `p`.

The current positive theorem is therefore reduced to:

```text
prove C^(infty)_p is nonempty for every finite bijective YBE solution X and
every p in P_X;
prove all-arity orbit-injectivity of J_n.
```

A finite negative search can now target the canonical obstruction:

```text
find X and p with C^(infty)_p empty,
```

or find an orbit-injectivity failure after the fixed point survives.

The next response is recorded in
`proofs/2026_06_07_theoretical_realizable_language_partial_automorphism_review.md`.
It tries to use finite partial-automorphism extension.  The naive finite
structure is

```text
A_X = P union {ell_p:p in P},
G(ell_p,q,r) iff q in D_p and lambda_p(q)=r.
```

Define

```text
theta_p(q)=lambda_p(q),
theta_p(ell_q)=ell_{lambda_p(q)}.
```

Preservation of `G` asks for

```text
lambda_p(lambda_q(a)) =
lambda_{lambda_p(q)}(lambda_p(a)).
```

YBE proves this identity only on jointly realizable contextual triples.  The
full relation `G` includes virtual triples that are pairwise forced but not
jointly fillable in an actual `X`-word.  Therefore `theta_p` is not proved to
be a partial automorphism of the naive finite graph.

The correct object is the realizable contextual language

```text
W_X = union_n J_n(X^n) subseteq P^*.
```

This language is regular because realization is witnessed by finite monoid
contexts:

```text
A_{i+1}=A_i m_{x_i},
B_i=B_{i+1} r_{x_{i+1}},
p_i=[A_i,x_i,B_i].
```

On `W_X`, local identities are actual YBE diagrams.  The current positive
target is to compress `W_X` into a finite relational structure whose partial
automorphisms encode all braid-relevant contexts and yield finite active
lifts.  The current negative target is an unbounded realizability obstruction:
a virtual contextual pattern locally compatible at every bounded level but not
globally realizable, eventually producing actual Brunnian detector-kernel
witnesses.

The next response is recorded in
`proofs/2026_06_07_theoretical_universal_local_rack_readout_review.md`.  It
proves that the two-sided contextual quotient `P_X` is universal among local
one-strand rack readouts.  If `R_X(x,y)=(u,v)`, then a strand readout

```text
c : M_L x X x M_R -> C
```

that can be used by a rack detector must preserve the detector color of the
same physical strand through a crossing.  Since a rack crossing has

```text
R_Y(a,b)=(a*b,a),
```

the old left detector color appears unchanged as the second output.  Therefore
for adjacent contextual states one must have

```text
c(A,x,B r_y) = c(A m_u,v,B).
```

These are exactly the generating relations defining

```text
P_X = (M_L x X x M_R)/~.
```

Thus every such local readout factors through `P_X`.  The consequence is that
suffix-action cancellation cannot be fixed by adding richer one-strand local
context data while keeping rack same-strand transport.  The remaining positive
route must either prove pure-loop faithfulness/all-arity orbit separation for
`P_X` itself or leave purely local one-strand readouts and build a genuinely
multi-strand or stateful finite rack detector.  The negative route still must
turn any failure into actual Brunnian detector-kernel braid witnesses for one
fixed finite `X`.

The next local/theoretical boundary is recorded in
`proofs/2026_06_08_theoretical_pure_kernel_monolith_congruence_review.md`.
For a smallest nonsimple counterexample with monolith `mu` and detector

```text
Q=(Y_mu x Y_ctx)^0 x T_2,
```

the correct stable relation is not Brunnian-only monodromy.  It is the
congruence generated by pure detector-kernel monodromy: coordinate colour
moves realized by braids in

```text
P_n cap ker rho^Q_n.
```

This relation is a braided congruence, is contained in `mu`, and is nontrivial
by the transparent-extension Brunnian reduction.  Hence it equals `mu` in a
minimal nonsimple counterexample.  The nonsimple branch is therefore an actual
pure-kernel monodromy problem inside monolith fibres.

The local six-point evidence is recorded in
`proofs/linear_f3_skew_flip_pure_kernel_monodromy_audit.md` and reviewed in
`proofs/2026_06_08_pure_kernel_monodromy_audit_review.md`.  For the 144
degenerate non-involutive linear skew-over-flip rows over `{0,1} x F_3`, the
audit tests the 64 subdirectly irreducible rows with nontrivial proper
monolith using the monolith quotient action plus the identity-extension
contextual rack.  It finds no two-strand pure detector-kernel X-motion in all
64 rows.  It also computes exact three-strand joint closures for the four
minimal contextual quotients `|P_X|=42`; each joint image has size `216` and
has no detector-kernel X-motion.  This does not prove domination, but it shows
that the earlier formal monolith `J`-collisions are not automatically realized
by small-arity pure detector-kernel monodromy in this family.

The artifact
`proofs/linear_f3_skew_flip_contextual_kernel_consequence.md` connects this
with the older orbit-injectivity audit.  Since the six-point linear F3 orbit
audit checks contextual readout orbit-injectivity through arity `5` for all
144 degenerate non-involutive rows, and since the identity-extension
contextual rack completion is verified in the same family, the contextual
rack kernel acts trivially on `X^n` for `n<=5`.  Therefore the pure
detector-kernel monodromy obstruction is excluded through arity `5` for all
64 subdirectly irreducible proper-monolith rows.  This is finite evidence
only; the remaining theorem target is still all-arity contextual pure-loop
faithfulness or a replacement finite detector.

The next GPT-5.5 Pro response is reviewed in
`proofs/2026_06_08_theoretical_active_lift_pure_loop_blocker_review.md`.  It
does not prove A or B.  It restates the contextual active-lift obstruction
for virtual triples and the contextual pure-loop/suffix-cancellation
obstruction, and it repeats the fixed-target B obstruction that the powered
Brunnian alternating-rack construction cannot be frozen.  These should now be
treated as known blockers, not as new reductions: a future A proof must prove
active-lift existence plus pure-loop faithfulness or supply a different
finite rack detector, and a future B proof must give one fixed finite target
with actual cofinal detector-kernel braid witnesses.

The displayed six-point residual representative is now closed in
`proofs/linear_f3_residual_representative_quotient_closure.md`, with finite
bookkeeping audited by
`proofs/linear_f3_residual_representative_closure_audit.md`.  The row has
matrices

```text
M_00=[0 1;2 2], M_01=[1 2;1 0],
M_10=[0 1;2 1], M_11=I,
```

and is row `20` in the degenerate non-involutive linear F3 audit.  Its
monolith collapses `f_0,f_1,f_2` and keeps `e_0,e_1,e_2` separate.  The
four-point quotient `Z={e_0,e_1,e_2,F}` is left-nondegenerate.  The lift
fibres are controlled by the all-arity invariant

```text
H_s=(-1)^k i + sum_{r=1}^k (-1)^{r-1} a_r in F_3,
```

where the tracked `F`-strand is lifted to `f_i` and has left `e`-list
`e_{a_1},...,e_{a_k}`.  Local crossings preserve `H_s`, so every braid
trivial on `Z^n` is trivial on `X^n`.  Thus

```text
ker rho^Z_n <= ker rho^X_n
```

for all `n`, and this row is dominated by the derived rack of `Z`.  Its formal
monolith `J`-collision is not braid-realized.  Future candidate searches in
this family must avoid this alternating-sum lift invariant.

The passive-certified part of the formal monolith-collision half of the
six-point linear `F_3` skew-over-flip residual branch is now closed in
`proofs/linear_f3_collision_quotient_invariant_closure.md`, with executable
bookkeeping in
`proofs/linear_f3_collision_quotient_invariant_audit.md`.  The audit checks
all `144` degenerate non-involutive rows, identifies the `64` subdirect rows,
and verifies the split

```text
32 rows: monolith J-separating, quotient degenerate,
32 rows: monolith J-collision, quotient nondegenerate.
```

For each of the `32` formal collision rows, the monolith has one collapsed
three-point fibre and three singleton quotient colours.  The quotient is a
four-point nondegenerate braided set `Z`.  The hidden fibre is controlled by
affine maps `S_a` over `F_3`.  A corrected passive-fibre invariant additionally
requires that visible-label transport across a different collapsed-fibre
strand does not change the relevant `S`-map:

```text
S_{alpha(a)} = S_a,
S_{sigma(a)} = S_a.
```

The audit verifies this passive transport condition in exactly `16` of the
`32` formal collision rows and records `16` passive failures.  For the `16`
certified rows, the audit also verifies

```text
S_a S_b = S_{I(a,b)} S_{J(a,b)},
S_{\sigma(a)} T_a = id,
R(F_i,F_j)=(F_i,F_j).
```

Thus the all-arity invariant

```text
H_s = S_{a_1} S_{a_2} ... S_{a_k}(i)
```

is preserved for each tracked collapsed-fibre strand.  Consequently every
braid trivial on the quotient `Z^n` is trivial on `X^n`, so

```text
ker rho^Z_n <= ker rho^X_n
```

for all `n`.  Since `Z` is nondegenerate, its derived rack dominates `Z`,
and hence dominates each of these `16` six-point lifts.  The displayed
residual row is one instance of this passive-certified quotient-invariant
certificate.  The remaining `16` passive-failure rows are not closed by this
one-strand invariant; they need either a stronger multi-fibre invariant or an
actual quotient-kernel braid witness.

The passive-failure rows are audited further in
`proofs/linear_f3_passive_failure_quotient_kernel_audit.md`.  This finite
probe checks the `16` passive-failure rows through arity `3` against the
kernel of their nondegenerate four-point monolith quotient.  It finds no
quotient-kernel `X`-motion and no truncation:

```text
passive-failure rows = 16,
arities checked = 2..3,
quotient-kernel X-motion rows = 0.
```

This was finite evidence only.  At that stage it showed the passive transport
failure was not itself an immediate small-arity B witness; the rows still
needed either a stronger multi-fibre invariant or a higher-arity
quotient-kernel witness.

The stronger multi-fibre invariant has now been found and recorded in
`proofs/linear_f3_gap_corrected_invariant_closure.md`, with executable checks
in `proofs/linear_f3_gap_corrected_invariant_audit.md`.  The corrected
invariant closes all `32` formal monolith-collision rows, including the `16`
passive-failure rows.  If a visible label `z` lies to the left of a tracked
collapsed-fibre strand and there are `g` other collapsed-fibre strands between
them, the invariant uses

```text
S_{alpha^g(z)}
```

rather than `S_z`.  The audit verifies, for all `32` rows,

```text
beta = alpha^{-1},
S_{alpha^g(z)} S_{alpha^g(w)}
  = S_{alpha^g(u)} S_{alpha^g(v)}
  whenever R_Z(z,w)=(u,v),
S_{beta(z)} T_z = id,
R(F_i,F_j)=(F_i,F_j).
```

It also directly checks the tagged-strand invariant through arity `5`.
The all-arity proof shows that every braid trivial on the nondegenerate
four-point monolith quotient `Z` is trivial on the six-point lift:

```text
ker rho^Z_n <= ker rho^X_n
```

for every `n`.  Hence all `32` formal collision rows are dominated by the
derived rack of `Z`.  The formal collision half of the subdirect six-point
linear `F_3` branch is therefore closed; future searches in this family must
focus on the monolith `J`-separating side or leave the linear skew-over-flip
family.

The monolith `J`-separating half of the subdirect six-point linear `F_3`
branch is now closed in `proofs/linear_f3_separating_quotient_closure.md`,
with executable checks in
`proofs/linear_f3_separating_quotient_closure_audit.md`.  For each of the
`32` separating rows, the audit verifies:

```text
|X/mu| = 4,
X/mu is involutive,
P_X has the identity-extension contextual rack completion,
(pi_mu^n,J_n) is injective for all n by the finite relative graph.
```

Since involutive finite solutions are dominated by finite racks, the relative
contextual extension theorem gives

```text
ker rho^{Y_mu x Y_ctx x T_2}_n <= ker rho^X_n
```

for every `n`, where `Y_mu` dominates the involutive quotient and `Y_ctx` is
the contextual rack completion.  Thus all `32` monolith `J`-separating
subdirect rows are finite-rack dominated.

Combining this with the gap-corrected invariant closure for the `32`
monolith-collision rows closes all `64` subdirectly irreducible
degenerate non-involutive rows in the six-point linear `F_3`
skew-over-flip family.

The remaining `80` non-subdirect degenerate non-involutive rows in the same
family are closed in
`proofs/linear_f3_nonsubdirect_quotient_factor_closure.md`, with executable
checks in
`proofs/linear_f3_nonsubdirect_quotient_factor_closure_audit.md`.  For each
non-subdirect row, the audit selects only proper quotient factors that are
already known finite-rack dominated:

```text
rack-form quotients,
nondegenerate quotients,
involutive quotients.
```

Those selected quotient factors still reconstruct the original point and pass
the active-factor finite certificate.  Thus the product of their rack
detectors dominates the original six-point row.  The audit verifies:

```text
non-subdirect rows = 80,
certified rows = 80,
failures = 0.
```

The whole degenerate non-involutive linear `F_3` skew-over-flip family is now
closed in `proofs/linear_f3_degenerate_noninvolutive_family_closure.md`.
Combining:

```text
80 non-subdirect rows: known quotient-factor closure,
32 monolith J-separating rows: relative involutive quotient closure,
32 formal monolith J-collision rows: gap-corrected quotient invariant,
```

all `144` degenerate non-involutive rows are finite-rack dominated.  Together
with the known nondegenerate and involutive theorems, every six-point linear
skew-over-flip solution over `F_3` is finite-rack dominated.  Future B
searches should leave this family.

The signed-affine active-fibre gauge proposed later is reviewed in
`proofs/2026_06_08_signed_affine_active_fiber_gauge_review.md`.  Under its
listed hypotheses, the gauge is coherent: the effective label
`(-1)^d a` is the `alpha^g(z)` gap correction in the special case
`alpha(a)=-a`, and the gauged active fibre evolves by the internal
three-point nondegenerate solution.  This gives useful intuition for an
active non-automorphic subfamily, but it is not a new dependency in the
canonical closure: the audited proof ledger already closes all six-point
linear `F_3` rows by the three branches above.  The active frontier therefore
remains outside the linear `F_3` skew-over-flip family.

The reusable abstraction is recorded in
`proofs/gap_gauged_one_fiber_extension_theorem.md`.  It applies to a braided
quotient `pi:X->Z` with exactly one nonsingleton fibre `W` over a distinguished
quotient point `*`, singleton visible fibres, quotient visible transport
`alpha,beta=alpha^{-1}`, and hidden transport permutations `S_z,T_z`.  If:

```text
S_{beta z} T_z = id,
S_{alpha^d z} S_{alpha^d w}
  = S_{alpha^d u} S_{alpha^d v}
  whenever R_Z(z,w)=(u,v),
and the gauge pairs
  (S_{alpha^d z}, S_{alpha^{d+1} z})
generate two-sided symmetries of W,
```

then domination of `Z` and domination of `W` imply domination of `X` by
`Y_Z x Y_W^0`.  The proof uses the gap-gauged hidden value obtained by listing
visible labels to the left of a tracked `*`-slot and replacing each label `z`
by `alpha^g(z)`, where `g` is the number of intervening `*`-slots.  The
composition convention is important: the nearest visible label acts first.
This theorem packages the passive, twisted-passive, active-automorphic, and
signed-affine six-point `F_3` gauges into one all-arity positive mechanism.

The more general finite-state decoder abstraction is recorded in
`proofs/finite_state_dominated_decoder_theorem.md`.  Let `pi:X->Z` be a
braided quotient and let `U` be another finite bijective YBE solution, with
both `Z` and `U` already finite-rack dominated.  If there are braid-equivariant
maps

```text
Gamma_n:X^n -> U^n
```

such that

```text
D_n(x)=(pi^n(x), Gamma_n(x))
```

is injective for every `n`, then the product of rack detectors for `Z` and
`U` dominates `X`.  A finite local certificate for `Gamma_n` consists of
finite context monoids `L,R`, updates `lambda:X->L`, `rho:X->R`, and a readout
`gamma:L x X x R -> U` satisfying the context product identities

```text
lambda(x)lambda(y)=lambda(u)lambda(v),
rho(y)rho(x)=rho(v)rho(u)
```

and the local crossing identity into `U` whenever `R_X(x,y)=(u,v)`.  The
all-arity injectivity of `(pi^n,Gamma_n)` is checked by a finite graph on
`L^2 x R^2 x X^2`, with a collision bound

```text
n <= 2 |L|^2 |R|^2 |X|^2.
```

This theorem subsumes the contextual readout route when the contextual
readout lands in an already dominated finite YBE solution, and it subsumes the
gap-gauged one-fibre theorem by taking `U` to be a transparent extension of
the internal fibre solution.  The next positive target can therefore be stated
as construction of finite dominated decoder data `Z,U,L,R,gamma` for arbitrary
finite `X`, rather than direct rackification of `P_X`.

The multi-fibre transparent decoder corollary is corrected and recorded in
`proofs/multi_fiber_transparent_decoder_corollary.md`.  Transparent support
follows physical strands, so transparent hidden channels are indexed by the
canonical strand-species quotient of the dominated quotient `Z`, not by
arbitrary quotient colours.  For `R_Z(a,b)=(u,v)`, define `E_sp` to be the
equivalence relation generated by

```text
u ~ b,
v ~ a.
```

Then `Sp(Z)=Z/E_sp` is the finest quotient on which the solution is the flip,
and any physical-strand label map `c:Z->S` satisfying `c(u)=c(b)` and
`c(v)=c(a)` factors through `Sp(Z)`.

Given a quotient `pi:X->Z` dominated by `Y_Z`, and for each species
`s in Sp(Z)` a finite dominated fibre readout solution `W_s` with rack
detector `Y_s`, suppose there are braid-equivariant transparent readouts

```text
Gamma^s_n:X^n -> (W_s^0)^n
```

supported only on coordinates with species `s`, i.e.
`Gamma^s_n(x)_i=0` when `sigma(pi(x_i)) != s`.  If

```text
D_n(x)=(pi^n(x), (Gamma^s_n(x))_{s in Sp(Z)})
```

is injective for every `n`, then

```text
Y_Z x product_{s in Sp(Z)} Y_s^0
```

dominates `X`.  With shared context monoids `L,R`, local readouts
`gamma_s:L x X x R -> W_s^0`, and the same context product identities, the
local crossing identities into each `W_s^0` give a finite sufficient
certificate for equivariance.  The support condition is compatible with
transparent crossings exactly because `sigma(pi(u))=sigma(pi(y))` and
`sigma(pi(v))=sigma(pi(x))`.  The all-arity injectivity test is the same
finite graph test, replacing the single readout equality by equality of all
`gamma_s` channels.  The global all-`A,B` local crossing identities are a
convenient sufficient certificate; the literal necessary condition only holds
on reachable context pairs.  The earlier quotient-colour-indexed formulation
is valid only in the special case `Sp(Z)=Z`.

The quotient-controlled injective-gauge subcase is recorded in
`proofs/quotient_controlled_species_gauge_theorem.md`.  It removes the
finite all-arity injectivity graph when the hidden gauges depend only on the
quotient context and are fibrewise injective.  Let `pi:X->Z` be a braided
quotient dominated by `Y_Z`, let `sigma:Z->Sp(Z)` be the strand-species
quotient, and let each species `s` have a dominated finite fibre solution
`W_s` with detector `Y_s`.  Suppose finite quotient-context monoids `L,R` and
updates

```text
lambda:Z->L,
rho:Z->R
```

are preserved by quotient crossings.  If, for every species `s`, quotient
colour `z` with `sigma(z)=s`, and quotient contexts `A,B`, there is an
injective gauge

```text
G^s_{A,z,B}: pi^{-1}(z) -> W_s,
```

and the induced transparent local crossing identities into each `W_s^0`
hold, then

```text
Y_Z x product_{s in Sp(Z)} Y_s^0
```

dominates `X`.  The proof is immediate once a detector-kernel braid fixes the
quotient word: the quotient-controlled contexts `A_i,B_i` are unchanged, so
equality of the transparent species readout and injectivity of
`G^s_{A_i,z_i,B_i}` recover each hidden coordinate.  Thus future obstruction
searches must avoid quotient-controlled injective species gauges and force
hidden monodromy depending essentially on hidden fibre context inside a
single strand species.

The iterated version is recorded in
`proofs/stratified_decoder_tower_theorem.md`.  Given a finite tower of
braided quotients

```text
X=X^(r) -> X^(r-1) -> ... -> X^(0),
```

with `X^(0)` already rack-dominated, suppose each layer `pi_k:X^(k)->X^(k-1)`
has transparent species readouts

```text
Gamma^{k,s}_n:(X^(k))^n -> (W_{k,s}^0)^n
```

indexed by `s in Sp(X^(k-1))`, where each `W_{k,s}` is already dominated.
If every layer decoder

```text
D_n^(k)=(pi_k^n, (Gamma^{k,s}_n)_s)
```

is injective in all arities, then

```text
Y_0 x product_k product_{s in Sp(X^(k-1))} Y_{k,s}^0
```

dominates `X`.  The proof is induction up the tower.  Each layer can be
certified by finite lower-layer context monoids and local crossing identities,
and each layer's all-arity injectivity is automatic if the combined local
readout

```text
x in pi_k^{-1}(a) -> (gamma_{k,s}(A,x,B))_s
```

is injective for every lower context `A,B` and lower colour `a`.  This tower
absorbs hidden-fibre dependence that becomes quotient-controlled only after
additional lower layers.  A remaining counterexample must therefore evade
all finite stratified decoder towers, rather than merely evade one-layer
quotient-controlled gauges.

The nondegenerate-reflection congruence is recorded in
`proofs/nondegenerate_reflection_congruence.md`.  For a finite bijective
solution `X` with

```text
R_X(x,y)=(lambda_x(y),rho_y(x)),
```

start with `E_0=Delta_X` and repeatedly add the pullback pairs

```text
y ~ y'  if lambda_x(y) E_k lambda_x(y') for some x,
x ~ x'  if rho_y(x) E_k rho_y(x') for some y,
```

then close under braided congruence for `R_X` and `R_X^{-1}`.  The stable
congruence `E_nd` has two key properties.  First, `X/E_nd` is two-sided
nondegenerate, hence rack-dominated by the known derived-rack/guitar theorem.
Second, if `F` is any braided congruence such that `X/F` is two-sided
nondegenerate, then `E_nd <= F`.  Thus `X/E_nd` is the largest nondegenerate
quotient of `X`.  If `E_nd` is proper, the canonical next positive attempt is
to decode the hidden layer over `X -> X/E_nd` by the relative contextual,
species-gauge, or stratified decoder-tower machinery.  If `E_nd` is
universal, `X` is degeneracy-perfect: it has no nontrivial nondegenerate
quotient.  In particular, any braided-simple degenerate candidate is
degeneracy-perfect, because degeneracy adds a nontrivial pullback pair at the
first stage and simplicity then forces `E_nd=X x X`.

The nondegenerate-reflection Brunnian obstruction is recorded in
`proofs/nondegenerate_reflection_brunnian_obstruction.md`.  Let
`Z=X/E_nd` be the nontrivial nondegenerate reflection quotient, and let
`F_{n-1}=ker(d_n:P_n->P_{n-1})` be the last-strand free group with meridian
generators `x_i=A_{i,n}`.  Put

```text
G^X_n=rho^X_n(F_{n-1}),
G^Z_n=rho^Z_n(F_{n-1}),
E_n=ker(G^X_n -> G^Z_n),
M_{i,n}=<<rho^X_n(x_i)>>_{G^X_n},
C^X_n=[M_{1,n},...,M_{n-1,n}]_Sigma.
```

If `E_n cap C^X_n=1` for all sufficiently large `n`, then `X` is
finite-rack dominated.  The proof combines a rack detector `Y_Z` for the
nondegenerate quotient, transparent fixed-arity racks for the finitely many
small arities, `T_2`, and the standard transparent Brunnian reduction.  For
large `n`, any Brunnian braid invisible to this product detector lies in
`F_{n-1}`, is trivial on `Z`, and has `X`-image in the all-meridian symmetric
commutator layer `C^X_n`; hence its image lies in `E_n cap C^X_n`, which is
trivial by assumption.  Therefore, if `X` is not dominated and `E_nd` is
proper, the relative intersections `E_n cap C^X_n` must be nontrivial for
unbounded `n`.  The proper-reflection branch is now reduced to eventual
vanishing of this canonical relative last-strand obstruction; the other
primitive branch is `E_nd=X x X`, the degeneracy-perfect case.

The nondegenerate-reflection filtration obstruction is recorded in
`proofs/nondegenerate_reflection_filtration_obstruction.md`.  Instead of
collapsing directly from `X` to `X/E_nd`, keep the finite construction chain

```text
Delta_X=E_0 <= E_1 <= ... <= E_t=E_nd,
X_i=X/E_i,
q_i:X_i->X_{i+1}.
```

For the last-strand free group define

```text
G^{(i)}_n=rho^{X_i}_n(F_{n-1}),
K^{(i)}_n=ker(G^{(i)}_n -> G^{(i+1)}_n),
M^{(i)}_{j,n}=<<rho^{X_i}_n(A_{j,n})>>_{G^{(i)}_n},
C^{(i)}_n=[M^{(i)}_{1,n},...,M^{(i)}_{n-1,n}]_Sigma.
```

The layer-lifting theorem says: if `X_{i+1}` is rack-dominated and
`K^{(i)}_n cap C^{(i)}_n=1` for all sufficiently large `n`, then `X_i` is
rack-dominated.  The proof is the same transparent Brunnian argument as the
single-quotient obstruction, applied to the one layer `X_i->X_{i+1}` with
fixed-arity rack factors for small `n`.  Since the top quotient `X_t` is
nondegenerate, downward induction gives: if every reflection layer has
eventually trivial relative all-meridian kernel, then `X` is rack-dominated.
Consequently any finite counterexample has one fixed bad layer with
`K^{(i)}_n cap C^{(i)}_n != 1` for unbounded `n`.  This also covers the
degeneracy-perfect case `E_nd=X x X`: even if the top nondegenerate quotient
is one point, the finite filtration still localizes any obstruction to an
elementary degeneracy-pullback layer.

The first-fold atom Brunnian obstruction is recorded in
`proofs/first_fold_atom_brunnian_obstruction.md`.  Let `F_1(X)` be the
braided congruence generated by immediate degeneracy folds

```text
y ~ y' if lambda_x(y)=lambda_x(y') for some x,
x ~ x' if rho_y(x)=rho_y(x') for some y.
```

If `X` is a smallest finite counterexample, then `X` is degenerate, so
`F_1(X)` is nontrivial.  Let `mu <= F_1(X)` be a minimal nontrivial braided
congruence.  For every finite rack prefix `P_m`, let `Y_mu` dominate the
proper quotient `X/mu`, and put `Q_m=(P_m x Y_mu)^0 x T_2`.  Since `Q_m`
cannot dominate `X`, the transparent Brunnian reduction gives a Brunnian
`Q_m`-invisible braid moving some word of `X^n`.  The `Y_mu` factor forces
all coordinate mismatches to lie inside `mu`; the mismatch-generated braided
congruence is nontrivial and contained in `mu <= F_1(X)`, so atom-minimality
forces it to equal `mu`.  The witnesses are unbounded in arity: otherwise
fixed-arity rack cofinality would add finitely many transparent factors
killing the bounded witnesses, giving a finite rack dominating `X`.  Thus a
minimal counterexample must have a first-fold atom generated cofinally by
actual Brunnian rack-prefix-invisible coordinate mismatches.

The unique first-fold atom monolith theorem is recorded in
`proofs/unique_first_fold_atom_monolith.md`.  If a smallest counterexample had
two distinct first-fold atoms `mu_1,mu_2 <= F_1(X)`, then
`mu_1 cap mu_2=Delta_X` by atom-minimality.  The diagonal map

```text
X -> X/mu_1 x X/mu_2
```

would be injective and braided.  Both quotients are proper and therefore
rack-dominated by minimality of `X`; product closure and injectivity would
pull domination back to `X`, contradiction.  Hence `F_1(X)` has a unique
atom `mu`.  For any nontrivial braided congruence `nu`, if
`mu cap nu=Delta_X` and `nu` is proper, the same diagonal-product argument
using `X/mu x X/nu` gives a contradiction; if `nu` is universal, containment
is automatic.  Therefore `mu cap nu` is nontrivial for every nontrivial `nu`,
and atom-minimality gives `mu <= nu`.  Thus the unique first-fold atom is the
global monolith `mu_X`.  A minimal counterexample is therefore either
braided-simple degeneracy-perfect, or subdirectly irreducible with monolith
`mu_X <= F_1(X)` generated cofinally by actual Brunnian detector-kernel
mismatches.

The cofinal monolith chief-factor obstruction is recorded in
`proofs/cofinal_monolith_chief_factor_obstruction.md`.  For a finite rack
prefix `P_m`, choose `Y_mu` dominating `X/mu` and put
`Q_m=(P_m x Y_mu)^0 x T_2`.  For the last-strand free group define the
combined finite image

```text
Phi_{m,n}:F_{n-1}->Gamma_{m,n}
  <= Sym(Q_m^n) x Sym(X^n),
K_{m,n}=ker(Gamma_{m,n}->rho^{Q_m}_n(F_{n-1})),
L_{m,n}=ker(Gamma_{m,n}->rho^X_n(F_{n-1})),
C_{m,n}=[N_{1,m,n},...,N_{n-1,m,n}]_Sigma.
```

For every prefix `P_m` and every `N`, there is `n>N` with
`K_{m,n} cap C_{m,n} != 1`.  Otherwise fixed-arity rack cofinality plus the
transparent Brunnian reduction would make `Q_m` dominate `X`.  Let
`H=K_{m,n} cap C_{m,n}`.  Since `H` is a nontrivial normal subgroup of the
finite group `Gamma_{m,n}`, choose a minimal nontrivial normal subgroup
`A <= H`; then `A/1` is a chief factor inside the detector kernel and inside
the exact all-meridian layer.  The projection kernels satisfy
`K_{m,n} cap L_{m,n}=1`, so `p_X(A)` is nontrivial.  Because `A <= K_{m,n}`
and `Q_m` contains `Y_mu^0`, the `X`-projection of `A` acts trivially on
`(X/mu)^n`; all coordinate mismatches lie inside `mu`.  The mismatch
congruence is nontrivial and contained in `mu`, and because `mu` is the
global monolith it equals `mu`.  Thus every finite rack prefix has unbounded
arities with a detector-invisible all-meridian chief factor whose
`X`-projection generates the unique first-fold monolith.  Applying the
chief-factor dichotomy gives either a nonabelian monolith-chief factor
covered by every meridian normal closure, or an elementary abelian
monolith-chief factor covered by the exact all-meridian subgroup.

The monolith-chief pairwise-core visibility correction is recorded in
`proofs/monolith_chief_pairwise_core_visibility.md`.  A tempting split into
pairwise-visible and central-pairwise-invisible monolith-chief obstructions is
too weak for the exact all-meridian subgroup used here.  For normal meridian
closures,

```text
C_{m,n}=[N_{1,m,n},...,N_{n-1,m,n}]_Sigma
  <= [N_{i,m,n},N_{j,m,n}]
```

for every pair `i!=j`.  Therefore

```text
C_{m,n} <= D_{m,n}:=intersection_{i<j}[N_{i,m,n},N_{j,m,n}].
```

Combining this with the cofinal monolith chief-factor obstruction gives:
for every finite rack prefix `P_m` and every cutoff, some larger arity has a
chief factor `A/1` with

```text
A <= K_{m,n} cap C_{m,n} <= K_{m,n} cap D_{m,n}.
```

The projection-kernel identity `K_{m,n} cap L_{m,n}=1` makes the `X`-action
of `A` nontrivial, while the `Y_mu^0` factor forces that action to stay
inside `mu`-fibres; since `mu` is the global monolith, the coordinate
mismatches generated by `p_X(A)` equal `mu`.  Thus even central elementary
abelian all-meridian monolith-chief factors are pairwise-core visible.  The
remaining positive target is to rule out cofinal detector-invisible
pairwise-core monolith motion; the negative target is a fixed finite `X`
whose unique first-fold monolith is generated cofinally by such pairwise-core
chief factors.

The bounded-support pairwise obstruction elimination is recorded in
`proofs/bounded_support_pairwise_obstruction_elimination.md`.  For a fixed
finite solution `X` and support bound `s`, choose fixed-arity racks
`Z_k`, `2<=k<=s+1`, with `ker rho^{Z_k}_k <= ker rho^X_k`, and set

```text
B_s(X)=product_{k=2}^{s+1} Z_k^0.
```

If a detector `Q` contains `B_s(X)` and `w in F_T` with `|T|<=s`, then
`rho^Q_n(w)=1` implies `rho^X_n(w)=1`: color only the active strands
`T union {n}` nontransparent in the `Z_{|T|+1}^0` factor and use the
transparent deletion formula, reducing to the fixed-arity detector
`Z_{|T|+1}`.  In finite-image terms, with

```text
Phi_n:F_{n-1}->Gamma_n<=Sym(Q^n)xSym(X^n),
iw(g)=min{|T|:g in Phi_n(F_T)},
```

one has

```text
g in K_n and iw(g)<=s  ==>  g=1.
```

because such a `g` is also in the `X`-kernel `L_n`, and `K_n cap L_n=1`.
Thus, after strengthening a prefix detector to

```text
Q_{m,s}=(P_m x Y_mu)^0 x T_2 x B_s(X),
```

every nontrivial monolith-generating detector-kernel obstruction has image
support width greater than `s`.  In particular, pairwise or pairwise-core
monolith obstructions cannot be disguised two-meridian or bounded-subset
phenomena; they must be same-image support ghosts requiring unbounded
meridian support.  Central elementary abelian high-Brunnian `p`-module
mechanisms, if they survive, are also not represented by bounded-support
detector-kernel elements once `B_s(X)` is included.

The parabolic-disjoint chief obstruction is recorded in
`proofs/parabolic_disjoint_chief_obstruction.md`.  With the strengthened
detector

```text
Q_{m,s}=(P_m x Y_mu)^0 x T_2 x B_s(X),
```

let `Phi_n:F_{n-1}->Gamma_n`, `K_n`, `L_n`, `N_{i,n}`, and `C_n` be the
usual combined finite-image objects, and for
`T subset {1,...,n-1}` set

```text
F_T=<x_i:i in T>,
H_T=Phi_n(F_T).
```

For every `m,s,N`, some `n>N` has a chief factor `A/B` of `Gamma_n` with

```text
B < A <= K_n cap C_n,
```

whose `X`-projection is nontrivial and generates the monolith `mu`, and which
is disjoint from every bounded parabolic image:

```text
A cap H_T B = B        whenever |T|<=s.
```

Indeed, choose `A/B` inside the nontrivial normal subgroup `K_n cap C_n`.
The `Y_mu^0` factor forces its `X`-motion to stay inside `mu`-fibres, and the
projection-kernel identity `K_n cap L_n=1` makes the motion nontrivial, hence
monolith-generating.  For parabolic disjointness, bounded-support
annihilation gives `K_n cap H_T=1`; if `a=hb in A cap H_TB` with `h in H_T`
and `b in B`, then `h=ab^{-1} in K_n cap H_T=1`, so `a in B`.  Thus a
surviving obstruction is not merely large-support.  No bounded parabolic
subgroup even meets the obstruction chief factor nontrivially modulo `B`.
Pairwise obstructions, if present, must be global conjugation ghosts: normal
closures of meridians cover the factor only after conjugation by unboundedly
many other meridians.  Central elementary abelian obstructions must be
high-Brunnian module classes whose every bounded parabolic restriction
vanishes.

The deletion-null monolith chief obstruction is recorded in
`proofs/deletion_null_monolith_chief_obstruction.md`.  With the same
strengthened detector `Q_{m,s}` and finite image
`Phi_n:F_{n-1}->Gamma_n`, the finite-image Brunnian theorem gives

```text
Phi_n(Brun_n cap ker rho^{Q_{m,s}}_n)=K_n cap C_n.
```

Choose a chief factor `A/B` inside `K_n cap C_n`, as in the
parabolic-disjoint theorem.  Then the same `A/B` has the parabolic-disjoint
property

```text
A cap H_TB=B        for every |T|<=s,
```

and its `X`-projection generates the monolith `mu`.  Moreover, every
nontrivial element `a in A` has an actual Brunnian representative:

```text
exists beta_a in Brun_n cap ker rho^{Q_{m,s}}_n
with Phi_n(beta_a)=a.
```

Since `beta_a` is Brunnian, every proper deletion shadow of `beta_a` is
literally trivial in the braid group.  Thus the obstruction is an exact
same-image, deletion-null, all-meridian chief factor, not merely a
large-support or same-image deletion-coherent finite-image element.  The
current positive target is to rule out first-fold monoliths generated by
deletion-null detector-invisible chief factors; the negative target is one
fixed finite `X` whose first-fold monolith is generated cofinally by such
chief factors against every finite rack prefix.

The Brunnian derivative chief dichotomy is recorded in
`proofs/brunnian_derivative_chief_dichotomy.md`.  For a deletion-null chief
factor `A/B <= K_n cap C_n`, choose for each `a in A` a Brunnian
`Q`-invisible representative `beta_a` with `Phi_n(beta_a)=a`.  Embed
`beta_a` into arity `n+1` by adding a new last strand, let `tau_i` be the
half-twist exchanging old strand `i` with the new strand, and define

```text
D_i beta_a=[iota(beta_a),tau_i].
```

Then `D_i beta_a` is Brunnian and `Q`-invisible: deleting the new strand
gives `[beta_a,1]`, deleting an old strand gives `[1,d_j(tau_i)]`, and the
`Q`-image is `[1,rho^Q(tau_i)]`.  Hence

```text
partial_i(a):=Phi_{n+1}(D_i beta_a)
```

is a well-defined set map `A->Gamma_{n+1}` landing in
`K_{n+1} cap C_{n+1}`.  The definition is independent of the chosen
Brunnian representative because equal combined `Q x X` images in arity `n`
remain equal after adding an idle strand and commuting with the same probe.
The resulting dichotomy is: either some `partial_i(a)` is nontrivial, giving
a new deletion-null monolith-generating Brunnian obstruction in arity `n+1`;
or all derivatives vanish, equivalently `p_X(A)` centralizes every
one-strand probe half-twist after adding a new strand.  Thus a minimal
counterexample must support either an infinite derivative-propagating tower
of monolith chief obstructions or cofinally many probe-central deletion-null
monolith chief factors.

The probe-central branch has been converted into a finite centralizer
condition in `proofs/probe_centralizer_chief_obstruction.md`.  For
`G^X_n=rho^X_n(F_{n-1})`, embed the `X`-image into arity `n+1` by adding an
idle strand,

```text
iota_n:G^X_n->Sym(X^{n+1}),
```

and let `T_{i,n}=rho^X_{n+1}(tau_i)`, where `tau_i` exchanges old strand `i`
with the new strand.  Define

```text
Z^pr_n(X)
  =
{g in G^X_n : [iota_n(g),T_{i,n}]=1 for every i=1,...,n}.
```

For the combined detector image `Gamma_n`, set

```text
PC_n=p_X^{-1}(Z^pr_n(X)).
```

If the derivative-visible branch fails cofinally, then for every detector
prefix and support cutoff there are unbounded arities with a chief factor

```text
B < A <= K_n cap C_n cap PC_n,
```

and the `X`-projection of `A` acts nontrivially inside `mu`-fibres and
generates the first-fold monolith.  Thus the probe-central obstruction is
exactly cofinal nontriviality of the finite subgroup intersection
`K_n cap C_n cap PC_n`.  The two remaining positive targets are now: rule out
infinite derivative-propagating deletion-null monolith-chief towers, and prove
`K_n cap C_n cap PC_n=1` eventually.  A negative proof must construct one
fixed finite `X` whose first-fold monolith survives cofinally in one of those
two exact forms.

The probe-central branch has been sharpened to the conjugated-probe core in
`proofs/conjugated_probe_core_obstruction.md`.  The one-probe centralizer
tests only half-twists between the added strand and the original old
positions.  Instead, for `h in G^X_n`, choose a last-strand braid `eta` with
`rho^X_n(eta)=h` and define

```text
T_{i,h}=rho^X_{n+1}(iota(eta) tau_i iota(eta)^{-1}).
```

Then

```text
CPC_n(X)
  =
{g in G^X_n : [iota_n(g),T_{i,h}]=1
              for every i and every h in G^X_n}
  =
cap_{h in G^X_n} h Z^pr_n(X) h^{-1}.
```

This is the normal core of the one-probe centralizer, and its pullback

```text
CPC^Gamma_n=p_X^{-1}(CPC_n(X))
```

is normal in the combined image.  Conjugated derivatives

```text
D_{i,eta} beta=[iota(beta),iota(eta)tau_i iota(eta)^{-1}]
```

remain Brunnian and `Q`-invisible.  Therefore, if some commutator
`[iota_n(p_X(a)),T_{i,h}]` is nontrivial, it produces a new
monolith-generating element of `K_{n+1} cap C_{n+1}`.  If all such conjugated
derivatives vanish cofinally, then the obstruction chief factors lie in

```text
B < A <= K_n cap C_n cap CPC^Gamma_n,
```

with `X`-projection acting nontrivially inside `mu`-fibres and generating the
first-fold monolith.  The current positive target is therefore sharper:
prove `K_n cap C_n cap CPC^Gamma_n=1` eventually, or rule out infinite
conjugated-derivative towers.  A negative proof must realize one of these two
exact behaviours for a fixed finite `X`.

The current endpoint obstruction is recorded in
`proofs/actual_mismatch_probe_visibility_gap.md`.  The attempted positive
closure would use `mu <= F_1(X)` to argue that a monolith-generating Brunnian
chief factor must move an actually probe-visible first-fold pair.  This is the
unproved step.  The finite-image obstruction only gives

```text
<actual coordinate mismatches of p_X(A)>_br = mu.
```

It does not say that any actual moved pair is itself an immediate degeneracy
fold, or even conjugated-probe visible.  The immediate fold may appear only
after closing the moved pairs under `R_X`, `R_X^{-1}`, and transitivity.
Brunnian derivatives see actual moved pairs, not the full braided congruence
generated by them.  The derivative-propagating branch also does not collapse
by bounded-support annihilation, because repeated derivatives may have
support growing with arity.  The attempted negative closure still lacks one
fixed finite `X` whose first-fold monolith supports cofinal deletion-null
Brunnian chief factors `K_n cap C_n` against every rack prefix; the known
powered alternating-group construction varies the target with the detector.

The actual-mismatch gap is repaired, but not resolved, by the finite motion
congruence in `proofs/probe_central_motion_congruence.md`.  For

```text
H_n=K_n cap C_n cap CPC^Gamma_n,
```

define `Pi_{Q,n}` to be the braided congruence generated by all coordinate
color changes caused by elements of `H_n`.  If the conjugated-derivative branch
fails cofinally, then for every detector prefix and support cutoff there are
unbounded arities with

```text
Pi_{Q,n}=mu.
```

The proof no longer tries to extract an immediate first-fold pair from an
actual moved pair.  Since `H_n <= K_n` and `Q` contains `Y_mu^0`, all
`H_n`-motions are trivial modulo `mu`, so `Pi_{Q,n} <= mu`.  The deletion-null
chief factor supplied by the core branch lies inside `H_n`, and
`K_n cap L_n=1` makes its `X`-projection nontrivial, so `Pi_{Q,n}` is
nontrivial.  Monolith minimality then forces `Pi_{Q,n}=mu`.  The remaining
positive targets are now: rule out infinite conjugated-derivative towers, and
prove `Pi_{Q,n} != mu` eventually for some finite detector.  The negative
target is one fixed finite `X` where conjugated derivatives persist cofinally
or `Pi_{Q,n}=mu` occurs unboundedly against every rack prefix.

The abelian layer of contextual separability is recorded in
`proofs/abelian_contextual_separability_test.md`.  The contextual Wirtinger
group

```text
G_X=<g_p | same-strand equalities, g_r=g_p g_q g_p^{-1} for forced p*q=r>
```

has abelianization generated by contextual classes `[p]`, with relations
`[p]=[p']` for same-strand equalities and `[r]=[q]` for forced products
`p*q=r`.  If `[g_p] != [g_{p'}]` in `G_X^ab`, residual finiteness of finitely
generated abelian groups gives a finite abelian contextual augmented quotient
separating the operator coordinates.  If `p,p'` lie in the same contextual
action component and `tau` labels a path from `p` to `p'`, then
`[tau] notin im(Lambda_p->G_X^ab)` also gives a finite abelian quotient
separating the transporter coset from the loop subgroup.  Therefore a
surviving contextual transition must satisfy both `[g_p]=[g_{p'}]` and
`[tau] in im(Lambda_p->G_X^ab)`.  Any remaining contextual separability
failure is genuinely nonabelian subgroup nonseparability:
`tau in closure_prof(Lambda_p) \ Lambda_p` while already abelianly
indistinguishable from a loop.

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
