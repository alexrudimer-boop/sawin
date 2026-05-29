# Product label words

Date: 2026-05-28

This note records the word-level normal form for swapped and direct
product-permutation intervals.  It is a symbolic reduction of the remaining
product gap, not a proof of the Master Local-Minimal Residual Theorem.

## Formal Label Words

For a swapped product table

```text
T_{a,b}(x,y) = (L_{a,b}(y), R_{a,b}(x)),
```

the braid action can be lifted from actual fibre maps to formal words in the
finite label alphabet

```text
L_{a,b}^{+/-1}, R_{a,b}^{+/-1}.
```

At a positive crossing of current colours `(a,b)`, the old right strand moves
to the left and appends `L_{a,b}`, while the old left strand moves to the
right and appends `R_{a,b}`.  At a negative crossing, using the inverse base
edge `(a,b) -> (c,d)`, the old right strand appends `R_{a,b}^{-1}` and the
old left strand appends `L_{a,b}^{-1}`.

The helper

```text
swapped_product_label_word_action(interval, color_tuple, braid_word)
```

returns these formal words together with the same dependency vector as
`product_permutation_action`.  The evaluator

```text
evaluate_swapped_product_label_word(interval, source_color, label_word)
```

checks source and target colours and evaluates the formal word to the actual
finite fibre bijection.  Unit tests verify that evaluating every returned
formal word gives exactly the coordinate map in the ordinary product normal
form, including negative crossings.

For a direct product table

```text
T_{a,b}(x,y) = (L_{a,b}(x), R_{a,b}(y)),
```

the same finite label alphabet works, but the dependency vector is always the
identity.  At a positive crossing of current colours `(a,b)`, the left
coordinate appends `L_{a,b}` and the right coordinate appends `R_{a,b}`.  At a
negative crossing, using the inverse base edge `(a,b) -> (c,d)`, the left
coordinate appends `L_{a,b}^{-1}` and the right coordinate appends
`R_{a,b}^{-1}`.

The helper

```text
direct_product_label_word_action(interval, color_tuple, braid_word)
```

records those direct-branch formal words, and

```text
evaluate_direct_product_label_word(interval, source_color, label_word)
```

evaluates them.  The direct tests mirror the swapped tests and verify equality
with the coordinate maps in `direct_product_action()`.

## Remaining Detection Obligation

For a braid in the sharp-kernel setting, the base colours are fixed and the
Artin permutation is trivial.  In the swapped branch this makes the dependency
vector the identity; in the direct branch it is always the identity.  The
residual fibre action is therefore trivial exactly when every formal label
word evaluates to the identity in the finite coloured permutation groupoid.

Thus the unresolved product theorem can be stated sharply:

> Construct a finite group `G`, depending only on the interval and base
> detector, such that identity finite-G Artin-longitude data forces every
> base-fixed swapped or direct product label word to evaluate trivially.

The already closed subcases fit this word-level statement:

- coboundary label words reduce to gauge transport and vanish when the base is
  fixed;
- one-colour local-minimal label words reduce to powers of a single prime
  cycle and are detected by cyclic abelian longitudes;
- identity-base swapped product label words lie in the centralizer of one
  fibre permutation and reduce to the same cyclic branch under
  local-minimality.

The branch is therefore a special case of
`proofs/label_longitude_factorization.md`: if every base-fixed formal product
label word is an evaluation, or finite product of evaluations, of recursive
Artin longitudes in one finite label group `H`, then `A_H` detects the branch
for all braid degrees.  The remaining genuinely coloured product theorem is
to prove exactly this label-longitude factorization, or to construct a
formal product-label word sequence that violates every fixed finite-group
longitude detector.

The finite label group is now explicit.  In
`proofs/product_label_group_detector.md`, every label is totalized to a
permutation of the tagged fibre union `disjoint union_a {a} x A_a`, swapping
its source and target tagged fibres by the label and inverse when the colours
are different, and acting inside one tagged fibre when the colours agree.
The generated finite permutation groups are returned by
`swapped_product_label_group()` and `direct_product_label_group()`.  Unit
tests compare the restriction of totalized label-word evaluation with the
original partial product-label evaluators for both swapped and direct
branches.  This gives a concrete `H_prod`; the unsolved part is proving that
the base-fixed `H_prod` word is forced by recursive Artin longitudes for all
braid degrees.

There is also a smaller normalized holonomy target.  After the coboundary
audit chooses gauges `g_a`, a formal label word `f:A_s->A_t` can be evaluated
as `g_t f g_s^{-1}` on the model fibre.  The helpers
`product_holonomy_label_permutation()` and
`product_holonomy_closed_label_permutations()` expose this normalization.
On closed base paths, the pure gauge part telescopes away, leaving only this
finite holonomy permutation to be detected by Artin longitudes.

The first bullet is now a theorem-level subcase rather than a slogan:
`proofs/product_coboundary_telescope.md` proves that every coboundary label
word telescopes to `g_target^{-1}g_source`.  Therefore base-fixed direct
product coboundaries and base-fixed, permutation-trivial swapped
coboundaries have identity residual fibre action for all braid degrees.

A B-style product counterexample would have to give a sequence of base-fixed
braids whose Artin longitudes are eventually invisible to every finite group
but whose formal product label words remain nontrivial in this finite
groupoid.
