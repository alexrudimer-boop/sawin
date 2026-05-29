# Atom-inner detector-lift rows

Date: 2026-05-29

This note closes one of the finite row checks left by
`proofs/artin_detector_lift_criterion.md`.  It does not prove the Master
Local-Minimal Residual Theorem.  It proves that once a Green atom quotient has
descended to a total rack-like layer, the atom-inner group factor automatically
satisfies the Artin detector-lift row identities.

Consequently, the rack-like atom-inner factor should no longer be listed as an
open row-identity burden in the bi-free universal-corridor branch.  The atom
quotient still has its separate theorem burden: prove descent and totality in
the target local-minimal interval, or route the information lost below a
descent-closed atom quotient to lower endpoint/unit holonomy.

## Positive row and its inverse

For a finite group `U`, write the positive active Artin detector row as

```text
P((m,u),(n,v)) =
  ((m n m^-1, m v), (m,u)).
```

The map is bijective.  Solving for the input from an output

```text
((M,U),(N,V))
```

gives

```text
P^-1((M,U),(N,V)) =
  ((N,V), (N^-1 M N, N^-1 U)).
```

This is exactly the negative detector-lift row.  Therefore a group-like
observer factor only needs a positive-row verification; the negative row then
follows formally by invertibility.

The executable helper

```text
artin_detector_lift_inverse_row_audit(U,left,right)
```

records this inverse check for supplied finite labels.

## Rack-inner positive row

Let `A` be a finite rack in the left convention

```text
R(a,b) = (a*b, a).
```

For `a in A`, let

```text
L_a(b) = a*b
```

and let

```text
U = Inn(A) = < L_a : a in A > <= Sym(A).
```

The rack self-distributive law says

```text
a*(b*c) = (a*b)*(a*c).
```

Equivalently,

```text
L_{a*b} L_a = L_a L_b.
```

Because every `L_a` is bijective,

```text
L_{a*b} = L_a L_b L_a^-1.
```

Now run one positive crossing on live atom labels `(a,b)`.  The rack crossing
sends

```text
(a,b) |-> (a*b,a).
```

Set the live meridian labels to

```text
m_i     = L_a,
m_{i+1} = L_b.
```

Then the output meridian labels are

```text
m_i'     = L_{a*b} = L_a L_b L_a^-1 = m_i m_{i+1} m_i^-1,
m_{i+1}' = L_a = m_i.
```

So the meridian half of the Artin detector-lift row is exact.

For endpoint labels, suppose the incoming live atoms are represented as

```text
a = u_i(a_0),
b = u_{i+1}(b_0),
```

with `u_i,u_{i+1} in U`.  After the crossing,

```text
a*b = L_a(b) = L_a u_{i+1}(b_0) = m_i u_{i+1}(b_0),
```

while the second output atom is

```text
a = u_i(a_0).
```

Therefore the endpoint labels update as

```text
u_i'     = m_i u_{i+1},
u_{i+1}' = u_i.
```

Together,

```text
(m_i,u_i),(m_{i+1},u_{i+1})
  |->
(m_i m_{i+1} m_i^-1, m_i u_{i+1}), (m_i,u_i),
```

which is exactly the required positive detector-lift row.  The negative row is
the inverse row from the preceding section.

## Atom quotient convention

The Green atom quotient appears in the right-rack-like convention

```text
R_A(A_0,A_1) = (A_1, A_0^A_1).
```

Passing to the side-opposite solution converts it to a left rack.  The left
translations of the side-opposite rack are exactly the right translations of
the original atom quotient, so the inner group is the same detector factor:

```text
G_A = < A_0 |-> A_0^A_1 > <= Sym(A).
```

Thus every rack-like atom quotient inner-group row satisfies the Artin
detector-lift identities.

## Consequence

Once atom descent and totality have been established for a local-minimal
Green/corridor interval, the atom-inner factor contributes endpoint labels
that are recursive Artin-longitude values in the fixed finite group `G_A`.
Identity finite-`G_A` longitude data therefore fixes the atom quotient
coordinate.  Product assembly with the other fixed factors is still handled by
`proofs/bifree_corridor_endpoint_factorization.md`.

The remaining open row checks are now:

```text
Green kernel-block symmetric factors,
Schutzenberger factors,
lower endpoint/unit holonomy factors.
```

The first two entries have since been reduced to one endpoint problem by
`proofs/green_first_output_defect_criterion.md`: a Green row is controlled by
its first-output defect, and kernel-block defects are Schutzenberger
pushforwards when there are no local-only edge-germs.  Thus the remaining
Green row burden is the transported Schutzenberger defect endpoint, not a
literal row-by-row Artin check.

The atom layer itself remains conditional on proving the descent/totality
theorem in the arbitrary local-minimal interval.  If that theorem fails, a B
route must still extract an explicit local-minimal interval and a
normalized-law obstruction sequence invisible to every finite group.

## Executable audit hooks

The code records this closure through:

```text
artin_detector_lift_inverse_row_audit(...)
rack_inner_detector_lift_row_audit(...)
rack_inner_detector_lift_audit(...)
right_rack_inner_detector_lift_audit(...)
atom_quotient_inner_detector_lift_audit(...)
atom_descent_quotient_inner_detector_lift_audit(...)
```

The rack-inner audit checks the positive row against the active detector row,
the translation conjugacy `L_{a*b}=L_a L_b L_a^-1`, the endpoint transport
formula, and the formal inverse relation giving the negative row.
