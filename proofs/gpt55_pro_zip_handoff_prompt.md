# GPT-5.5 Pro zip handoff prompt

I am attaching a zip archive of a research workspace for the Sawin
finite-rack domination problem for finite bijective set-theoretic
Yang-Baxter solutions. Treat the archive as the source of record. Inspect the
proof notes, code, tests, generated Word proof log, spreadsheet audit, and
candidate obstruction artifacts before answering.

Your job is to completely resolve the problem. Return exactly one of:

A. A complete proof of Sawin finite-rack domination.

B. An explicit finite bijective set-theoretic Yang-Baxter counterexample not
dominated by any finite rack, with a normalized-law obstruction sequence.

Global theorem: for every finite bijective set-theoretic YBE solution `X`,
prove or disprove the existence of a finite rack `Y`, independent of braid
index `n`, such that for all `n`,

```text
ker rho_{Y,n} subset ker rho_{X,n}.
```

Hard constraints:

- Do not give finite-search-only evidence.
- Do not use timeout evidence.
- Do not use a rack or detector group depending on `n`.
- Every computational certificate in the zip must be converted into a
  symbolic all-`n` argument before it can close A or B.

First read:

1. `proofs/progress_summary.md`
2. `README.md`
3. `proofs/sawin_status.md`
4. `proofs/gpt55_pro_resolution_prompt.md`
5. `proofs/diagonal_normalized_obstruction.md`
6. `proofs/normalized_law_sequence_gate.md`
7. `proofs/longitude_subgroup_witness_calculus.md`
8. `proofs/artin_defect_longitudinalization_sieve.md`
9. `proofs/artin_detector_lift_criterion.md`
10. `proofs/atom_inner_detector_lift_rows.md`
11. `proofs/green_first_output_defect_criterion.md`
12. `proofs/green_defect_kernel_quotient_detection.md`
13. `proofs/green_defect_potential_coboundary.md`
14. `proofs/artin_defect_abelianization_barrier.md`
15. `proofs/green_defect_abelianization_split.md`
16. `proofs/abelian_longitude_image_criterion.md`
17. `proofs/green_balanced_defect_gauge_decomposition.md`
18. `proofs/terminal_gauge_longitudinalization_criterion.md`
19. `proofs/principal_gauge_extension_detector.md`
20. `proofs/transport_state_rackification_detector.md`
21. `proofs/continuation_congruence_descent_gate.md`
22. `proofs/elementary_continuation_closure.md`
23. `proofs/universal_continuation_derivation_certificate.md`
24. `proofs/product_readout_kernel_assembly.md`
25. `proofs/product_readout_descent_separation.md`
26. `proofs/readout_seed_saturation.md`
27. `proofs/local_minimal_seed_saturation_dichotomy.md`
28. `proofs/lost_edge_external_routing.md`
29. `proofs/routed_lost_edge_endpoint_witness.md`
30. `proofs/chart_transport_collapse.md`
31. `proofs/descent_separation_transport_rack_closure.md`
32. `proofs/unit_continuation_final_obstruction.md`
33. `proofs/sawin_proof_log.docx`
34. `tables/reduction_audit.xlsx`
35. The code and tests under `src/`, `tools/`, and `tests/`

Then audit and use these reductions:

1. Quotient/residual setup.  For `pi:X->Z`, with `Z` dominated by rack `Q`,
   set `N_n=ker rho_{Q,n}`.  For `z in Z^n`, let
   `X_z=prod_i pi^{-1}(z_i)`, define
   `delta_{n,z}:N_n->Sym(X_z)`, and bundle the residual action as
   `Delta_n(beta)=(delta_{n,z}(beta))_z`.

2. Sharp obstruction theorem.  For finite group `G`,
   `A_G=T_2 x (G x G)` with
   `(a,u)▷(b,v)=(aba^{-1},av)` detects finite-`G` Artin-longitude data
   `Lambda_{G,n}(beta)`.  Residual detection is equivalent to finding one
   finite `G`, independent of `n`, such that for all `n` and
   `beta,gamma in N_n`,

   ```text
   Lambda_{G,n}(beta)=Lambda_{G,n}(gamma) => Delta_n(beta)=Delta_n(gamma).
   ```

   The kernel form suffices:

   ```text
   Lambda_{G,n}(beta)=Lambda_{G,n}(1) => Delta_n(beta)=1.
   ```

   Then `Q x A_G` dominates the interval.  In the archive this is
   implemented by `sharp_obstruction_rack(Q,G)`.

