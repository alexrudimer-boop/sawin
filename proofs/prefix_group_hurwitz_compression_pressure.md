# Prefix group-Hurwitz compression pressure

Date: 2026-06-03

The prefix-edge transducer gives a finite braid-compatible tower for
degenerate memory.  It does not by itself give the finite augmented
Artin-envelope lemma, because that lemma asks for a fixed finite group
`H_X`, a conjugation-stable subset `C_X`, and bounded-exponent vertical
kernels over the ordinary group-Hurwitz point-pushing tower.

This note records the finite equations any such compression must satisfy.

## Label Map

Let `E_X` be the prefix-edge alphabet

```text
E_X = {(P,x,P lambda_x): P in M_lambda, x in X}.
```

A group-Hurwitz compression would provide a finite group `H`, a
conjugation-stable subset `C subset H`, and a label map

```text
a:E_X -> C.
```

For every local prefix-edge path

```text
(P,x,P lambda_x), (P lambda_x,y,P lambda_x lambda_y)
```

with `r(x,y)=(u,v)`, the local braid move must descend to the Hurwitz rule:

```text
a(P,u,P lambda_u)
  = a(P,x,P lambda_x) a(P lambda_x,y,P lambda_x lambda_y)
    a(P,x,P lambda_x)^-1,

a(P lambda_u,v,P lambda_u lambda_v)
  = a(P,x,P lambda_x).
```

These are finite equations, one pair for every `P in M_lambda` and
`x,y in X`.

## Product Invariance

Ordinary group-Hurwitz moves preserve the ordered product of labels.  Hence
the label product along any prefix path is a braid invariant:

```text
a(e_1) a(e_2) ... a(e_m).
```

This is a strong group-theoretic constraint not automatically present in a
finite transformation transducer.  Any proposed compression must either make
the prefix-edge moves preserve this product exactly or place the failure in a
bounded-exponent vertical kernel.

## Point-Forgetting

Interior point-forgetting rescans prefixes.  Thus a compression must be
lumpable under suffix rescanning:

```text
a(P,x,P lambda_x)=a(P',x,P' lambda_x)
```

must remain compatible after appending every `z in X`:

```text
a(P lambda_x,z,P lambda_x lambda_z)
 =
a(P' lambda_x,z,P' lambda_x lambda_z).
```

Otherwise the compressed labels cannot update deterministically after an
interior point is forgotten.

## Nonunit Prefix Warning

If `M_lambda` contains a noninvertible transformation, then the prefix monoid
cannot be faithfully embedded as a transformation monoid inside a group.
This does not disprove group-Hurwitz compression, because the compression may
quotient memory or store nonunit information vertically.  But it proves that
the prefix-edge transducer is not already the requested group-Hurwitz base.

For genuinely degenerate examples this is the first hard gate: noninvertible
prefix data must be represented by finite group labels plus bounded vertical
noise without losing point-forgetting compatibility.

## First Obstruction Surface

The first meaningful computations remain:

```text
Q_X(3)=<rho_X(alpha_{1,4}),rho_X(alpha_{2,4}),rho_X(alpha_{3,4})>,
Q_X(4)=<rho_X(alpha_{1,5}),...,rho_X(alpha_{4,5})>.
```

A counterexample to group-Hurwitz compression must show that every fixed
finite group label model satisfying the local equations above leaves a
compatible vertical kernel whose exponent cannot be bounded uniformly in the
tower.

Thus the pressure test is now sharper than "finite memory exists":

```text
finite prefix transducer tower
  versus
fixed finite group-Hurwitz tower + bounded-exponent vertical kernel.
```

## Generated audit

The executable helper is

```text
prefix_group_hurwitz_compression_pressure_audit(X)
```

and the generated report is

```text
proofs/prefix_group_hurwitz_compression_pressure_audit.md
```
