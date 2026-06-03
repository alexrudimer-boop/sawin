# Pullback-coskeletal criterion audit

Date: 2026-06-03

This generated audit records the logical boundary between two
different statements in the finite-base pullback route.

For one fixed proposed finite operator-label base, the finite
gauge/pullback solution sets in arities `<=N` form an inverse
system when restriction maps are part of the data.  Nonemptiness
at every finite `N` gives an all-arity branch by compactness.

That is not the same as a uniform bounded-arity cutoff.  A cutoff
requires an additional coskeletality or finite-type lemma saying
that higher deletion cocycles, coefficient transports, and
section-gauge relations are forced by a bounded skeleton.

## Flags

- fixed-base inverse-limit compactness recorded: `True`;
- bounded-arity cutoff rejected without extra hypothesis: `True`;
- pullback-coskeletal hypothesis identified: `True`;
- finite obstruction certificate identified: `True`;
- records route boundary: `True`.

Missing lemma:

```text
finite YBE point-pushing deletion towers are d-pullback-coskeletal over one fixed finite operator-label Hurwitz base, for some d depending only on the finite solution or on the proposed base
```

## Cases

### fixed_base_inverse_limit

- role: `valid_compactness_principle`;
- finite data: for one fixed base B, finite sets S_N(B) of gauge/pullback solutions through arity N and restriction maps S_{N+1}(B)->S_N(B);
- criterion: every S_N(B) is nonempty and the restrictions make these sets an inverse system;
- consequence: König/compactness gives one compatible all-arity solution for that fixed base;
- failure mode: some finite S_N(B) is empty; this is a real obstruction to that fixed base.

### bounded_cutoff_requires_coskeletality

- role: `missing_positive_hypothesis`;
- finite data: a comparison tower whose cocycles, coefficient transports, and gauge cochains above arity d are forced by their d-skeleton;
- criterion: the tower is d-pullback-coskeletal and section-gauge relations are generated in arity at most d;
- consequence: checking the finite gauge/pullback system through arity d is enough for the fixed base;
- failure mode: new independent obstruction coordinates can first appear in arbitrarily high arity.

### finite_obstruction_certificate

- role: `valid_negative_certificate_for_fixed_base`;
- finite data: the finite system S_N(B) of base comparison maps, vertical coefficient labels, and section-change cochains;
- criterion: S_N(B) is empty for a specified finite arity N;
- consequence: no all-arity pullback to that fixed base exists, because any all-arity solution restricts to S_N(B);
- failure mode: nonemptiness of S_N(B) for small N alone does not certify an all-arity solution unless the inverse-system or coskeletal hypotheses are supplied.

### general_uniform_cutoff_failure

- role: `warning_countermechanism`;
- finite data: a finite-state-looking tower with an independent new gauge/pullback constraint introduced at each higher arity;
- criterion: for every d there is a tower whose first failed constraint appears above d;
- consequence: there is no universal bounded-arity pullback test without extra finite-type or coskeletal structure;
- failure mode: a proof that uses only bounded prefix checks silently assumes the missing pullback-coskeletal lemma.

## Meaning

A finite negative certificate for a fixed proposed base is honest:
if the gauge/pullback system is empty at arity `N`, no all-arity
pullback to that base can exist.

A finite positive prefix is weaker.  It proves only that no
obstruction has appeared yet.  To upgrade a bounded prefix to an
all-arity theorem, one must prove the missing pullback-coskeletal
lemma or another noetherian finite-type replacement.

Thus the next all-arity work is not another small prefix audit.
It is either a proof of coskeletality for finite YBE point-pushing
deletion towers, or a countermechanism where independent
gauge/pullback constraints first appear in arbitrarily high
arity.
