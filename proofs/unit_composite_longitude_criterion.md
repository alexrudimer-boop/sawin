# Unit composite longitude criterion

## Purpose

The unit-section criterion is intentionally strong: it asks every unit factor
in a residual section word to lie in `V_beta(U(M))`.  A real corridor proof
may telescope internally, so this note records the weaker endpoint condition
that is actually needed by the sharp obstruction theorem.

## Criterion

Let `M` be a finite transformation monoid on a finite set and let `U(M)` be
its unit/permutation group.  Fix `beta in B_n` and suppose a residual branch
map is represented in `M` by a word

```text
h_beta = f_k ... f_1.
```

Assume:

1. every `f_i` belongs to the fixed monoid `M`;
2. the final branch map `h_beta` is a permutation, hence an element of
   `U(M)`;
3. the endpoint unit `h_beta` lies in the longitude-value subgroup

```text
V_beta(U(M)) =
< phi(L_i(beta)) : phi:F_n -> U(M), 1 <= i <= n >.
```

Then identity finite-`U(M)` longitude data for `beta` forces
`h_beta=1`.

Proof.  If `Lambda_{U(M),n}(beta)=Lambda_{U(M),n}(1)`, then the Artin
permutation is trivial and every recursive longitude evaluates to the
identity under every homomorphism `F_n -> U(M)`.  Hence
`V_beta(U(M))={1}`.  Since `h_beta` lies in this subgroup, `h_beta=1`.

The unit-factorization lemma still has a role: when a branch proof produces a
word in a finite transformation monoid and the resulting residual action is a
permutation, it guarantees that all successful factors are already units.
But for detection, the endpoint membership `h_beta in V_beta(U(M))` is enough;
individual factors may lie outside `V_beta(U(M))` and cancel or telescope in
the product.

## Relation To Section Detection

The section criterion in `proofs/unit_section_detection_criterion.md` is a
sufficient condition for this endpoint criterion: if every unit factor lies in
`V_beta(U(M))`, then the product `h_beta` lies there because
`V_beta(U(M))` is a subgroup.

The converse need not hold.  For example, in a `C_2` unit group and a braid
whose `V_beta(C_2)` is trivial, a word `s s` has endpoint identity even
though the individual factor `s` is not in `V_beta(C_2)`.  Thus endpoint
membership is the correct target for branches with telescoping transports.

## A-Route Use

For a local-minimal corridor interval, an A proof may now choose either of
two targets:

- prove the stronger section condition, where every unit label belongs to
  `V_beta(U(M))`; or
- prove directly that each residual endpoint unit/composite belongs to
  `V_beta(U(M))`.

The second target is often more natural when Green, Schutzenberger, or
product-label transports cancel internally.  The fixed finite detector group
is still `U(M)`, or a finite product of such unit groups as in
`proofs/unit_section_product_detector.md`.

## B-Route Consequence

A B obstruction through a finite transformation-monoid observer must now do
more than show that some intermediate unit label is outside the longitude
subgroup.  It must produce a nonidentity endpoint unit `h_beta` outside
`V_beta(U(M))`, and then upgrade this to a normalized-law sequence escaping
every finite group detector.  Intermediate labels outside the subgroup may be
harmless if the residual endpoint telescopes into the subgroup.

The note `proofs/endpoint_unit_dichotomy.md` records this as an explicit
A/B fork.  A finite endpoint failure against `U(M)` is useful only as a
warning: by itself it is not outcome B unless it is diagonalized into a
normalized-law sequence defeating every finite group.

## Executable Audit

The helper

```text
unit_composite_detection_audit(monoid,n,beta,factors)
```

composes the supplied word, checks whether the endpoint is a unit/permutation,
and tests the endpoint itself against `V_beta(U(M))`.
It also exposes `is_finite_unit_detector_failure`, which is true when the
braid has identity finite-`U(M)` longitude data but the endpoint unit is
nonidentity.

Regression tests cover:

- a `C_2` telescoping word `s s`, where section-level membership fails but
  endpoint membership succeeds;
- a `C_3` visible unit at an identity longitude signature, correctly
  rejected;
- a reset word, rejected because its endpoint is not a residual permutation.

The companion route helper

```text
unit_composite_longitude_route_audit(monoid,n,beta,factors)
```

records the proof ladder for one endpoint: identity endpoint, single
evaluated-longitude witness, and membership in the full longitude-value
subgroup.  The third condition is the theorem-level criterion.  The helper is
documented in `proofs/unit_composite_longitude_route_audit.md`.

The expression helper

```text
unit_composite_longitude_expression_audit(
    monoid,n,beta,factors,assignment,expression
)
```

checks a stronger symbolic certificate: the endpoint itself is a displayed
word in evaluated recursive longitudes for one assignment into `U(M)`.  Such
an expression proves endpoint membership in `V_beta(U(M))` without enumerating
the subgroup.  This is documented in
`proofs/endpoint_longitude_expression_certificate.md`.
