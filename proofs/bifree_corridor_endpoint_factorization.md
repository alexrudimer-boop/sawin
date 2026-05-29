# Bi-free corridor endpoint factorization

Date: 2026-05-29

This note performs the proof-side assembly step for the remaining
`bi_free_universal_corridor_bottleneck` branch.  It does not prove the Master
Local-Minimal Residual Theorem.  It proves the algebraic reduction from
factorwise endpoint-longitude expressions to the single fixed finite detector
implication required by the sharp obstruction theorem.

The remaining all-`n` work is therefore narrowed to one concrete construction:
in every target interval, display each residual Green/corridor group-like
endpoint as a finite product of evaluated recursive Artin longitudes in the
fixed detector factors attached to that interval.

## Setup

Fix a local-minimal interval

```text
pi : X -> Z
```

over a quotient solution `Z` dominated by a finite rack `Q`.  Let

```text
N_n = ker rho_{Q,n}.
```

For `z in Z^n`, write

```text
X_z = product_i pi^{-1}(z_i)
```

and let

```text
delta_{n,z}: N_n -> Sym(X_z)
```

be the residual action.

Assume the interval has reached the verdict

```text
bi_free_universal_corridor_bottleneck.
```

Thus the semisplit and local-minimality gates have passed, no closed product or
known whole-solution finite-`G` branch applies, and the output coordinate-kernel
closure is universal rather than equality.

Let

```text
H(pi,Q) = product_s H_s
```

be the finite detector product specified in
`proofs/bifree_universal_corridor_factorization_target.md`: two-sided symmetric
Green kernel-block groups, two-sided Schutzenberger groups, atom-quotient inner
groups whenever the atom quotient is rack-like, quotient detector factors from
`Q`, known branch factors that remain after quotienting, and fixed endpoint/unit
detector factors.  The product is fixed by the interval and quotient detector;
it has no braid-index parameter.

## Endpoint-longitude expression hypothesis

For a braid `beta in N_n`, an endpoint factor is a finite group element

```text
h_e(beta,z,x) in H_s
```

arising from one residual readout component: a Green kernel-block coordinate, a
Schutzenberger coordinate, a rack-like atom quotient coordinate, or a lower
endpoint/unit coordinate in a fixed finite unit group.

The endpoint has a longitude expression in `H_s` if there are:

- an assignment `phi_e:F_n -> H_s`;
- indices `i_1,...,i_r` in `{1,...,n}`;
- signs `epsilon_m in {+1,-1}`;

such that

```text
h_e(beta,z,x) =
  phi_e(L_{i_1}(beta))^{epsilon_1}
  ...
  phi_e(L_{i_r}(beta))^{epsilon_r}
```

inside `H_s`, where `L_i(beta)` are the recursive Artin longitudes.

The assignment and the word may depend on `n`, `beta`, `z`, the input fibre tuple
`x`, the output coordinate, and finite corridor state.  The target group `H_s`
may not depend on `n`.

This is exactly the certificate format of
`proofs/endpoint_longitude_expression_certificate.md`, specialized to the fixed
factors of `H(pi,Q)`.

## Lemma 1: factor expressions lift to one product detector

Lemma.  Suppose finitely many endpoint factors

```text
h_e(beta,z,x) in H_{s(e)}
```

have endpoint-longitude expressions in their respective fixed factors of
`H(pi,Q)`.  Then the tuple of these endpoint factors has a literal subgroup
witness in

```text
V_beta(H(pi,Q)).
```

Equivalently, after embedding each `h_e` into the corresponding direct-product
coordinate, the product of the embedded endpoint factors belongs to the
longitude-value subgroup of the single finite group `H(pi,Q)`.

Proof.  Write

```text
H = H_1 x ... x H_m.
```

For one expression in the factor `H_s`, extend its assignment

```text
phi:F_n -> H_s
```

to a product assignment

```text
Phi:F_n -> H
```

by putting `phi` in coordinate `s` and the identity homomorphism in all other
coordinates.  Then for every Artin longitude,

```text
Phi(L_i(beta)) = (1,...,1, phi(L_i(beta)), 1,...,1).
```

Therefore the embedded expression is literally a word in generators of
`V_beta(H)`.  Multiplying the embedded expressions for all endpoint factors
still gives a word in the same subgroup, because `V_beta(H)` is a subgroup.
This is the certificate-level direct-product argument used by
`direct_product_longitude_subgroup_witness(...)`; no enumeration of the product
subgroup is needed.  QED.

## Lemma 2: identity product longitudes kill endpoint readouts

Lemma.  If

```text
Lambda_{H(pi,Q),n}(beta)=Lambda_{H(pi,Q),n}(1),
```

then every endpoint factor satisfying the expression hypothesis is identity.

Proof.  Project the equality of finite-`H` longitude data to a factor `H_s`.
Every recursive longitude evaluates to the identity in `H_s` under every
assignment `F_n -> H_s`: any such assignment is the `s`-projection of a product
assignment into `H` with identity assignments in all other coordinates.  Hence

```text
V_beta(H_s) = {1}.
```

By the endpoint expression hypothesis, `h_e(beta,z,x)` lies in `V_beta(H_s)`,
so `h_e(beta,z,x)=1`.  QED.

