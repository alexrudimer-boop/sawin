# Rees rectangle cocycle flatness target

Date: 2026-06-03

This note records the current semigroup-corridor pressure test after the
rack point-pushing route was corrected.  The usable rack-only point-pushing
invariant is not bounded exponent of the whole point-pushing image.  It is an
operator-label Hurwitz quotient with a uniformly bounded-exponent vertical
kernel.  Therefore a semigroup/Green route can only help if it proves that the
non-rack part of a finite bijective YBE tower is still controlled by a fixed
finite group-Hurwitz base, up to bounded vertical noise.

The remaining semigroup bottleneck is a Rees rectangle cocycle.

## Local Rees data

For one regular residual transformation-semigroup component write the local
Rees matrix data as

```text
M[G; I, Lambda; P].
```

Rows are indexed by `Lambda`, columns by `I`, and the sandwich entry at
`(lambda,i)` is `p[lambda,i] in G`.  The rectangle obstruction is

```text
omega(lambda,mu; i,j)
  = p[lambda,i] p[mu,i]^{-1} p[mu,j] p[lambda,j]^{-1}.
```

With a base row `lambda0` and base column `i0`, the flat base-gauge condition
is

```text
p[lambda,i]
  = p[lambda,i0] p[lambda0,i0]^{-1} p[lambda0,i].
```

Equivalently, in this convention, all rectangle cocycles are trivial exactly
when the sandwich matrix factors as

```text
p[lambda,i] = r_lambda c_i.
```

The generated audit `proofs/rees_rectangle_cocycle_audit.md` fixes this
convention and checks two finite rows:

- a flat `C3` row-column matrix;
- the smallest nonflat `C2` square with three identity entries and one
  nonidentity entry.

## What ordinary Green theory does not prove

Ordinary Green/Rees theory supplies the component coordinates, the
Schutzenberger group, and the sandwich matrix.  It does not force
`omega=1`.  The Rees rectangle cocycle is exactly the residual obstruction to
collapsing a regular component into a pure group-label Hurwitz observer.

Thus the positive route must add a YBE-specific input.  A theorem that only
says "regular components have finite Schutzenberger groups" is too weak.  The
needed statement must say that the particular rectangles traversed by Artin
corridors in a finite bijective YBE solution are flat, or at least become
flat after a uniformly bounded vertical extension.

## YBE-flatness lemma target

A sufficient lemma would be the following.

**Finite Artin-Rees Flatness Lemma.**  Let `X` be a finite bijective
set-theoretic YBE solution.  Fix a finite residual quotient-fibre interval
appearing in the point-pushing tower and a regular Green component of its
transition semigroup.  Suppose an Artin corridor uses two independent local
row choices `lambda, mu` and two independent local column choices `i, j`
inside this component.  Then the associated Rees rectangle cocycle satisfies

```text
omega(lambda,mu; i,j) = 1
```

after passing to the finite operator-label quotient required by the corridor;
more generally, it is a row-column coboundary whose residual values land in a
finite vertical group of exponent bounded independently of the braid index.

The proof skeleton should be in Rees coordinates.

1. Normalize every local residual row by the base-gauge
   `p[lambda,i0] p[lambda0,i0]^{-1} p[lambda0,i]`.
2. Write the two sides of the braid/YBE equation on a three-strand corridor in
   Rees coordinates.
3. Compare the two factorizations of the same endpoint through the
   `(lambda,mu; i,j)` rectangle.
4. Show that all non-rectangle factors cancel by the bijective strand
   continuation identities.
5. Deduce `omega=1`, or record the remaining value as a bounded vertical
   kernel element.

This is the precise point where the proof must use the YBE equation, not just
finite semigroup structure.

## Obstruction route if flatness fails

The smallest algebraic obstruction pattern is the `C2` square

```text
G = C2 = {0,1}
I = {i0,i1}
Lambda = {lambda0,lambda1}

p[lambda0,i0] = 0
p[lambda0,i1] = 0
p[lambda1,i0] = 0
p[lambda1,i1] = 1.
```

Then

```text
omega(lambda0,lambda1; i0,i1) = 1 != 0.
```

This square is not, by itself, a YBE solution.  It is a search target.  A
negative route must realize this nonflat square, or a larger nonflat analogue,
as an actual finite bijective YBE local quotient-fibre interval traversed by
point-pushing Artin corridors.  The first meaningful braid-level test is a
three-strand local corridor, equivalently the `n=3`, `m=4` point-pushing
window when translated to the standard generators
`alpha_{1,4}, alpha_{2,4}, alpha_{3,4}`.

If such a YBE realization exists and its nonflat rectangle values persist in
the compatible point-pushing tower, then finite rack domination would require
a fixed finite `(H,C)` group-Hurwitz base and a fixed exponent bound `e` whose
vertical kernels absorb these rectangle cocycles.  A genuine obstruction must
prove that no such fixed bounded vertical extension can absorb the resulting
sequence.

The companion note `proofs/rees_braid_cocycle_obstruction_pattern.md`
sharpens this target.  It supplies explicit `C2`-labeled quotient rows on
four states which satisfy the local braid relation while the commutator
`[sigma1^2, sigma2^2]` closes on the quotient and records the nonidentity
Schutzenberger label.  Thus a counterexample search should not merely look
for a nonflat sandwich matrix; it should look for this labeled braid-cocycle
pattern inside an actual finite bijective YBE local interval.

## Relation to the rack route

For a finite rack `Y`, the operator map

```text
y |-> L_y
```

lands in `Inn(Y)` and gives an equivariant quotient to finite group-Hurwitz
tuples.  The vertical subgroup acts fibrewise by elements of `Inn(Y)`, hence
has exponent dividing `exp Inn(Y)`.  This is why unbounded order in the whole
point-pushing image is not an obstruction.

The Rees rectangle question is the semigroup analogue of that rack operator
label quotient.  Proving flatness would say that every finite bijective YBE
point-pushing tower has a finite augmented Artin-envelope model, up to bounded
vertical noise.  Producing a persistent nonflat YBE rectangle would give the
first credible obstruction to such a model.

At present this note records the exact missing lemma and the smallest
algebraic nonflat pattern.  It does not claim either the positive flatness
lemma or a YBE counterexample.
