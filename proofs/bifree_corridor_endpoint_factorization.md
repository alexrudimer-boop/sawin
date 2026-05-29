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

## Artin-defect refinement

The follow-up note
`proofs/artin_defect_longitudinalization_sieve.md` gives a sharper sufficient
form for the missing endpoint expressions.  It proves that every Artin
permutation defect

```text
beta(w) p_beta(w)^-1
```

lies in the normal closure of the recursive Artin longitudes, and that every
finite-group value of such a defect belongs to `V_beta(G)`.  Hence it is
enough, and now preferred, to display each remaining elementary group-like
endpoint as a finite product of evaluated Artin permutation defects in one of
the fixed factors of `H(pi,Q)`.  Such a display automatically supplies the
longitude-subgroup witness required by Lemmas 1 and 2 above.  This refinement
still does not prove the local theorem; it specifies the narrower all-`n`
identity that remains to be proved for Green kernel-block, Schutzenberger,
atom-inner, and lower endpoint/unit generators.
The atom-inner part of this list is now handled by
`proofs/atom_inner_detector_lift_rows.md` once atom descent and totality are
available: rack-like atom quotient inner groups satisfy the detector-lift rows
automatically.  The unresolved endpoint identities are therefore concentrated
in Green kernel-block, Schutzenberger, and lower endpoint/unit holonomy
generators.
The Green kernel-block and Schutzenberger generators have now been compressed
to the first-output defect endpoint in
`proofs/green_first_output_defect_criterion.md`.  That note shows that the
second output has no separate obstruction and that kernel-block defects are
Schutzenberger pushforwards in the globally realized case.  The follow-up
`proofs/green_defect_kernel_quotient_detection.md` kills the non-defect
quotient `U_C/Def_C` by detector-lift.  The remaining Green endpoint to
longitudinalize is the transported finite defect-kernel product
`D_C(beta) in Def_C`.  The potential-coboundary refinement
`proofs/green_defect_potential_coboundary.md` proves each elementary defect is
`eta(q^a)eta(q)^-1`; therefore the finite Green check left for endpoint
longitudinalization is whether this `Def_C`-valued potential is principal for
the Artin detector transport.  The abelianization guardrail
`proofs/artin_defect_abelianization_barrier.md` rules out the too-strong
version where every elementary defect is an Artin permutation defect product:
Artin permutation defects land in `[Def_C,Def_C]`, but audited defect kernels
may have nontrivial abelian defect rows.  The endpoint proof must therefore
first handle the finite abelian quotient `Def_C/[Def_C,Def_C]`, as separated
in `proofs/green_defect_abelianization_split.md`.  The finite abelian
subgroup itself is computed exactly by
`proofs/abelian_longitude_image_criterion.md`: it is generated by the
`a^{m_ij}` values coming from the abelianized recursive-longitude matrix.
Only after that layer is handled may any remaining endpoint be reduced to
commutator-level methods.
The balanced refinement
`proofs/green_balanced_defect_gauge_decomposition.md` then shows that a raw
Green/Schutzenberger first-output defect is an Artin-visible commutator times
a conjugated inverse second-output gauge.  Therefore the genuinely remaining
Green/Schutzenberger endpoint is terminal gauge holonomy, which belongs with
the lower endpoint/unit factors in the product detector.
The terminal gauge certificate itself is isolated in
`proofs/terminal_gauge_longitudinalization_criterion.md`: chart labels
`g_0,...,g_t` produce gauge increments `s_k=g_k g_{k-1}^-1` that telescope to
`g_t g_0^-1`, and this endpoint is then handled by the same longitude
expression/product witness machinery as any other endpoint factor.
The principal gauge subcase is closed by
`proofs/principal_gauge_extension_detector.md`: a lower row
`(a,r)*(b,s)=(a*b,c(a,b)s)` is a finite rack extension exactly when `c`
satisfies the nonabelian rack-cocycle law, and then the fixed group
`Inn(A x U)` supplies the detector-lift factor.
The transport-state refinement
`proofs/transport_state_rackification_detector.md` removes principality for
strand-continuing rows: the finite state `(a,r)` is itself the rack element,
so `Inn(A x E)` detects any bijective YBE row
`((a,r),(b,s))->((a*b,F_{a,b,r}(s)),(a,r))`.