## Lemma 3: rack-like atom factors are already endpoint expressions

Lemma.  Suppose the Green atom quotient, saturated or descent-closed, is a total
finite rack-like layer with inner group

```text
G_A <= Sym(A).
```

Then identity finite-`G_A` longitude data fixes the atom tuple of every residual
readout.

Proof.  The atom layer has crossing

```text
R_A(A_0,A_1) = (A_1, A_0^A_1),
```

so it is a finite right-rack layer.  The standard rack longitude factorization
uses the input-dependent assignment

```text
x_i |-> right translation by the i-th input atom
```

into `G_A`.  Therefore the atom output coordinates are evaluations of recursive
Artin longitudes in `G_A`.  If the finite-`G_A` longitude data is identity, all
those evaluations are identity and the atom tuple is fixed.  QED.

This is the atom-coordinate part of the Green atom-rack lift criterion.  Any
information lost below a descent-closed atom quotient is not handled here; it
must appear as lower endpoint/unit data covered by Lemmas 1 and 2.

## Endpoint factorization criterion

The following statement is the usable proof target for the remaining corridor
branch.

Proposition.  Fix a target interval and its detector product `H=H(pi,Q)`.
Assume that for every braid index `n`, every `beta in N_n`, every base tuple
`z in Z^n`, every fibre tuple `x in X_z`, and every residual output coordinate,
the residual Green/corridor readout decomposes into finitely many components of
the following three kinds:

1. rack-like atom quotient actions through finite atom inner groups included in
   `H`;
2. known quotient or closed-branch detector actions through fixed finite factors
   included in `H`;
3. group-like Green, Schutzenberger, or lower endpoint/unit elements that have
   endpoint-longitude expressions in fixed factors of `H`.

Assume also that the readout is faithful in the following minimal sense: if all
components in this finite decomposition are identity, then the corresponding
residual output coordinate equals the input coordinate.

Then

```text
Lambda_{H,n}(beta)=Lambda_{H,n}(1)
    => delta_{n,z}(beta)(x)=x
```

for all `n`, `beta`, `z`, and `x`.  Hence the target interval is detected by
the sharp rack factor

```text
Q x A_H.
```

Proof.  Let `beta,z,x` be fixed and assume
`Lambda_{H,n}(beta)=Lambda_{H,n}(1)`.

Projection from `H` to each atom inner group gives identity finite-longitude
data in that atom group, so Lemma 3 fixes every rack-like atom component.
Projection from `H` to every known quotient or closed-branch detector factor
kills the corresponding component by the already proved detector implication
for that branch.  Projection from `H` to each Green, Schutzenberger, or lower
unit factor kills every endpoint expression by Lemma 2.

All components in the faithful residual readout are now identity.  Therefore the
chosen output coordinate is fixed.  The coordinate, input tuple, base tuple,
braid, and braid index were arbitrary, so `delta_{n,z}(beta)` is the identity
permutation for every `z`.  Thus the bundled residual action `Delta_n(beta)` is
identity, and the sharp obstruction theorem supplies the finite rack detector
`Q x A_H`.  QED.

## Equivalent single-line theorem burden

The proposition shows that the remaining A route is not to find larger and
larger fixed-index images.  It is the following uniform lemma.

```text
Endpoint longitudinalization lemma.
In every local-minimal interval with verdict
bi_free_universal_corridor_bottleneck, every group-like atom-trivial
Green/corridor completed-context endpoint arising from a residual braid action
has an endpoint-longitude expression in a fixed factor of H(pi,Q), compatibly
with the finite readout decomposition above.
```

If this lemma is proved, the proposition closes the local interval.  Congruence
chain induction then multiplies the resulting local detector groups into the
global finite rack promised by outcome A.

If this lemma fails, the failure is not yet outcome B.  A B route must extract
from the failure an explicit local-minimal target interval and a normalized-law
sequence whose endpoint units remain nonidentity while every finite group has
identity recursive Artin-longitude data.

## Factor-by-factor audit checklist

A proof of the endpoint longitudinalization lemma should supply the following
factor checks.

1. Kernel-block factors.  For each left and right Green kernel-block quotient,
   the induced residual block permutation must be displayed as a product of
   recursive-longitude evaluations in the fixed symmetric group on that block
   quotient.
2. Schutzenberger factors.  For each regular Green class, the residual
   Schutzenberger coordinate must either be killed by the atom quotient or be
   displayed as an endpoint-longitude expression in the fixed Schutzenberger
   action group.
3. Atom quotient factors.  Once descent is total, the atom tuple is a finite
   rack-like layer and is handled by the inner group.  Nontrivial
   descent-closed coarsening pushes only the lost lower information to the
   endpoint/unit factors.
4. Lower unit factors.  Every remaining lower section or endpoint composite
   must be a unit in one fixed finite monoid and must have an
   endpoint-longitude expression in that monoid's unit group.
5. Product assembly.  The preceding four items may use separate finite factors,
   but Lemma 1 assembles all factor witnesses into one product detector
   `H(pi,Q)`.  No step may introduce a detector depending on `n`.

This checklist is deliberately stronger than a finite subgroup-membership audit
at one braid index.  It asks for the symbolic expressions that make the
subgroup membership true uniformly in `n`.
