# Non-permutation size-three higher-arity frontier

Date: 2026-06-06

This note records the post-q=5 frontier for the non-permutation
\(|X|=3\) branch, following the reported closure of the arity-3 endpoint gate
in `proofs/nonperm3_arity3_q5_resolution.md`.

## Status after q=5

Reported finite endpoint-gate result:

```text
non-permutation |X|=3, arity 3
principal bad endpoint pairs:       37692
finite rack separated:              37692
remaining unresolved candidates:        0
```

Together with the arity-2 checkpoint, this closes the known fixed-arity
endpoint-gate batches through arity 3 for non-permutation size-three
solutions.  It does not, by itself, prove all-arity finite-rack domination.

The q=5 certificate is still recorded as externally reported data until the
full JSON certificate and verifier are available in the local workspace.

## What arity 3 gives

Each verified contextual detector schema \((M,Q,\alpha)\) is reusable in every
arity where the same evaluated contextual endpoint pattern occurs: the
contextual \(T\)- and \(R\)-relations are checked in \(M\times X\times M\),
not in a single tuple orbit.

Thus the q=5 closure is useful beyond the literal finite count.  It supplies a
finite list of endpoint readouts that can separate any higher-arity endpoint
pair whose prefix and suffix contexts evaluate to one of the same separated
patterns.

What is not proved is the bounded-core assertion:

```text
every higher-arity bad endpoint pair has a detector-separated core of
arity at most 3.
```

That assertion is a new theorem.  Without it, a higher arity could contain a
Brunnian or high-context kernel-fiber monodromy: all arity-2 and arity-3
shadows are harmless, while the full \(n\)-strand action still moves \(X^n\).

## Width-3 propagation target

The most concrete all-arity bridge is a width-3 relative parabolic generation
statement.

For a fixed non-permutation size-three table \(X\), let \(Y_X\) be the
componentwise product of the distinct finite rack targets appearing in the
verified arity-2 and arity-3 endpoint detector schemas for \(X\).  This product
should be represented by its component actions rather than physically expanded.

For each arity \(n\), write

```text
K^Y_n = ker(B_n -> Sym(Y_X^n))
H^X_n = ker(B_n -> Sym(X^n)).
```

Finite-rack domination by this detector product is:

```text
K^Y_n <= H^X_n for every n.
```

Let \(J^Y_{3,n}\) be the normal closure in \(B_n\) of all consecutive
parabolic copies of \(K^Y_k\) for \(k\le3\).  A sufficient all-arity theorem is:

```text
rho^X_n(K^Y_n) = rho^X_n(J^Y_{3,n}) for every n.
```

The stronger rack-side version \(K^Y_n=J^Y_{3,n}\) would also suffice, but the
relative \(X\)-realized equality is the actual requirement.

If this statement holds, then the arity-2 and arity-3 endpoint closures
propagate to every arity for this \(X\).

## Next computations

1. Import the q=5 artifacts:

```text
proofs/nonperm3_arity3_q5_resolution_certificate.json
proofs/nonperm3_arity3_q5_resolution_verifier.py
expected reported sha256:
376e901839c978530ecd32893da56de5ff69b26dd3c407d1cb3eda365c63fc75
```

The verifier should recompute the 55 non-permutation tables, all 37,692
arity-3 bad endpoint pairs, the 22 new q=5 schemas, the 216 new coverages, and
`remaining_unresolved_candidates 0`.

2. Build a detector-product index for each of the 55 non-permutation tables:

```text
table X
  distinct target rack tables Q used by arity-2 and arity-3 detector schemas
  monoid/alpha endpoint schemas attached to each Q
  component action representation for Y_X = product(Q_i)
```

3. Directly verify the base kernel inclusions:

```text
K^Y_2 <= H^X_2
K^Y_3 <= H^X_3
```

These should follow from the endpoint gate, but a direct joint-image
certificate is a cleaner bridge from endpoint separation to braid-kernel
domination.

4. Run the first relative cross-effect audit:

```text
C^{X,Y}_{3,4} = rho^X_4(K^Y_4) / rho^X_4(J^Y_{3,4})
```

Then attempt \(n=5\) and \(n=6\) as feasible.  A trivial quotient is evidence
for width-3 propagation.  A nontrivial quotient supplies a concrete
higher-arity witness:

```text
table X
arity n >= 4
braid beta in K^Y_n
moved tuple x with beta.x != x in X^n
proof beta is not generated, as an X-action, by width <= 3 detector-kernel
relations
```

This would not yet be a Sawin counterexample.  It would be a failure of the
current finite detector product and would need to be promoted to a cofinal
rack-prefix obstruction.

5. In parallel, run the endpoint-pattern extension scan at arity 4:

```text
enumerate principal bad endpoint pairs in arity 4;
evaluate all imported arity-2 and arity-3 schemas on their M-contexts;
count separated pairs and misses;
classify misses by monoid context pattern.
```

No misses in arity 4 and 5 would be strong finite evidence.  It would still
not replace the symbolic width-3 or bounded-core theorem.

## Smoke audit

As a quick check, the displayed q=5 rack for the first arity-3 candidate was
tested as a single detector rack against that same \(X\) using the existing
componentwise cross-effect helper.

```text
X = [0,3,6,1,4,7,5,2,8]
Y = displayed q=5 rack from nonperm3_arity3_q5_resolution.md
state_limit = 200000

n=2:
  joint_image_size = 12
  kernel_image_size = 1
  parabolic_image_size = 1
  quotient_size = 1
  quotient_nontrivial = False
  truncated = False

n=3:
  truncated = True

n=4:
  truncated = True
```

This is not a detector-product certificate.  It only shows that naive
joint-image closure for even one q=5 component becomes too large at arity 3
under the generic closure algorithm.  The higher-arity plan therefore needs
the imported detector-product index plus stronger compression, or a symbolic
parabolic-generation argument.

The implementation hook for the product-index version is:

```text
ybe_domination.componentwise_realized_parabolic_cross_effect_audit
tools/run_componentwise_cross_effect_audit.py
```

It stores the detector side as a tuple of component rack permutation images,
which is equivalent to the Cartesian product detector but avoids constructing
the product rack state set.

The decision rule for the first full product audit is:

```text
if any non-permutation size-three table has quotient_nontrivial = True:
  the width-3 propagation lemma is false for that detector product;

if all 55 rows are untruncated and quotient_size = 1:
  there is no four-strand obstruction, but an all-n induction is still needed;

if any row truncates:
  the result is inconclusive, and the closure step needs stronger permutation
  group compression.
```

## Exact missing lemma

For the current non-permutation \(|X|=3\) endpoint route, the missing lemma is:

```text
Width-3 endpoint/rack-kernel propagation.

For every non-permutation size-three YBE table X, let Y_X be the product of
the finite rack targets appearing in the verified arity-2 and arity-3 endpoint
detector basis.  If a braid beta is invisible to Y_X in arity n, then its
action on X^n is generated, as an X-action, by consecutive parabolic copies of
invisible actions in arities 2 and 3.
```

Equivalently:

```text
rho^X_n(K^Y_n) = rho^X_n(J^Y_{3,n}) for all n.
```

For a complete MathOverflow answer, the broader missing theorem is:

```text
Primitive endpoint-change finite-basis theorem.

For every finite bijective YBE solution X, finitely many finite-rack-separable
one-coordinate contextual endpoint-change patterns cover every actual
kernel-fiber bad pair.
```

The q=5 batch is positive finite evidence for this strategy in the
non-permutation size-three arity-3 endpoint gate.  The all-arity bridge remains
the unsolved part.