## Executable certificate layer

The group-only certificate helpers implementing Lemmas 1 and 2 are:

```text
endpoint_longitude_expression_audit(
    group,n,beta,endpoint,assignment,expression
)

endpoint_product_longitude_expression_audit(
    groups,n,beta,endpoints,assignments,expressions
)

endpoint_coordinate_readout_audit(
    endpoint_audit,input_coordinate,output_coordinate
)

endpoint_residual_readout_audit(coordinate_audits)

endpoint_residual_action_audit(
    n,beta,residual_readouts,expected_row_count=None
)

endpoint_artin_defect_audit(
    group,n,beta,endpoint,terms
)

endpoint_product_artin_defect_audit(
    groups,n,beta,endpoints,terms_by_factor
)
```

The first helper checks one displayed endpoint expression in a fixed finite
group.  The second helper embeds the factor expressions into the direct product
and evaluates the literal product witness in `V_beta(product_s H_s)`, using
identity assignments in all non-active coordinates.  Its flags

```text
product_endpoint_lies_in_product_longitude_subgroup_by_expression
identity_longitudes_kill_product_endpoint_by_expression
```

record exactly the two proof-side facts used above: the endpoint tuple has a
non-enumerative product-subgroup witness, and identity finite product-longitude
data kills it.  The tests in `tests/test_endpoint_factorization.py` cover
visible endpoints, identity-signature endpoints, bad expressions, and malformed
parallel data.

The readout helpers implement the last line of the proposition for finite
certificate rows.  A coordinate row records whether an identity endpoint tuple
really fixes the residual output coordinate.  A residual row bundles these
coordinate checks and records whether identity finite product-longitude data
kills the whole residual tuple by expression.  These are still row-level proof
objects: a complete corridor proof must construct such faithful readout rows
uniformly for every `n`, `beta`, `z`, `x`, and output coordinate.
The residual-action helper bundles the supplied residual rows for one braid
word.  It checks that all endpoint certificates use the same braid data, that
identity finite product-longitude data kills every supplied row, and, when an
`expected_row_count` is supplied, that the displayed row table has the claimed
size.  This is still not a finite-search proof of the corridor theorem: the
all-`n` proof must explain why the supplied rows cover every relevant
`(z,x)` uniformly.
The Artin-defect helpers verify the refined certificate form: each supplied
term is a value of `beta(w)p_beta(w)^-1` under an input-dependent assignment,
and the helper constructs the corresponding literal word in `V_beta(G)` by
absorbing normal conjugators into changed assignments.
The detector-lift helpers in
`proofs/artin_detector_lift_criterion.md` verify a different sufficient route:
finite local rows carrying live-strand pairs `(m,u)` match the active
`G x G` Artin detector update.  Once those row identities hold, the global
braid induction gives terminal `u`-labels equal to evaluated recursive
longitudes, so the older endpoint expression helpers can be applied directly.
For rack-like atom quotient factors this finite row check is automatic after
descent; the executable hooks are `rack_inner_detector_lift_audit(...)`,
`right_rack_inner_detector_lift_audit(...)`, and
`atom_quotient_inner_detector_lift_audit(...)`.
For Green kernel-block and Schutzenberger factors, the corresponding
normal-form hooks are `schutzenberger_first_output_defect_audits(...)`,
`kernel_block_first_output_defect_audits(...)`, and
`schutzenberger_kernel_defect_pushforward_audits(...)`.

These helpers do not produce the missing endpoint expressions.  They verify the
last algebraic and faithful-readout steps once a symbolic corridor proof has
supplied those expressions in the fixed factors of `H(pi,Q)`.
