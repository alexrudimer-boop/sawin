# Flip-across twisted unions preserve rack domination

This note isolates the closure theorem suggested by the size-four degenerate
non-involutive examples.  It proves a genuine positive operation on solutions,
but not the whole Sawin conjecture.

## Flip-across union

Let `(A,r_A)` and `(B,r_B)` be finite bijective set-theoretic YBE solutions.
Define

```text
X = A sqcup B
```

and define `r_X` by using the original crossing inside each component and the
ordinary flip across components:

```text
r_X(a,a') = r_A(a,a')                       a,a' in A
r_X(b,b') = r_B(b,b')                       b,b' in B
r_X(a,b)  = (b,a),   r_X(b,a) = (a,b).      a in A, b in B
```

Call this the flip-across twisted union.

The construction is implemented as
`flip_disjoint_union_solution` in
`src/ybe_domination/finite_braided_set.py`.

## YBE check

The color map

```text
kappa_n:X^n -> {A,B}^n
```

is equivariant for the braid action on `X^n` and the usual permutation action
`B_n -> S_n` on color words.  Indeed, an adjacent same-color crossing preserves
the two colors, and an adjacent mixed-color crossing is exactly the flip, so it
swaps the two colors.

For a triple, the braid words `sigma_1 sigma_2 sigma_1` and
`sigma_2 sigma_1 sigma_2` induce the same final permutation of the three
colored strands.  If all three colors are equal, equality is precisely the YBE
for `A` or for `B`.  If two colors occur, then only the two same-colored
strands can ever use a nontrivial component crossing; those two strands cross
once on each side, while the different-colored strand only flips past them.
Thus the same component crossing is applied to the same two strand values on
both sides.  Therefore `r_X` satisfies the YBE.

This argument also proves bijectivity: the same-color parts are bijective by
hypothesis, and the mixed-color parts are flips.

## Pure braid decomposition

Let `beta in P_n` be pure, and let `I subset {1,...,n}` be the set of
positions colored by `A`; its complement is colored by `B`.  The fiber of
`kappa_n` over this color pattern identifies with

```text
A^I x B^{I^c}.
```

Let

```text
d_I(beta) in P_|I|,       d_{I^c}(beta) in P_|I^c|
```

be the usual strand-deletion homomorphisms, forgetting the strands outside the
chosen subset.

On the fiber over the color pattern `I`, the action of `beta` decomposes as

```text
rho^X_n(beta)|_{A^I x B^{I^c}}
  =
rho^A_|I|(d_I beta) x rho^B_|I^c|(d_{I^c} beta).
```

Reason: mixed-color crossings are flips, so they merely move values along
their colored strands.  The only crossings that can change `A`-values are
crossings between two `A`-colored strands, and their ordered history is exactly
the deleted braid `d_I(beta)`.  The same argument applies to `B`.

## Domination theorem

Suppose finite racks `R` and `S` dominate `A` and `B`, respectively:

```text
ker(B_m -> Sym(R^m)) <= ker(B_m -> Sym(A^m))       for all m,
ker(B_m -> Sym(S^m)) <= ker(B_m -> Sym(B^m))       for all m.
```

Let

```text
Y = R sqcup S
```

be the flip-across union.  Since `R` and `S` are racks, `Y` is again a rack:
inside a component use the original rack operation, and across components set
`y*z=z`, so the crossing is the flip.

Then `Y` dominates `X=A sqcup B`.

Proof.  Fix `n` and let `beta in B_n` act trivially on `Y^n`.  The color map
for `Y` is equivariant through `B_n -> S_n`.  Since both components of `Y` are
nonempty, triviality on all of `Y^n` forces `beta` to fix every color word, so
`beta in P_n`.

Now choose any color pattern `I`.  By the pure decomposition for `Y`, the
restrictions

```text
d_I(beta)       and       d_{I^c}(beta)
```

act trivially on `R^|I|` and `S^|I^c|`.  By the component domination
hypotheses, they act trivially on `A^|I|` and `B^|I^c|`.  Applying the pure
decomposition for `X`, `beta` acts trivially on the fiber of `X^n` over this
color pattern.  Since the pattern was arbitrary, `beta` acts trivially on
`X^n`.

Thus

```text
ker(B_n -> Sym(Y^n)) <= ker(B_n -> Sym(X^n))
```

for every `n`, as required.

## Kernel-equivalence corollary

If the component dominators have equality of braid kernels with the components,
then the flip-across unions also have equality of braid kernels.  The converse
direction of the proof is the same: if `beta` acts trivially on `X^n`, then it
is pure by color equivariance, and the deleted component braids act trivially
on `A` and `B`; component kernel equality transfers this to `R` and `S`, and
the pure decomposition gives triviality on `Y^n`.

## Consequence

Finite-rack domination is closed under flip-across twisted union.  Therefore
the known positive families are closed under iterating this operation.  In
particular, twisted unions of left-nondegenerate pieces, involutive/trivial
pieces, and already rack-equivalent pieces remain dominated after replacing
the component detectors by the flip-across union of their rack detectors.

This explains why the observed size-four Type B degenerate non-involutive
examples are not counterexamples: their mixed-block structure is exactly a
flip-across union, so the color-pattern decomposition reduces domination to
the component pieces.

The theorem does not prove that every finite degenerate solution decomposes in
this way.  A remaining obstruction would have to be a genuinely non-split
hidden-fiber action that is not reducible to flip-across component deletion and
is not detected by any finite rack gauge.
