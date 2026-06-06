# Non-permutation size-three arity-3 q=5 resolution

Date: 2026-06-06

This note records the reported q=5 resolution of the finite-rack endpoint
gate for non-permutation-form \(|X|=3\), arity \(n=3\).

## Reported Verifier Output

The q=5 resolution certificate was reported with:

```text
OK nonperm3 arity-3 q5 resolution certificate verified
sha256 376e901839c978530ecd32893da56de5ff69b26dd3c407d1cb3eda365c63fc75
new_positive_detector_coverages 216
new_positive_detector_schemas 22
combined_positive_detector_coverages 37692
remaining_unresolved_candidates 0
```

The previous q<=4 checkpoint was reported and is already recorded in
`proofs/nonperm3_arity3_endpoint_gate_checkpoint.md`:

```text
OK nonperm3 arity-3 q4 checkpoint verified
sha256 bdd034c1c1fd665054818b58a76249bc009a0532dec33fea404063d61a82fee8
nonpermutation_ybe_tables 55
arity3_bad_endpoint_pairs 37692
positive_detector_coverages 37476
positive_detector_schemas 320
unresolved_obstruction_candidates 216
by_rack_size {'q2': 16416, 'q3': 20736, 'q4': 324}
by_monoid {'truncated_structure_monoid_length_1': 15309, 'truncated_structure_monoid_length_2': 22167}
```

Thus the combined reported classification is:

```text
non-permutation |X|=3 arity-3 bad endpoint pairs: 37692
positive finite rack detector coverages through q=4: 37476
new q=5 positive finite rack detector coverages: 216
combined positive finite rack detector coverages: 37692
remaining unresolved candidates: 0
bounded negatives: 0
residual-collapse claims: 0
```

Equivalently:

```text
Every non-permutation-form |X|=3, n=3 principal bad endpoint pair is
separated by a positive finite rack detector with |Q| <= 5.
```

This is a finite endpoint-gate classification.  It is not an all-arity proof
of Sawin finite-rack domination.

## Artifact Status

The reported artifact paths were:

```text
sandbox:/mnt/data/nonperm3_arity3_q5_resolution_certificate.json
sandbox:/mnt/data/nonperm3_arity3_q5_resolution_verifier.py
sandbox:/mnt/data/nonperm3_arity3_endpoint_gate_q4_checkpoint.json
sandbox:/mnt/data/nonperm3_arity3_endpoint_gate_q4_verifier.py
```

Those `sandbox:/mnt/data` files were not accessible from this Windows
workspace at the time this note was added.  The original JSON bytes and
canonicalization have still not been recovered, so the reported SHA256 remains
external provenance.

A deterministic local reconstruction has now generated the q=5-only schema
certificate:

```text
proofs/nonperm3_arity3_q5_resolution_certificate.json
```

It is generated against the reconstructed q<=4 baseline:

```text
proofs/nonperm3_arity3_endpoint_gate_q4_full_schema_certificate.json
```

The reconstructed q=5 certificate has:

```text
new_positive_detector_coverages 216
new_positive_detector_schemas 22
combined_positive_detector_coverages 37692
remaining_unresolved_candidates 0
by_rack_size {'q5': 216}
by_monoid {'truncated_structure_monoid_length_2': 216}
reported_sha256 376e901839c978530ecd32893da56de5ff69b26dd3c407d1cb3eda365c63fc75
reconstructed_sha256 2e62015a2a91853354206421e80be6035ba293127b2e5213b7bb02ccf1af72c9
sha256_matches_reported False
coverage_partition_verified True
```

It passes:

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

The displayed first q=5 detector has now been copied into a standalone
schema fixture:

```text
proofs/nonperm3_displayed_q5_detector_schema.json
```

This fixture is not the full q=5 certificate.  It records only the displayed
detector for the first q<=4 unresolved candidate.  It passes the schema-level
contextual verifier:

```text
python tools/verify_contextual_detector_schema_certificate.py \
  proofs/nonperm3_displayed_q5_detector_schema.json \
  --require-records

OK contextual detector schema verification
contextual_detector_records 1
verified_contextual_detector_records 1
failed_contextual_detector_records 0
```

The local reconstruction is recorded in
`proofs/nonperm3_endpoint_detector_reconstruction.md`.  It recovers the
reported q=5 counts and schemas but not the original reported certificate
hash.

## Displayed First Candidate

The first q<=4 unresolved candidate was:

```text
ybe_table = [0,3,6,1,4,7,5,2,8]
partition = [0,0,0]
arity = 3
braid_word = [1,0]
e  = [00,2,epsilon]
e' = [epsilon,2,00]
```

The reported q=5 detector uses the truncated length-2 structure monoid
\(M_2(r)\) of size 10 and the fixed rack

```text
[
  [0,1,3,4,2],
  [0,1,4,2,3],
  [1,0,2,4,3],
  [1,0,4,3,2],
  [1,0,3,2,4]
]
```

with default \(\alpha([p,x,s])=0\) and nonzero support:

```text
[
  [0,0,6,1],
  [0,2,4,3],
  [0,2,5,4],
  [0,2,7,2],
  [1,0,3,1],
  [1,2,1,4],
  [1,2,2,2],
  [2,0,3,1],
  [2,2,1,3],
  [2,2,2,4],
  [3,0,1,1],
  [3,0,2,1],
  [4,2,0,2],
  [5,2,0,4],
  [6,0,0,1],
  [7,2,0,3]
]
```

The local regression test
`tests/test_nonperm3_arity3_checkpoint.py::NonPerm3Arity3CheckpointTests.test_displayed_q5_detector_separates_first_unresolved_candidate`
checks this displayed detector directly:

1. the computed \(M_2(r)\) has the displayed size and generator images;
2. the displayed q=5 table is a rack;
3. all \(10^2\cdot 3^2=900\) contextual T-relations hold;
4. all \(900\) contextual R-relations hold;
5. the target endpoints have values \(2\) and \(3\).

Thus the displayed first candidate is locally checked as separated by the
reported q=5 detector.

## Remaining Frontier

This q=5 batch closes the non-permutation \(|X|=3\), arity-3 endpoint gate.
The remaining finite-search frontier is higher arity for non-permutation
\(|X|=3\), not the arity-3 batch.

## All-arity implication

Closing arities 2 and 3 is finite evidence for the endpoint-detector program,
but it is not by itself a proof of Sawin domination.  The missing step is a
uniform theorem converting fixed-arity contextual separation into one finite
rack detector working for all braid arities relevant to the fixed solution
\(X\).

The local proof log currently isolates this as one of the following equivalent
or near-equivalent obligations:

```text
bounded bad-arity theorem:
  there exists N=N(X) such that detecting all principal bad endpoint pairs in
  arities <= N detects all principal bad endpoint pairs in every arity;

bounded harmful-core theorem:
  every harmful kernel-fiber monodromy contains a bounded-arity harmful core;

uniform finite-state contextual separation:
  one finite two-sided contextual state system and one finite rack quotient
  separate all same-orbit endpoint pairs in every arity.
```

Thus the q=5 certificate closes the arity-3 batch, while the next proof-grade
target is either:

1. prove one of the uniformity/bounded-core statements for the remaining
   non-permutation \(|X|=3\) branch; or
2. compute the first higher-arity endpoint frontier, beginning at arity 4, and
   produce the same kind of positive finite rack detector coverage or an
   explicit obstruction certificate.

The concrete higher-arity plan is recorded in
`proofs/nonperm3_size3_higher_arity_frontier.md`.
