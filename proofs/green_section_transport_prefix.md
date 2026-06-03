# Green section transport finite-prefix audit

Date: 2026-06-03

This note records a finite-prefix check for the Green section transport
rigidity gate.

The symbolic gate says that hidden section branches must be compared using
actual deterministic completed-context transport, not formal Green/Rees or
ambient Schutzenberger moves.  A finite counterexample should therefore show
a nonidentity group-like atom-trivial loop in the actual completed-context
category that is not already routed to a known finite-G branch.

The generated audit

```text
proofs/green_section_transport_prefix_audit.md
```

scans every bijective YBE solution of sizes `2` and `3` at completed-context
depth `2`.  It uses the existing finite completed-context category and then
keeps only total bijective atom-trivial loops.  Reset-like atom-trivial
collapses are deliberately ignored because residual braid actions are
permutations.

The prefix result is:

```text
size 2:
  YBE solutions = 5
  hidden atom-trivial loop solutions = 1
  hidden bijective loop solutions = 0
  unresolved nonidentity group-like loop solutions = 0

size 3:
  YBE solutions = 73
  hidden atom-trivial loop solutions = 7
  hidden bijective loop solutions = 3
  nonidentity group-like loop solutions = 3
  involutive nonidentity group-like loop solutions = 3
  unresolved nonidentity group-like loop solutions = 0
```

Thus the finite prefix does not produce a new Green section-holonomy
counterexample.  The only nonidentity group-like atom-trivial loops through
this prefix occur in already known involutive rows.

This does not prove the all-depth rigidity lemma.  It is a diagnostic filter:
a genuine B-route example must now produce an actual group-like atom-trivial
loop outside the known involutive/permutation/rack/nondegenerate branches, and
then upgrade that loop to unequal transported units in a cyclic p-primary
hidden section fibre.
