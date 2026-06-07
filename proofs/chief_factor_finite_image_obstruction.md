# Chief-Factor Finite-Image Obstruction

Date: 2026-06-06

This note records a proof-grade refinement of the finite-image
symmetric-commutator boundary.  It also corrects an important framing issue:
the class of degenerate finite bijective solutions is not a smaller residual
case.  Solving all degenerate solutions would solve the full problem.

This is still a C-type result.  It does not prove Sawin's statement and does
not construct a counterexample.

Update.  The subsequent note
`proofs/pairwise_or_central_finite_image_obstruction.md` sharpens this
chief-factor boundary: when the meridian normal closures generate the finite
image, every nonabelian chief-factor obstruction and every noncentral abelian
chief-factor obstruction is already detected by a two-meridian commutator.
Only central elementary abelian chief factors can genuinely require the full
all-meridian symmetric commutator.

## Degenerate Solutions Are Not A Smaller Case

Let `D` be a finite set with `|D|>1`, and let

```text
R_D(a,b) = (a,b).
```

This is a finite bijective set-theoretic YBE solution.  Every braid generator
acts trivially on `D^n`, and the solution is degenerate because, for fixed
`a`, the first-coordinate map `b -> a` is constant.

Let `Z` be any finite bijective set-theoretic YBE solution, and form the
product solution

```text
X = D x Z,
```

with

```text
R_X((d,z),(d',z')) = ((d,z_1),(d',z_2))
```

whenever `R_Z(z,z')=(z_1,z_2)`.  Then `X` is finite, bijective, and
degenerate.  Its braid action is

```text
rho^X_n = id_{D^n} x rho^Z_n,
```

so

```text
ker rho^X_n = ker rho^Z_n
```

for every `n`.

Therefore, if every finite degenerate bijective solution were dominated by a
finite rack, then every finite bijective solution would be dominated by a
finite rack.  The genuinely degenerate examples remain the only place not
covered by the derived-rack theorem, but a theorem covering all degenerate
solutions is equivalent to the full Sawin problem.

## Setup

Fix a finite bijective YBE solution `X`.  Let `Y` be a finite rack and set

```text
Q = Y^0 x T_2,
```

where `Y^0` is the transparent extension and `T_2` is the two-element trivial
rack.  For `n>=2`, let

```text
F_{n-1}=ker(d_n:P_n -> P_{n-1})
```

be the last-strand free group with free generators

```text
x_i=A_{in},        1 <= i <= n-1.
```

Let

```text
Phi_n:F_{n-1}->Gamma_n<=Sym(Q^n) x Sym(X^n)
```

be the combined finite image.  Write

```text
K_n = ker(Gamma_n -> rho^Q_n(F_{n-1})),
L_n = ker(Gamma_n -> rho^X_n(F_{n-1})).
```

For each meridian define

```text
N_{i,n}=<<Phi_n(x_i)>>_{Gamma_n},
```

and put

```text
C_n=[N_{1,n},...,N_{n-1,n}]_Sigma.
```

The finite-image symmetric-commutator theorem gives

```text
Phi_n(Brun_n cap ker rho^Q_n) = K_n cap C_n.
```

The previous domination criterion was

```text
K_n cap C_n <= L_n
```

for every `n`.  Since `Gamma_n` is a subgroup of

```text
Sym(Q^n) x Sym(X^n),
```

the two projection kernels intersect trivially:

```text
K_n cap L_n = 1.
```

Hence, in this finite-image model, the obstruction condition is exactly

```text
K_n cap C_n != 1.
```

Equivalently, `Q` dominates `X` if and only if

```text
K_n cap C_n = 1
```

for every `n`.

## Chief-Factor Coverage

Let `G` be a finite group and let `A/B` be a chief factor of `G`.  A normal
subgroup `U triangleleft G` is said to cover `A/B` if

```text
A <= U B.
```

Equivalently, the image of `U cap A` in `A/B` is nontrivial, hence all of
`A/B`, because `A/B` is a minimal normal subgroup of `G/B`.

## Theorem

Let `G` be a finite group, let

```text
K,N_1,...,N_r triangleleft G,
```

and set

```text
C=[N_1,...,N_r]_Sigma.
```

Then

```text
K cap C != 1
```

if and only if some chief factor `A/B` of `G` lying inside `K` is covered by
`C`.

Moreover:

1. If `A/B` is nonabelian, then `C` covers `A/B` if and only if every `N_i`
   covers `A/B`.

2. If `A/B` is abelian and `C` covers `A/B`, then every `N_i` covers `A/B`
   and `gamma_r(G)` covers `A/B`.

