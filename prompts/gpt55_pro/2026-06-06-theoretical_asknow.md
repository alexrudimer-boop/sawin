theoretical_asknow

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

Current theoretical frontier:

The non-permutation |X|=3 endpoint-detector basis through arity 3 is locally
reconstructed and verified.  The branch has full arity-2, arity-3 q<=4, and
q=5-only contextual detector schema certificates.  The q=5-only certificate
covers the 216 q<=4-unresolved arity-3 endpoint candidates, giving 37,692
combined arity-3 coverages and 0 remaining unresolved principal endpoint
candidates.

This remains finite fixed-arity evidence only.  The missing all-arity bridge
is not the q=5 endpoint count; it is a width-3 endpoint/rack-kernel propagation
theorem.

For a fixed non-permutation size-three solution X, let Y_X be the componentwise
product of the distinct finite rack targets appearing in the verified arity-2
and arity-3 endpoint detector schemas for X.  For braid index n, write:

  K^Y_n = ker(B_n -> Sym(Y_X^n)).

Let J^Y_{3,n} be the normal closure in B_n of all consecutive parabolic copies
of K^Y_k for k<=3.  The tautological inclusion is:

  rho^X_n(J^Y_{3,n}) <= rho^X_n(K^Y_n).

The missing direction is:

  rho^X_n(K^Y_n) <= rho^X_n(J^Y_{3,n}).

Equivalently, one tests finite realized cross-effects:

  C^{X,Y_X}_{3,n}
    =
  rho^X_n(K^{Y_X}_n) / rho^X_n(J^{Y_X}_{3,n}).

New finite evidence:

The arity-4 realized cross-effect has now been computed for all 55
non-permutation size-three tables using a stabilizer method in
`componentwise_stabilizer_realized_parabolic_cross_effect_audit`.

Certificate:

  proofs/nonperm3_width3_arity4_cross_effect_audit_stabilizer.json

Verifier:

  python tools/verify_nonperm3_width3_cross_effect_audit.py \
    proofs/nonperm3_width3_arity4_cross_effect_audit_stabilizer.json \
    --require-complete-basis \
    --require-run-audit

Result:

  detector_index_rows 55
  audit_rows 55
  truncated rows 0
  quotient_nontrivial rows 0
  quotient_size distribution {1: 55}
  kernel_image_size distribution {1: 55}

Thus the first possible finite obstruction, n=4, is absent for the current
detector products Y_X.  In fact every arity-4 row has trivial realized
detector-kernel image on X^4.  This still does not prove any all-n theorem.

Important guardrails:

- Do not claim the problem is solved from fixed-arity finite evidence.
- Do not treat q<=4 misses as negative evidence after the q=5 closure.
- Do not treat a high-arity miss against one detector product as a Sawin
  counterexample unless it is upgraded to a cofinal rack-prefix obstruction.
- Do not treat the arity-4 trivial quotient as an induction step unless the
  induction hypothesis and transition map are explicitly proved.

Relevant branch files to inspect:

  proofs/nonperm3_endpoint_detector_reconstruction.md
  proofs/nonperm3_size3_higher_arity_frontier.md
  proofs/width3_cross_effect_propagation_response_review.md
  proofs/parabolic_kernel_generation_bounded_width.md
  proofs/rack_residual_obstruction_tower.md
  proofs/nonperm3_width3_arity4_cross_effect_audit_stabilizer.json
  src/ybe_domination/rack_residual_tower.py
  src/ybe_domination/nonperm3_detector_products.py
  src/ybe_domination/nonperm3_endpoint_detector_basis.py

Task:

Try to prove or refute a genuine all-arity theorem behind the width-3 bridge.
Do not use q<=5 endpoint closure or the arity-4 cross-effect computation as an
all-arity proof.  Focus on one of these exact outputs:

A. A rigorous theorem proving width-3 realized kernel propagation for every
   non-permutation size-three X and every detector product Y_X built from the
   arity-2 and arity-3 contextual endpoint detector basis.  The proof must
   explain why Brunnian or high-context kernel-fiber monodromy cannot occur.
   The new arity-4 data may be used only as finite evidence or as a base case
   if an actual induction is supplied.

B. A rigorous obstruction mechanism showing how an element of K^Y_n, necessarily
   with n>=5 after the current computation, can move X^n while all width-3
   parabolic shadows are harmless.  This should be a normalized obstruction
   sequence, not just a high-arity miss against one finite detector product.

C. A precise no-go analysis showing which additional structural hypothesis
   would make the width-3 theorem true, and whether the reconstructed
   contextual detector basis or the new arity-4 trivial-kernel data suggests
   that hypothesis.

Return theorem/proof, finite evidence, heuristic, and unsupported claims in
separate categories.  If a proof attempt fails, identify the exact first
unproved implication in mathematical terms.
