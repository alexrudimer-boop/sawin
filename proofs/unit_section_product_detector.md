# Unit section and composite product detectors

## Purpose

The sharp obstruction theorem uses one finite detector group for a local
interval.  Branch proofs, however, often produce several finite transition
monoids: product-label monoids, normalized holonomy monoids, unit-holonomy
monoids, Green kernel-block monoids, and Schutzenberger monoids.  This note
records the formal step that turns separate unit-section or endpoint-composite
checks into one finite detector group.

## Statement

For finitely many finite transformation monoids `M_1,...,M_r`, let

```text
U_i = U(M_i)
```

be their unit/permutation groups and set

```text
G = U_1 x ... x U_r.
```

Suppose that, for a braid `beta`, each residual branch factorization in
`M_i` satisfies the unit-section detection criterion:

- its final residual branch map is a permutation;
- all section factors lie in `M_i`;
- every unit section factor lies in `V_beta(U_i)`.

Then the combined branch data is detected by the single finite group `G`.
In particular, if `Lambda_{G,n}(beta)=Lambda_{G,n}(1)`, then all branch
composites in all factors are identity.

The same product conclusion applies, and is often the preferred target, if
one uses the weaker endpoint criterion from
`proofs/unit_composite_longitude_criterion.md` in each factor: it is enough
that each final unit composite lies in `V_beta(U_i)`.  In that form, internal
section labels may telescope before the product detector readout.

## Proof

The direct-product longitude lemma gives

```text
V_beta(U_1 x ... x U_r)
  =
V_beta(U_1) x ... x V_beta(U_r).
```

Equivalently, the projection of the product detector's longitude-value
subgroup to the `i`-th factor is exactly `V_beta(U_i)`, and every tuple of
factor longitude values is realized in the product subgroup.  Therefore the
separate unit labels may be regarded as elements of one fixed product
subgroup in `G`.

If the finite-`G` longitude data of `beta` is identity, functoriality under
the projections `G -> U_i` forces identity finite-`U_i` longitude data in
each factor.  The unit-section detection criterion then kills each branch
composite.  Thus the whole finite list of unit-section readouts is killed by
one finite group `G`, independent of the braid index.

## Consequence For The Master Local Theorem

In the bi-free universal-corridor branch, it is legitimate to prove separate
factorizations through several fixed finite unit groups, provided the list of
groups is attached to the interval and quotient detector, not to `n`.  The
single local detector is their direct product, and the local rack is

```text
Q x A_G.
```

This avoids a common audit mistake: a proof may use many named factors for
readability, but it must not leave them as an `n`-dependent family.  Once the
factor list is finite and fixed, the direct product is the one group required
by the sharp obstruction theorem.

## Consequence For B

A counterexample cannot defeat this product step by saying that different
branch coordinates use different finite unit groups.  A normalized-law B
sequence must be eventually invisible to every finite product group as well,
and hence to the product of any finite list of unit groups extracted from the
interval.  The only remaining B route is a genuine all-finite-group escape
with residual motion surviving after all such fixed products are killed.

## Executable Audit

The section helper

```text
unit_section_product_detection_audit(monoids,n,beta,factor_words)
```

applies `unit_section_detection_audit(...)` to each factor.  When the direct
product of the unit groups is small enough to enumerate, it also checks the
identity

```text
V_beta(prod_i U_i) = prod_i V_beta(U_i).
```

When the product is too large, the helper marks the finite enumeration as
truncated; the symbolic product lemma still supplies the theorem-level
justification.

The endpoint helper

```text
unit_composite_product_detection_audit(monoids,n,beta,factor_words)
```

applies `unit_composite_detection_audit(...)` instead.  This is the executable
form to use when a branch proof supplies endpoint units after telescoping.  It
also records the actual product endpoint

```text
(h_1(beta),...,h_r(beta)) in prod_i U_i
```

and, when the product subgroup is enumerated, whether that endpoint tuple lies
in `V_beta(prod_i U_i)`.  Thus the audit witnesses the single-product
detector membership directly, not only through separate factor booleans.
It also exposes `is_finite_product_unit_detector_failure`, which marks the
finite warning case where the endpoint tuple is nonidentity despite identity
finite-longitude data in the listed unit factors.  This is not B unless it is
upgraded to an all-finite-group normalized-law sequence.

The endpoint audit now separates the exact product-group criterion from the
factorwise display:

```text
product_endpoint_lies_in_product_longitude_subgroup
identity_product_longitude_signature
identity_longitudes_kill_product_endpoint
proves_product_endpoint_detector_when_enumerated
```

The first flag is the direct membership statement in
`V_beta(prod_i U_i)`.  This is the condition required by the sharp
obstruction theorem.  The factorwise subgroup equality remains useful for
auditing that separate displayed factors really assemble as expected, but the
endpoint tuple is what the single product detector actually kills.  When the
product longitude signature is not identity, the implication is vacuous for
that fixed braid word; when it is identity, membership forces the endpoint
tuple to be the product identity.

When a proof supplies explicit endpoint longitude expressions rather than an
enumerated subgroup membership check, the helper

```text
unit_composite_product_longitude_expression_audit(...)
```

is the matching product certificate.  It checks each endpoint expression in
its fixed unit group and then builds the corresponding literal product
subgroup witness in the one product group.  Each witness letter records a
product-group assignment, a longitude index, and a sign; different letters may
use different assignments.  The audit records both the witness and
`product_witness_value`, and the product certificate is accepted only when
`product_witness_matches_endpoint` holds.  This is the preferred
non-enumerative form for an all-`n` proof because it displays the actual word
in `V_beta(prod_i U_i)` rather than relying on subgroup enumeration.

Tests cover:

- `C_2 x C_3` unit-section factors with full product subgroup;
- an identity-signature word where the product subgroup is trivial;
- a telescoped `C_2 x C_3` endpoint product where section membership fails
  but endpoint membership succeeds in the one product subgroup;
- product endpoint expression certificates for visible and identity-signature
  endpoints, including the explicit product subgroup witness value;
- a deliberately small product-order cap that skips enumeration without
  changing the symbolic conclusion.
