# Local-minimal seed-saturation dichotomy

Date: 2026-05-29

This note follows `proofs/readout_seed_saturation.md`.  It does not prove the
Master Local-Minimal Residual Theorem.  It records the exact consequence of
local-minimality for seed-saturating a fixed readout factor.

## Statement

Let `pi:X->Z` be a local-minimal interval in rack-side convention, and let

```text
r_a:A_a -> E_a
```

be a finite readout factor whose kernel `Phi^r` is admissible.

Let `Sat(r)` be the least admissible congruence family containing `Phi^r` and
all continuation seed pairs `x~v`.

Then exactly one of the following holds:

1. `Phi^r` is universal, and `Sat(r)` is universal.
2. `Phi^r` is equality and no continuation seed survives; then `Sat(r)` is
   equality.
3. `Phi^r` is equality and some continuation seed survives; then `Sat(r)` is
   universal.

In particular, there is no proper nontrivial seed-saturated middle quotient in
a local-minimal interval.

## Proof

Since the interval is local-minimal, every admissible congruence family is
either equality or universal.  The readout kernel `Phi^r` is admissible, so it
is equality or universal.

The saturation `Sat(r)` is admissible by construction and contains `Phi^r`.
Therefore `Sat(r)` is also equality or universal.

If `Phi^r` is universal, then no strictly larger fibrewise congruence exists,
so `Sat(r)` is universal.

Assume `Phi^r` is equality.  If no continuation seed survives, then every
continuation seed pair is already contained in equality.  Since equality is
admissible, the least admissible congruence containing `Phi^r` and the seed
pairs is equality.

If some continuation seed survives, then the seed pair is nontrivial and is
not contained in equality.  Thus `Sat(r)` strictly contains equality.  Since
the only admissible congruence families are equality and universal, `Sat(r)`
must be universal.  QED.

## Consequence for descent separation

This is the precise local-minimal guardrail behind the product
descent-separation audit.

Because product kernels are meets, every factor in a tuple-valued readout must
kill every continuation seed if the product quotient is to become
strand-continuing.  But in a local-minimal interval, a factor that has
admissible equality kernel and fails to kill a nontrivial seed can only be
seed-saturated by collapsing to universal.

Therefore a positive proof must explicitly route the information lost by such
universal collapse.  It cannot claim that a hidden proper quotient keeps both
faithfulness and strand-continuation unless the interval was not actually
local-minimal or the proposed readout kernel was not admissible.

## Code certificate

The helper

```text
local_minimal_seed_saturation_dichotomy_audit(interval, labels)
```

wraps `readout_seed_saturation_audit(...)` and records:

- whether the interval is local-minimal;
- whether the original readout kernel has a local-minimal kind;
- whether the saturation has a local-minimal kind;
- the expected saturation kind, computed from seed survival;
- whether a nontrivial seed forces universal collapse;
- whether external routing is needed after that collapse.

Its property

```text
proves_local_minimal_seed_saturation_dichotomy
```

is true only when the interval is local-minimal, the original kernel is
admissible, the original and saturated kernels have equality/universal kind,
and the actual saturation kind matches the expected dichotomy.

## Remaining theorem pressure

The final descent-separation theorem now has a sharper burden:

```text
For every bottleneck interval, construct fixed detector factors so that any
factor forced to universal seed-saturation loses only information carried by
another fixed factor or by the transport-state rack quotient.
```

A finite failure of this routing is still not outcome B.  It must still be
turned into a normalized-law sequence invisible to every finite group while
moving a residual tuple.
