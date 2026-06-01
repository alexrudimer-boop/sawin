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

## Rack assembly

Once the local theorem supplies fixed finite detector groups for a saturated
chain, the final rack is no longer a prose-only recurrence.  The module
`src/ybe_domination/chain_rack.py` provides

```text
assemble_congruence_chain_rack(Q_m, groups)
```

where `Q_m` is the terminal quotient rack and `groups` is the finite list of
local detectors encountered while descending the chain.  The helper iterates

```text
Q_i = Q_{i+1} x A_{G_i}
```

by calling `sharp_obstruction_rack(Q,G)` at every step.  Its audit record
stores:

- `terminal_rack_size`;
- the detector group orders `|G_i|`;
- one row per interval with input size, detector rack size `2*|G_i|^2`, and
  output size; and
- the final finite rack object.

The constructor deliberately takes no braid degree.  Therefore it checks the
formal requirement that, after the still-open local theorem has provided the
fixed groups `G_i`, the global rack is finite and independent of `n`.

The local-summary handoff is now executable as well.  A closed bottleneck
summary exposes `closed_detector_product_group`, which is the single finite
group for that interval: a lone group is returned unchanged, while several
closed factors are multiplied into `prod_j G_{i,j}`.  The helper

```text
closed_local_detector_chain(summaries)
```

collects these one-per-interval groups and records any row that is still an
open product/corridor verdict or has a delegated detector gap.  The wrapper

```text
assemble_closed_local_detector_chain_rack(Q_m, summaries)
```

therefore refuses to build `Q_0` unless every local row has supplied an actual
fixed finite group.  This makes the congruence-chain induction audit
construction-shaped without pretending that the remaining Master Local-Minimal
Residual Theorem has been proved.

The handoff now also recognizes the endpoint-observer closure verdicts from
the post-linear U/C/M layer, including
`closed_by_routed_endpoint_certificates`, the individual U, C, and M
endpoint-witness or symmetric-fork closures, and the monodromy-coboundary
observer-build verdicts
`closed_by_triangular_recovery_endpoint_observer_family_build`,
`closed_by_universal_continuation_endpoint_observer_family_build`,
`closed_by_mixed_unit_endpoint_observer_family_build`, and
`closed_by_endpoint_observer_family_build`.  These verdicts are accepted only
when the local summary supplies an actual fixed detector product group and no
detector gap rows.  Gap rows dominate a supplied group: if a summary reports
any delegated or residual gap, the chain records that row as incomplete rather
than using the group.  Thus the conditional endpoint-observer theorem can
feed the chain assembly directly once its local group `G(pi,Q)` is
constructed, while a bare closed-looking endpoint verdict without that group,
or with an unresolved residual gap, is still rejected.

## Limitation

The congruence code enumerates finite partitions only for small examples.  It
is a correctness harness for examples and candidate counterexamples.  The
global proof still needs a symbolic argument that every local-minimal interval
has a finite detector `G(pi,Q)` independent of braid index `n`.
