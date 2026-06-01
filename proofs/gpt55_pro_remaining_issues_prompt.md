# GPT-5.5 Pro remaining-issues prompt

Date: 2026-05-31

You are GPT-5.5 Pro.  I am attaching the current repository zip for a
research workspace on the Sawin finite-rack domination problem for finite
bijective set-theoretic Yang-Baxter solutions.  Treat the attached files as
the source of record.  Do not use the internet.  Inspect the proof notes,
code, tests, generated proof log, and spreadsheet audits before answering.

Your task is to completely resolve the problem.  Return exactly one of these
two outcomes if you can prove it:

A. A complete proof of finite-rack domination for every finite bijective
set-theoretic Yang-Baxter solution.

B. An explicit finite bijective set-theoretic Yang-Baxter counterexample not
dominated by any finite rack, together with a normalized-law obstruction
sequence defeating every finite rack.

Problem statement.  For every finite bijective set-theoretic Yang-Baxter
solution `X`, prove or disprove the existence of one finite rack `Y`,
independent of braid index `n`, such that for every `n`,

```text
ker rho_{Y,n} <= ker rho_{X,n}.
```

Hard constraints:

- Do not give finite-search-only evidence.
- Do not use timeout evidence.
- Do not use a rack, detector group, quotient, or obstruction group that
  depends on `n`.
- Every computational audit in the repository is only a certificate checker,
  reduction checker, example generator, or convention audit.  A decisive
  step must be converted into a symbolic all-`n` proof.
- Do not present an incomplete A proof or an incomplete B construction as a
  resolution.

## Start Here

Read these files first, in this order:

1. `proofs/progress_summary.md`
2. `README.md`
3. `proofs/sawin_status.md`
4. `proofs/proof_critic_gap_audit.md`
5. `proofs/descent_endpoint_repair_contract.md`
6. `proofs/post_linear_remaining_finite_system.md`
7. `proofs/post_linear_completion_audit.md`
8. `proofs/nonlinear_overlap_reduction_after_linear_closure.md`
9. `proofs/nonlinear_overlap_refined_obstruction.md`
10. `proofs/triangular_k_left_defect_ledger.md`
11. `proofs/triangular_k_left_kernel_closure.md`
12. `proofs/triangular_k_left_recovery_routing.md`
13. `proofs/triangular_k_left_coordinate_unit_routing.md`
14. `proofs/universal_continuation_identity_routing.md`
15. `proofs/universal_continuation_identity_endpoint_witness.md`
16. `proofs/endpoint_family_symmetric_fork.md`
17. `proofs/triangular_recovery_symmetric_endpoint_fork.md`
18. `proofs/universal_continuation_symmetric_endpoint_fork.md`
19. `proofs/mixed_unit_context_symmetric_endpoint_fork.md`
20. `proofs/triangular_recovery_unit_observer.md`
21. `proofs/triangular_recovery_longitude_expression_certificate.md`
22. `proofs/triangular_recovery_derived_series_fork.md`
23. `proofs/unit_continuation_abelian_kernel_lift.md`
24. `proofs/unit_continuation_derived_series_reduction.md`
25. `proofs/unit_perfect_residual_symmetric_dichotomy.md`
26. `proofs/normalized_law_sequence_gate.md`
27. `proofs/diagonal_normalized_obstruction.md`
28. `proofs/normalized_law_counterexample_certificate.md`
29. `proofs/symmetric_tower_counterexample_certificate.md`
30. `proofs/master_local_residual_positive_closure.md`
31. `proofs/gpt55_pro_resolution_prompt.md`

Then inspect the relevant code and tests:

```text
src/ybe_domination/nonlinear_overlap.py
src/ybe_domination/endpoint_factorization.py
src/ybe_domination/repair_contract.py
src/ybe_domination/triangular.py
src/ybe_domination/continuation.py
tests/test_nonlinear_overlap.py
tests/test_endpoint_factorization.py
tools/build_proof_log_docx.py
```

## Current State

