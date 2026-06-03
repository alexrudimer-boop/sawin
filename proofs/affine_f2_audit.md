# Affine F2 audit

## Purpose

This audit extends the linear `F_2^2` scan by allowing translations:

```text
R(x,y) = M(x,y) + t
```

where `M` is an invertible `4 x 4` matrix over `F_2` and `t in F_2^4`.
This is still a candidate search only.  Affine branches are already
bookkept as finite-G measurable, so the audit is not used as proof evidence
for the master theorem.  Its role is to stress-test the narrowed bi-free
branch in the smallest translated affine universe.

## Results

The generated report is `proofs/affine_f2_audit.json`.

```text
affine maps checked: 1048576
invertible affine maps: 322560
affine YBE tables: 481
local-minimal intervals: 84
affine-only bi-free primitive examples: 0
```

Combined two-sided retraction/coretraction counts among all `481` affine YBE
tables:

```text
retraction=equality,     coretraction=equality:       84
retraction=equality,     coretraction=proper_mixed:   12
retraction=equality,     coretraction=universal:       1
retraction=proper_mixed, coretraction=equality:       240
retraction=proper_mixed, coretraction=proper_mixed:    24
retraction=universal,    coretraction=equality:       120
```

All `84` local-minimal cases are bi-free.  Their branch tags are:

```text
12 involutive
24 involutive nondegenerate
46 nondegenerate
2  rack-type nondegenerate
```

The local-minimal output coordinate-kernel corridor closures split as:

```text
72 equality
12 universal
```

All `12` universal output-kernel closures have stable depth `1`, not depth
`0`; each of them is in the involutive branch.  Thus the translated affine
`F_2^2` universe does exhibit transported universal coordinate-kernel
corridors, but not outside the already finite-G-measurable involutive branch.

Thus the translated affine `F_2^2` universe has no local-minimal bi-free
example outside the already measurable involutive/nondegenerate/rack-type
branches.  The untagged affine examples in the full scan all have proper
mixed retraction/coretraction families, so they are not local-minimal
primitive intervals.

The generated full-twist companion audit
`proofs/affine_f2_full_twist_audit.md` also checks the central element
`(sigma_1 ... sigma_{n-1})^n` for `1 <= n <= 7` in this same universe using
affine block-map composition.  All `24` untagged affine rows have the prefix
order profile

```text
1, 2, 1, 2, 1, 2, 1.
```

Thus the untagged affine rows neither form primitive intervals nor stress the
central full-twist obstruction in the checked prefix.

## Consequence

The smallest translated affine four-point universe does not produce B and does
not expose a new bi-free local-minimal branch.  A counterexample must leave
this affine family, or exploit a larger affine construction in a way not seen
at `F_2^2`; either way, it still has to evade the finite-G measurable affine
branch in the user-provided reductions.
