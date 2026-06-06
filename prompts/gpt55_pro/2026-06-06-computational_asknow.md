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

After checkout:

  git clone https://github.com/alexrudimer-boop/sawin.git
  cd sawin
  git checkout codex/atom-inner-row-lift

Current finite-computational status:

1. The branch locally reconstructs the non-permutation |X|=3 endpoint-detector
   schema basis needed to define the detector product Y_X.

   Full schema certificates:

     proofs/nonperm3_arity2_endpoint_gate_full_schema_certificate.json
     proofs/nonperm3_arity3_endpoint_gate_q4_full_schema_certificate.json
     proofs/nonperm3_arity3_q5_resolution_certificate.json

2. Verified endpoint-gate counts:

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

   Arity 3 q=5-only over the q<=4 unresolved baseline:

     new_positive_detector_coverages 216
     new_positive_detector_schemas 22
     combined_positive_detector_coverages 37692
     remaining_unresolved_candidates 0
     by_rack_size {'q5': 216}
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

   They also pass:

     python tools/verify_nonperm3_endpoint_detector_basis.py \
       <certificate> \
       --require-candidate-partition

   The standalone verifier recomputes the candidate universe and checks that
   covered, baseline-covered, and unresolved candidate IDs form the expected
   partition.

4. The complete detector-product import index exists:

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

5. The old BFS componentwise audit timed out on q=5-component rows.  The
   branch now adds a stabilizer method:

     ybe_domination.componentwise_stabilizer_realized_parabolic_cross_effect_audit
     tools/run_nonperm3_detector_product_cross_effect_audit.py --method stabilizer

   Method summary:

   - embed the detector component actions and X-action in one disjoint-union
     permutation action;
   - compute the pointwise stabilizer of every detector point using SymPy
     Schreier-Sims;
   - restrict stabilizer generators to the X block, giving
     rho^X_n(K^Y_n);
   - compute lower-width kernel images the same way;
   - normal-close their parabolic embeddings inside the finite X-action image.

   This should be equivalent to the componentwise product-rack quotient, but it
   should be audited carefully.

6. The full arity-4, bound-3 non-permutation size-three audit now exists:

     proofs/nonperm3_width3_arity4_cross_effect_audit_stabilizer.json
     proofs/nonperm3_width3_arity4_cross_effect_rows_stabilizer.jsonl

   Command used:

     python tools/run_nonperm3_detector_product_cross_effect_audit.py \
       --certificate proofs/nonperm3_arity2_endpoint_gate_full_schema_certificate.json \
       --certificate proofs/nonperm3_arity3_endpoint_gate_q4_full_schema_certificate.json \
       --certificate proofs/nonperm3_arity3_q5_resolution_certificate.json \
       --bound 3 \
       --arity 4 \
       --state-limit 1000000 \
       --method stabilizer \
       --require-all-55 \
       --run-audit \
       --row-output-jsonl proofs/nonperm3_width3_arity4_cross_effect_rows_stabilizer.jsonl \
       --output proofs/nonperm3_width3_arity4_cross_effect_audit_stabilizer.json

   Verifier:

     python tools/verify_nonperm3_width3_cross_effect_audit.py \
       proofs/nonperm3_width3_arity4_cross_effect_audit_stabilizer.json \
       --require-complete-basis \
       --require-run-audit

   Result:

     detector_index_rows 55
     audit_rows 55
     incomplete_detector_basis False
     truncated rows 0
     quotient_nontrivial rows 0
     quotient_size distribution {1: 55}
     kernel_image_size distribution {1: 55}
     max joint_image_size 3454279995636458717184

   Thus there is no four-strand width-3 cross-effect obstruction for this
   detector product.  This is still finite fixed-arity evidence only and not
   an all-arity proof.

Relevant files to inspect:

  src/ybe_domination/rack_residual_tower.py
  src/ybe_domination/nonperm3_endpoint_detector_basis.py
  src/ybe_domination/nonperm3_detector_products.py
  tools/reconstruct_nonperm3_endpoint_detector_basis.py
  tools/verify_contextual_detector_schema_certificate.py
  tools/verify_nonperm3_endpoint_detector_basis.py
  tools/run_nonperm3_detector_product_cross_effect_audit.py
  tools/verify_nonperm3_width3_cross_effect_audit.py
  proofs/nonperm3_endpoint_detector_reconstruction.md
  proofs/nonperm3_size3_higher_arity_frontier.md
  proofs/nonperm3_width3_arity4_cross_effect_audit_stabilizer.json

Task:

Give a rigorous computational audit of the stabilizer arity-4 certificate and
the next finite test.

Specifically:

1. Verify mathematically whether the stabilizer method computes exactly

     rho^X_n(K^{Y_X}_n) / rho^X_n(J^{Y_X}_{3,n})

   for the componentwise product detector, or identify the first incorrect
   implication.  Pay attention to the disjoint-union embedding, detector
   pointwise stabilizer, restriction to the X block, and normal closure inside
   the X-action image.

2. Audit whether the current verifier is strong enough.  If it is only
   structural, specify the exact independent verifier needed to recheck the
   stabilizer certificate without rerunning all row searches blindly.

3. Decide the next finite computation after the absent arity-4 obstruction:
   arity 5 stabilizer cross-effect, a direct proof that the arity-4 trivial
   kernel image pattern persists for the 55 tables, an endpoint-pattern
   extension scan at arity 4/5, or another sharper finite obstruction test.
   Give exact commands and expected certificate fields.

4. If arity 5 is feasible, propose safe CLI additions such as per-row timing,
   `--table-index`, `--start-index`, `--component-count-max`, and independent
   row verification.  If it is not feasible, identify the precise bottleneck
   and a stronger group-theoretic compression.

5. Interpret the current arity-4 result correctly:

   - no nontrivial row means no four-strand obstruction for this detector
     product;
   - it does not prove Sawin's all-arity statement;
   - a future high-arity miss against this product would not be a Sawin
     counterexample unless promoted to a cofinal rack-prefix obstruction.

Return theorem/proof, finite evidence, heuristic, and unsupported claims in
separate categories.
