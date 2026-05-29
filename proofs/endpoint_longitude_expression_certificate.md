# Endpoint longitude expression certificate

Date: 2026-05-29

This note records a stronger proof object for the endpoint-unit branch.  It is
not a proof that every corridor endpoint has such an expression, but it
identifies the exact symbolic certificate that would prove endpoint
membership in the longitude-value subgroup without finite subgroup
enumeration.

## Setup

Let `M` be a finite transformation monoid and let

```text
U(M)
```

be its finite unit group.  Fix a braid `beta in B_n`.  Suppose a residual
branch endpoint is represented by a word in `M`,

```text
h_beta = f_k ... f_1,
```

whose composite is a unit.  Let

```text
L_1(beta),...,L_n(beta)
```

be the recursive Artin longitudes.

An endpoint longitude expression certificate consists of:

1. an assignment

   ```text
   phi : F_n -> U(M);
   ```

2. a finite word in the evaluated longitude values

   ```text
   phi(L_{i_1}(beta))^{epsilon_1}
   ...
   phi(L_{i_r}(beta))^{epsilon_r},
   epsilon_j in {+1,-1};
   ```

3. an equality in `U(M)`

   ```text
   h_beta =
   phi(L_{i_1}(beta))^{epsilon_1}
   ...
   phi(L_{i_r}(beta))^{epsilon_r}.
   ```

Then

```text
h_beta in V_beta(U(M)),
```

where

```text
V_beta(U(M)) =
< psi(L_i(beta)) : psi:F_n -> U(M), 1<=i<=n >.
```

This is immediate because the right side is literally a product of generators
of the longitude-value subgroup and their inverses.

## Detection Consequence

If the finite-`U(M)` longitude data of `beta` is identity, then every
longitude value `psi(L_i(beta))` is identity for every assignment
`psi:F_n -> U(M)`.  In particular all factors in the displayed expression are
identity, so the endpoint unit `h_beta` is identity.

Thus the expression certificate is a strictly more constructive sufficient
condition for the endpoint criterion from
`proofs/unit_composite_longitude_criterion.md`.

It is also compatible with product detectors.  For finitely many monoids
`M_1,...,M_r`, expression certificates in each unit group assemble into a
single certificate in

```text
U(M_1) x ... x U(M_r)
```

by `proofs/longitude_subgroup_products.md`.

Concretely, if each endpoint `h_i(beta)` is displayed as a word in longitude
values in `U(M_i)`, then

```text
(h_1(beta),...,h_r(beta))
  in V_beta(U(M_1) x ... x U(M_r)).
```

Indeed, each factor expression embeds in the product group by using the given
assignment in that factor and the identity assignment in all other factors.
Multiplying the embedded factor expressions gives the endpoint tuple.  This
is the product-detector certificate required by the sharp obstruction theorem.
This product certificate is not merely a citation of the product subgroup
lemma: it is a literal word in generators of `V_beta(U(M_1) x ... x U(M_r))`.
Its letters may use different product-group assignments, exactly as the
definition of `V_beta(G)` permits.

## Executable Form

The helper

```text
evaluate_longitude_expression(group, assignment, braid_word, expression)
```

evaluates a word in the longitude values for a fixed assignment.  Expression
letters are zero-based pairs

```text
(longitude_index, exponent)
```

with exponent `+1` or `-1`.

The subgroup-word helper

```text
evaluate_longitude_subgroup_witness(group,n,braid_word,witness)
```

evaluates the more literal certificate for membership in `V_beta(G)`.  Each
witness letter is

```text
(assignment, longitude_index, exponent),
```

where `assignment` is an `n`-tuple of elements of `G`.  Consecutive letters may
use different assignments, so this is exactly a word in the subgroup
generators `psi(L_i(beta))`.

The companion helpers in `proofs/longitude_subgroup_witness_calculus.md`
push such witnesses through fixed finite homomorphisms and assemble factor
witnesses into direct-product witnesses.  They are the certificate-level
versions of the functoriality and product lemmas for `V_beta(-)`.

The endpoint helper

```text
unit_composite_longitude_expression_audit(
    monoid,n,beta,factors,assignment,expression
)
```

checks:

- the factor word lies in the fixed monoid;
- the endpoint composite is a unit;
- the assignment lands in `U(M)`;
- the displayed expression evaluates to the endpoint composite.

When these checks pass, the flag

```text
composite_lies_in_longitude_subgroup_by_expression
```

is the certificate-level proof of endpoint subgroup membership.  The flag

```text
identity_longitudes_kill_composite_by_expression
```

records the corresponding fixed-word implication.

The product helper

```text
unit_composite_product_longitude_expression_audit(
    monoids,n,beta,factor_words,assignments,expressions
)
```

checks the same certificate for a finite list of endpoint monoids, returns
the product endpoint in the single fixed unit group product, and constructs
the explicit product subgroup witness described above.  The witness value is
recorded as

```text
product_witness_value
```

and the equality with the endpoint tuple is recorded as

```text
product_witness_matches_endpoint
```

Its flag

```text
product_endpoint_lies_in_product_longitude_subgroup_by_expression
```

is true only when this explicit product witness evaluates to the endpoint
tuple.  It is the non-enumerative product analogue of the endpoint-subgroup
membership flag in `unit_composite_product_detection_audit(...)`.

For Green/corridor endpoint factors that already live in finite groups rather
than transformation monoid unit groups, the corresponding group-only helpers
are:

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
```

They implement the certificate layer of
`proofs/bifree_corridor_endpoint_factorization.md`: one helper checks a single
endpoint expression in a fixed factor, and the product helper constructs a
literal word in `V_beta(product_i G_i)`.  Thus kernel-block,
Schutzenberger, atom-inner, quotient-detector, and endpoint/unit factors can
all be audited with the same direct-product witness convention.
The readout helpers record the faithful-readout clause: when the endpoint
tuple is identity, the corresponding residual coordinate or tuple must
actually be fixed.  They are the executable row format for the final implication
from killed endpoints to killed residual motion.

## Role In The Master Local Theorem

For outcome A, a Green/corridor proof does not have to enumerate
`V_beta(U(M))`.  It may instead construct, for every residual endpoint and
every `beta in N_n`, an input-dependent assignment to the fixed unit group and
an explicit longitude expression for the endpoint.  The assignment and
expression may depend on the braid, base tuple, fibre tuple, endpoint, and
finite corridor state; the group `U(M)` must remain fixed by the interval and
quotient detector and must not depend on `n`.

For outcome B, failure to find such an expression is not enough.  A
counterexample must still produce a normalized-law sequence whose endpoint
unit remains nonidentity after every finite group has identity Artin-longitude
data.
