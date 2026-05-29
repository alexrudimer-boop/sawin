# Small YBE law-braid search

Date: 2026-05-28

This note records a small bounded search for finite bijective YBE tables whose
action is moved by the embedded commutator law braid.

## Scope

The script `tools/run_small_ybe_law_search.py` checks:

- all bijective tables on a two-element set (`4! = 24` tables);
- the first `50,000` bijective tables on a three-element set, in deterministic
  permutation order.

For each YBE table it records whether the table is rack-type, and whether a
non-rack table is moved by the embedded commutator law braid in `B_3`.

This is deliberately not a proof and not a counterexample.  It is a bounded
candidate screen.

## Interpretation

A hit would only produce a local candidate: it would still need symbolic YBE,
an explicit normalized-law sequence, eventual invisibility for every finite
group, and explicit moved tuples for unbounded braid indices.

A miss only says that this small search region does not contain the desired
counterexample pattern.  It does not eliminate larger fibres, quotient colours,
or non-prefix portions of the size-three table enumeration.

The generated report is `proofs/small_ybe_law_search.json`.

