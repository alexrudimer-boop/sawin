# Regular-module framed-to-conjugation cover frontier

This note records the strongest current candidate for replacing framed Artin
detector racks by finite conjugation racks.

It also records the proof gap precisely.  The regular-module construction is
the right next target, but the unconditional cover theorem is not yet proved
from the present ingredients.

## Framed detector

Let `G` be a finite group and write

```text
A_G = artin_detector_rack(G, include_trivial_two=False).
```

The active labels are pairs `(g,u) in G x G`.  The braid action records:

1. the Artin image tuple in `G`;
2. the Artin longitude tuple in `G`.

Thus, for pure braids, nontriviality of the `A_G` action is precisely
nontriviality of some Artin longitude value in `G`.

## Candidate cover group

Let

```text
V_G = F_2[G]
```

be the left regular permutation module of `G` over `F_2`, and define

```text
C_reg(G) = V_G semidirect G,
```

where `G` acts on `V_G` by left translation of basis elements.

The left regular action is faithful: if `l != 1` in `G`, then `l` moves the
basis vector `[1]`.

The desired cover statement is:

```text
K_n(C_reg(G)^conj) <= K_n(A_G^+)
qquad for all n.
```

If true, every finite framed Artin detector is dominated by a finite
conjugation rack.

## Where the naive proof works

Let beta be a pure braid and fix an assignment

```text
x=(x_1,...,x_n) in G^n.
```

Let

```text
l_i = L_i(beta)(x_1,...,x_n)
```

be an Artin longitude value.  If beta is invisible to
`C_reg(G)^conj`, then every lift of the assignment to
`C_reg(G)^n` is fixed.

Projecting to `G` shows that `l_i` centralizes `x_i`.

If the vector part of the lifted longitude were independent of the vector
coordinate `v_i`, then varying `v_i` would force

```text
l_i v_i = v_i
qquad for all v_i in V_G.
```

Faithfulness of the regular action would imply `l_i=1`.

This is exactly the intended regular-module detection mechanism.

## The gap

The vector part of the lifted longitude is not generally independent of the
input vector coordinates.  In particular, it can depend on `v_i` itself.

Writing the lifted longitude in `C_reg(G)` as

```text
(a,l_i),
```

the vector term `a` is a Fox-derivative expression in the input vectors.  The
fixed-point equation has the schematic form

```text
(l_i - 1)v_i + (1 - x_i) a(v_1,...,v_n) = 0.
```

The second term can, in principle, cancel the first.  Therefore the elementary
argument "vary `v_i`, so `l_i=1`" is incomplete.

## Exact missing lemma

The regular-module cover is equivalent to the following finite Fox-separation
statement.

```text
Regular-Module Artin Longitude Separation Lemma.

Let G be finite.  Let beta be a pure braid.  Suppose some Artin longitude
value L_i(beta)(x_1,...,x_n) is nonidentity in G.

Then beta acts nontrivially on C_reg(G)^n under the conjugation-rack Hurwitz
action, where C_reg(G)=F_2[G] semidirect G.
```

Equivalently,

```text
K_n(C_reg(G)^conj) <= K_n(A_G)
```

for all `n`.

The missing point is exactly to prove that the Fox-derivative vector terms in
`F_2[G]` cannot cancel every nontrivial Artin longitude value simultaneously.

## Evidence and solved subcases

The abelian case is already solved by generalized dihedral groups:

```text
proofs/framed_abelian_dihedral_cover_theorem.md
```

For `G=C2`, the cover reduces to the mod-2 pure quotient and is dominated by
`S3^conj`:

```text
proofs/framed_c2_s3_all_arity_cover_proof.md
```

The regular-module candidate passes small direct checks:

```text
G=C2, n=2,3;
G=C3, n=2.
```

These checks are not a proof of the Fox-separation lemma.

## Consequence if the lemma is proved

If the Regular-Module Artin Longitude Separation Lemma holds, then every finite
framed envelope

```text
P_X = A_{H_1}^+ x ... x A_{H_s}^+
```

can be replaced by the finite conjugation rack

```text
C_reg(H_1)^conj x ... x C_reg(H_s)^conj.
```

Then the only remaining Sawin-hard step is the Uniform Framed Fan-Envelope
Theorem, equivalently exclusion of diagonal Brunnian fan ghosts.

## Correct current status

The framed-to-conjugation bridge is reduced to a concrete Fox-calculus problem
for Artin longitudes in the regular module `F_2[G]`.

It is not currently proved unconditionally in this worktree.
