# Bounded-Support Pairwise Obstruction Elimination

This note records a finite-arity detector guardrail: once the detector is
augmented by all fixed-arity rack detectors up to a support bound `s`, no
detector-invisible last-strand element of image support at most `s` can remain
`X`-visible.

Consequently, any cofinal monolith obstruction in the pairwise or
pairwise-core finite-image branch must have unbounded image support.  It
cannot be a disguised two-strand or bounded-subset phenomenon.

## Bounded-Support Detector

Fix a finite bijective YBE solution `X` and an integer `s>=1`.

For each arity

```text
2 <= k <= s+1,
```

fixed-arity rack cofinality gives a finite rack `Z_k` satisfying

```text
ker rho^{Z_k}_k <= ker rho^X_k.
```

Define the bounded-support rack

```text
B_s(X)=product_{k=2}^{s+1} Z_k^0,
```

where `Z_k^0` denotes the transparent extension.

## Last-Strand Support

For arity `n`, let

```text
F_{n-1}=ker(d_n:P_n->P_{n-1})
```

be the last-strand free group, with meridian generators

```text
x_i=A_{i,n},        1 <= i <= n-1.
```

For

```text
T subset {1,...,n-1},
```

write

```text
F_T=<x_i:i in T> <= F_{n-1}.
```

Elements of `F_T` are last-strand pure braids supported on the active strands

```text
T union {n}.
```

If `|T|=r`, the active arity is `r+1`.

## Bounded-Support Annihilation Theorem

Let `Q` be any finite rack detector containing `B_s(X)` as a direct product
factor.  If

```text
w in F_T,        |T| <= s,
```

and

```text
rho^Q_n(w)=1,
```

then

```text
rho^X_n(w)=1.
```

### Proof

Let `r=|T|`.  Since `Q` contains the transparent factor `Z_{r+1}^0`,

```text
rho^{Z_{r+1}^0}_n(w)=1.
```

Color only the active strands `T union {n}` by nontransparent colors and
color every other strand by the transparent color.  The transparent deletion
formula gives

```text
rho^{Z_{r+1}}_{r+1}(w_T)=1,
```

where `w_T` is the induced `(r+1)`-strand braid on the active strands, after
the order-preserving relabeling of `T union {n}`.

By the choice of `Z_{r+1}`,

```text
rho^X_{r+1}(w_T)=1.
```

Since `w` uses no strands outside `T union {n}`, its `X^n`-action is exactly
the `X^{r+1}`-action of `w_T` on the active coordinates and the identity on
all inactive coordinates.  Therefore

```text
rho^X_n(w)=1.
```

## Finite-Image Form

For a detector `Q`, define

```text
Phi_n:F_{n-1}->Gamma_n
  <= Sym(Q^n) x Sym(X^n).
```

Let

```text
K_n=ker(Gamma_n->rho^Q_n(F_{n-1})),
L_n=ker(Gamma_n->rho^X_n(F_{n-1})).
```

The projection kernels satisfy

```text
K_n cap L_n = 1.
```

Define the image support width of `g in Gamma_n` by

```text
iw(g)=min{|T|:g in Phi_n(F_T)}.
```

If `Q` contains `B_s(X)`, then

```text
g in K_n and iw(g)<=s  ==>  g=1.
```

Indeed, choose `w in F_T` with `|T|<=s` and `g=Phi_n(w)`.  Since `g in K_n`,
we have `rho^Q_n(w)=1`.  The bounded-support annihilation theorem gives
`rho^X_n(w)=1`, so `g in L_n`.  Hence

```text
g in K_n cap L_n = 1.
```

Thus every nontrivial detector-kernel element has image support width `>s`.

## Consequence For The Monolith Branch

Let `X` be a smallest finite counterexample, with unique first-fold monolith
`mu`.  For a finite rack prefix `P_m`, let `Y_mu` dominate `X/mu`, and define
the strengthened detector

```text
Q_{m,s}
  =
(P_m x Y_mu)^0 x T_2 x B_s(X).
```

Since `X` is a counterexample, `Q_{m,s}` still does not dominate `X`.  The
transparent Brunnian reduction and fixed-arity cofinality again give
unbounded arities with nontrivial detector-kernel all-meridian obstructions.

But the finite-image form above says:

```text
K_{m,s,n} cap Phi_{m,s,n}( union_{|T|<=s} F_T ) = 1.
```

Therefore every nontrivial obstruction element in the detector kernel has

```text
iw(g)>s.
```

In particular, every nontrivial monolith-generating element in the pairwise
or pairwise-core branch,

```text
g in K_{m,s,n} cap [N_{i,n},N_{j,n}]
```

or

```text
g in K_{m,s,n} cap intersection_{i<j}[N_{i,n},N_{j,n}],
```

has image support width greater than `s`.

Since `s` was arbitrary, a genuine cofinal pairwise/pairwise-core monolith
obstruction must have unbounded image support.

## What This Rules Out

The naive pairwise obstruction is dead:

```text
maybe a two-meridian commutator survives.
```

No.  Any detector-invisible element represented on a bounded set of
last-strand meridians is killed after adding the finite bounded-support rack
`B_s(X)`.

Thus a genuine pairwise obstruction must be a same-image support ghost: it
lies in a pairwise commutator or pairwise-core subgroup of the finite image,
but every bounded-support representative is either detector-visible or
`X`-trivial.

The central elementary abelian high-Brunnian mechanism can still exist as a
`p`-module phenomenon, but after the pairwise-core visibility correction it
also cannot be represented by bounded-support detector-kernel elements once
`B_s(X)` is included.

The remaining high-complexity targets are:

```text
unbounded-support pairwise/pairwise-core monolith ghosts,
```

or

```text
central elementary abelian high-Brunnian p-module ghosts,
also with unbounded detector-kernel image support.
```
