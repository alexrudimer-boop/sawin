# Local-minimal descent-readout collapse

Date: 2026-05-30

This note follows `proofs/readout_descent_separation_certificate.md` and
`proofs/local_minimal_seed_saturation_dichotomy.md`.  It does not prove the
Master Local-Minimal Residual Theorem.  It records the immediate consequence
of local-minimality for the *combined* descent readout used in the repair
contract.

## Setup

Let

```text
pi:X -> Z
```

be a local-minimal interval in rack-side convention

```text
R_Z(a,b)=(a*b,a).
```

Let

```text
r_a:A_a -> E_a
```

be a fixed finite descent readout with kernel family

```text
K^r_a = { (x,y) : r_a(x)=r_a(y) }.
```

Assume this combined readout passes the descent-separation hypotheses:

1. `K^r` is an admissible local congruence family;
2. every continuation seed

   ```text
   T_{a,b}(x,y)=(u,v),      v in A_a
   ```

   satisfies

   ```text
   x K^r_a v.
   ```

## Lemma

Exactly one of the following holds.

1. `K^r` is equality.  Then every continuation seed is trivial:

   ```text
   v=x
   ```

   for every local row.  The original lower row is already strand-continuing.

2. `K^r` is universal.  The readout quotient is fibrewise constant, and every
   lower distinction needed for faithful residual reconstruction must be
   carried by external endpoint/readout factors.

In particular, a local-minimal interval has no proper nontrivial
descent-separating readout quotient.

Proof.  Since `K^r` is admissible and the interval is local-minimal, `K^r` is
either equality or universal.

If `K^r` is equality and every continuation seed satisfies `x K^r_a v`, then
each seed has `x=v`, so the row is strand-continuing before quotienting.

If some nontrivial continuation seed has `x != v`, then equality cannot contain
that seed.  Therefore any admissible descent-separating `K^r` must be
universal.  QED.

## Consequence for the repair contract

The fixed descent readout in
`proofs/descent_endpoint_repair_contract.md` cannot be a hidden middle layer in
a local-minimal bottleneck interval.  The descent part of the proof splits
cleanly:

1. **Equality case.**  There are no nontrivial continuation seeds.  The lower
   row is already strand-continuing, so transport-state rackification applies
   directly.
2. **Universal case.**  The combined descent readout is fibrewise constant.
   Transport-state rackification only sees the collapsed quotient.  Faithful
   residual detection must come entirely from the fixed external endpoint
   factors and their `V_beta` witnesses.

Thus the proof-critic gap may be stated more sharply:

```text
In the only non-strand-continuing local-minimal case, construct endpoint
factors that faithfully recover the information lost by universal descent
collapse, and prove their all-n V_beta membership.
```

This is consistent with the endpoint-family symmetric fork: once those fixed
endpoint factors are chosen, either one symmetric detector degree kills them
all, or their failures supply a symmetric-tail normalized-law seed.

## What this rules out

A proposed positive proof cannot claim that a proper partial finite readout
simultaneously:

- is admissible;
- kills a nontrivial continuation seed;
- remains a non-universal local-minimal quotient.

Such a quotient would be an intermediate admissible congruence, contradicting
local-minimality.  If a finite audit exhibits it, then either the interval is
not local-minimal or the readout kernel is not actually admissible.

The note is a structural guardrail only.  It does not construct the endpoint
witnesses required for outcome A and does not construct the normalized-law
sequence required for outcome B.