3. Congruence-chain induction.  For a maximal congruence chain
   `Delta_X=kappa_0<...<kappa_m=Nabla_X`, it suffices to prove the local
   theorem for every local-minimal interval
   `X/kappa_i -> X/kappa_{i+1}`.  If the local detector is `G_i`, the global
   rack is obtained by iterating `Q_i=Q_{i+1} x A_{G_i}`.  The archive
   implements this assembly as `assemble_congruence_chain_rack(Q_m, groups)`,
   which records the size factor `2*|G_i|^2` at each step and has no braid
   index input.  The resulting detector must be finite and independent of
   `n`.

4. Local residual table.  For `R_Z(a,b)=(a dot b, a*b)` and fibres `A_a`,
   local maps

   ```text
   T_{a,b}: A_a x A_b -> A_{a dot b} x A_{a*b}
   ```

   satisfy the coloured YBE

   ```text
   T^{12}_{a dot b,(a*b) dot c} T^{23}_{a*b,c} T^{12}_{a,b}
   =
   T^{23}_{a*(b dot c),b*c} T^{12}_{a,b dot c} T^{23}_{b,c}.
   ```

   Local-minimality means the only admissible congruence families
   `theta_a` are all equality or all universal, where
   `T_{a,b}(theta_a x theta_b)=theta_{a dot b} x theta_{a*b}`.  You must
   handle semisplit families, not just ordinary fibre partitions.

