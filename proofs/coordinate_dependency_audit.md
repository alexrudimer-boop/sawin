# Coordinate dependency audit

This note records a narrow degenerate branch for the central
full-twist obstruction route.  It is not a classification of all
finite bijective set-theoretic YBE solutions.

## Same-side collapse

Let `R(x,y)=(f(x),h(x,y))` be a finite bijective YBE table whose
first output depends only on `x`.  Bijectivity makes `f` a
permutation and each map `h_x:y -> h(x,y)` a permutation.  Comparing
the first coordinate in `R_12 R_23 R_12 = R_23 R_12 R_23` gives
`f^2=f`, hence `f=id`.  The second coordinate then gives
`h_x^2=h_x` for every `x`, so each permutation `h_x` is the
identity.  Thus `R=id`.  Applying the side-opposite argument gives
the dual case where the second output depends only on `y`.

Therefore a same-side coordinate dependency cannot produce a
nontrivial full-twist obstruction.

## Opposite-side routing

If the first output depends only on `y`, then bijectivity forces that
one-variable first-coordinate map to be a permutation and also forces
the second-coordinate maps in the remaining variable to be
permutations.  The solution is nondegenerate.  The same argument
applies when the second output depends only on `x`.  These rows are
routed to the existing left-nondegenerate/guitar branch, whose
central full-twist order is bounded through the derived rack.

## Exact tiny-corpus census

- audited sizes: `[1, 2, 3]`;
- full-twist prefix: `1 <= n <= 5`;
- all coordinate-dependency rows closed: `True`.

### Size 1

- YBE tables: `1`;
- coordinate-dependency rows: `1`;
- same-side rows: `1`;
- opposite-side-only rows: `0`;
- unclosed coordinate-dependency rows: `0`;
- maximum checked full-twist order: `1`.

- profile counts: `{'first_depends_only_on_x+first_depends_only_on_y+second_depends_only_on_x+second_depends_only_on_y': 1}`;
- coordinate-dependency reasons: `{'same_side_dependency_identity_collapse': 1}`;
- known full-twist reasons: `{'involutive_artin_permutation': 1}`.

### Size 2

- YBE tables: `5`;
- coordinate-dependency rows: `5`;
- same-side rows: `1`;
- opposite-side-only rows: `4`;
- unclosed coordinate-dependency rows: `0`;
- maximum checked full-twist order: `2`.

- profile counts: `{'first_depends_only_on_x+second_depends_only_on_y': 1, 'first_depends_only_on_y+second_depends_only_on_x': 4}`;
- coordinate-dependency reasons: `{'opposite_side_dependency_nondegenerate_branch': 4, 'same_side_dependency_identity_collapse': 1}`;
- known full-twist reasons: `{'involutive_artin_permutation': 3, 'permutation_form_twist_order': 2}`.

### Size 3

- YBE tables: `73`;
- coordinate-dependency rows: `55`;
- same-side rows: `1`;
- opposite-side-only rows: `54`;
- unclosed coordinate-dependency rows: `0`;
- maximum checked full-twist order: `3`.

- profile counts: `{'first_depends_only_on_x+second_depends_only_on_y': 1, 'first_depends_only_on_y': 18, 'first_depends_only_on_y+second_depends_only_on_x': 18, 'none': 18, 'second_depends_only_on_x': 18}`;
- coordinate-dependency reasons: `{'opposite_side_dependency_nondegenerate_branch': 54, 'same_side_dependency_identity_collapse': 1}`;
- known full-twist reasons: `{'involutive_artin_permutation': 19, 'left_nondegenerate_derived_rack_exponent': 35, 'permutation_form_twist_order': 12, 'rack_inner_group_exponent': 7}`.

## Consequence for the MO route

A finite unbounded-central-full-twist counterexample, if it exists,
must avoid these one-coordinate dependency profiles.  In particular
it cannot be triangular in the elementary sense above; it must live
in the genuinely remaining degenerate classes not already routed
through the identity, permutation-form, rack, involutive,
left-nondegenerate/guitar, or affine `F_2` guardrails.
