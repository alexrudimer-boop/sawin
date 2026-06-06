# Non-permutation size-three endpoint detector reconstruction

Date: 2026-06-06.

This note records review of the GPT-5.5 Pro response proposing local
reconstruction of the missing q=5 detector basis, rather than waiting for a
sandbox-only certificate artifact.

## Proof status

The response does not prove the Sawin finite-rack domination problem.  Its
valid contribution is an implementation route for reconstructing the finite
endpoint-detector basis needed to define the detector product `Y_X` locally.

The reported q=5 endpoint gate remains finite fixed-arity evidence:

- arity 3 endpoint candidates over the 55 non-permutation size-three tables
  are reportedly all separated by q<=5 rack detectors;
- this is not an all-arity proof;
- q<=4 misses are not negative evidence after the reported q=5 closure;
- an arity-4 cross-effect against one reconstructed detector product would
  refute only the width-3 propagation lemma for that product unless promoted
  to a cofinal rack-prefix obstruction.

The missing theorem direction is still

```text
rho^X_n(K^Y_n) <= rho^X_n(J^Y_{3,n}).
```

The first finite obstruction remains

```text
C^{X,Y_X}_{3,4}
  = rho^X_4(K^{Y_X}_4) / rho^X_4(J^{Y_X}_{3,4}).
```

## Locally implemented reconstruction inputs

The labelled rack catalog enumerator in `finite_rack_sat.py` now uses
left-translation propagation from the rack identity

```text
L_{L_a(b)} = L_a L_b L_a^{-1}.
```

This preserves the q<=4 catalog and makes q=5 deterministic enumeration
feasible.  The verified labelled rack counts are:

```text
q=2: 2
q=3: 13
q=4: 114
q=5: 1708
```

The new module `src/ybe_domination/nonperm3_endpoint_detector_basis.py`
reconstructs the finite endpoint-candidate input data:

- the universal truncated structure monoid of length 1;
- the solution-dependent truncated structure monoid of length 2;
- the five canonical partitions of `{0,1,2}`;
- quotient YBE tables induced by rack-admissible partitions;
- endpoint T-classes with the corrected endpoint transport convention;
- tuple braid orbits;
- principal bad endpoint candidates.

The reconstructed compact candidate counts match the archived checkpoint
counts:

```text
arity 2 bad endpoint pairs: 2064
arity 3 bad endpoint pairs: 37692
arity 2 partition distribution:
  (0,0,0): 1416
  (0,0,1): 216
  (0,1,0): 216
  (0,1,1): 216
  (0,1,2): 0
```

The first q<=4 unresolved arity-3 pair for
`[0,3,6,1,4,7,5,2,8]`,
namely `(0,0,2)@2` versus `(2,0,0)@0` under partition `(0,0,0)`,
is present in the reconstructed candidate basis.

## Remaining computational work

The full detector schema basis is not yet reconstructed.  The next
implementation target is:

1. Build deterministic schema search over reconstructed candidates, requested
   monoid families, and labelled racks up to qmax.
2. Export one deterministic first-found detector per covered candidate.
3. Deduplicate identical contextual schemas while preserving all covered
   candidate IDs.
4. Verify exported schemas by rebuilding the contextual presentation and
   checking the rack assignment and endpoint separation.
5. Generate the full arity-2, arity-3 q<=4, and arity-3 q=5-only schema
   certificates.
6. Run the componentwise width-3 arity-4 cross-effect audit against the
   resulting detector product index.

Until those certificates exist and the arity-4 audit runs, the local branch has
only reconstructed the finite endpoint-candidate basis, not the detector
product needed for `C^{X,Y_X}_{3,4}`.

## Verification

The focused local regression suite passes:

```text
python -m unittest \
  tests.test_finite_rack_sat \
  tests.test_nonperm3_endpoint_detector_basis \
  tests.test_nonperm3_arity3_checkpoint \
  tests.test_nonperm3_detector_products

Ran 24 tests in 39.310s
OK
```
