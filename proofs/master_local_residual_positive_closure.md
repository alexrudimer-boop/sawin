# Master Local-Minimal Residual Theorem: positive closure assembly

Date: 2026-05-30

This note assembles the positive A-route after the kink-predecessor
cancellation theorem.  Its purpose is to connect the local branch reductions to
the sharp obstruction theorem and the congruence-chain induction.  It is the
proof-side closure of the Master Local-Minimal Residual Theorem, subject to the
individual branch notes cited below.

Update.  The proof-critic audit in `proofs/proof_critic_gap_audit.md` found
that this note is not yet a complete proof.  The failure is in the
bi-free universal-corridor closure: the cited endpoint factorization and
transport-rackification notes are conditional criteria, not proofs of the
missing endpoint expressions, faithful residual decomposition, or descent
separation.  This file should therefore be read as a candidate assembly
template whose missing input is the uniform descent-separation and
endpoint-longitudinalization theorem.

## Theorem

Let

```text
pi : X -> Z
```

be a finite local-minimal interval of finite bijective set-theoretic
Yang-Baxter solutions.  Assume `Z` is dominated by a finite rack `Q`.  For
each braid index `n`, let

```text
N_n = ker rho_{Q,n}.
```

For `z in Z^n`, write

```text
X_z = product_i pi^{-1}(z_i),
```

and let

```text
delta_{n,z}: N_n -> Sym(X_z)
```

be the residual fibre action.  Let

```text
Delta_n(beta) = (delta_{n,z}(beta))_z.
```

Then there is a finite group

```text
H(pi,Q)
```

depending only on the interval and quotient detector, not on `n`, such that
for every `n` and every `beta in N_n`,

```text
Lambda_{H(pi,Q),n}(beta)=Lambda_{H(pi,Q),n}(1)
    => Delta_n(beta)=1.                 (MLR)
```

Consequently the local interval is dominated by the finite rack

```text
Q x A_{H(pi,Q)}.
```

## Detector group

Define `H(pi,Q)` as the finite direct product of the interval-level factors
selected by the branch routing:

```text
H(pi,Q) =
H_Green x H_Sch x H_atom x H_known x H_endpoint x H_transport.
```

The factors are:

- two-sided Green kernel-block symmetric groups;
- two-sided Schutzenberger action groups;
- atom-quotient inner groups for every total descent-closed rack-like atom
  quotient;
- quotient and known-branch detector factors inherited from `Q` and the
  product/permutation, nondegenerate/guitar, involutive/permutation, affine,
  pairwise-linking, and coboundary branches;
- unit groups of finite endpoint/unit transition monoids that actually appear
  in residual permutation branches;
- inner groups of finite transport-state racks for strand-continuing lower
  gauge rows.

Every factor is constructed from finite interval data and the already fixed
quotient detector.  No factor has a braid-index parameter.

## Branch closure

A local-minimal interval is routed as follows.

1. Semisplit or non-local-minimal rows are not local intervals of the maximal
   congruence-chain induction.  The semisplit and single-pair closure audits
   verify this gate.
2. Product/permutation rows route to the product finite-G detector branches:
   coboundary telescope, one-colour pairwise cyclic detector, finite affine
   fibre-size-two detector, identity-base cyclic detector, or known total
   branch factors.
3. Equality coordinate-kernel rows are locally nondegenerate/guitar and are
   finite-G measurable by the known branch.
4. Known whole-solution rows, including involutive/permutation and rack-type
   rows, use their whole-solution finite-G detector factors.
5. The only remaining route is the
   `bi_free_universal_corridor_bottleneck`.

The rest of the proof handles item 5.

## Bi-free universal-corridor closure

In the bi-free universal-corridor branch, the residual readout decomposes into
Green, Schutzenberger, atom, endpoint/unit, and transport-state components.
The endpoint factorization criterion says that it is enough to prove every
component lies in the longitude-value subgroup of its fixed factor.

The following notes provide the required factorwise certificates.

1. Direct-product assembly:
   `proofs/bifree_corridor_endpoint_factorization.md` proves that factorwise
   endpoint-longitude expressions assemble into one fixed product detector.
   Normality and chart transport are handled by
   `proofs/chart_transport_collapse.md`.
2. Artin-recursive rows:
   `proofs/artin_detector_lift_criterion.md` proves that any finite observer
   row satisfying the active Artin detector update has terminal labels equal
   to evaluated recursive Artin longitudes.  Rack-like atom-inner rows satisfy
   this automatically by
   `proofs/atom_inner_detector_lift_rows.md`.
