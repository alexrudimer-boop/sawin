# Review: Full-Deletion Ghost Collapse and Fixed-Depth Survival

Date: 2026-06-07

Verdict: C.

The response does not prove Sawin's finite-rack domination statement and does
not give a cofinal rack-prefix counterexample.  It gives proof-grade progress
on the same-image deletion ghost quotient:

1. the quotient formula from the Moore-coherent boundary is correct;
2. all same-image ghosts collapse to the true all-meridian commutator when
   every proper deletion is imposed;
3. bounded-depth same-image ghosts survive cofinally in finite p-group
   images;
4. therefore no detector-independent bounded-deletion collapse can prove
   Sawin domination.

## Formula Check

Let `phi:F_S -> G` be a surjection, let `R=ker phi`, let
`R_i=<<x_i>>_{F_S}`, and put

```text
D_S=[R_i | i in S]_Sigma.
```

For fixed deletion depth `a`, define

```text
A_a(phi)
  =
intersection_{T proper subset S, 1 <= |S\T| <= a}
epsilon_T^{-1}(R),
```

where `epsilon_T=iota_T d_T` deletes outside `T` and reinserts into `F_S`.
Then

```text
M_{S,a}(phi)=phi(A_a(phi)),
C_S=phi(D_S),
D_S <= A_a(phi),
```

and

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

With a detector obstruction `K` and skeletal supergroup `Sk_{S,q}^{(d)}`,
let

```text
H=phi^{-1}(K cap Sk_{S,q}^{(d)}).
```

Then

```text
K cap (Sk_{S,q}^{(d)} cap M_{S,a}(phi))=1
  iff
A_a(phi) cap H <= R.
```

This confirms the previous same-image deletion ghost formulation.

## Full-Deletion Collapse

Let `r=|S|`.  If deletion depth is full, `a=r-1`, then

```text
M_{S,r-1}(phi)=C_S
```

for every surjection `phi:F_S -> G`, finite or infinite.  Equivalently,

```text
A_{r-1}(phi) <= D_S ker(phi).
```

Proof idea.  Write `e_U` for deletion of the generators indexed by `U`.
The free Brunnian identity gives

```text
D_U=[R_i | i in U]_Sigma = intersection_{i in U} R_i.
```

For `w in A_{r-1}(phi)`, order `S={i_1,...,i_r}` and recursively define

```text
z_0=w,
z_t=z_{t-1} e_{i_t}(z_{t-1})^{-1}.
```

Every correction term has trivial `phi`-image because it is built from
proper deletion evaluations of `w`, all of which lie in `ker phi`.  The
recursive correction kills one deletion face at a time without reviving the
previously killed faces.  Hence `z_r` lies in

```text
intersection_{i in S} R_i = D_S,
```

and `phi(z_r)=phi(w)`.  Therefore `w in D_S ker(phi)`.

This shows that same-image ghosts are a bounded-depth phenomenon: they vanish
if all proper deletions are imposed.

## Face Confinement

For fixed `a`, if `w in A_a(phi)` and `U subset S` has `|U|<=a`, then

```text
w in D_U ker(phi),
```

so

```text
phi(w) in [N_i | i in U]_Sigma.
```

Consequently,

```text
M_{S,a}(phi)
  <=
intersection_{U subset S, 1 <= |U| <= a}
[N_i | i in U]_Sigma.
```

Thus a depth-`a` ghost must be simultaneously confined to every exact
small-support symmetric commutator of size at most `a`.  This confinement is
still weaker than membership in the full all-meridian subgroup when `|S|` is
unbounded and `a` is fixed.

## Fixed-Depth Finite-Image Survival

For every fixed `a>=1`, there are arbitrarily large finite sets `S`, finite
p-groups `G`, and surjections

```text
phi:F_S -> G
```

such that

```text
M_{S,a}(phi) != C_S.
```

In fact one can arrange `C_S=1` while `M_{S,a}(phi)` contains a nontrivial
element of order `p`.

Construction.  Put `k=a+1`, choose a prime `p>k`, and set `r=p+k`.  For every
`k`-element subset `A={i_1<...<i_k}` of `S={1,...,r}`, define the left-normed
commutator

```text
c_A=[...[ [x_{i_1},x_{i_2}],x_{i_3}],...,x_{i_k}].
```

Let

```text
w=product_{|A|=k} c_A
```

in a fixed order.  Work in the finite class-`k`, exponent-`p` nilpotent
quotient

```text
B=F_S/(F_S^p gamma_{k+1}(F_S)).
```

The `c_A` lie in the central layer `gamma_k(B)`, and distinct supports are
linearly independent in that layer.  Let `G` be the further quotient killing
all deletion products `e_U(w)` with `1<=|U|<=a`.

Then `w in A_a(phi)` by construction.  To see that `phi(w) != 1`, use the
linear functional on the span of the `c_A` with value `1` on each `c_A`.
For `|U|=u`,

```text
ell(e_U(w)) = binomial(r-u,k).
```

Since `r=p+k`, Lucas' theorem gives

```text
binomial(p+k-u,k) = 0 mod p       for 1<=u<=k-1,
```

but

```text
binomial(p+k,k) = 1 mod p.
```

Thus all killed deletion elements have zero `ell`, while `w` has nonzero
`ell`, so `w` survives in `G`.  Since `r>k`, the full symmetric commutator
`D_S` maps trivially to the class-`k` group `G`; hence `C_S=1`.

## Consequence

The same-image ghost quotient has a sharp detector-independent boundary:

```text
M_{S,|S|-1}(phi)=C_S
```

always, but for every fixed `a`,

```text
M_{S,a}(phi)/C_S
```

can be nontrivial cofinally in finite nilpotent images.

Therefore a positive proof of Sawin domination cannot come from a uniform
bounded-deletion collapse

```text
A_a(Phi_n) <= D_S ker(Phi_n).
```

Any successful proof through this boundary must use the actual rack detector
`Q=Y^0 x T_2` to kill

```text
K_n cap M_{S,a}(Phi_n)
```

or must construct a cofinal rack-prefix sequence in which such detector-
specific ghosts survive.  Detector-independent Moore/deletion structure,
finite image, bounded skeletal depth, and exact small-support confinement are
now known to be insufficient.
