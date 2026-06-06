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

All file paths below are repo-relative after checking out:

  git clone https://github.com/alexrudimer-boop/sawin.git
  cd sawin
  git checkout codex/atom-inner-row-lift

Current theoretical frontier:

The non-permutation |X|=3, arity-3 endpoint gate is reported closed by finite
q=5 rack detectors, and the endpoint-candidate input basis is locally
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

Important guardrails:

- Do not claim the problem is solved from fixed-arity finite evidence.
- Do not treat q<=4 misses as negative evidence after the reported q=5 closure.
- Do not treat a high-arity miss against one detector product as a Sawin
  counterexample unless it is upgraded to a cofinal rack-prefix obstruction.

Relevant branch files to inspect:

  proofs/nonperm3_endpoint_detector_reconstruction.md
  proofs/nonperm3_size3_higher_arity_frontier.md
  proofs/width3_cross_effect_propagation_response_review.md
  proofs/parabolic_kernel_generation_bounded_width.md
  proofs/rack_residual_obstruction_tower.md
  src/ybe_domination/rack_residual_tower.py
  src/ybe_domination/nonperm3_detector_products.py
  src/ybe_domination/nonperm3_endpoint_detector_basis.py

Task:

Try to prove or refute a genuine all-arity theorem behind the width-3 bridge.
Do not use q<=5 endpoint closure as an all-arity proof.  Focus on one of these
exact outputs:

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

Return theorem/proof, finite evidence, heuristic, and unsupported claims in
separate categories.  If a proof attempt fails, identify the exact first
unproved implication in mathematical terms.
