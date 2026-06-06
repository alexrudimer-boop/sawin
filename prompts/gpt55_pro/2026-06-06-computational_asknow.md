computational_asknow

We are working on Will Sawin's MathOverflow problem:

For every finite bijective set-theoretic Yang-Baxter solution X, prove or
disprove the existence of a finite rack Y, independent of braid index n, such
that for all n:

  ker rho_{Y,n} <= ker rho_{X,n}.

Assume you do not have access to my local workspace.  You do have the GitHub
repository/branch and should download or inspect it before making repo-specific
claims:

  https://github.com/alexrudimer-boop/sawin/tree/codex/atom-inner-row-lift

All file paths below are repo-relative after checking out:

  git clone https://github.com/alexrudimer-boop/sawin.git
  cd sawin
  git checkout codex/atom-inner-row-lift

Current finite-computational frontier:

1. The non-permutation |X|=3, arity-3 endpoint gate is reported closed by
   q=5 finite rack detectors, but the full q=5 detector schema certificate is
   not local.

   Reported q=5 verifier output:

     sha256 376e901839c978530ecd32893da56de5ff69b26dd3c407d1cb3eda365c63fc75
     new_positive_detector_coverages 216
     new_positive_detector_schemas 22
     combined_positive_detector_coverages 37692
     remaining_unresolved_candidates 0

   This is finite fixed-arity evidence only.  Do not claim an all-arity proof
   from it.

2. The branch locally reconstructs the endpoint-candidate input basis and
   labelled rack catalog:

     src/ybe_domination/nonperm3_endpoint_detector_basis.py
     tools/reconstruct_nonperm3_endpoint_detector_basis.py
     tests/test_nonperm3_endpoint_detector_basis.py

   Verified input counts:

     labelled racks: q2=2, q3=13, q4=114, q5=1708
     principal bad endpoint pairs: arity2=2064, arity3=37692

3. The full arity-2 schema certificate has been reconstructed locally:

     proofs/nonperm3_arity2_endpoint_gate_full_schema_certificate.json

   It contains 930 deduplicated contextual detector schema records covering all
   2064 arity-2 principal bad endpoint pairs and passes:

     python tools/verify_contextual_detector_schema_certificate.py \
       proofs/nonperm3_arity2_endpoint_gate_full_schema_certificate.json \
       --require-records

   It also passes the internal `verify_detector_basis_payload` verifier.

4. Arity-3 q<=4 reconstruction status:

   With monoid-family-first detector search, a q<=4 probe reproduces the
   archived coverage-level checkpoint exactly:

     positive_detector_coverages 37476
     unresolved_obstruction_candidates 216
     by_rack_size {'q2': 16416, 'q3': 20736, 'q4': 324}
     by_monoid {
       'truncated_structure_monoid_length_1': 15309,
       'truncated_structure_monoid_length_2': 22167
     }

   However, the current schema-level deduplication/export still does not
   reproduce the archived compact schema count.  The archived checkpoint says:

     positive_detector_schemas 320

   Current local attempts:

   - endpoint-class-sensitive schema key: 1176 schemas;
   - schema-level key `(X, arity, monoid family, monoid table, gen, rack table,
     assignment_by_class)`: 600 schemas.

   The 600-schema basis appears to preserve the correct finite coverage data,
   but it is not byte/count-identical to the archived compact q<=4 checkpoint.
   The key open computational issue is to determine the correct historical
   schema equivalence or compression that yields 320 without weakening
   independent verification of every covered endpoint pair.

Relevant files to inspect:

  src/ybe_domination/nonperm3_endpoint_detector_basis.py
  src/ybe_domination/finite_rack_sat.py
  src/ybe_domination/nonperm3_detector_products.py
  tools/reconstruct_nonperm3_endpoint_detector_basis.py
  tools/verify_contextual_detector_schema_certificate.py
  tools/run_nonperm3_detector_product_cross_effect_audit.py
  proofs/nonperm3_endpoint_detector_reconstruction.md
  proofs/nonperm3_arity2_endpoint_gate_full_schema_certificate.json
  proofs/nonperm3_arity3_endpoint_gate_checkpoint.md
  proofs/nonperm3_arity3_endpoint_gate_checkpoint_certificate.json
  proofs/nonperm3_arity3_q5_resolution.md
  proofs/nonperm3_displayed_q5_detector_schema.json

Task:

Give a rigorous computational audit and patch-level plan for finishing the
arity-3 detector basis reconstruction.

Specifically:

1. Determine whether the current 600-schema q<=4 basis is proof-grade even
   though it does not match the archived 320 schema count.

2. If the archived 320 schema count can be reproduced, identify the exact
   schema equivalence relation/compression and explain how to verify every
   covered endpoint pair after compression.

3. If 320 is only a historical implementation count rather than a required
   mathematical invariant, propose revised certificate fields that record both:

     archived_positive_detector_schemas = 320
     reconstructed_positive_detector_schemas = 600
     positive_detector_coverages = 37476
     unresolved_obstruction_candidates = 216

   while still giving proof-grade verification of all coverages.

4. Give the safest next command sequence for:

   - generating the arity-3 q<=4 full schema certificate;
   - extracting the 216 unresolved candidate baseline;
   - generating the q=5-only resolution certificate;
   - verifying both;
   - running the arity-4 width-3 componentwise cross-effect audit.

5. Identify any code changes needed before the q=5-only run, especially
   performance/resume controls or SAT/CSP replacement for fixed-rack assignment
   search.

Return theorem/proof, finite evidence, heuristic, and unsupported claims in
separate categories.  Do not treat fixed-arity finite evidence as a proof of
Sawin's all-arity statement.
