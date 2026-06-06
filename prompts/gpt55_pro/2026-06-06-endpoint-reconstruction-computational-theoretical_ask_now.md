computational

We are working on Will Sawin's MathOverflow problem:

For every finite bijective set-theoretic Yang-Baxter solution X, prove or
disprove the existence of a finite rack Y, independent of braid index n, such
that for all n:

  ker rho_{Y,n} <= ker rho_{X,n}.

You should assume you do not have access to my local workspace.  You do have
the GitHub repository/branch and should download or inspect that branch before
making repo-specific claims:

  https://github.com/alexrudimer-boop/sawin/tree/codex/atom-inner-row-lift

All file paths below are repo-relative after checking out:

  git clone https://github.com/alexrudimer-boop/sawin.git
  cd sawin
  git checkout codex/atom-inner-row-lift

Current finite-computational frontier:

1. The non-permutation |X|=3, arity-3 endpoint gate is reported closed by
   q=5 finite rack detectors, but the full q=5 detector schema certificate is
   not local.

   Reported verifier output:

     sha256 376e901839c978530ecd32893da56de5ff69b26dd3c407d1cb3eda365c63fc75
     new_positive_detector_coverages 216
     new_positive_detector_schemas 22
     combined_positive_detector_coverages 37692
     remaining_unresolved_candidates 0

   This is finite fixed-arity evidence only.  Do not claim an all-arity proof
   from it.

2. The branch now reconstructs the endpoint-candidate input basis locally:

     src/ybe_domination/nonperm3_endpoint_detector_basis.py
     tests/test_nonperm3_endpoint_detector_basis.py
     proofs/nonperm3_endpoint_detector_reconstruction.md

   Verified counts:

     labelled racks:
       q=2: 2
       q=3: 13
       q=4: 114
       q=5: 1708

     principal bad endpoint pairs:
       arity 2: 2064
       arity 3: 37692

     arity 2 partition distribution:
       (0,0,0): 1416
       (0,0,1): 216
       (0,1,0): 216
       (0,1,1): 216
       (0,1,2): 0

   Focused tests pass:

     python -m unittest \
       tests.test_finite_rack_sat \
       tests.test_nonperm3_endpoint_detector_basis \
       tests.test_nonperm3_arity3_checkpoint \
       tests.test_nonperm3_detector_products

3. The branch also has detector-product import and contextual schema
   verification machinery:

     src/ybe_domination/nonperm3_detector_products.py
     tools/verify_contextual_detector_schema_certificate.py
     tools/run_nonperm3_detector_product_cross_effect_audit.py
     tools/verify_nonperm3_width3_cross_effect_audit.py

   The displayed first q=5 detector is stored in:

     proofs/nonperm3_displayed_q5_detector_schema.json

   It is only one checked schema fixture, not the full q=5 certificate.

Next computational target:

Complete the deterministic detector schema reconstruction/export layer without
overclaiming its mathematical status.  Specifically, inspect the branch and
give patch-level guidance or code for:

1. `src/ybe_domination/nonperm3_endpoint_detector_basis.py`
   - dataclasses for exported detector schemas;
   - deterministic candidate search over q, monoid family, and rack table;
   - q=2 fast path reuse;
   - MRV or another deterministic improvement to `_assignment_for_fixed_rack`
     if needed;
   - schema deduplication while retaining all covered candidate IDs.

2. `tools/reconstruct_nonperm3_endpoint_detector_basis.py`
   - CLI arguments:
       --arity
       --qmax
       --monoid-family
       --baseline
       --emit-new-q5-only
       --output
   - JSON export with full rack table, monoid quotient, assignment by class,
     endpoint classes, endpoint values, example endpoint pair, covered
     candidate IDs, and canonical reconstructed SHA.

3. Verification:
   - rebuild every contextual presentation from exported schema data;
   - verify the rack assignment and endpoint separation;
   - hard-fail if compact checkpoint counts do not match:

     arity 2:
       bad endpoint pairs 2064
       positive detector coverages 2064
       by rack size q2=1200, q3=864
       unresolved 0

     arity 3 q<=4:
       bad endpoint pairs 37692
       positive detector coverages 37476
       positive detector schemas 320
       unresolved 216
       by rack size q2=16416, q3=20736, q4=324
       by monoid length1=15309, length2=22167

     arity 3 q=5-only over the q<=4 unresolved baseline:
       new positive detector coverages 216
       new positive detector schemas 22
       combined coverages 37692
       remaining unresolved 0

