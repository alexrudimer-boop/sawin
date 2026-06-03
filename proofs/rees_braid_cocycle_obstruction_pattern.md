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

## Direct locality shadow

There is an immediate caution.  A literal three-strand action coming from a
set-theoretic solution has coordinate-local shadows:

```text
sigma1 preserves the third-coordinate fibres,
sigma2 preserves the first-coordinate fibres.
```

Therefore, if the four quotient states themselves were a visible direct
coordinate quotient, `s1` would have a nontrivial fixed partition and `s2`
would have a nontrivial fixed partition, and some pair of those partitions
would jointly separate the four states.

The generated audit checks this necessary direct-locality condition.  A
control `2 x 2` coordinate model passes.  The obstruction rows above do not:
both `s1` and `s2` are four-cycles, so neither has a nontrivial fixed
partition.  Consequently this pattern cannot be realized as a literal
four-state coordinate-local quotient of a three-strand action.

This does not rule out realization inside a finite bijective YBE solution.
It narrows the realization problem: the pattern would have to appear deeper
in a quotient-fibre interval after the outside-coordinate partitions have
already been collapsed, transported, or hidden by the residual construction.

The generated audit also performs a direct adjacent two-body search for
`|A|=2`: it asks whether there is a single bijection `R: A^2 -> A^2` and an
embedding of the four quotient states into `A^3` such that `R` on coordinates
`(1,2)` induces `s1` and the same `R` on coordinates `(2,3)` induces `s2`.
No such realization exists, even before requiring `R` to satisfy YBE on all
of `A^3`.  Hence the obstruction pattern is not a direct two-element
three-strand set-theoretic action; any actual YBE realization must be less
literal.

There is, however, a raw adjacent-slice realization once one outside
coordinate is hidden.  Because both `s1` and `s2` are four-cycles, the direct
locality partitions force the embedded states to have form

```text
(a0, m_q, c0).
```

If the basis is exactly the four middle symbols, the two forced slices overlap
at `(a0,c0)` and would require fixed points of both rows.  No such fixed
points exist.  With one extra outer symbol the overlap disappears, and the
partial rules

```text
R(a0,m_q) = (a0,m_{s1(q)}),
R(m_q,c0) = (m_{s2(q)},c0)
```

are consistent and extend to a bijection of `A^2`.  The generated audit
constructs such a raw extension for `|A|=5`, but the displayed completion does
not satisfy YBE on all of `A^3`.  The remaining realization problem is
therefore a global YBE-completion problem for this partial adjacent slice.

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
