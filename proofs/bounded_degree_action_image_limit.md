# Bounded-Degree Action-Image Limit

This note records a common false A-route.  It is tempting to take the finite
braid-action image

```text
I_n(X) = rho_{X,n}(B_n) <= Sym(X^n)
```

or the product of the degree-`n` structure-orbit holonomy groups, and use it
as the finite detector group.  This cannot by itself prove Sawin domination,
because the group then depends on the braid index `n`.

## Fixed-Degree Images Are Not Uniform Detectors

For each fixed `n`, the action image `I_n(X)` is finite.  Exact image closure
can therefore prove fixed-degree statements such as:

```text
for this n, no braid in the tested kernel state moves X^n.
```

But Sawin domination asks for one finite rack `Y`, hence one finite detector
group in the sharp-obstruction construction, working for every braid index.
The family `I_n(X)` is not such a group unless it factors through a single
finite group `G_X` independent of `n`.

The same warning applies to structure-orbit holonomy.  Degree-`n` structure
classes are exactly `B_n`-orbits in `X^n`, and each orbit has a finite
internal action group.  These groups are excellent places to locate residual
motion, but the collection changes with `n`.  A proof must show that all
these moving holonomy groups are controlled by fixed finite longitude
detector factors, such as Green kernel-block groups, Schutzenberger groups,
product-label groups, affine/cyclic factors, or another finite group built
from the interval data.

## Not A Counterexample By Itself

Moving image growth also does not prove outcome B.  Racks themselves can have
growing braid-action images.  For example, the three-point dihedral rack has
larger degree-`4` structure-orbit/action images than degree `3`, but it is
dominated by its own finite inner group through the standard rack longitude
formula.  Thus a B proof must show more than moving finite image growth: it
must produce a normalized-law sequence whose longitudes are eventually
trivial in every fixed finite group while the moving action image still acts
nontrivially.

This is the role of
`proofs/moving_variety_counterexample_criterion.md` and
`proofs/structure_orbit_law_obstruction.md`.

## Correct Use

Fixed-degree action-image audits remain useful in two ways.

- They can disprove an overoptimistic proposed detector at a specific degree
  by finding an exact kernel mover.
- They can identify the moving holonomy groups that a normalized-law B
  construction would need to keep nontrivial.

They cannot replace the all-`n` finite-longitude factorization theorem, and
they cannot justify a rack whose construction depends on `n`.
