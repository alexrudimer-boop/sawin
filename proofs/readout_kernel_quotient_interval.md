# Readout-kernel quotient interval

Date: 2026-05-29

This note follows `proofs/readout_descent_separation_certificate.md`.  It does
not prove the Master Local-Minimal Residual Theorem.  It records the explicit
finite quotient local interval carried by an admissible readout kernel.

The purpose is to make the phrase "the quotient row is strand-continuing"
literal: once the readout kernel is admissible, there is an actual local
interval on readout blocks, and the continuation audit can be run on that
quotient interval.

## Setup

Let `pi:X->Z` be a local interval with fibres `A_a`.  Let

```text
Phi = (Phi_a)_a
```

be an admissible local congruence family.  Write

```text
[x]_Phi
```

for the block of `x in A_a`.

## Quotient construction

Define a new local interval

```text
X/Phi -> Z
```

with the same colours and the same base row `R_Z`.  The fibre over `a` is the
finite set of blocks

```text
A_a/Phi_a.
```

For a local row

```text
T_{a,b}(x,y) = (u,v),
```

define

```text
Tbar_{a,b}([x],[y]) = ([u],[v]).
```

This is well-defined because `Phi` is admissible: product-equivalent source
pairs are transported exactly to product-equivalent target pairs.  Since the
original `T_{a,b}` is bijective and admissibility includes exact image equality,
each `Tbar_{a,b}` is bijective.

The coloured YBE for `Tbar` follows by applying the quotient map to the
coloured YBE for `T`.  Both sides of the YBE on blocks are represented by the
corresponding original sides on any chosen representatives, and the original
interval has equal outputs before passing to blocks.  Thus `X/Phi -> Z` is a
finite coloured local interval.

## Readout-kernel specialization

If finite readout labels

```text
r_a:A_a -> E_a
```

are given, their kernel family is `Phi^r`.  When
`readout_kernel_audit(interval,r)` is admissible, the quotient interval is

```text
readout_kernel_quotient_interval(interval,r).
```

The generic constructor is

```text
quotient_interval_by_family(interval,Phi).
```

The descent-separation audit now carries this quotient interval when the
readout kernel is admissible.  It also runs

```text
continuation_congruence_audit(X/Phi -> Z)
```

on the quotient itself.

## Lemma

If `readout_descent_separation_audit(interval,r)` proves descent separation,
then the quotient interval stored by the audit is strand-continuing on the
nose.

Proof.  The audit requires the base row to be in rack-side form, the readout
kernel to be admissible, and every continuation seed `x~v` to be killed by the
kernel.  Therefore, in the quotient interval,

```text
Tbar_{a,b}([x],[y]) = ([u],[v]) = ([u],[x]).
```

So the quotient has no nontrivial continuation seed rows.  The audit verifies
this directly by running `continuation_congruence_audit` on the quotient
interval and requiring `is_strand_continuing_on_the_nose`.  QED.

## Consequence for the A-route

The remaining descent-separation construction target is now:

```text
For every bottleneck interval, construct fixed detector labels r such that
readout_descent_separation_audit(interval,r) passes.
```

When it passes, the quotient local interval on readout blocks is an explicit
strand-continuing finite row.  The transport-state rackification theorem then
builds the finite rack detector for the remaining lower gauge.

This note still does not construct the labels from Green, Schutzenberger,
atom, or unit detector factors.  That construction remains the open
Master-Local-Minimal residual step.

## B-route meaning

A failed quotient construction is precise:

- if the readout kernel is not admissible, there is no quotient interval and
  the transport failure row is recorded;
- if the quotient interval exists but has surviving continuation seeds, those
  rows are recorded;
- if the base row is not in rack-side form, the side convention or higher
  readout must be corrected before transport-rack closure applies.

As before, any such finite failure is not yet outcome B.  It must still be
upgraded to a normalized-law sequence invisible to every finite group while
moving a residual tuple.