4. Runtime:
   - identify which current functions will bottleneck first;
   - give deterministic memoization keys;
   - if necessary, give a SAT/CSP replacement for fixed-rack assignment search.

After the full schema basis exists, the branch will run:

  python tools/run_nonperm3_detector_product_cross_effect_audit.py \
    --certificate proofs/nonperm3_arity2_endpoint_gate_full_schema_certificate.json \
    --certificate proofs/nonperm3_arity3_endpoint_gate_q4_full_schema_certificate.json \
    --certificate proofs/nonperm3_arity3_q5_resolution_certificate.json \
    --bound 3 \
    --arity 4 \
    --state-limit 1000000 \
    --require-all-55 \
    --run-audit \
    --output proofs/nonperm3_width3_arity4_cross_effect_audit.json

Decision rule:

- any quotient_nontrivial=true disproves width-3 propagation only for that
  detector product;
- all 55 untruncated quotient_size=1 gives no arity-4 obstruction but still no
  all-n theorem;
- any truncation is inconclusive.

Return theorem/proof, finite evidence, heuristic, and unsupported claims in
separate categories.

theoretical

We are working on Will Sawin's MathOverflow problem:

For every finite bijective set-theoretic Yang-Baxter solution X, prove or
disprove the existence of a finite rack Y, independent of braid index n, such
that for all n:

  ker rho_{Y,n} <= ker rho_{X,n}.

You should assume you do not have access to my local workspace.  You do have
the GitHub repository/branch and should download or inspect that branch before
making repo-specific claims:

  https://github.com/alexrudimer-boop/sawin/tree/codex/atom-inner-row-lift

All file paths below are repo-relative after checking out:

  git clone https://github.com/alexrudimer-boop/sawin.git
  cd sawin
  git checkout codex/atom-inner-row-lift

Current theoretical frontier:

The non-permutation |X|=3, arity-3 endpoint gate is reported closed by finite
q=5 rack detectors, and the endpoint-candidate input basis is now locally
reconstructed.  This is finite fixed-arity evidence only.  The missing
all-arity bridge is not the q=5 count; it is the width-3 endpoint/rack-kernel
propagation statement.

For a fixed non-permutation size-three solution X, let Y_X be the componentwise
product of the distinct finite rack targets appearing in the verified arity-2
and arity-3 endpoint detector schemas for X.  For braid index n, write:

  K^Y_n = ker(B_n -> Sym(Y_X^n)).

Let J^Y_{3,n} be the normal closure in B_n of all consecutive parabolic copies
of K^Y_k for k<=3.  The tautological inclusion is:

  rho^X_n(J^Y_{3,n}) <= rho^X_n(K^Y_n).

The missing direction is:

  rho^X_n(K^Y_n) <= rho^X_n(J^Y_{3,n}).

Equivalently, the first finite obstruction to this width-3 bridge is:

  C^{X,Y_X}_{3,4}
    =
  rho^X_4(K^{Y_X}_4) / rho^X_4(J^{Y_X}_{3,4}).

Task:

Try to prove or refute a genuine all-arity theorem behind this bridge.  Do not
use q<=5 endpoint closure as an all-arity proof.  Focus on one of these exact
outputs:

A. A rigorous theorem proving width-3 realized kernel propagation for every
   non-permutation size-three X and every detector product Y_X built from the
   arity-2 and arity-3 contextual endpoint detector basis.  The proof must
   explain why Brunnian or high-context kernel-fiber monodromy cannot occur.

B. A rigorous obstruction mechanism showing how an element of K^Y_n can move
   X^n while all width-3 parabolic shadows are harmless.  This should be a
   normalized obstruction sequence, not just a high-arity miss against one
   finite detector product.

C. A precise no-go analysis showing which additional structural hypothesis
   would make the width-3 theorem true, and whether the reconstructed
   contextual detector basis has any plausible chance of satisfying it.

Relevant branch files to inspect:

  proofs/nonperm3_endpoint_detector_reconstruction.md
  proofs/nonperm3_size3_higher_arity_frontier.md
  proofs/width3_cross_effect_propagation_response_review.md
  proofs/parabolic_kernel_generation_bounded_width.md
  proofs/rack_residual_obstruction_tower.md
  src/ybe_domination/rack_residual_tower.py
  src/ybe_domination/nonperm3_detector_products.py
  src/ybe_domination/nonperm3_endpoint_detector_basis.py

Return theorem/proof, finite evidence, heuristic, and unsupported claims in
separate categories.  If a proof attempt fails, identify the exact first
unproved implication in mathematical terms.