The repository does not yet contain a final solution.  The old candidate
positive closure is conditional; the proof critic found a real gap in uniform
descent separation and endpoint longitudinalization.  The finite-linear
overlap route has been closed, and the current remaining nonlinear target is
packaged by

```text
post_linear_remaining_finite_system_audit(...)
```

as an explicit finite post-linear system.  The active remaining families are:

- System K: a live kink-completion deficit in the missing-Latin triangular
  ledger.
- System U: the triangular-recovery unit endpoint family, reached after a K
  deficit is routed to the fixed `U_tri` endpoint observer.
- System C: identity-routed universal-continuation endpoint edges.
- System M: mixed-unit context endpoint keys.

Systems U, C, and M may appear together as a product of routed endpoint
families.  A certificate for one endpoint family must remove only that
family; it must not hide an unclosed family in the same product row.

The latest repository state added supplied-certificate symmetric fork
interfaces:

- `triangular_recovery_symmetric_endpoint_fork_audit(...)` closes System U
  only when it uses the fixed `U_tri` observer, covers exactly the routed
  U endpoint keys, and proves a faithful symmetric endpoint cutoff.
- `universal_continuation_identity_symmetric_endpoint_fork_audit(...)`
  closes System C only when it matches the identity-routing ledger, covers
  exactly the identity-routed lost edges, and proves a faithful symmetric
  cutoff for that continuation endpoint family.
- `mixed_unit_context_symmetric_endpoint_fork_audit(...)` closes System M
  only when it matches the coordinate-unit routing ledger, covers exactly the
  mixed-unit context keys, and proves a faithful symmetric cutoff for that
  mixed endpoint family.

These are not uniform theorems.  They are exact supplied-data interfaces.  To
prove A, you must construct the witnesses or symmetric cutoffs uniformly for
every remaining local-minimal interval.  To prove B, you must turn failure of
all such finite endpoint certificates into a normalized-law sequence with
actual residual movement.

One additional K guardrail is already closed in the executable wrapper: a
supplied triangular-Latin defect closure with any proper generated
congruence row is a local-minimality contradiction.  It is classified as
`closed_by_triangular_latin_proper_closure` and must not be routed to an
endpoint family.  Only universal closure rows are candidates for the System U
recovery endpoint route.

## What Must Be Done To Resolve The Problem

1. Audit the post-linear reduction.

   Verify that every unresolved local-minimal primitive overlap after finite
   linear closure really lands in System K or in routed endpoint Systems U,
   C, M as described by `post_linear_remaining_finite_system.md`.  If a
   reduction note is conditional, either prove the missing condition
   symbolically or keep that condition as an explicit unresolved obligation.

2. Close or refute System K.

   A direct System K survivor has nonempty
   `live_k_missing_latin_row_defects`.  To prove A, show that every such
   live missing-Latin triangular defect is impossible in a genuine
   local-minimal finite YBE interval, or route it through fixed detector data
   into Systems U, C, or M with an audited routing certificate.  Do not treat
   a downstream endpoint certificate as closing System K until the K defect
   itself has been routed or eliminated.

   To prove B from K, construct one explicit finite local interval with a
   live K defect and prove that no fixed finite detector can kill the
   resulting residual motion.  Then upgrade that motion to the normalized-law
   obstruction sequence described in `diagonal_normalized_obstruction.md`.

3. Close or refute System U.

   System U is the triangular-recovery endpoint problem in the fixed unit
   group `U_tri`.  To prove A, prove uniformly in `n` that every routed
   triangular-recovery endpoint lies in `V_beta(U_tri)`.  Acceptable proof
   formats include:

   - active detector-lift rows for the endpoint observer;
   - explicit endpoint-longitude expressions;
   - derived-series reduction plus a stable perfect-residual witness;
   - direct subgroup membership with a symbolic all-`n` argument;
   - a fixed symmetric endpoint cutoff for the finite routed `U_tri` family.

   The supplied checker
   `triangular_recovery_symmetric_endpoint_fork_audit(...)` verifies only the
   last format for a supplied finite family.  It does not construct the
   uniform family for you.

