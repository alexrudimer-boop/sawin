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

1. The branch locally reconstructs the non-permutation |X|=3 detector schema
   basis needed to build the detector product Y_X.

   Full schema certificates:

     proofs/nonperm3_arity2_endpoint_gate_full_schema_certificate.json
     proofs/nonperm3_arity3_endpoint_gate_q4_full_schema_certificate.json
     proofs/nonperm3_arity3_q5_resolution_certificate.json

2. Verification status:

   Arity 2:

     positive_detector_schemas 456
     positive_detector_coverages 2064
     unresolved_obstruction_candidates 0

   Arity 3 q<=4:

     archived_positive_detector_schemas 320
     reconstructed_positive_detector_schemas 600
     positive_detector_coverages 37476
     unresolved_obstruction_candidates 216
     by_rack_size {'q2': 16416, 'q3': 20736, 'q4': 324}
     by_monoid {
       'truncated_structure_monoid_length_1': 15309,
       'truncated_structure_monoid_length_2': 22167
     }

   Arity 3 q=5-only over the q<=4 unresolved baseline:

     new_positive_detector_coverages 216
     new_positive_detector_schemas 22
     combined_positive_detector_coverages 37692
     remaining_unresolved_candidates 0
     by_rack_size {'q5': 216}
     by_monoid {'truncated_structure_monoid_length_2': 216}
     reported_sha256 376e901839c978530ecd32893da56de5ff69b26dd3c407d1cb3eda365c63fc75
     reconstructed_sha256 2e62015a2a91853354206421e80be6035ba293127b2e5213b7bb02ccf1af72c9
     sha256_matches_reported False

   The reconstructed q=5 SHA differs from the reported SHA because the
   original sandbox certificate bytes/canonicalization were not recovered.
   The counts and contextual schema verification match the reported q=5
   resolution.

3. All three schema certificates pass:

     python tools/verify_contextual_detector_schema_certificate.py \
       <certificate> \
       --require-records

   The arity-2, arity-3 q<=4, and q=5-only payloads also pass:

     python tools/verify_nonperm3_endpoint_detector_basis.py \
       <certificate> \
       --require-candidate-partition

   This standalone verifier recomputes the candidate universe and checks that
   covered, baseline-covered, and unresolved candidate IDs form the expected
   partition.

4. This is still finite fixed-arity evidence only.  Do not claim an all-arity
   proof from the endpoint-gate certificates.

5. The complete detector-product import index exists:

     proofs/nonperm3_detector_product_full_import_audit.json

   It passes:

     python tools/verify_nonperm3_width3_cross_effect_audit.py \
       proofs/nonperm3_detector_product_full_import_audit.json \
       --require-complete-basis

   Summary:

     detector_index_rows 55
     audit_rows 0
     incomplete_detector_basis False
     schema_like_detector_records 1078
     component_count_distribution {0: 1, 1: 12, 2: 12, 3: 24, 4: 6}

   The zero-component row is the identity table
   [0,1,2,3,4,5,6,7,8], which has no arity-2 or arity-3 principal bad endpoint
   pairs.

6. A full arity-4 run with `state_limit=1000000` timed out after about 904
   seconds before producing a final JSON payload.  A two-row smoke run checked
   the identity row and first nontrivial row; both had quotient_size=1 and were
   untruncated.

   The wrapper now supports row-level progress:

     --row-output-jsonl proofs/nonperm3_width3_arity4_cross_effect_rows.jsonl
     --resume-row-output-jsonl

   A two-row smoke run with `--row-output-jsonl` wrote both rows successfully.

Next decisive computation:

Run and audit the arity-4 width-3 componentwise cross-effect:

  C^{X,Y_X}_{3,4}
    =
  rho^X_4(K^{Y_X}_4) / rho^X_4(J^{Y_X}_{3,4})

for every one of the 55 non-permutation |X|=3 tables, where Y_X is the
componentwise product of the distinct finite rack targets appearing in the
verified arity-2 and arity-3 endpoint detector basis for X.

Relevant files to inspect:

  src/ybe_domination/nonperm3_endpoint_detector_basis.py
  src/ybe_domination/nonperm3_detector_products.py
  src/ybe_domination/rack_residual_tower.py
  tools/reconstruct_nonperm3_endpoint_detector_basis.py
  tools/verify_contextual_detector_schema_certificate.py
  tools/run_nonperm3_detector_product_cross_effect_audit.py
  tools/verify_nonperm3_width3_cross_effect_audit.py
  proofs/nonperm3_endpoint_detector_reconstruction.md
  proofs/nonperm3_size3_higher_arity_frontier.md
  proofs/nonperm3_arity2_endpoint_gate_full_schema_certificate.json
  proofs/nonperm3_arity3_endpoint_gate_q4_full_schema_certificate.json
  proofs/nonperm3_arity3_q5_resolution_certificate.json

The intended command is:

  python tools/run_nonperm3_detector_product_cross_effect_audit.py \
    --certificate proofs/nonperm3_arity2_endpoint_gate_full_schema_certificate.json \
    --certificate proofs/nonperm3_arity3_endpoint_gate_q4_full_schema_certificate.json \
    --certificate proofs/nonperm3_arity3_q5_resolution_certificate.json \
    --bound 3 \
    --arity 4 \
    --state-limit 1000000 \
    --require-all-55 \
    --run-audit \
    --row-output-jsonl proofs/nonperm3_width3_arity4_cross_effect_rows.jsonl \
    --resume-row-output-jsonl \
    --output proofs/nonperm3_width3_arity4_cross_effect_audit.json

Decision rule:

- if any row has `quotient_nontrivial = true`, the width-3 propagation lemma is
  false for that detector product only;
- if all 55 rows are untruncated and `quotient_size = 1`, there is no arity-4
  obstruction for this detector product, but still no all-n theorem;
- if any row truncates, the result is inconclusive and needs stronger
  permutation-group compression.

Task:

Give a rigorous computational audit and patch-level plan for the arity-4
cross-effect step.

Specifically:

1. Audit whether the current detector-product importer correctly deduplicates
   by distinct target rack table per X and preserves enough schema provenance.

2. Audit whether `componentwise_realized_parabolic_cross_effect_audit` is
   computing the intended quotient:

     rho^X_4(K^{Y_X}_4) / rho^X_4(J^{Y_X}_{3,4})

   using componentwise detector actions rather than explicitly constructing
   the Cartesian product rack.

3. Identify the likely runtime bottleneck for the 55-row audit and propose
   safe resumable/per-row output and compression strategies.  The immediate
   issue is timeout before final JSON output, not missing detector basis.

4. If you see a flaw in the certificate/import/audit chain, give the exact
   code or verifier change needed before running the command.

5. If the command succeeds, specify exactly how to interpret each possible
   output row without overclaiming a Sawin proof or counterexample.

Return theorem/proof, finite evidence, heuristic, and unsupported claims in
separate categories.  Do not treat fixed-arity finite evidence as a proof of
Sawin's all-arity statement.