Thus the nonabelian obstruction is exactly common chief-factor coverage, while
the abelian obstruction also needs genuine lower-central depth.

## Proof

The subgroup `C` is normal in `G`.  Every generator of `C` is an iterated
commutator involving one input from each `N_i`; since each `N_i` is normal,
such a commutator lies in each `N_i`.  Therefore

```text
C <= N_i
```

for every `i`.  Also every generator is an `r`-fold commutator, so

```text
C <= gamma_r(G).
```

Suppose first that `K cap C != 1`.  Since `K cap C` is normal in `G`, choose a
chief series of `G` refining

```text
1 <= K cap C <= K <= G.
```

Some chief factor `A/B` lies inside `K cap C`; in particular it lies inside
`K`, and `C` covers it.

Conversely, suppose a chief factor `A/B` lies inside `K` and is covered by
`C`.  Then

```text
A <= C B.
```

By Dedekind's modular law,

```text
A = (A cap C) B.
```

Thus `A cap C` is not contained in `B`, so `A cap C` is nontrivial.  Since
`A<=K`, this gives

```text
1 != A cap C <= K cap C.
```

Hence `K cap C != 1`.

For a nonabelian chief factor, assume first that `C` covers `A/B`.  Since
`C<=N_i`, each `N_i` covers `A/B`.

Conversely suppose every `N_i` covers `A/B`.  Work modulo `B`.  The image
`A/B` is a minimal normal nonabelian subgroup of `G/B`, hence a direct product
of isomorphic nonabelian simple groups and is perfect.  Since each `N_i`
covers `A/B`, the image of each `N_i` contains `A/B`.  Therefore the
symmetric commutator subgroup contains the iterated commutators obtained by
taking every input inside `A/B`; because `A/B` is perfect, these generate
`A/B`.  Hence `C` covers `A/B`.

For an abelian chief factor, if `C` covers `A/B`, then `C<=N_i` for every
`i`, so every `N_i` covers `A/B`.  Also `C<=gamma_r(G)`, so
`gamma_r(G)` covers `A/B`.  These are necessary conditions; the statement does
not assert that they are sufficient in the abelian case.

## Application To The Finite-Image Boundary

Apply the theorem with

```text
G = Gamma_n,
K = K_n,
N_i = N_{i,n},
r = n-1,
C = C_n.
```

Because `K_n cap L_n=1`, failure of domination in arity `n` is equivalent to

```text
K_n cap C_n != 1.
```

Therefore every finite-image failure has one of the following chief-factor
forms.

Type I: nonabelian common-chief obstruction.  There is a nonabelian chief
factor `A/B` of `Gamma_n` lying inside `K_n` such that every meridian normal
closure covers it:

```text
N_{i,n} covers A/B        for all i=1,...,n-1.
```

For nonabelian chief factors this condition is sufficient.

Type II: abelian deep-lower-central obstruction.  There is an abelian chief
factor `A/B` of `Gamma_n` lying inside `K_n` that is covered by `C_n`.  This
can happen only if every `N_{i,n}` covers `A/B` and

```text
gamma_{n-1}(Gamma_n)
```

covers `A/B`.

## Sufficient Criterion

For a fixed finite rack detector `Q=Y^0 x T_2`, suppose that for all
sufficiently large `n`:

1. no nonabelian chief factor inside `K_n` is covered by every meridian normal
   closure `N_{i,n}`;

2. no abelian chief factor inside `K_n` that is covered by every
   `N_{i,n}` is also covered by `gamma_{n-1}(Gamma_n)`.

Then

```text
K_n cap [N_{1,n},...,N_{n-1,n}]_Sigma = 1
```

for all sufficiently large `n`.  Fixed-arity rack cofinality handles the
remaining finitely many arities, so a finite enlargement of `Q` dominates
`X`.

## Remaining Boundary

For a positive solution from this route, it is enough to prove that for every
finite bijective solution `X` one can choose a finite rack detector
`Q=Y^0 x T_2` so that neither chief-factor obstruction occurs in sufficiently
large arities.

For a negative solution, one must construct an explicit finite bijective `X`
such that for every finite rack prefix `P_m`, with

```text
Q_m=P_m^0 x T_2,
```

there are unbounded arities `n_m` and chief factors inside the corresponding
`K_{n_m}` that produce either the nonabelian common-chief obstruction or the
abelian deep-lower-central obstruction.

Thus the remaining obstruction is not merely an ordinary Brunnian element or
an all-meridian symmetric commutator.  It must survive as a chief factor
inside the detector-invisible finite image.