4. Close or refute System C.

   System C consists of identity-routed universal-continuation lost edges.
   To prove A, construct fixed product endpoint-longitude witnesses for every
   identity-routed lost edge, or prove a fixed faithful symmetric endpoint
   cutoff for the exact continuation endpoint family.  Use
   `universal_continuation_identity_endpoint_witness_audit(...)` or
   `universal_continuation_identity_symmetric_endpoint_fork_audit(...)` only
   as supplied-certificate checkers.

   To prove B from C, exhibit an explicit routed continuation endpoint miss,
   prove that every fixed finite endpoint detector fails on it, and upgrade
   the miss to a normalized-law sequence with moved residual tuples.

5. Close or refute System M.

   System M consists of mixed-unit context endpoint keys
   `(left_color, right_color, side)`.  To prove A, prove that each routed
   mixed-unit context endpoint factors through fixed detector/readout data,
   or prove a fixed faithful symmetric endpoint cutoff for the exact mixed
   endpoint family.  Use
   `mixed_unit_context_endpoint_witness_audit(...)` or
   `mixed_unit_context_symmetric_endpoint_fork_audit(...)` only as supplied
   checkers.

   To prove B from M, find a genuine mixed-unit endpoint miss that survives
   all fixed finite detector groups and upgrade it to the required
   normalized-law obstruction sequence.

6. Respect the product guardrail.

   In product endpoint rows, Systems U, C, and M are independent obligations.
   A witness or symmetric fork for U removes only U from
   `unclosed_routed_endpoint_systems`; likewise for C and M.  A correct A
   proof must close every active endpoint family in the product.  A correct B
   proof may use one unclosed family only after proving it cannot be killed by
   any fixed finite detector group.

7. Finish outcome A if all systems close.

   Once K and all routed endpoint systems close, construct the local detector
   group `G(pi,Q)` as one fixed finite product of the Green,
   Schutzenberger, atom, known-branch, endpoint/unit, transport-state, and
   newly proved endpoint factors.  Prove the all-`n` implication

   ```text
   Lambda_{G,n}(beta) = Lambda_{G,n}(1) => Delta_n(beta) = 1
   ```

   for every braid index `n`.  Then use the sharp obstruction rack
   `A_G = T_2 x (G x G)` and the congruence-chain induction to build the
   final finite rack.  The final rack must not depend on `n`.

8. Finish outcome B if any system cannot close.

   A B solution must include:

   - an explicit finite set `X`;
   - an explicit bijective YBE map `R_X:X^2 -> X^2`;
   - a symbolic proof of the Yang-Baxter equation;
   - explicit braids `beta_j in B_{q_j}` with `q_j -> infinity`;
   - proof that for every finite group `G`,
     `Lambda_{G,q_j}(beta_j)=Lambda_{G,q_j}(1)` eventually;
   - proof that `rho_{X,q_j}(beta_j)` moves explicit tuples;
   - the normalized-law/Brunnian sequence required by
     `normalized_law_sequence_gate.md` and
     `diagonal_normalized_obstruction.md`;
   - an explanation through the sharp obstruction theorem that this defeats
     domination by every finite rack.

## Mandatory Final Audit

Before returning a claimed resolution, explicitly answer:

1. Is any decisive step finite-search-only?
2. Are semisplit local-minimal families fully handled?
3. Is every detector group and every rack independent of braid index `n`?
4. If returning A, where exactly is `G(pi,Q)` constructed and how does the
   congruence-chain induction produce the final rack?
5. If returning B, why does the obstruction defeat every finite group `G`,
   hence every finite rack?
6. Are product endpoint rows handled family-by-family without hiding any
   unclosed U, C, or M obligation?

Return outcome A or outcome B only if the proof is genuinely complete.  If
you cannot complete either outcome, state the exact missing lemma or exact
missing counterexample ingredient and the shortest route to settle it.