5. Semigroup and corridor gates.  Use the finite-semigroup holonomy notes,
   `proofs/unit_holonomy_longitude_gate.md`, and
   `proofs/unit_factorization_gate.md`.  Also use
   `proofs/unit_section_detection_criterion.md`,
   `proofs/unit_composite_longitude_criterion.md`, and
   `proofs/unit_section_product_detector.md`.  If a finite
   transformation-monoid observer word has final residual action a
   permutation, every factor in that word is already a unit/permutation;
   reset-like nonunit labels cannot hide inside a B obstruction.  If the
   final unit composite lies in `V_beta(U(M))` for the fixed unit group,
   identity finite longitude data kills the branch; this endpoint condition
   is enough even if intermediate labels telescope.  Finitely many such fixed
   unit groups must be multiplied into one product detector independent of
   `n`; use `unit_composite_product_detection_audit(...)` as the executable
   endpoint guardrail and check the recorded endpoint tuple in the product
   longitude subgroup.  Any semigroup-channel B obstruction must survive in
   the unit/group part and defeat every finite group by normalized laws.
   Also use `proofs/unit_composite_longitude_route_audit.md`: the endpoint
   route ladder is identity endpoint, single evaluated-longitude witness, and
   membership in the full longitude-value subgroup.  A missing single witness
   is not a B obstruction if subgroup membership holds.
   Also use `proofs/endpoint_longitude_expression_certificate.md`: displaying
   the endpoint as a word in evaluated recursive longitudes for one assignment
   into the fixed unit group is the non-enumerative A-side certificate for
   endpoint subgroup membership.  For several endpoint groups, use the product
   expression audit to package those factor certificates into one product
   detector certificate, and audit the returned explicit product subgroup
   witness (`product_witness_value` and `product_witness_matches_endpoint`).
   This witness is a literal word in `V_beta(prod_i U(M_i))`; its letters may
   use different product-group assignments, as allowed in the definition of
   the longitude-value subgroup.
   Also use `proofs/artin_defect_longitudinalization_sieve.md`: it proves that
   Artin permutation defects `beta(w)p_beta(w)^-1` lie in the normal closure
   of the recursive longitudes and that every finite-group value of such a
   defect lies in `V_beta(G)`.  Thus the newest A-side target is not an
   arbitrary endpoint-longitude search, but the sharper local lemma that every
   elementary Green/corridor endpoint generator is a product of Artin
   permutation defect values in fixed factors of `H(pi,Q)`.  The helpers
   `artin_permutation_defect_witness_audit(...)`,
   `endpoint_artin_defect_audit(...)`, and
   `endpoint_product_artin_defect_audit(...)` verify supplied displays and
   assemble them into one product detector witness.  They do not prove that
   such displays always exist.
   Also use `proofs/artin_detector_lift_criterion.md`: if a fixed
   Green/corridor observer factor carries live-strand labels `(m_k,u_k)` and
   each positive/negative crossing row matches the active `U x U` Artin
   detector update, induction gives `u_k(beta)=phi(L_k(beta))`.  This resolves
   the unbounded braid-word recursion after the finite row identities are
   proved.  Audit proposed rows with `artin_detector_lift_transition_audit(...)`
   and the convention with `artin_detector_lift_braid_audit(...)`.
   Also use `proofs/atom_inner_detector_lift_rows.md`: after atom descent and
   totality, a rack-like atom quotient automatically satisfies the detector-lift
   rows in its inner group.  Positive rows follow from
   `L_{a*b}=L_a L_b L_a^-1`; negative rows are inverse positive rows.  Thus
   atom-inner groups are no longer an open row-identity factor; the remaining
   rows are Green kernel-block, Schutzenberger, and lower endpoint/unit
   holonomy factors.
   Also use `proofs/green_first_output_defect_criterion.md`: Green
   kernel-block and Schutzenberger rows are controlled by the single
   first-output defect `d_C(a,q)=g(q^a)g(q)^-1`; the second output is forced
   by the product relation.  Kernel-block defects are Schutzenberger
   pushforwards when no local-only edge-germs occur.  The remaining Green
   quotient step is `proofs/green_defect_kernel_quotient_detection.md`: for
   each observer `U_C`, quotient by the normal closure `Def_C` of all
   first-output defects.  The projected rows in `U_C/Def_C` are exact
   side-opposite rack-Artin rows and are killed by detector-lift.  The
   intermediate Green defect-kernel target is the endpoint
   `D_C(beta) in V_beta(Def_C)`.  Also use
   `proofs/green_defect_potential_coboundary.md`: it proves every elementary
   defect is a finite coboundary `eta(q^a)eta(q)^-1` in `Def_C`; this made
   potential principalness explicit before the balanced gauge refinement.
   Also use
   `proofs/artin_defect_abelianization_barrier.md`: Artin permutation defect
   values always lie in `[Def_C,Def_C]`, so elementary defects with nontrivial
   abelianization cannot be handled by Artin-defect displays alone.  Use full
   recursive-longitude membership, endpoint cancellation, or detector-lift
   labels for such abelian defect-kernel data.  Also use
   `proofs/green_defect_abelianization_split.md`: it separates the finite
   abelian target `Def_C/[Def_C,Def_C]` from the commutator endpoint, so the
   abelian layer can be attacked by ordinary finite abelian longitude data.
   Also use `proofs/abelian_longitude_image_criterion.md`: for finite
   abelian `A`, it identifies `V_beta(A)` with the subgroup generated by
   `a^{m_ij}` from the abelianized recursive-longitude exponent matrix.
   Also use `proofs/green_balanced_defect_gauge_decomposition.md`: it splits
   raw Green/Schutzenberger first-output defects into an Artin-visible
   commutator and a terminal second-output gauge boundary, so a final proof
   should focus on terminal gauge/unit holonomy.
   Also use `proofs/terminal_gauge_longitudinalization_criterion.md`: it
   packages terminal gauge holonomy as a telescope plus an endpoint-longitude
   certificate in fixed gauge factors.
   Also use `proofs/principal_gauge_extension_detector.md`: it closes the
   principal lower endpoint/unit gauge subcase by turning
   `(a,r)*(b,s)=(a*b,c(a,b)s)` and the YBE cocycle law into the finite rack
   `A x U` and fixed detector `Inn(A x U)`.
   Also use `proofs/transport_state_rackification_detector.md`: it removes
   principality for any strand-continuing finite gauge row by rackifying the
   finite state `A x E`; the remaining theorem burden is descent separation.
   Also use `proofs/continuation_congruence_descent_gate.md`: it reduces
   non-strand-continuing lower motion to the least admissible congruence
   generated by continuation changes `x~v`, leaving only the universal
   continuation corridor as the nontrivial local-minimal case.
   Also use `proofs/elementary_continuation_closure.md`: in a valid
   local-minimal target every single nontrivial continuation seed already has
   universal closure, so the remaining obstruction is seed-level rather than
   collective-only.
   Also use `proofs/universal_continuation_derivation_certificate.md`: it
   exposes the finite derivation rows for every edge in a universal
   single-seed continuation closure.  A positive proof must route those
   derived edges through fixed Green/Schutzenberger/atom readouts; a B proof
   must choose one derived edge and upgrade it to a normalized-law sequence.
   Also use `proofs/continuation_readout_propagation.md`: it proves that an
   admissible fixed readout relation containing one representative
   continuation seed contains that seed's whole least admissible closure.
   After this, the positive burden is representative seed visibility plus
   admissibility of the fixed readout relation, not separate proof for every
   derived edge.
   Also use `proofs/readout_kernel_admissibility.md`: it turns finite
   fibrewise detector labels into the fixed readout relation by taking their
   kernel, and `readout_kernel_audit(...)` checks exact admissibility by local
   table transport.  A positive proof must construct labels from fixed
   Green/Schutzenberger/atom/unit factors whose kernel is admissible and
   contains each representative seed.
   Also use `proofs/readout_descent_separation_certificate.md`: it combines
   readout-kernel admissibility with continuation seed killing.  If
   `readout_descent_separation_audit(...)` passes, the quotient lower row is
   strand-continuing and the transport-state rackification theorem applies.
   Also use `proofs/readout_kernel_quotient_interval.md`: it constructs the
   explicit finite quotient local interval on readout blocks and verifies the
   quotient continuation audit directly.  This is now the concrete object to
   which transport-state rackification applies.
   Also use `proofs/product_readout_kernel_assembly.md`: it assembles
   finitely many factor label systems into one tuple-valued product readout,
   with kernel equal to the meet of factor kernels.  This is the local readout
   analogue of multiplying fixed detector factors into one `H(pi,Q)`.
   Also use `proofs/product_readout_descent_separation.md`: it records the
   seed-level guardrail for product readouts.  A product readout kills a
   continuation seed only when every factor kills it, so product seed survival
   is the union of factor seed survival.
   Also use `proofs/readout_seed_saturation.md`: it computes the least
   admissible coarsening forced by one factor readout plus all continuation
   seeds.  In a local-minimal interval, a non-killing admissible equality
   factor saturates to universal, so any lost information must be routed
   elsewhere.
   Also use `proofs/local_minimal_seed_saturation_dichotomy.md`: it makes the
   equality/universal seed-saturation consequence executable and records
   forced universal collapse as an external-routing obligation.
   Also use `proofs/lost_edge_external_routing.md`: it separates descent
   quotient labels from external endpoint routing labels and records which
   seed-saturation edges are lost, routed, or still unrouted.
   Then use `proofs/routed_lost_edge_endpoint_witness.md`: every routed lost
   edge needs a product endpoint-longitude certificate in fixed detector
   factors; missing certificates are only unresolved obligations unless they
   are upgraded to normalized laws.
   Also use `proofs/chart_transport_collapse.md`: it proves transported
   elementary generators need no separate proof once one chart-conjugacy orbit
   representative is certified, because `V_beta(G)` is normal.  Then read
   `proofs/descent_separation_transport_rack_closure.md`: it records that
   transport-rack closure is proved and that descent separation is the final
   unproved A-route theorem.
   Also read `proofs/unit_continuation_final_obstruction.md`: in the final
   constant-observer universal-continuation case `Theta^cont=Nabla` and
   `K^O=Nabla`, nonunit continuation factors cannot move a residual
   permutation branch.  The only remaining obstruction in that channel is a
   unit endpoint `S_beta in U(M_cont)` whose membership in
   `V_beta(U(M_cont))` must be proved, or upgraded to a normalized-law B
   sequence if false.
   Also audit the Green atom-action layer through `proofs/green_branch_audit.md`
   and `atom_action_summary(...)`: it checks whether completed rows descend to
   operations on saturated atoms, `p(a) triangleright p(q)=p(a^q)` and
   `p(a^q) triangleleft p(q)=p(a)`.  A proof of A should either prove this
   descent symbolically in the relevant corridor branch or bypass it with a
   stronger finite readout; a proof of B may exploit an explicit failure only
   after upgrading it to the required normalized-law sequence.
   Also read `proofs/green_atom_quotient_layer.md`: when the atom action is
   total, `atom_quotient_solution(...)` gives the finite crossing
   `(A,Q)->(Q,A^Q)`, a right-rack-like YBE layer.  The helper
   `atom_quotient_rack_audit(...)` checks bijective right translations and
   right self-distributivity directly.  The remaining Green obstruction should
   therefore be section/unit holonomy below this atom rack layer, unless the
   atom descent theorem fails in a genuine local-minimal interval.
   Also read `proofs/green_atom_descent_closure.md`: the closure helper
   `atom_descent_closure_summary(...)` gives the least coarsening required
   for atom action and inverse bookkeeping to descend.  A proof of A must show
   this closure is trivial or controlled uniformly; a proof of B must turn a
   genuine closure failure into the required all-finite-group normalized-law
   sequence.
   Then use `proofs/green_atom_rack_lift_criterion.md`: the Green detector is
   the atom inner group multiplied by the lower unit groups, and the all-`n`
   burden is endpoint membership in that one product longitude-value subgroup.
   Also use `proofs/fixed_detector_readout_audit.md`: fixed-index readout
   tables are allowed only as audits.  A proof of A must construct the
   residual-fibre readout uniformly in `n` from one fixed finite detector, and
   a proof of B must defeat every finite group rather than one fixed-index
   readout table.
   The helper `symmetric_detector_readout_audit(X,n)` is the direct
   `Sym(X)` version over the one-point quotient; it proves some fixed-degree
   stress rows but is not an all-`n` theorem.
   Also read `proofs/direct_symmetric_known_branches.md`: it proves the
   direct `Sym(X)` implication on rack-type, involutive, permutation-form,
   and nondegenerate/guitar branches, and explains why the size-2/3
   symmetric-audit truncations are branch-closed rather than counterexample
   evidence.
   For two-strand failures of a proposed finite group detector, use
   `two_strand_group_detector_failure_certificate(X,G)`: it returns the
   explicit invisible braid `sigma_1^(2 exp(G))` and a moved tuple whenever
   `ord(R_X)` does not divide `2 exp(G)`.  The symmetric specialization kills
   the direct `A_{Sym(X)}` shortcut if it ever fires, but not the full Sawin
   theorem unless every finite group is defeated.
   Also use `proofs/two_strand_cyclic_detector.md`: for
   `r=ord(R_X)`, the cyclic group `C_r` always detects the two-strand action,
   so a pure crossing-order mismatch is not outcome B.
   The helper `exact_detector_product_readout_audit(...)` may be used only to
   check, in enumerable fixed-degree cases, that a displayed factor list is
   equivalent to one direct-product detector readout.

