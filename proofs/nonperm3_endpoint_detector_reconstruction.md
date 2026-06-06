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

The first finite obstruction target was

```text
C^{X,Y_X}_{3,4}
  = rho^X_4(K^{Y_X}_4) / rho^X_4(J^{Y_X}_{3,4}).
```

It has now been verified trivial for all 55 non-permutation size-three tables
using the reconstructed detector products; see
`proofs/nonperm3_width3_arity4_cross_effect_audit_stabilizer.json`.

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
positive_detector_schemas 456
positive_detector_coverages 2064
unresolved_obstruction_candidates 0
reconstructed_sha256 a3b794bef765948e05f65aa0922551d583bd50f81abe25c6a1f586898026d9e6
```

The generated full schema certificate also passes the contextual detector
schema verifier:

```text
python tools/verify_contextual_detector_schema_certificate.py \
  proofs/nonperm3_arity2_endpoint_gate_full_schema_certificate.json \
  --require-records

OK contextual detector schema verification
contextual_detector_records 456
verified_contextual_detector_records 456
failed_contextual_detector_records 0
```

It also passes the standalone detector-basis verifier:

```text
python tools/verify_nonperm3_endpoint_detector_basis.py \
  proofs/nonperm3_arity2_endpoint_gate_full_schema_certificate.json \
  --require-candidate-partition

OK nonperm3 endpoint detector basis verification
positive_detector_schemas 456
positive_detector_coverages 2064
unresolved_obstruction_candidates 0
coverage_partition_verified True
```

## Arity-4 product cross-effect audit

The full arity-2 and arity-3 detector schema bases are reconstructed locally,
and the first finite cross-effect audit has now been run against the resulting
detector product index.

The generic componentwise BFS audit timed out on q=5-component rows, so the
branch now also provides:

```text
ybe_domination.componentwise_stabilizer_realized_parabolic_cross_effect_audit
tools/run_nonperm3_detector_product_cross_effect_audit.py --method stabilizer
```

This method computes the detector-kernel image by a pointwise stabilizer of the
detector blocks in a disjoint-union permutation action, then restricts the
stabilizer to the X block and compares it with the normal closure of lower
width parabolic kernel images inside the X-action image.

The completed arity-4 certificate is:

```text
proofs/nonperm3_width3_arity4_cross_effect_audit_stabilizer.json
proofs/nonperm3_width3_arity4_cross_effect_rows_stabilizer.jsonl
```

Verifier output:

```text
python tools/verify_nonperm3_width3_cross_effect_audit.py \
  proofs/nonperm3_width3_arity4_cross_effect_audit_stabilizer.json \
  --require-complete-basis \
  --require-run-audit

OK nonperm3 width-3 audit verification
detector_index_rows 55
audit_rows 55
incomplete_detector_basis False
```

Summary:

```text
truncated rows:                  0
quotient_nontrivial rows:        0
quotient_size distribution:      {1: 55}
kernel_image_size distribution:  {1: 55}
max joint_image_size:            3454279995636458717184
```

Therefore the first possible finite obstruction
`C^{X,Y_X}_{3,4}` is trivial for all 55 non-permutation size-three tables and
the current detector products.  This is finite arity-4 evidence only.  It does
not prove the all-arity Sawin statement.

## Arity-3 q<=4 reconstruction probe

The detector search order was adjusted to try all rack sizes for
`truncated_structure_monoid_length_1` before moving to
`truncated_structure_monoid_length_2`.  With that monoid-family-first order,
the arity-3 q<=4 reconstruction reproduces the archived checkpoint at the
coverage level:

```text
positive_detector_coverages 37476
unresolved_obstruction_candidates 216
by_rack_size {'q2': 16416, 'q3': 20736, 'q4': 324}
by_monoid {'truncated_structure_monoid_length_1': 15309,
           'truncated_structure_monoid_length_2': 22167}
```

This is the mathematically important finite endpoint-gate frontier for q<=4.
However, the current local schema deduplication does not yet reproduce the
archived compact schema count:

```text
archived positive_detector_schemas: 320
local endpoint-class-sensitive schema key: 1176
local schema-level (X,M,Q,alpha) key: 600
```

The current 600-schema basis has now been exported and verified with every
`covered_candidate_ids` entry checked against the exported `(X,M,Q,alpha)`
schema.  It is not byte/count-identical to the archived q<=4 checkpoint.  The
certificate therefore records `archived_positive_detector_schemas = 320` and
`reconstructed_positive_detector_schemas = 600` as distinct provenance fields.

The generated q<=4 certificate is:

```text
proofs/nonperm3_arity3_endpoint_gate_q4_full_schema_certificate.json
```

Generation/verifier output:

```text
OK nonperm3 endpoint detector basis reconstruction
positive_detector_schemas 600
positive_detector_coverages 37476
unresolved_obstruction_candidates 216
reconstructed_sha256 ecd47d65f9c303cbc1cd7e826828f5b95b952d7bc271d503655e7ca23f4835cc
```

It passes the contextual detector schema verifier:

```text
python tools/verify_contextual_detector_schema_certificate.py \
  proofs/nonperm3_arity3_endpoint_gate_q4_full_schema_certificate.json \
  --require-records

OK contextual detector schema verification
contextual_detector_records 600
verified_contextual_detector_records 600
failed_contextual_detector_records 0
```

It also passes:

```text
python tools/verify_nonperm3_endpoint_detector_basis.py \
  proofs/nonperm3_arity3_endpoint_gate_q4_full_schema_certificate.json \
  --require-candidate-partition

OK nonperm3 endpoint detector basis verification
positive_detector_schemas 600
positive_detector_coverages 37476
unresolved_obstruction_candidates 216
coverage_partition_verified True
```

## Arity-3 q=5-only reconstruction

Using the q<=4 certificate as the baseline, the q=5-only reconstruction covers
exactly the 216 q<=4-unresolved candidates:

```text
proofs/nonperm3_arity3_q5_resolution_certificate.json
```

Generation/verifier output:

```text
OK nonperm3 endpoint detector basis reconstruction
positive_detector_schemas 22
positive_detector_coverages 216
unresolved_obstruction_candidates 0
reconstructed_sha256 2e62015a2a91853354206421e80be6035ba293127b2e5213b7bb02ccf1af72c9
```

Summary fields:

```text
new_positive_detector_coverages 216
new_positive_detector_schemas 22
combined_positive_detector_coverages 37692
remaining_unresolved_candidates 0
by_rack_size {'q5': 216}
by_monoid {'truncated_structure_monoid_length_2': 216}
reported_sha256 376e901839c978530ecd32893da56de5ff69b26dd3c407d1cb3eda365c63fc75
sha256_matches_reported False
```

The reconstructed SHA does not match the reported SHA because the original
sandbox certificate bytes and canonicalization were not recovered.  The counts
and schema verification do match the reported q=5 resolution.

It passes the contextual detector schema verifier:

```text
python tools/verify_contextual_detector_schema_certificate.py \
  proofs/nonperm3_arity3_q5_resolution_certificate.json \
  --require-records

OK contextual detector schema verification
contextual_detector_records 22
verified_contextual_detector_records 22
failed_contextual_detector_records 0
```

It also passes:

```text
python tools/verify_nonperm3_endpoint_detector_basis.py \
  proofs/nonperm3_arity3_q5_resolution_certificate.json \
  --require-candidate-partition

OK nonperm3 endpoint detector basis verification
positive_detector_schemas 22
positive_detector_coverages 216
baseline_covered_candidate_count 37476
combined_positive_detector_coverages 37692
remaining_unresolved_candidates 0
coverage_partition_verified True
```

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
