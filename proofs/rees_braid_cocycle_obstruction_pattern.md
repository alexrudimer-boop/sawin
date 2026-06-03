# Rees braid-cocycle obstruction pattern

Date: 2026-06-03

This note records the sharpened obstruction-route output from the theoretical
ChatGPT pressure test.  The previous Rees note isolated the sandwich
rectangle cocycle.  The new point is that the local braid/YBE equation can
hold for group-labeled quotient rows while the Rees rectangle cocycle remains
nontrivial.

This is not yet a finite bijective YBE counterexample.  It is a finite local
pattern that any counterexample search should try to realize inside an actual
quotient-fibre interval.

## The finite pattern

Use the group `C2 = {0,1}` additively, with `0` the identity.  Let

```text
I = {i0, i1}
Lambda = {lambda0, lambda1}.
```

Take the Rees sandwich matrix

```text
          i0  i1
lambda0   0   0
lambda1   0   1
```

Then

```text
omega(lambda0, lambda1; i0, i1) = 1.
```

So the rectangle is not flat and the sandwich matrix is not row-column
coboundary in the convention used by
`proofs/rees_rectangle_cocycle_flatness_target.md`.

Now set

```text
Omega = {q00, q01, q10, q11}.
```

Define two quotient permutations and two `C2`-labels:

```text
q        q00  q01  q10  q11
s1(q)    q10  q11  q01  q00
ell1(q)  0    0    0    1
s2(q)    q01  q10  q11  q00
ell2(q)  0    0    1    0
```

The lifted row maps on `Omega x C2` are

```text
T_k(q,g) = (s_k(q), g + ell_k(q)).
```

The audit `proofs/rees_braid_cocycle_obstruction_audit.md` verifies

```text
T1 T2 T1 = T2 T1 T2.
```

Thus the row labels satisfy the local braid cocycle identity.

## Closed commutator holonomy

Let

```text
beta = [sigma1^2, sigma2^2]
     = sigma1^2 sigma2^2 sigma1^-2 sigma2^-2.
```

For the finite row pattern above, the induced transformation satisfies

```text
T_beta(q,g) = (q, g + 1)
```

for every `q in Omega`.  Hence `beta` is closed on the quotient state but
produces the nontrivial Schutzenberger label `1`.

This is the local mechanism missing from a naive semigroup proof.  The YBE
relation forces a braid cocycle identity; it does not by itself force that
cocycle to be exact or Rees-flat.

## Meaning for rack domination

For a finite rack, the operator-label quotient gives a fixed finite
group-Hurwitz tower and the residual vertical kernel has uniformly bounded
exponent.  Therefore a finite bijective YBE solution can only be obstructed
by this route if an actual point-pushing tower contains compatible nonflat
Rees braid-cocycle holonomy that cannot be absorbed by any fixed bounded
vertical extension over a fixed finite group-Hurwitz base.

The concrete search target is:

1. Find a finite bijective degenerate YBE solution.
2. Find a local quotient-fibre interval whose residual rows contain, up to
   relabelling and Rees gauge, the `C2` pattern above.
3. Check the braid index `m=3` corridor for the commutator
   `[sigma1^2, sigma2^2]`.
4. Verify that the quotient state closes while the Schutzenberger `C2`
   factor records the nontrivial label.
5. Prove this persists compatibly in the point-pushing tower and cannot be
   routed through any fixed finite group-Hurwitz base with bounded-exponent
   vertical kernel.

If step 5 is achieved, this would be a real obstruction to finite rack
domination.  If every actual finite bijective YBE local interval forbids or
verticalizes this pattern, then the positive route becomes a precise
finite augmented Artin-envelope lemma.
