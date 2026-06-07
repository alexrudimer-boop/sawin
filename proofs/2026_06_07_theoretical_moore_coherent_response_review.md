# Review: Theoretical Moore-Coherent Response

Date: 2026-06-07

Verdict: C.

The response does not prove Sawin's finite-rack domination statement and does
not give a cofinal rack-prefix counterexample.  It gives proof-grade progress
on the current Moore-coherent boundary:

1. the Moore-coherent containment is correct;
2. the exact remaining obstruction is a same-image deletion ghost quotient;
3. the existential Moore target is equivalent to Sawin domination when the
   detector is allowed to vary;
4. Moore coherence alone does not force vanishing, because perfect
   point-pushing commutators survive cofinally against weak detectors even in
   finite rack examples.

## Moore Containment

Let `S` be finite, let `F_S=<x_i | i in S>`, and let

```text
phi:F_S -> G
```

be a surjection.  Put

```text
N_i=<<phi(x_i)>>_G.
```

For `T subset S`, write

```text
partial_T^phi = phi iota_T d_T : F_S -> G.
```

Let

```text
M_{S,a}(phi)
  =
phi(
  intersection_{T proper subset S, 1 <= |S\T| <= a}
  ker partial_T^phi
).
```

Then

```text
C_S=[N_i | i in S]_Sigma <= M_{S,a}(phi).
```

Proof sketch.  Let `R_i=<<x_i>>_{F_S}`.  Since `phi` is surjective,
`phi(R_i)=N_i`.  A generator of `C_S` is the `phi`-image of a fully
parenthesized commutator with one input from each `R_i`.  Deleting any proper
subset kills at least one required input, hence kills the whole commutator
before applying `phi`.  Applying `phi` gives the containment.

Therefore

```text
C_S <= MSk_{S,q,a}^{(d)}(phi)
     = Sk_{S,q}^{(d)} cap M_{S,a}(phi).
```

## Same-Image Deletion Ghost Quotient

Let

```text
R=ker phi,
epsilon_T=iota_T d_T:F_S -> F_S,
```

and

```text
A_a(phi)
  =
intersection_{T proper subset S, 1 <= |S\T| <= a}
epsilon_T^{-1}(R).
```

Then

```text
M_{S,a}(phi)=phi(A_a(phi)).
```

Let

```text
D_S=[R_i | i in S]_Sigma,
R_i=<<x_i>>_{F_S}.
```

Since `C_S=phi(D_S)` and `D_S<=A_a(phi)`,

```text
M_{S,a}(phi)/C_S
  ~= A_a(phi)R / D_S R
  ~= A_a(phi)/(A_a(phi) cap D_S R).
```

Thus the exact collapse criterion is

```text
M_{S,a}(phi)=C_S
  iff
A_a(phi) <= D_S R.
```

For a detector obstruction, let

```text
H=phi^{-1}(K cap Sk_{S,q}^{(d)}).
```

Then

```text
K cap MSk_{S,q,a}^{(d)}
  = phi(A_a(phi) cap H),
```

and therefore

```text
K cap MSk_{S,q,a}^{(d)}=1
  iff
A_a(phi) cap H <= R.
```

Equivalently, the obstruction is a word `w in F_S` satisfying:

```text
epsilon_T(w) in ker phi       for all relevant deletions T,
phi(w) in K cap Sk_{S,q}^{(d)},
phi(w) != 1.
```

This is the precise same-image deletion ghost.

## Equivalence With Sawin Domination

The existential Moore target is equivalent to Sawin domination.

If a detector `Q=Y^0 x T_2` and fixed `q,d,a` satisfy

```text
K_n cap MSk_{n,q,a}^{(d)}=1
```

eventually, then `C_n<=MSk_{n,q,a}^{(d)}` gives `K_n cap C_n=1`
eventually.  The Brunnian finite-image theorem and fixed-arity rack cofinality
then give one finite rack dominating `X`.

Conversely, if a finite rack detector already dominates `X`, then in the
combined image `Gamma_n<=Sym(Q^n)xSym(X^n)` any element in `K_n` has trivial
`Q`-action and hence trivial `X`-action.  Since the two projection kernels
intersect trivially, `K_n=1`, so the Moore target holds for every `q,d,a`.

Thus the Moore target is not formally weaker than Sawin's problem.  Its value
is diagnostic: it identifies the exact ghost quotient that a proposed
detector must kill.

## Survival Against Weak Detectors

Moore coherence alone does not imply vanishing.

Let `P=A_5` and let `X=P` with the conjugation rack operation

```text
a*b = a b a^{-1}.
```

Take the weak detector `Q=T_2`.  Its braid action factors through the
symmetric group, so pure braids are `Q`-invisible.

For `n=r+1`, let `F_r=ker(d_n:P_n->P_{n-1})` with generators
`x_i=A_{i,n}`.  Define the left-normed commutator

```text
c_2=[x_1,x_2],
c_{j+1}=[c_j,x_{j+1}].
```

The braid `beta_n=c_r(A_{1,n},...,A_{r,n})` is ordinary Brunnian, so it is
`Q`-invisible.

Under the point-pushing/Artin interpretation of the conjugation rack, this
braid conjugates the last coordinate by the value of `c_r` on the first `r`
coordinates.  Because `A_5` is centerless and perfect, one can choose
`g_1,...,g_r` recursively so that

```text
h_r=c_r(g_1,...,g_r) != 1,
```

then choose `g_n` not commuting with `h_r`.  Hence `beta_n` moves
`(g_1,...,g_r,g_n)` in `X^n`.

Therefore

```text
Phi_n(beta_n) in K_n cap C_n
```

is nontrivial, and hence lies in

```text
K_n cap MSk_{n,q,a}^{(d)}
```

for every fixed `q,d,a` once `n` is large enough.

This is not a Sawin counterexample because `X` itself is a rack and therefore
dominates itself.  It does show that any positive proof must use the detector
`Q` in an essential way; Moore coherence, finite image, and bounded skeletal
depth do not by themselves kill perfect point-pushing ghosts.

## Remaining Target

The next prompt should no longer ask merely for Moore coherence.  It should
ask for detector-specific annihilation of the same-image deletion ghost:

```text
A_a(Phi_n) cap Phi_n^{-1}(K_n cap Sk_{n,q}^{(d)})
  <=
ker Phi_n
```

eventually, for a detector constructed from `X`, or for an explicit finite
`X` proving cofinal survival against every finite rack prefix.
