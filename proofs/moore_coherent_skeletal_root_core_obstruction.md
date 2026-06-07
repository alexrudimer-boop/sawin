# Moore-Coherent Skeletal Root-Core Obstruction

Date: 2026-06-07

This note records the next C-type sharpening of the finite-image obstruction
for Sawin's finite-rack domination problem.  It does not prove Sawin's
statement and does not provide a cofinal counterexample.  Its contribution is
to add a lift-level deletion-coherence condition to the q-skeletal recursive
root-core target.

The key point is that an actual all-meridian/Brunnian obstruction is not only
an element of subgroup-level skeletal approximations inside a finite image.  It
has a single lift to the last-strand free group whose deleted evaluations are
trivial.  Different representatives for different deletions are not enough.

## Setup

Let `S={1,...,r}` and let

```text
phi:F_S -> G
```

be a surjection from the free group `F_S=<x_i | i in S>` onto a group `G`.
Put

```text
N_i=<<phi(x_i)>>_G.
```

For `T subset S`, let

```text
d_T:F_S -> F_T
```

delete the generators outside `T`, and let

```text
iota_T:F_T -> F_S
```

be the natural inclusion.  Define the same-image deletion evaluation

```text
partial_T^phi = phi iota_T d_T : F_S -> G.
```

For `a>=1`, define the a-deletion Moore image

```text
M_{S,a}(phi)
  =
phi(
  intersection_{T proper subset S, 1 <= |S\T| <= a}
  ker partial_T^phi
).
```

In particular, `M_{S,1}(phi)` consists of finite-image elements admitting a
single lift whose every one-generator deletion evaluates trivially in the same
finite image.

Let `Sk_{S,q}^{(d)}(G;N_i)` denote the q-skeletal recursive root-core from
`q_skeletal_root_core_finite_image_obstruction.md`.  Define the
Moore-coherent q-skeletal root-core by

```text
MSk_{S,q,a}^{(d)}(phi)
  =
Sk_{S,q}^{(d)}(G;N_i) cap M_{S,a}(phi).
```

## Moore-Coherent Narrowing

For every `q>=3`, `d>=0`, and `a>=1`,

```text
C_S=[N_i | i in S]_Sigma
  <=
MSk_{S,q,a}^{(d)}(phi)
  <=
Sk_{S,q}^{(d)}(G;N_i).
```

Also, if `a' >= a`, then

```text
MSk_{S,q,a'}^{(d)}(phi)
  <=
MSk_{S,q,a}^{(d)}(phi).
```

Proof.  Let

```text
tilde N_i=<<x_i>>_{F_S}
```

and

```text
tilde C_S=[tilde N_i | i in S]_Sigma.
```

Since `phi` is surjective and maps `tilde N_i` onto `N_i`, it maps
`tilde C_S` onto `C_S`.

Every generator of `tilde C_S` is a fully parenthesized commutator with one
input from each `tilde N_i`.  If `T` is a proper subset of `S`, then deleting
all labels outside `T` kills at least one required input, so the deleted word
is trivial.  Hence

```text
tilde C_S
  <=
intersection_{T proper subset S, 1 <= |S\T| <= a}
ker partial_T^phi.
```

Applying `phi` gives

```text
C_S <= M_{S,a}(phi).
```

The q-skeletal theorem gives `C_S <= Sk_{S,q}^{(d)}`, so

```text
C_S <= Sk_{S,q}^{(d)} cap M_{S,a}(phi).
```

The remaining containments follow immediately from the definitions.

## Finite-Image Consequence

In the Sawin finite-image setup, take

```text
F_{n-1}=<x_i=A_{i,n} | 1<=i<=n-1>,
Phi_n:F_{n-1}->Gamma_n<=Sym(Q^n)xSym(X^n),
N_{i,n}=<<Phi_n(x_i)>>_{Gamma_n}.
```

Write

```text
MSk_{n,q,a}^{(d)}
  =
MSk_{{1,...,n-1},q,a}^{(d)}(Phi_n).
```

Since

```text
C_n <= MSk_{n,q,a}^{(d)},
```

a finite rack detector `Q=Y^0 x T_2` dominates `X` if there are fixed
integers `q>=3`, `d>=0`, and `a>=1` such that

```text
K_n cap MSk_{n,q,a}^{(d)} = 1
```

for all sufficiently large `n`, after adding fixed-arity rack detectors for
the remaining small arities.

The relative quotient version is identical.  If `Z` is a dominated braided
quotient of `X`, with

```text
G_n^X=rho_n^X(F_{n-1}),
E_n=ker(G_n^X -> G_n^Z),
psi_n:F_{n-1}->G_n^X,
```

then it is enough to prove fixed `q,d,a` with

```text
E_n cap MSk_{n,q,a}^{X,(d)} = 1
```

for all sufficiently large `n`.

## Interpretation

This is a strict conceptual narrowing of the q-skeletal target:

```text
K_n cap Sk_{n,q}^{(d)} = 1
```

can be replaced by

```text
K_n cap MSk_{n,q,a}^{(d)} = 1.
```

The new term remembers that a true obstruction comes from one lift whose
deleted evaluations vanish in the same finite image.  Subgroup-level tests
alone can admit elements that pass each deletion test using incompatible
representatives.

The response also supplied a finite p-group strictness model showing
`MSk < Sk` can occur.  That model is useful evidence that the refinement is
not merely notational, but it is not a YBE counterexample.

## Remaining Problem

The current exact positive target is:

```text
For every finite bijective YBE solution X, find a finite rack detector
Q=Y^0 x T_2 and fixed q,d,a such that

  K_n cap MSk_{n,q,a}^{(d)} = 1

for all sufficiently large n.
```

The exact negative target is:

```text
Construct a finite bijective solution X such that for every finite rack
prefix P_m there are unbounded n_m and nontrivial elements

  gamma_m in K_{n_m} cap C_{n_m},

hence gamma_m also lies in every fixed Moore-coherent skeletal target
K_{n_m} cap MSk_{n_m,q,a}^{(d)} once n_m is large enough.
```

No current artifact proves either target.
