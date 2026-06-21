# Uniform Brunnian fan-evaluation frontier

This note records the current sharp endpoint of the finite-group detector
route.

The remaining problem is no longer a framed-rack issue, a central-value issue,
or a fixed-arity issue.  Those have been separated out.  The only remaining
uniformity question is whether one finite group can separate all
`X`-visible Brunnian fan words.

## Current exact reduction

Let `X` be a finite bijective set-theoretic YBE solution.

For each `m >= 2`, let

```text
L_m = ker(P_m -> P_{m-1}) ~= F_{m-1},
```

with fan generators

```text
y_i = A_{i,m},        1 <= i <= m - 1.
```

Let

```text
Br_m subset L_m
```

be the ordinary Brunnian fan subgroup.  A word

```text
w(y_1,...,y_{m-1}) in Br_m
```

is `X`-visible if

```text
rho_m^X(w) != 1.
```

The previous criterion states that if there are finite groups

```text
H_1,...,H_s
```

such that every `X`-visible Brunnian fan word has a nonidentity evaluation in
some `H_i`, then `X` is dominated by a finite conjugation rack.

Because a finite family of finite groups can be replaced by their direct
product, this is equivalent to the following single-group statement.

## Uniform Brunnian Fan-Evaluation Group Lemma

For every finite bijective YBE solution `X`, there exists a finite group `H_X`
such that for every `m >= 2` and every

```text
w in Br_m subset F(y_1,...,y_{m-1}),
```

one has

```text
rho_m^X(w) != 1
    =>
exists (h_1,...,h_{m-1}) in H_X^{m-1}
such that w(h_1,...,h_{m-1}) != 1.
```

Equivalently, every Brunnian fan word that is a law on `H_X` is already
`X`-invisible:

```text
w is a law on H_X and w in Br_m
    =>
rho_m^X(w) = 1.
```

This is the cleanest finite-group target.

## Why this would solve Sawin

Assume the Uniform Brunnian Fan-Evaluation Group Lemma for `X`.

Let

```text
C_reg(H_X) = F_2[H_X] semidirect H_X
```

with `H_X` acting on `F_2[H_X]` by the left regular action.  The fan-only
regular-module theorem says that any nonidentity evaluation of a fan word in
`H_X` is detected by the conjugation rack

```text
C_reg(H_X)^conj.
```

Therefore

```text
Br_m cap K_m(C_reg(H_X)^conj) subset K_m(X)
```

for every `m`.

The pointed-Brunnian reduction then gives

```text
K_n((C_2 x C_reg(H_X))^conj) subset K_n(X)
```

for every `n`.  Thus `X` is dominated by the finite conjugation rack

```text
(C_2 x C_reg(H_X))^conj.
```

So proving the single-group lemma proves the finite-group detector theorem,
and hence Sawin's finite-rack domination theorem.

## Equivalent no-ghost form

The negation is a diagonal law ghost:

there exist

```text
m_j -> infinity,
w_j in Br_{m_j},
rho_{m_j}^X(w_j) != 1,
```

such that for every fixed finite group `H`, the word `w_j` is eventually a law
on `H`.

That means:

```text
for every finite H,
for all sufficiently large j,
for all (h_1,...,h_{m_j-1}) in H^{m_j-1},
w_j(h_1,...,h_{m_j-1}) = 1.
```

This is the only remaining obstruction on the finite-group route.

It is important that this is a diagonal obstruction.  No individual nontrivial
fan word is invisible to all finite groups, because free groups are residually
finite.  The issue is that the detecting finite group might have to grow with
`j`.

## Most plausible positive route

For each `m`, set

```text
G_m^X = rho_m^X(L_m),
g_{m,i} = rho_m^X(A_{i,m}).
```

Then an `X`-visible Brunnian fan word is precisely a word

```text
w in Br_m
```

with

```text
w(g_{m,1},...,g_{m,m-1}) != 1
```

inside the finite moving group `G_m^X`.

A sufficient theorem would be:

```text
Marked Fan-Image Variety Bound.

There exists a finite group H_X such that, for every m, every Brunnian word
that is a law on H_X is also a law on the marked tuple
(g_{m,1},...,g_{m,m-1}) whenever it lies in Br_m.
```

Equivalently, the Brunnian-relevant identities of all moving fan-image tuples
are implied by the identities of one fixed finite group.

The distinction between this exact marked condition and the stronger full
group-variety condition `G_m^X in var(H_X)` is recorded in

```text
proofs/marked_fan_image_variety_bound_frontier.md
```

The natural proof attempt is finite-state:

1. Encode the action of the fan generators `A_{i,m}` on `X^m` by the finite
   local transition data seen by the moving last strand.
2. Assume a diagonal ghost exists.
3. Choose a minimal pair of tuples in `X^{m_j}` separated by `w_j`.
4. Extract a recurrent transition pattern from the finite alphabet of local
   states.
5. Convert that recurrent pattern into a fixed finite group `H_X`.
6. Show that `w_j` has a nonidentity evaluation in `H_X` for infinitely many
   `j`, contradicting that `w_j` is eventually a law on every fixed finite
   group.

This is the next best theoretical step.

## Most plausible counterexample route

To refute Sawin through this frontier, one must construct a finite `X` and
Brunnian fan words `w_j` with arities tending to infinity such that:

```text
rho_{m_j}^X(w_j) != 1,
```

but `w_j` is eventually a law on every fixed finite group.

This cannot come from:

- central or abelian fan-image values, since framed/regular-module detectors
  detect them;
- fixed arity, since `G_m^X` itself detects all `X`-visible words in that
  arity;
- one fixed moving image variety, since a fixed finite group generating that
  variety would kill the ghost.

Thus a genuine counterexample must have finite fan-image groups whose
Brunnian-relevant law theory escapes every fixed finite group variety.

## Prompt for the next proof attempt

```text
Prove or refute the Uniform Brunnian Fan-Evaluation Group Lemma.

Let X be a finite bijective set-theoretic YBE solution.  For each m, let
L_m = ker(P_m -> P_{m-1}) ~= F_{m-1}, generated by y_i = A_{i,m}, and let
Br_m <= L_m be the ordinary Brunnian fan subgroup.

Show that there exists one finite group H_X such that every X-visible
Brunnian fan word has a nonidentity evaluation in H_X:

    rho_m^X(w) != 1
        =>
    exists h_1,...,h_{m-1} in H_X with
        w(h_1,...,h_{m-1}) != 1.

Equivalently, exclude a diagonal sequence m_j -> infinity and w_j in Br_{m_j}
such that rho_{m_j}^X(w_j) != 1 while w_j is eventually a law on every fixed
finite group.

Suggested proof strategy:
extract a finite recurrent transition type from the X-action of the fan
generators, build a fixed finite group H_X realizing that transition type, and
show every recurrent X-visible Brunnian fan word evaluates nontrivially in
H_X.

If proved, Sawin follows with the explicit finite conjugation rack

    (C_2 x C_reg(H_X))^conj,

where C_reg(H_X) = F_2[H_X] semidirect H_X.
```
