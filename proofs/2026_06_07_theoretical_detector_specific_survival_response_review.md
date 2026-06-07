# Review: Detector-Specific Brunnian Ghost Survival

Date: 2026-06-07

Verdict: C.

The response does not prove Sawin's finite-rack domination statement and does
not give a fixed finite non-rack counterexample.  It gives proof-grade
detector-specific survival in the opposite quantifier order: for every fixed
finite rack detector `Q`, there is a finite rack target `X_Q` and unbounded
braid indices where `Q` has nontrivial full-Brunnian ghosts on `X_Q`.

This is not a Sawin counterexample, because the target varies with the
detector and each `X_Q` is itself a rack.  It is still a useful no-go theorem:
no finite rack detector can be expected to annihilate all same-image deletion
ghosts uniformly across all finite rack targets.

## Formula Check

The same-image deletion ghost formulas remain correct.  For a surjection
`phi:F_S -> G`, `R=ker phi`, and

```text
A_a(phi)
  =
intersection_{T proper subset S, 1 <= |S\T| <= a}
epsilon_T^{-1}(R),
```

with `R_i=<<x_i>>_{F_S}` and

```text
D_S=[R_i | i in S]_Sigma,
```

one has

```text
M_{S,a}(phi)/C_S
  ~= A_a(phi)R / D_S R
  ~= A_a(phi)/(A_a(phi) cap D_S R).
```

Thus

```text
M_{S,a}(phi)=C_S
  iff
A_a(phi) <= D_S R.
```

For a detector obstruction `K` and skeletal supergroup `Sk`, with
`H=phi^{-1}(K cap Sk)`,

```text
K cap (Sk cap M_{S,a})=1
  iff
A_a(phi) cap H <= R.
```

The full-deletion collapse and bounded-depth face confinement from the
previous review are also compatible, with the convention `U != empty` in the
face confinement statement.

## Theorem

Let `Q` be a finite rack and define

```text
e(Q)=ord(rho^Q_2(sigma_1^2)).
```

Choose an odd prime `ell>=5` not dividing `e(Q)`, and let

```text
G=A_ell,
X_Q=Conj(G),
```

the conjugation rack `a*b=aba^{-1}`.

For every `r>=2`, put `n=r+1` and let

```text
F_r=ker(d_n:P_n -> P_{n-1})=<x_1,...,x_r>,
x_i=A_{i,n}.
```

Define the left-normed powered Brunnian word

```text
w_r=[...[ [x_1^{e(Q)},x_2^{e(Q)}],x_3^{e(Q)}],...,x_r^{e(Q)}].
```

Then

```text
rho^Q_n(w_r)=1
```

but

```text
rho^{X_Q}_n(w_r) != 1
```

for every `r>=2`.  Moreover, every proper deletion of `w_r` is already
trivial in the free group.  Therefore, for the combined image

```text
Phi_n=(rho^Q_n,rho^{X_Q}_n),
```

one has a nontrivial element

```text
Phi_n(w_r) in K_n cap C_n.
```

Thus the ghost lies in the full symmetric commutator layer, not merely in a
bounded-depth Moore approximation.

## Proof Sketch

All pure generators `A_{i,n}` are braid-conjugate to a square of an elementary
braid generator.  Therefore their `Q`-actions have order dividing `e(Q)`, so
each `x_i^{e(Q)}` acts trivially on `Q^n`; hence the commutator word `w_r`
acts trivially on `Q^n`.

The word is Brunnian because deleting any generator turns one commutator input
into `1`.  Since `x_i^{e(Q)} in <<x_i>>`, the word lies in

```text
D_S=[R_i | i in S]_Sigma.
```

To see that the conjugation rack sees it, let

```text
V={g^{e(Q)}:g in A_ell}.
```

Because `ell` does not divide `e(Q)`, an `ell`-cycle has nontrivial
`e(Q)`-th power.  Thus `V` is a nontrivial conjugacy-invariant subset of the
simple group `A_ell`, so it generates `A_ell`.  Since `A_ell` is centerless,
one can recursively choose `v_i in V` such that

```text
c_r=[...[ [v_1,v_2],v_3],...,v_r] != 1
```

for all `r`: if `c_{r-1} != 1`, choose `v_r` outside its proper centralizer.
Pick `g_i` with `g_i^{e(Q)}=v_i`.

For the conjugation rack, the Artin/Hurwitz point-pushing action of
`F_r=ker(P_{r+1}->P_r)` conjugates the last coordinate by the evaluated word
in the first `r` coordinates.  Evaluating `x_i` at `g_i`, the word `w_r`
evaluates to the noncentral element `c_r`.  Choose the last color `h` not
commuting with `c_r`; then `w_r` changes the last coordinate.  Hence
`rho^{X_Q}_n(w_r)` is nontrivial.

## Rack-Prefix Consequence

For any finite rack prefix `P_m`, set

```text
Q_m=P_m^0 x T_2.
```

Applying the theorem to `Q_m` gives a finite rack

```text
X_m=Conj(A_{ell_m})
```

and unbounded indices `n=r+1` with Brunnian words `w_{m,r}` satisfying

```text
rho^{Q_m}_n(w_{m,r})=1,
rho^{X_m}_n(w_{m,r}) != 1.
```

This is a cofinal rack-prefix diagonal mechanism in the varying-target sense:
each finite prefix misses some finite rack target outside the prefix.

It is not a Sawin counterexample.  A true negative answer needs one fixed
finite YBE solution `X` such that every rack prefix misses `X` at some
unbounded arity.  Here the target `X_m` changes with the prefix and is itself
a rack.

## Consequence

The theorem rules out any proof strategy that tries to find one finite rack
detector annihilating all full-Brunnian ghosts for all finite rack targets.
The quantifier order is the point:

```text
for every detector Q, there exists a rack target X_Q with ghosts.
```

Sawin's positive statement asks for the different target-specific quantifier
order:

```text
for every fixed finite YBE target X, there exists a detector Q_X.
```

The active prompt must therefore force the next response to address
target-specific detector construction or a fixed-target cofinal obstruction.