3. Green and Schutzenberger rows:
   `proofs/green_balanced_defect_gauge_decomposition.md` expresses each raw
   Green/Schutzenberger first-output defect as an Artin-visible commutator
   times a terminal second-output gauge.  The preceding Green defect notes
   handle quotient, potential, abelian, and homomorphic pushforward layers.
   Thus Green/Schutzenberger mismatch is not an independent endpoint
   obstruction.
4. Strand-continuing gauge:
   `proofs/transport_state_rackification_detector.md` proves that every
   strand-continuing finite gauge row rackifies on a finite transport state
   `A x E`; the inner group of that rack is a fixed detector factor.
5. Nonunit continuation:
   `proofs/unit_factorization_gate.md` and
   `proofs/unit_continuation_final_obstruction.md` show that nonunit/reset
   continuation maps cannot be final moving residual permutation branches.
   Any moving branch uses only finite unit factors.
6. Mixed-unit and triangular rows:
   `proofs/two_sided_unit_collapse.md`,
   `proofs/mixed_unit_companion_separation.md`, and
   `proofs/rank_profile_collapse_mixed_unit.md` reduce hidden mixed-unit
   context recovery to constant-section triangular rows.
   `proofs/constant_section_triangular_bundle_partition.md`,
   `proofs/triangular_bundle_recovery_inverse.md`, and
   `proofs/constant_column_collapse_triangular.md` reduce these rows to the
   Latin-unit triangular case.
   `proofs/latin_triangular_ybe_split.md` routes alpha transport to the closed
   product/permutation branch and isolates companion shear.
   `proofs/one_colour_latin_triangular_collapse.md` eliminates one-colour
   companion shear.
   Finally, `proofs/kink_predecessor_latin_triangular_cancellation.md` proves
   that over a rack base every Latin-unit triangular row has singleton fibres,
   so the rack-base companion-shear obstruction is trivial.

Therefore every residual component in the bi-free universal-corridor branch is
either killed by a fixed factor of `H(pi,Q)` or is impossible/nonmoving.

## Longitude implication

Let `beta in N_n` and assume

```text
Lambda_{H(pi,Q),n}(beta)=Lambda_{H(pi,Q),n}(1).
```

Project this equality to every direct-product factor of `H(pi,Q)`.

- Rack-like atom and transport-state rack factors are killed by the
  detector-lift theorem.
- Product/permutation and known-branch factors are killed by their closed
  finite-G detector proofs.
- Green and Schutzenberger factors are killed after splitting off
  Artin-visible commutators and routing terminal gauge.
- Unit endpoint factors are killed by the unit endpoint criteria; nonunit
  maps cannot occur in a moving residual permutation branch.
- Triangular Latin-unit shear contributes no nontrivial factor by the
  kink-predecessor cancellation theorem.

The endpoint factorization criterion is faithful: if all these components are
identity, each residual output coordinate equals its input coordinate.  Hence

```text
delta_{n,z}(beta)=1
```

for every `z in Z^n`.  Thus

```text
Delta_n(beta)=1.
```

This proves `(MLR)`.

## Sharp obstruction step

For a finite group `H`, the sharp detector rack is

```text
A_H = T_2 x (H x H),
```

with rack operation

```text
(a,u) ▷ (b,v) = (aba^{-1}, av).
```

The sharp obstruction theorem states that `(MLR)` is exactly the kernel form
needed to dominate the local interval.  Therefore

```text
Q' = Q x A_{H(pi,Q)}
```

is a finite rack satisfying, for every `n`,

```text
ker rho_{Q',n} subset ker rho_{X,n}
```

over this interval.

## Congruence-chain induction

Let

```text
Delta_X = kappa_0 < kappa_1 < ... < kappa_m = Nabla_X
```

be a maximal congruence chain.  The terminal quotient `X/kappa_m` is the
one-point rack, hence is dominated by the one-point rack `Q_m`.

Apply the local theorem downward.  For the interval

```text
X/kappa_i -> X/kappa_{i+1},
```

let the finite detector group be `H_i`.  Define

```text
Q_i = Q_{i+1} x A_{H_i}.
```

The sharp obstruction step gives

```text
ker rho_{Q_i,n} subset ker rho_{X/kappa_i,n}
```

whenever `Q_{i+1}` dominates `X/kappa_{i+1}`.  Induction gives a finite rack

```text
Y = Q_0
```

such that, for all braid indices `n`,

```text
ker rho_{Y,n} subset ker rho_{X,n}.
```

The construction uses only finitely many finite interval-level detector
groups; it is independent of `n`.

## Conclusion

Every finite bijective set-theoretic Yang-Baxter solution is finitely
rack-dominated.

The proof is not a finite search or timeout argument.  The executable audits
serve only to check finite local certificates, detector bookkeeping, OOXML
artifacts, and branch guardrails.  The all-`n` input is the symbolic
factorwise longitude proof assembled above.
