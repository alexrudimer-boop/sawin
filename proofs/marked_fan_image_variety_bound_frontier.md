# Marked fan-image variety bound frontier

This note gives the next proof/counterexample fork after the single-group
fan-evaluation reduction.

The finite-group detector route now asks for one finite group `H_X` whose
ordinary group laws control all `X`-visible Brunnian fan words.  This can be
viewed as a marked variety problem for the moving fan-image groups.

## Moving fan-image tuples

For a finite bijective YBE solution `X`, define

```text
L_m = ker(P_m -> P_{m-1}) ~= F_{m-1},
```

with fan generators

```text
y_i = A_{i,m}.
```

Let

```text
theta_m^X : L_m -> Sym(X^m)
```

be the restricted fan action, and set

```text
G_m^X = theta_m^X(L_m),
g_{m,i} = theta_m^X(y_i).
```

Thus every fan word `w(y_1,...,y_{m-1})` acts on `X^m` as

```text
w(g_{m,1},...,g_{m,m-1}).
```

The final finite-group basis lemma is equivalent to finding a finite group
`H_X` such that every Brunnian word that is a law on `H_X` is also a law on
the marked tuple

```text
(g_{m,1},...,g_{m,m-1})
```

for every `m`.

## Strong sufficient condition: fixed variety bound

A sufficient condition is:

```text
exists finite H_X such that G_m^X in var(H_X) for every m.
```

Then every ordinary group law of `H_X` holds on every element tuple of
`G_m^X`, hence in particular on the marked fan tuple.  Therefore every
Brunnian word law on `H_X` is `X`-invisible.

This condition is stronger than necessary.  Sawin only needs laws to hold on
the special marked tuple and only for words in the Brunnian subgroup `Br_m`.
The moving group `G_m^X` itself may fail to lie in one fixed variety for
irrelevant reasons outside the all-variable fan direction.

## Exact condition: Brunnian marked variety bound

The exact positive target is:

```text
exists finite H_X such that for every m and every w in Br_m,
    w is a law on H_X
        =>
    w(g_{m,1},...,g_{m,m-1}) = 1 in G_m^X.
```

Call this the Brunnian marked variety bound for `X`.

This is equivalent to the Uniform Brunnian Fan-Evaluation Group Lemma:

```text
rho_m^X(w) != 1
    =>
exists h_1,...,h_{m-1} in H_X
with w(h_1,...,h_{m-1}) != 1.
```

If the bound holds, the fan-only regular-module theorem gives the explicit
finite conjugation-rack detector

```text
(C_2 x C_reg(H_X))^conj,
qquad C_reg(H_X)=F_2[H_X] semidirect H_X.
```

## Exact failure: diagonal marked variety escape

Failure of the exact condition gives a sequence

```text
m_j -> infinity,
w_j in Br_{m_j},
w_j(g_{m_j,1},...,g_{m_j,m_j-1}) != 1,
```

such that `w_j` is eventually a law on every fixed finite group.

This is a diagonal marked variety escape.  It is stronger than merely showing
that the groups `G_m^X` grow or have unbounded order.  It must produce
Brunnian all-variable words that:

1. vanish on every fixed finite group eventually;
2. remain nontrivial on the particular marked fan tuple of `X`.

## False shortcuts

The following do not prove failure of Sawin.

### Growing group size

The sizes of `G_m^X` may grow while all Brunnian marked identities are still
controlled by one finite group.

### Escaping a fixed full variety outside Brunnian words

It may happen that `G_m^X` does not lie in `var(H)` for any fixed `H`, but the
escaping words are not Brunnian, or do not move the marked tuple
`(g_{m,1},...,g_{m,m-1})`.

### Central or abelian fan-image values

Central and abelian values are not an obstruction after the framed and
regular-module correction.  A nonidentity evaluation in any finite group is
enough to produce a finite conjugation-rack detector for fan words.

### Fixed arity

For each fixed `m`, the finite group `G_m^X` itself detects all `X`-visible
fan words in that arity.  Any genuine obstruction must have `m_j -> infinity`.

## Existing finite-prefix evidence

The rank-2 and rank-3 nonpermutation size-3 frontiers are already controlled.

The audit

```text
proofs/nonperm3_rank2_fan_image_structure_audit.md
```

records that, for the stored nonpermutation size-3 corpus:

- the hard rank-2 fan-image rows are marked-isomorphic to one group `H24`;
- the remaining rank-2 fan-image rows are abelian of order `1` or `4`;
- the `H24` row has derived-series orders `[24,8,2,1]`, including the
  central second-derived layer which conjugation racks alone miss.

After the framed/regular-module repair, that central layer is harmless for
fan words.  Thus rank 2 in this corpus is controlled by a fixed finite group,
for example a product of `H24` with the relevant abelian order-4 factors.

This evidence is deliberately limited.  It does not prove the uniform lemma,
because a genuine diagonal ghost must have rank tending to infinity.  It does
show that the previously identified `H24` central layer is not the final
obstruction.

The next audit

```text
proofs/nonperm3_rank3_fan_image_structure_audit.md
```

records the same kind of collapse in rank 3:

- the hard rank-3 rows are marked-isomorphic to one reusable group `F648`;
- all non-hard rank-3 rows are abelian of order `1` or `8`;
- `F648` has derived-series orders `[648,216,54,27,3,1]`.

Thus, in the stored size-3 nonpermutation corpus, the first unrecorded place
where marked fan-image variety escape could begin is rank `4`, not rank `2`
or rank `3`.  This is still only finite-prefix evidence; it is useful because
it rules out the most obvious low-rank central/abelian explanation.

The representative rank-4 probe

```text
proofs/nonperm3_rank4_fan_image_representative_probe.md
```

then identifies the first concrete higher-rank hard image to control:

- trivial representative row `0` has image order `1`;
- abelian representative row `6` has image order `16`;
- hard representative row `15` has image order `51840` and exponent `360`,
  with four fan generators of order `3` and pair products of order `6`.

This helps focus the next proof attempt.  It does not by itself threaten
Sawin, because growing marked fan-image groups are harmless unless they carry
Brunnian all-variable words that are eventually laws on every fixed finite
group but remain nontrivial on the marked tuple.  The rank-4 hard image is
therefore a finite pressure point, not a counterexample.

## Most plausible positive theorem

The strongest plausible positive theorem is a finite-state recurrence result:

```text
Finite-State Brunnian Marked Variety Bound.

For every finite bijective YBE solution X, the marked tuples
(G_m^X; g_{m,1},...,g_{m,m-1}) have Brunnian identities controlled by one
finite group H_X.
```

A proof should use the finite local nature of the YBE gate:

1. write the point-pushing action of `A_{i,m}` as a finite transducer on
   anchor labels and the moving strand state;
2. suppose a diagonal marked variety escape exists;
3. choose a minimal moved pair of `X^m` tuples;
4. extract a recurrent transition type from the finite set of local
   transition states;
5. build a fixed finite group realizing that recurrent transition type;
6. evaluate the same Brunnian word nontrivially in that group.

## Most plausible negative theorem

A counterexample must give:

```text
finite X,
m_j -> infinity,
w_j in Br_{m_j},
```

where `w_j` is eventually a law on every fixed finite group, but

```text
w_j(g_{m_j,1},...,g_{m_j,m_j-1}) != 1.
```

Equivalently, the marked fan-image tuples of `X` must escape every fixed
finite group variety in the Brunnian all-variable direction.

This is the current exact negative target.
