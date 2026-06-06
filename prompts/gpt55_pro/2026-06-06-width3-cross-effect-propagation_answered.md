# GPT-5.5 Pro width-3 cross-effect prompt

Status: answered on 2026-06-06.  The response returned outcome `C`: no
proof-grade width-3 propagation theorem from current branch data, and the next
required step is importing or reconstructing the full q=5 detector schema
certificate before running the arity-4 componentwise cross-effect audit.

Review note:
`proofs/width3_cross_effect_propagation_response_review.md`

Date: 2026-06-06

Use this as the next focused prompt for ChatGPT 5.5 Pro / Extended Pro.  It is
not a broad "solve everything" prompt; it asks for the first decisive
higher-arity step after the reported q=5 arity-3 closure.

```text
We are working on Will Sawin's MathOverflow problem:

For every finite bijective set-theoretic Yang-Baxter solution X, prove or
disprove the existence of a finite rack Y, independent of braid index n, such
that for all n:

  ker rho_{Y,n} <= ker rho_{X,n}.

Current workspace branch:
  alexrudimer-boop/sawin, branch codex/atom-inner-row-lift

Important current status:

1. The non-permutation |X|=3, arity-3 endpoint gate is reported closed by
   finite rack detectors with |Q|<=5.

   Reported q=5 verifier output:

   OK nonperm3 arity-3 q5 resolution certificate verified
   sha256 376e901839c978530ecd32893da56de5ff69b26dd3c407d1cb3eda365c63fc75
   new_positive_detector_coverages 216
   new_positive_detector_schemas 22
   combined_positive_detector_coverages 37692
   remaining_unresolved_candidates 0

   Previous q<=4 checkpoint:

   sha256 bdd034c1c1fd665054818b58a76249bc009a0532dec33fea404063d61a82fee8
   nonpermutation_ybe_tables 55
   arity3_bad_endpoint_pairs 37692
   positive_detector_coverages 37476
   positive_detector_schemas 320
   unresolved_obstruction_candidates 216
   by_rack_size {'q2': 16416, 'q3': 20736, 'q4': 324}
   by_monoid {'truncated_structure_monoid_length_1': 15309,
              'truncated_structure_monoid_length_2': 22167}

2. The full q=5 JSON certificate and verifier are not yet local in the
   workspace.  Treat the q=5 batch counts as reported unless you see the
   actual certificate.  The displayed first q=5 detector is locally checked by
   tests.

3. The displayed first q=5 detector:

   ybe_table = [0,3,6,1,4,7,5,2,8]
   endpoints = [00,2,epsilon] and [epsilon,2,00]
   M = truncated structure monoid length 2, |M|=10
   Q = fixed rack of size 5
   endpoint values = 2 and 3
   all 900 contextual T-relations and all 900 contextual R-relations verified
   locally.

4. Closing arity 3 does not prove all-arity domination.  The missing bridge is
   a uniform bounded-core / parabolic propagation theorem, or a precise
   higher-arity obstruction.

Files to inspect first:

  proofs/nonperm3_arity3_q5_resolution.md
  proofs/nonperm3_size3_higher_arity_frontier.md
  proofs/nonperm3_detector_product_import_gap.md
  proofs/parabolic_kernel_generation_bounded_width.md
  proofs/finite_endpoint_change_cover_theorem.md
  src/ybe_domination/rack_residual_tower.py
  src/ybe_domination/nonperm3_detector_products.py
  tools/run_componentwise_cross_effect_audit.py
  tools/run_nonperm3_detector_product_cross_effect_audit.py
  tests/test_rack_residual_tower.py
  tests/test_nonperm3_detector_products.py
  tests/test_nonperm3_arity3_checkpoint.py

Focused task:

Analyze the following proposed all-arity bridge.

For each non-permutation size-three YBE table X, let Y_X be the componentwise
product of all distinct finite rack targets appearing in the verified arity-2
and arity-3 endpoint detector schemas for X.

For each arity n:

  K^Y_n = ker(B_n -> Sym(Y_X^n))
  H^X_n = ker(B_n -> Sym(X^n))

Let J^Y_{3,n} be the normal closure in B_n of all consecutive parabolic copies
of K^Y_k for k<=3.

The proposed width-3 propagation lemma is:

  rho^X_n(K^Y_n) = rho^X_n(J^Y_{3,n}) for every n.

Equivalently, any braid beta invisible to Y_X in arity n has X-action
generated, as an X-action, by consecutive parabolic copies of invisible
actions in arities 2 and 3.

Your job:

1. Try to prove this width-3 propagation lemma in a proof-grade way for the
   non-permutation |X|=3 branch.

2. If it cannot be proved from current data, identify the exact obstruction.
   The expected first obstruction is the realized four-strand cross-effect:

     C^{X,Y_X}_{3,4}
       = rho^X_4(K^Y_4) / rho^X_4(J^Y_{3,4}).

3. Specify the smallest decisive computation and the exact certificate shape.
   The current local helper is:

     ybe_domination.componentwise_realized_parabolic_cross_effect_audit
     tools/run_componentwise_cross_effect_audit.py

   The importer/full-table wrapper added after the first prompt draft is:

     tools/run_nonperm3_detector_product_cross_effect_audit.py

   Current local compact-artifact import status:

     schema_like_detector_records: 1
     nonpermutation_ybe_tables: 55
     tables_with_detector_components: 1
     missing_table_count: 54
     incomplete_detector_basis: true

   This is an artifact gap only.  It is not evidence against width-3
   propagation and not a Sawin counterexample.

   The intended first full audit is:

     for each of the 55 non-permutation |X|=3 tables:
       X = flat YBE table
       detectors = all rack target tables in the imported arity-2 and arity-3
                   endpoint detector basis for that X
       bound = 3
       arity = 4

   Required row fields:

     ybe_table
     detector_component_count
     detector_component_sizes
     bound
     arity
     joint_image_size
     kernel_image_size
     parabolic_image_size
     quotient_size
     quotient_nontrivial
     seed_count
     first_witness_word
     first_moved_tuple
     first_moved_tuple_image
     truncated

4. Apply this decision rule:

   if any row has quotient_nontrivial = true:
     the width-3 propagation lemma is false for that detector product;

   if all 55 rows are untruncated and quotient_size = 1:
     there is no four-strand obstruction, but an all-n induction is still
     required;

   if any row truncates:
     the result is inconclusive and needs stronger permutation-group
     compression.

5. Be strict about theorem versus finite evidence:

   - Do not claim that arity-3 closure proves all arities.
   - Do not treat a q<=4 miss as negative evidence after q=5 closure.
   - Do not treat a single high-arity miss against this product detector as a
     Sawin counterexample; it is only a failure of the proposed width-3 bridge
     unless upgraded to a cofinal rack-prefix obstruction.

Return one of:

A. A proof of the width-3 propagation lemma, with all definitions and the
   exact induction/parabolic-generation argument.

B. A concrete obstruction certificate shape showing the lemma is false,
   preferably with an explicit n=4 witness if enough data is available.

C. A precise statement that the q=5 certificate must first be imported, plus
   the exact next computation and why it is decisive.
```
