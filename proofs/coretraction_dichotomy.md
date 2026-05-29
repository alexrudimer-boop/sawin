# Two-sided coretraction dichotomy

## Statement

The two-sided retraction relation treats a fibre point as the parameter of the
one-sided local operations.  There is a dual relation that treats a fibre point
as an input coordinate.

For `x,x' in A_a`, define the forward coretraction profile by the conditions

```text
pr_1 T_{b,a}(y,x) = pr_1 T_{b,a}(y,x')   for all b,y,
pr_2 T_{a,b}(x,y) = pr_2 T_{a,b}(x',y)   for all b,y.
```

As in the retraction note, take the meet of this relation with the analogous
relation for the inverse local table, then iteratively refine by all opposite
unary contexts for both orientations.  Call the stable family `eta_infty`.

Then `eta_infty` is an admissible local congruence family for every finite
coloured local bijection.  Consequently, in a local-minimal interval it is
either all equality or all universal.

## Proof

The proof is the same two-sided triangle argument as in
`proofs/retraction_dichotomy.md`, with the roles of "parameter" and "input
coordinate" swapped.

Assume `eta` is below the forward coretraction profile and is stable under the
forward opposite-context closure.  If

```text
x eta_a x',  y eta_b y',
T_{a,b}(x,y)    = (u,v),
T_{a,b}(x',y')  = (u',v'),
```

then first change `x` to `x'` while holding `y` fixed.  The second outputs are
equal by the coretraction profile, and the first outputs are `eta`-related by
opposite-context closure.

Then change `y` to `y'` while holding `x'` fixed.  The first outputs are equal
by the coretraction profile, and the second outputs are `eta`-related by
opposite-context closure.

Thus the forward table sends `eta_a x eta_b` into
`eta_{a.b} x eta_{a*b}`.  Applying the same argument to the inverse local table
gives the reverse inclusion.  The stable two-sided family is therefore an
exact admissible congruence family.  This uses only finite descent and
bijectivity of the coloured tables.

## Universal side

If `eta_infty` is universal, then it is below the forward coretraction profile.
So, for every colour pair `(a,b)`, the first output is independent of the right
input and the second output is independent of the left input:

```text
T_{a,b}(x,y) = (L_{a,b}(x), R_{a,b}(y)).
```

Since `T_{a,b}` is a bijection, `L_{a,b}` and `R_{a,b}` are bijections between
the corresponding fibres.  This is the direct product-permutation branch.  On
a fixed base-colour orbit, braid words act fibrewise by a finite coloured
permutation groupoid; no fibre coordinate depends on another fibre coordinate.
The exact all-`n` braid-action normal form is implemented as
`direct_product_action(interval, color_tuple, word)` and recorded in
`proofs/product_permutation_branch.md`.  This is the local mechanism behind
the already bookkept permutation and coboundary measurable branches.

## Combined dichotomy

For a local-minimal interval, the two-sided retraction family and the
two-sided coretraction family are each extreme.  Therefore:

1. universal retraction gives the swapped product-permutation branch
   `T(x,y)=(L(y),R(x))`;
2. universal coretraction gives the direct product-permutation branch
   `T(x,y)=(L(x),R(y))`;
3. the only remaining primitive case is both retraction-free and
   coretraction-free.

The finite scans now reflect this sharper split.  Among the size-3
local-minimal congruence-cover intervals, the combined counts are:

```text
retraction=equality,   coretraction=equality:   18
retraction=equality,   coretraction=universal:   6
retraction=universal,  coretraction=equality:   110
```

The `18` bi-free cases in the tiny corpus are all already in known measurable
branches: `6` involutive, `11` nondegenerate, and `1` rack-type
nondegenerate.  This is still candidate search only, but the theorem-level
reduction has improved: a B-style counterexample must be bi-free after the two
symbolic dichotomies, or else lie in one of the product-permutation branches.
