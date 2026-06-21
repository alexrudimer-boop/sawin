# Framed finite abelian detectors are covered by dihedral conjugation racks

This note extends

```text
proofs/framed_c2_s3_all_arity_cover_proof.md
```

from `C2` to every finite abelian group.

Let `A` be a finite abelian group, written additively, and let `e=exp(A)`.
Let

```text
A_A = artin_detector_rack(A, include_trivial_two=False).
```

For `e > 1`, let

```text
D_e = C_{2e} semidirect C_2
```

where the nontrivial element of `C_2` acts on `C_{2e}` by inversion.  Thus
`D_e` is the generalized dihedral group of the cyclic group `C_{2e}`.  For
`e=1`, the statement is trivial.

## Theorem

For every finite abelian group `A` of exponent `e`, and every arity `n`,

```text
K_n(D_e^conj) <= K_n(A_A).
```

Thus the framed Artin detector of every finite abelian group is dominated by a
finite conjugation rack.

## Proof

First, describe the `A_A` action.  Since `A` is abelian, the first active
coordinate in `A_A` is merely carried by the strand permutation.  On pure
braids, the only possible motion is the framed coordinate.  That coordinate is
the Artin longitude value in `A`.

After abelianization, the Artin longitude matrix of a pure braid is exactly the
ordinary pairwise-linking matrix:

```text
L_i(beta) = sum_{j != i} lk_{ij}(beta) x_j
```

in additive notation.  Therefore a pure braid acts trivially on `A_A^n` iff

```text
lk_{ij}(beta) == 0 mod e
```

for every pair `i<j`.  Equivalently, the `A_A` action factors through

```text
B_n / (P_n' P_n^e),
```

the quotient that remembers the strand permutation and the pure braid
abelianization modulo `e`.

Now prove that `D_e^conj` detects this quotient.

If a braid has nontrivial strand permutation, place one nonidentity element of
`D_e` in a moved coordinate and identities elsewhere.  Identity-labelled
strands are transparent in a conjugation rack, so the braid is detected.
Hence

```text
K_n(D_e^conj) <= P_n.
```

Now let beta be pure and suppose some pairwise linking number
`lk_{ij}(beta)=k` is not divisible by `e`.  Put reflections

```text
r_0=(0,1),     r_1=(1,1)
```

in coordinates `i,j` and identities elsewhere.  Deletion naturality reduces the
action to the two-strand action of `A_12^k`.

In the reflection sector of `D_e^conj`, the braid generator acts by the
dihedral rack rule

```text
sigma(r_x,r_y) = (r_{2x-y}, r_x)
```

with labels in `C_{2e}`.  Therefore

```text
sigma^2(r_x,r_y) = (r_{x+2(x-y)}, r_{y+2(x-y)}).
```

For `(x,y)=(0,1)`, the displacement under `sigma^{2k}` is `-2k` in `C_{2e}`.
This is zero in `C_{2e}` iff `e` divides `k`.  Since `e` does not divide `k`,
the tuple is moved.  Thus beta is detected by `D_e^conj`.

Consequently, if beta lies in `K_n(D_e^conj)`, then beta is pure and all
pairwise linking numbers are divisible by `e`.  By the first paragraph, beta
acts trivially on `A_A^n`.

Hence

```text
K_n(D_e^conj) <= K_n(A_A)
```

for every `n`.

## Consequence

The central/abelian framed longitude layer is not an obstruction to the
finite-group detector route.  It is covered by ordinary finite conjugation
racks, namely generalized dihedral racks.

What remains in the Framed-to-Conjugation Cover Lemma is genuinely nonabelian:
for a nonabelian finite group `G`, the framed detector `A_G` records full
nonabelian Artin longitude values, not just pairwise linking modulo an
exponent.