Known eliminated or finite-G-measurable branches in the archive include:
nondegenerate/guitar; fibre size 2 affine over `F_2`; two-colour fibre size 3
flip base with no strict primitive nonlinear obstruction; affine,
involutive/permutation, pairwise-linking, bounded Magnus/nilpotent, finite
semidirect affine, coboundary, product-longitude, and direct-product detector
branches.  Do not reopen these as search-only cases; either prove the missing
symbolic bridge they reduce to, or show exactly where a proof note is false.

Main task:

Prove the Master Local-Minimal Residual Theorem for arbitrary finite fibres
and quotient colours, or construct B.  The master theorem is:

For every local-minimal interval `pi:X->Z` with `Z` dominated by `Q`, there is
a finite group `G=G(pi,Q)`, independent of `n`, satisfying the finite-`G`
longitude implication above.

If proving A:

- Explicitly construct the finite group `G(pi,Q)` or the final finite rack
  `Y`.
- Prove braid-action-level detection for all `n`.
- Handle arbitrary fibre size and arbitrary quotient colours.
- Handle semisplit local-minimality.
- Finish the congruence-chain induction.

If proving B:

- Give an explicit finite set `X` and bijection `R_X:X^2->X^2`.
- Prove YBE symbolically.
- Construct braids `beta_j in B_{q_j}` with `q_j->infty` such that for every
  finite group `G`, `Lambda_{G,q_j}(beta_j)=Lambda_{G,q_j}(1)` eventually,
  but `rho_{X,q_j}(beta_j) != 1`.
- Give explicit moved tuples.
- Prove this defeats every finite rack via the sharp obstruction theorem.
- The obstruction sequence must be normalized-law based, not merely a
  growing finite search or timeout artifact.
- After proving that one explicit interval defeats every finite detector
  group, use `proofs/diagonal_normalized_obstruction.md` to obtain the
  normalized-law sequence.  Audit the product diagonalization and right-strand
  stabilization conventions with `diagonal_product_invisibility_audit(...)`
  and `right_stabilization_longitude_audit(...)`.

Before finalizing, explicitly answer this audit checklist:

1. Is any decisive step finite-search-only?
2. Is semisplit local-minimality fully handled?
3. Is the detector group/rack independent of `n`?
4. If returning B, does the obstruction defeat every finite group `G`, hence
   every finite rack through the sharp obstruction theorem?
5. Is the congruence-chain induction valid from local intervals to the final
   finite rack?

Return only a complete A proof or a complete B counterexample. If neither is
complete, state the precise missing lemma and the strongest partial progress,
but do not present it as a solution.
