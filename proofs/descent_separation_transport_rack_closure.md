# Descent separation and transport-rack closure target

Date: 2026-05-29

This note states the exact positive theorem that would finish the current
A-route from the `bi_free_universal_corridor_bottleneck`.  It separates the
part already proved from the part still missing.

It does not prove Sawin finite-rack domination.  It records that the remaining
unproved theorem is descent separation.

## Fixed detector context

Let

```text
pi : X -> Z
```

be a local-minimal interval in the bottleneck branch, with `Z` dominated by a
finite rack `Q`.  Let

```text
N_n = ker rho_{Q,n}.
```

The desired local implication is still

```text
Lambda_{G(pi,Q),n}(beta)=Lambda_{G(pi,Q),n}(1)
  => Delta_n(beta)=1
```

for all `n` and every `beta in N_n`, where `G(pi,Q)` is finite and has no
braid-index parameter.

The candidate detector product has interval-level factors only:

```text
H(pi,Q) =
  H_Green x H_Sch x H_atom x H_known x H_unit.
```

Here the factors are the two-sided Green kernel-block groups, two-sided
Schutzenberger action groups, rack-like atom-inner groups, quotient or known
branch detector factors, and endpoint/unit or transport-state factors.

## Final theorem target

The missing theorem is:

```text
Descent separation.
Every residual endpoint motion in the bottleneck branch separates into
Green/Schutzenberger motion, rack-like atom motion, and strand-continuing
finite transport-rack gauge motion.
```

Equivalently, after quotienting by the Green/Schutzenberger readout and the
atom descent closure, every remaining lower endpoint row has the form

```text
R~((a,r),(b,s)) =
  ((a*b, F_{a,b,r}(s)), (a,r))
```

or the side-opposite version, where `A` is a finite rack-like atom state set,
`E` is a finite lower endpoint/unit state set, and every

```text
F_{a,b,r}: E -> E
```

is a bijection.

Any lower motion that is not of this strand-continuing form must be completely
visible in the fixed Green kernel-block, Schutzenberger, or atom readouts.

## Proved part: transport-rack closure

Assume the strand-continuing form above.  Define

```text
A^ = A x E
```

and

```text
(a,r) *^ (b,s) = (a*b, F_{a,b,r}(s)).
```

Then

```text
R~(x,y) = (x *^ y, x).
```

Since `R~` is a completed row of the original finite YBE solution, it satisfies
the set-theoretic Yang-Baxter equation.  For a row of rack form
`R(x,y)=(x*^y,x)`, YBE is exactly self-distributivity:

```text
x *^ (y *^ z) = (x *^ y) *^ (x *^ z).
```

Since `R~` is bijective, every left translation

```text
L_x : y |-> x *^ y
```

is bijective.  Therefore `A^` is a finite rack.

Let

```text
W = Inn(A^) <= Sym(A^).
```

Rack self-distributivity gives

```text
L_{x *^ y} = L_x L_y L_x^-1.
```

Thus the active row in `W` is exactly the Artin detector-lift row.  The
detector-lift theorem gives terminal labels

```text
u_k(beta) = phi(L_k(beta))
```

for an input-dependent assignment `phi:F_n -> W`.  Identity finite-`W`
longitude data kills the transport-gauge endpoint.  This is the proved
transport-rack closure step.

## Completion if descent separation holds

If descent separation is proved, the A-route closes as follows.

1. Raw Green/Schutzenberger first-output defects split into Artin-visible
   commutators and terminal gauge boundaries.
2. Rack-like atom-inner rows are detected by finite atom inner groups after
   atom descent and totality.
3. Every remaining strand-continuing gauge row is detected by the finite rack
   `A x E`, with detector group `Inn(A x E)`.
4. Chart-transport collapse reduces representative checks to one finite
   chart-conjugacy orbit representative per elementary generator orbit.
5. Elementary continuation closure reduces universal continuation to one
   nontrivial seed pair at a time: in a local-minimal interval every
   individual continuation seed has universal admissible closure.
6. Continuation readout propagation reduces derived-edge visibility to
   representative seed visibility: an admissible fixed readout relation that
   contains the seed contains the whole generated seed closure.
7. Readout-kernel admissibility turns fixed detector labels into that
   admissible relation by checking exact transport through every local table.
8. The readout descent-separation certificate checks that no continuation seed
   survives in the quotient, so the quotient lower row is strand-continuing.
9. The readout-kernel quotient constructor builds the explicit finite local
   interval on readout blocks and verifies its continuation audit directly.
10. Product readout-kernel assembly combines the Green, Schutzenberger, atom,
   known-branch, and unit labels into one fixed tuple-valued readout whose
   kernel is the meet of the factor kernels.
11. Product witness calculus assembles all factor witnesses into one fixed
   `H(pi,Q)`.
12. The endpoint-factorization criterion gives

```text
Lambda_{H(pi,Q),n}(beta)=Lambda_{H(pi,Q),n}(1)
  => Delta_n(beta)=1.
```

13. The sharp obstruction theorem supplies the local rack `Q x A_H`.
14. Congruence-chain induction assembles the local racks into one finite rack
   independent of `n`.

## Why this is still open

The branch does not yet prove descent separation.  It still must construct
fixed Green, Schutzenberger, atom, or unit readout labels whose kernel is
admissible and kills every representative nontrivial continuation seed.  By
continuation readout propagation, that would force the whole generated
continuation closure to be readout-visible, and the integrated readout
descent-separation certificate would construct a quotient interval whose row is
strand-continuing.  Equivalently, after those readouts, the remaining lower
endpoint motion must be strand-continuing.

There is also a guardrail against an invalid shortcut: elementary Green defects
cannot always be products of Artin permutation defects.  The abelianization
barrier records finite stress rows with nontrivial abelian defect kernels.
Thus a complete proof must use ordinary recursive-longitude membership,
endpoint cancellation, abelian matrix witnesses, transport-rack closure, or
another valid fixed-factor certificate.  It cannot rely on a rowwise
Artin-defect-only display.

## Exact B seed if A fails

A finite failure of descent separation is not itself outcome B.  It becomes a
B route only if it can be upgraded to:

```text
beta_j in B_{q_j}, q_j -> infinity,
```

such that every finite group has eventually identity recursive-longitude data
on `beta_j`, while the residual tuple still moves through the non-separated
lower endpoint motion.

Thus the current honest status is:

```text
No complete resolution yet.  The final missing theorem is descent separation.
```
