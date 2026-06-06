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

## Full arity-2 schema certificate

The deterministic schema reconstruction/export layer is now implemented in:

```text
src/ybe_domination/nonperm3_endpoint_detector_basis.py
tools/reconstruct_nonperm3_endpoint_detector_basis.py
```

It exports full contextual detector schema records with:

- the target rack table;
- the finite monoid quotient;
- `assignment_by_class`;
- raw `alpha` on `M x X x M`;
- endpoint classes and endpoint values;
- an example endpoint pair;
- all covered candidate IDs for each deduplicated schema.

The full non-permutation size-three arity-2 schema certificate has been
regenerated locally:

```text
proofs/nonperm3_arity2_endpoint_gate_full_schema_certificate.json
```

Generation command:

```text
python tools/reconstruct_nonperm3_endpoint_detector_basis.py \
  --arity 2 \
  --qmax 3 \
  --monoid-family truncated_structure_monoid_length_1 \
  --output proofs/nonperm3_arity2_endpoint_gate_full_schema_certificate.json
```

Verifier output:

```text
OK nonperm3 endpoint detector basis reconstruction
positive_detector_schemas 930
positive_detector_coverages 2064
unresolved_obstruction_candidates 0
reconstructed_sha256 313ef4f32ddfcef401af0b231da9fea445734a5b99c2df776f23d1318017df83
```

The generated full schema certificate also passes the contextual detector
schema verifier:

```text
python tools/verify_contextual_detector_schema_certificate.py \
  proofs/nonperm3_arity2_endpoint_gate_full_schema_certificate.json \
  --require-records

OK contextual detector schema verification
contextual_detector_records 930
verified_contextual_detector_records 930
failed_contextual_detector_records 0
```

## Remaining computational work

The full arity-2 detector schema basis is reconstructed.  The remaining
detector-basis targets are:

1. Generate and verify the full arity-3 q<=4 schema certificate.
2. Generate and verify the arity-3 q=5-only schema certificate over the q<=4
   unresolved baseline.
3. Run the componentwise width-3 arity-4 cross-effect audit against the
   resulting detector product index.

Until the arity-3 certificates exist and the arity-4 audit runs, the local
branch still does not have the full detector product needed for
`C^{X,Y_X}_{3,4}`.

## Verification

The focused local regression suite passes:

```text
python -m unittest \
  tests.test_finite_rack_sat \
  tests.test_nonperm3_endpoint_detector_basis \
  tests.test_nonperm3_arity3_checkpoint \
  tests.test_nonperm3_detector_products

Ran 26 tests in 49.219s
OK
```
