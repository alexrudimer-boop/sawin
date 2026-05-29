# Congruence-chain mechanics

Date: 2026-05-28

This note records the executable mechanics behind the congruence-chain
reduction.  It is not a proof of the Master Local-Minimal Residual Theorem;
it is an audit layer ensuring that quotient intervals and local tables are
being constructed correctly.

## Congruences

For a finite braided set `(X,R)`, a partition `theta` is treated as a
congruence when

```text
x ~ x' and y ~ y'
implies
R_1(x,y) ~ R_1(x',y') and R_2(x,y) ~ R_2(x',y').
```

The module `src/ybe_domination/congruence.py` implements:

- `is_congruence(X, theta)`;
- `congruences(X)`, for small finite examples only;
- `quotient_solution(X, theta)`, returning the quotient braided set and the
  quotient map;
- `interval_covers(...)`, detecting cover relations in the finite congruence
  lattice;
- `maximal_congruence_chain(X)`, selecting a saturated chain from equality to
  universal;
- `CongruenceInterval(X, lower, upper).local_interval()`, extracting the
  coloured local residual table for `X/lower -> X/upper`.

## Local interval from a congruence cover

Given congruences `lower <= upper`, the interval

```text
X/lower -> X/upper
```

has:

- colours = `upper`-blocks;
- fibre over colour `C` = the `lower`-blocks contained in `C`;
- base operation induced by the quotient `X/upper`;
- local table induced by the quotient `X/lower`.

The extracted `LocalInterval` is then checked against the coloured YBE and
against the same admissible-congruence-family test used for semisplit audits.

## Cover versus local-minimality

For finite congruence lattices, an interval cover has no intermediate global
congruence.  The local table test is the finite audit counterpart of the
local-minimality condition in the reduction:

```text
only all-equality and all-universal admissible fibre congruence families.
```

The test suite includes a small rack example verifying that a cover interval
extracts to a local-minimal local table.  It also includes a rectangular
involutive example

```text
R((a,b),(c,d)) = ((a,d),(c,b)),
```

where fibre points in the extracted interval are themselves congruence blocks.
This guards an important normalization detail: equality partitions in local
tables must be canonicalized, otherwise the same equality family can compare
unequal merely because blocks are represented by unordered `frozenset`
objects.  After canonicalization, every congruence cover in this example
extracts to a local-minimal interval, as required by the cover/local-minimal
reduction.

## Limitation

The congruence code enumerates finite partitions only for small examples.  It
is a correctness harness for examples and candidate counterexamples.  The
global proof still needs a symbolic argument that every local-minimal interval
has a finite detector `G(pi,Q)` independent of braid index `n`.
