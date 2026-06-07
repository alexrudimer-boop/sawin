# Review: Strict A/B Attempt

Date: 2026-06-07

Verdict: no A/B.

This response did not prove Sawin's finite-rack domination statement and did
not give a fixed finite counterexample.  It is still useful because it
identified the two exact fatal blockers that remain after the detector-specific
survival theorem.

## Positive Blocker

The positive route breaks at all-arity finite contextual rack encoding for an
arbitrary genuinely degenerate finite bijective YBE solution.

The coordinatewise finite left-nondegenerate-cover shortcut cannot work in
general.  If

```text
pi : X_tilde -> X
```

were a finite coordinatewise braided quotient from a finite left-nondegenerate
solution, then for each `x in X` the first-coordinate map

```text
y -> pr_1 R_X(x,y)
```

would preserve positive fiber weights.  Hence it would be surjective, and
because `X` is finite, bijective.  Thus this cover method only applies when
`X` was already left-nondegenerate.

The remaining plausible positive route is non-coordinatewise: a contextual,
guitar, endpoint, or finite-state readout whose rack action separates all
`X`-orbits in every arity.  The missing theorem is:

```text
For every finite bijective X, there is a finite rack-valued contextual readout
whose product readout is orbit-separating for all n.
```

No proof of that all-arity orbit-separation theorem was given.

## Negative Blocker

The negative route breaks at freezing the varying-target detector survival
construction into one fixed finite target.

The known survival theorem says that for every finite rack detector `Q`, one
can choose a new rack target

```text
Conj(A_ell)
```

with `ell` avoiding the detector order `e(Q)`, and then produce unbounded
Brunnian words invisible to `Q` but visible to that new target.  This does not
give a Sawin counterexample because the target varies with `Q` and each target
is itself a rack.

The missing theorem for a negative answer is:

```text
There exists one fixed finite bijective YBE solution X such that every finite
rack prefix P_m has unbounded Brunnian words invisible to P_m^0 x T_2 but
visible to X.
```

No such fixed finite target was constructed.

## Prompt Consequence

The next theoretical prompt should not request another reduction or boundary
theorem.  It should directly attack one of the two fatal steps:

```text
Positive: prove the non-coordinatewise all-arity contextual/guitar endpoint
encoding theorem for arbitrary finite degenerate X.

Negative: construct one fixed finite degenerate X replacing the varying
Conj(A_ell) rack targets in the detector-survival argument.
```

