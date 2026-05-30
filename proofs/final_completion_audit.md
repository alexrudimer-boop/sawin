# Final completion audit

Date: 2026-05-30

This note records an internal completion audit after
`proofs/master_local_residual_positive_closure.md` and
`proofs/kink_predecessor_latin_triangular_cancellation.md`.  It is not a new
mathematical reduction.  Its purpose is to check the assembled positive
A-route against the obligations in the Sawin finite-rack domination problem.

Update.  The subsequent proof-critic response recorded in
`proofs/proof_critic_gap_audit.md` found a fatal gap in this optimistic
completion audit.  In particular, the candidate master-local closure used the
conditional endpoint-factorization and transport-rackification criteria as if
they supplied the missing endpoint expressions and descent separation.  They
do not.  This file is retained as a historical internal audit, not as the
current final status.

## Superseded candidate final outcome

The superseded internal audit claimed the proof-side outcome was positive:

```text
Every finite bijective set-theoretic Yang-Baxter solution is dominated by a
finite rack.
```

The local theorem used for the global proof is the Master Local-Minimal
Residual Theorem:

```text
Lambda_{H(pi,Q),n}(beta)=Lambda_{H(pi,Q),n}(1)
    => Delta_n(beta)=1
```

for a finite group `H(pi,Q)` depending only on the local interval `pi:X -> Z`
and the quotient rack detector `Q`, not on the braid index `n`.

## Required reductions

1. Quotient and residual setup.

   The residual action is taken on

   ```text
   N_n = ker rho_{Q,n},
   X_z = product_i pi^{-1}(z_i),
   delta_{n,z}:N_n -> Sym(X_z),
   Delta_n(beta)=(delta_{n,z}(beta))_z.
   ```

   This is the setup used in
   `proofs/master_local_residual_positive_closure.md`.

2. Sharp obstruction theorem.

   The detector rack is

   ```text
   A_H = T_2 x (H x H),
   (a,u) ▷ (b,v) = (aba^{-1}, av).
   ```

   The proof uses only the kernel form:

   ```text
   Lambda_{H,n}(beta)=Lambda_{H,n}(1) => Delta_n(beta)=1.
   ```

   The local rack is then `Q x A_H`.

3. Congruence-chain induction.

   For a maximal congruence chain

   ```text
   Delta_X=kappa_0<...<kappa_m=Nabla_X,
   ```

   the proof starts at the one-point quotient and defines

   ```text
   Q_i = Q_{i+1} x A_{H_i}.
   ```

   Each `H_i` is finite interval-level data, so the final rack

   ```text
   Y=Q_0
   ```

   is finite and independent of `n`.

4. Local residual table and semisplit local-minimality.

   The local table is routed only after coloured YBE and local-minimality
   checks.  Semisplit equality/universal families are treated as ordinary
   admissible congruence families and must be absent before the local theorem
   is invoked.  The proof does not use Bell-number enumeration as a theorem;
   the single-pair closure criterion is the symbolic local-minimality gate.

5. Known eliminated branches.

   Product/permutation, locally nondegenerate/guitar,
   involutive/permutation, affine, pairwise-linking, coboundary, and known
   whole-solution branches route to fixed finite detector factors before the
   bi-free universal-corridor branch is reached.

## Master local audit

The remaining `bi_free_universal_corridor_bottleneck` branch is closed by the
following symbolic chain.

- Endpoint factorization reduces the all-`n` implication to showing that each
  residual endpoint component lies in `V_beta(H_s)` for a fixed detector
  factor.
- Direct-product witness calculus assembles factorwise certificates into one
  fixed finite product `H(pi,Q)`.
- Chart transport is harmless because `V_beta(G)` is normal in every finite
  group `G`.
- Atom-inner rack layers satisfy the Artin detector-lift rows by rack
  self-distributivity.
- Green and Schutzenberger first-output defects split into Artin-visible
  commutators plus terminal gauge.
- Strand-continuing terminal gauge rackifies on a finite transport-state rack
  `A x E`.
- Nonunit continuation maps cannot be final moving residual permutation
  factors, by rank monotonicity in finite total transformation monoids.
- Mixed-unit hidden continuation reduces to constant-section triangular rows.
- Constant-column collapse routes non-Latin triangular rows to
  product/permutation holonomy.
- One-colour Latin triangular companion shear is impossible.
- Rack-base Latin triangular companion shear is impossible by
  kink-predecessor cancellation: all fibres in such a row are singleton.

Thus every residual endpoint component in the bottleneck branch is either
killed by a fixed finite detector factor or cannot contribute nontrivial
motion.

## Fixed-detector audit

The detector group used in the local proof is

```text
H(pi,Q)=
H_Green x H_Sch x H_atom x H_known x H_endpoint x H_transport.
```

Each factor is finite and interval-level:

- Green kernel-block symmetric groups;
- Schutzenberger action groups;
- atom quotient inner groups for total descent-closed rack-like quotients;
- quotient and known-branch factors inherited from `Q` and closed branches;
- unit groups of finite endpoint/unit transition monoids that appear in
  residual permutation branches;
- inner groups of finite transport-state racks.

Assignments into those groups may depend on `n`, `beta`, the base tuple, and
the fibre tuple.  The groups themselves do not depend on `n`.

## Finite-search audit

The proof does not use timeout evidence or finite search as the all-`n`
argument.  Executable tests and spreadsheets serve as guardrails for:

- coloured YBE arithmetic on examples;
- semisplit and local-minimality bookkeeping;
- finite detector bookkeeping;
- OOXML artifact integrity;
- regression tests for the local certificates.

They are not used to replace the symbolic endpoint-longitude proof.

## External proof-critic attempt

The requested GPT-5.5 Pro proof critic could not be reached in this local
session.  Both Chrome and in-app Browser control depend on the same browser
bridge.  The bridge failed before it could list tabs, with the diagnostic:

```text
windows sandbox failed: spawn setup refresh
```

This audit therefore does not count as an external GPT-5.5 Pro review.  The
candidate proof remains the repository's internal positive A-route assembly.

## Superseded completion checklist

- No finite-search-only step is used for the all-`n` theorem.
- Semisplit local-minimality is kept as a gate before local theorem use.
- The local detector group `H(pi,Q)` is finite and independent of `n`.
- Outcome B is not asserted; no normalized-law counterexample is constructed.
- The sharp obstruction theorem converts the local kernel implication to the
  rack factor `Q x A_H`.
- Congruence-chain induction assembles finitely many local rack factors into
  one global finite rack independent of `n`.

This conclusion is superseded by `proofs/proof_critic_gap_audit.md`; outcome A
is not currently proved.
