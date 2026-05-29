# Principal gauge-extension detector

Date: 2026-05-29

This note follows
`proofs/terminal_gauge_longitudinalization_criterion.md`.  It does not prove
the Master Local-Minimal Residual Theorem.  It closes the lower
endpoint/unit holonomy branch under one explicit structural hypothesis:
the remaining gauge row is a principal finite rack-extension cocycle.

The remaining global problem is therefore sharpened again.  After the Green
balanced decomposition and terminal-gauge criterion, the unresolved corridor
obstruction is nonprincipal terminal gauge holonomy.

## Principal row

Let `A` be a finite rack in the left convention

```text
R_A(a,b) = (a*b, a).
```

Let `U` be a finite unit group carrying lower endpoint/unit gauge.  Suppose
the surviving lower row over `A` has the principal form

```text
((a,r),(b,s)) |-> ((a*b, c(a,b)s), (a,r)),
```

where

```text
c : A x A -> U
```

is the local gauge increment.  Define

```text
A~ = A x U
```

with operation

```text
(a,r) * (b,s) = (a*b, c(a,b)s).
```

The left unit coordinate `r` is carried by the strand but does not enter the
new left translation; this is the principal-gauge assumption.

## Rack-cocycle identity

The operation on `A~` is self-distributive precisely when

```text
c(a,b*d)c(b,d) = c(a*b,a*d)c(a,d)
```

for all `a,b,d in A`.

Proof.  The left side of self-distributivity gives

```text
(a,r) * ((b,s) * (d,t))
  = (a,r) * (b*d, c(b,d)t)
  = (a*(b*d), c(a,b*d)c(b,d)t).
```

The right side gives

```text
((a,r)*(b,s)) * ((a,r)*(d,t))
  = (a*b, c(a,b)s) * (a*d, c(a,d)t)
  = ((a*b)*(a*d), c(a*b,a*d)c(a,d)t).
```

The `A`-coordinates agree because `A` is a rack.  The `U`-coordinates agree
for all `t` exactly when the displayed cocycle identity holds.

The left translations of `A~` are bijective because left translations of `A`
are bijective and left multiplication by each `c(a,b)` is a bijection of `U`.
Thus the identity is exactly the remaining rack condition.  QED.

## Detector consequence

When the cocycle identity holds, `A~` is a finite rack.  Set

```text
W = Inn(A~) <= Sym(A~).
```

This finite group depends only on the interval data `A`, `U`, and `c`, not on
the braid index `n`.

For the left translation `L_x(y)=x*y`, rack self-distributivity gives

```text
L_{x*y} = L_x L_y L_x^-1.
```

Therefore the positive crossing row in `W` is exactly the active Artin
detector-lift row

```text
(m_i,u_i),(m_{i+1},u_{i+1})
  |-> (m_i m_{i+1} m_i^-1, m_i u_{i+1}), (m_i,u_i).
```

The inverse row is the negative crossing row.  Hence
`proofs/artin_detector_lift_criterion.md` applies to `W`: for every braid
word `beta`, terminal endpoint labels in this principal extension are
recursive Artin-longitude evaluations in the fixed group `W`.

Consequently identity finite-`W` longitude data kills the principal terminal
gauge endpoint.

## Why YBE supplies the cocycle law

If a completed corridor row is already known to have the principal form above
and the full local row satisfies the coloured Yang-Baxter equation, then
projecting the YBE to the final `U` coordinate gives exactly

```text
c(a,b*d)c(b,d) = c(a*b,a*d)c(a,d).
```

Thus, in the principal case, the cocycle law is not an additional all-`n`
condition.  It is the finite row-level YBE identity read in the unit gauge
coordinate.

## Corridor consequence

The previously open row list was:

```text
Green kernel-block rows
+ Schutzenberger rows
+ lower endpoint/unit holonomy rows.
```

The balanced Green decomposition removes raw Green/Schutzenberger defects as
independent obstructions: each such defect is an Artin-visible commutator
times terminal gauge holonomy.  The terminal gauge criterion then packages the
remaining gauge endpoint as a standard fixed-group longitude-certificate
target.  This note closes the target whenever the lower gauge row is a
principal finite rack-extension cocycle, by adding the fixed detector group
`Inn(A~)`.

Thus the remaining make-or-break structural statement is:

```text
Principal-gauge normal form.
In every local-minimal interval that reaches the
bi_free_universal_corridor_bottleneck, every surviving endpoint/unit holonomy
row is, after the correct side convention and atom descent, a principal finite
rack-extension cocycle.
```

If this structural statement is proved, the positive route closes through the
existing sharp obstruction theorem and congruence-chain induction.  If it
fails, the failure is a finite nonprincipal unit transition row.  Outcome B
would still require upgrading that row to a normalized-law sequence invisible
to every finite group while moving an explicit residual tuple.

## Executable audit hooks

The code records the finite check with:

```text
principal_gauge_cocycle_failures(...)
principal_gauge_extension_rack(...)
principal_gauge_extension_detector_audit(...)
```

The audit checks the nonabelian cocycle identity, builds the finite rack
`A x U`, verifies the YBE/rack form, computes `Inn(A x U)`, and reuses
`rack_inner_detector_lift_audit(...)` to certify the fixed detector row.
