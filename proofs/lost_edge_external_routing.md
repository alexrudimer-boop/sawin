# Lost-edge external routing ledger

Date: 2026-05-29

This note follows `proofs/local_minimal_seed_saturation_dichotomy.md`.  It does
not prove the Master Local-Minimal Residual Theorem.  It records the finite
bookkeeping needed when descent separation forces a readout factor to collapse
to a coarser seed-saturated quotient.

The key distinction is:

```text
descent quotient labels != external endpoint routing labels.
```

The descent quotient labels are used to make the lower row
strand-continuing.  External routing labels may remember information that the
descent quotient collapses, but they must not be inserted back into the
descent quotient product.  Adding them back as quotient factors would refine
the product kernel and could make continuation seeds survive again.

## Setup

Let `pi:X->Z` be a local-minimal interval in rack-side convention.  Let

```text
r_a:A_a -> E_a
```

be the descent readout factor.  Suppose its seed-saturation `Sat(r)` collapses
some additional fibre pairs:

```text
x Sat(r)_a y
```

even though

```text
x not Phi^r_a y.
```

These pairs are the lost edges of the descent quotient.

Let

```text
s_a:A_a -> F_a
```

be a separate external routing label system.  It routes a lost edge
`(a,x,y)` when

```text
s_a(x) != s_a(y).
```

## Lemma: routed lost edges are externally remembered

If every lost edge of `Sat(r)` is routed by `s`, then the descent quotient may
identify the endpoints of every continuation seed while the external routing
ledger still records which original fibre points were collapsed by the
saturation.

Proof.  The descent quotient uses only `Sat(r)`, so all continuation seeds are
identified exactly as in the seed-saturation certificate.  The external labels
are not included in that quotient, hence they do not refine the quotient
kernel and do not reintroduce surviving continuation seeds.

For each lost edge `(a,x,y)`, the routing condition `s_a(x) != s_a(y)` says
that the external readout distinguishes the two original endpoints.  Thus the
information lost by the quotient is present in a separate fixed finite
readout ledger.  QED.

## Guardrail

This ledger is not by itself a proof of Sawin finite-rack domination.

To close the A-route, the external routing labels must still be shown to come
from fixed interval-level detector factors with all-`n` recursive-longitude
visibility.  The ledger only says which collapsed finite edges such a detector
must remember.

Conversely, if a lost edge is not externally routed, that is still only a B
seed.  It must be upgraded to a normalized-law sequence invisible to every
finite group while moving a residual tuple.

## Code certificate

The helper

```text
lost_edge_external_routing_audit(interval, descent_labels, routing_labels)
```

records:

- the local-minimal seed-saturation dichotomy audit for the descent labels;
- the kernel audit of the external routing labels;
- the lost edges added by seed-saturation;
- which lost edges are distinguished by the routing labels;
- which lost edges remain unrouted.

Its property

```text
proves_external_routing_ledger
```

is true when the local-minimal dichotomy is certified and either no forced
universal collapse requires routing, or every lost edge is routed.

## Updated target

The remaining descent-separation theorem can now be stated as a two-level
construction:

1. choose descent quotient labels whose seed-saturation makes the quotient row
   strand-continuing;
2. choose external endpoint detector labels that route every edge lost by that
   saturation and prove recursive-longitude visibility for those external
   labels.

This is the exact place where the all-`n` endpoint-factorization burden
returns.  The finite ledger only identifies the target edges; it does not
replace the required Artin-longitude proof.
