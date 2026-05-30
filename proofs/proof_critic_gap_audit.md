# Proof critic gap audit

Date: 2026-05-30

This note records the external proof-critic response to the candidate positive
assembly in `proofs/master_local_residual_positive_closure.md`.  It supersedes
the optimistic conclusion of `proofs/final_completion_audit.md`.

## Verdict

The current branch does not yet contain a complete proof of Sawin finite-rack
domination and does not contain outcome B.  The sharp obstruction theorem and
the congruence-chain kernel direction are not the issue.  The gap is in the
claimed closure of the `bi_free_universal_corridor_bottleneck`.

## Fatal gap 1: conditional endpoint factorization was used as an unconditional theorem

Location:

```text
proofs/master_local_residual_positive_closure.md
sections: Bi-free universal-corridor closure; Longitude implication
```

The positive closure note asserts that every residual component in the
bi-free universal-corridor branch is either killed by a fixed factor of
`H(pi,Q)` or is impossible/nonmoving, and then concludes that

```text
Lambda_{H(pi,Q),n}(beta)=Lambda_{H(pi,Q),n}(1)
    => Delta_n(beta)=1.
```

The cited dependency

```text
proofs/bifree_corridor_endpoint_factorization.md
```

does not prove this.  It proves a conditional assembly proposition:

- if each endpoint component already has a recursive Artin-longitude
  expression in a fixed factor;
- and if the residual readout is faithful;
- then the product detector kills the residual action.

The missing theorem is precisely the uniform endpoint-longitudinalization
statement that supplies those expressions for every residual Green,
Schutzenberger, atom, and lower endpoint component.  The master closure note
therefore converts a conditional criterion into an unconditional theorem.

## Fatal gap 2: descent separation remains unproved

Location:

```text
proofs/descent_separation_transport_rack_closure.md
sections: Final theorem target; Why this is still open
```

The proof needs a theorem saying that every residual endpoint motion separates
into:

- Green/Schutzenberger motion;
- rack-like atom motion;
- strand-continuing finite transport-rack gauge motion.

The descent-separation note states this as the needed theorem rather than
proving it.  The transport-state rackification theorem closes only the
strand-continuing subcase after such a separation has already been established.
It does not prove that all lower endpoint/unit holonomy is strand-continuing
or otherwise visible in fixed Green/Schutzenberger/atom readouts.

## Conditional atom descent

The atom-inner detector-lift rows are valid only after atom descent and
totality have been established.  The files

```text
proofs/atom_inner_detector_lift_rows.md
proofs/green_atom_descent_closure.md
```

still leave a theorem burden: prove descent/totality, or prove that all lost
lower information routes to endpoint/unit holonomy with fixed-factor
longitude witnesses.  Thus the atom factor is not yet a complete detector for
arbitrary local-minimal corridor intervals.

## Green/Schutzenberger status

The balanced Green decomposition proves an algebraic split:

```text
first-output defect = Artin-visible commutator * terminal gauge boundary.
```

This reduces the Green/Schutzenberger problem, but it does not eliminate the
terminal gauge boundary.  That gauge endpoint still requires fixed-factor
longitude visibility or a faithful descent-separation theorem.

## Kink-predecessor cancellation status

The critic did not find the fatal gap in

```text
proofs/kink_predecessor_latin_triangular_cancellation.md
```

under its stated hypotheses.  The rack-kink algebra, alpha cancellation, and
Latin-unit singleton-fibre conclusion appear sound.  The limitation is scope:
the theorem closes only the final rack-base Latin-unit triangular case.  It
does not prove that all mixed-unit universal-continuation corridors reduce to
that case, nor does it prove endpoint longitudinalization or descent
separation.

## Current missing theorem package

To complete outcome A, the branch still needs a uniform
descent-separation and endpoint-longitudinalization theorem:

For every local-minimal `bi_free_universal_corridor_bottleneck` interval, every
residual Green/Schutzenberger/atom/lower endpoint component must admit a
faithful finite readout through fixed interval-level factors, and every
resulting group-like endpoint must lie in the appropriate `V_beta` subgroup of
those fixed factors, uniformly for all braid indices `n`, all
`beta in ker rho_{Q,n}`, all base tuples, and all fibre tuples.

Equivalently, the proof must construct the missing endpoint expressions and
faithful residual decomposition.  Product calculus alone is insufficient.

## Audited answers

- Finite search is not the fatal issue; finite audits are mostly labelled as
  guardrails.  The issue is an unproved symbolic theorem.
- Semisplit local-minimality is conceptually gated before the master theorem.
- The proposed factors of `H(pi,Q)` are finite and have no explicit
  braid-index parameter, but completeness of the factor list is unproved.
- Endpoint factorization implies `Delta_n(beta)=1` only under the explicit
  faithful-readout and endpoint-expression hypotheses.
- Atom descent and non-total/non-rack cases are not fully routed.
- Green/Schutzenberger defects reduce to terminal gauge, which remains a
  problem.
- Transport-state rackification covers only strand-continuing rows.
- The triangular chain narrows the final obstruction but does not prove every
  mixed-unit universal-continuation corridor reaches the rack-base Latin-unit
  hypotheses.
- The kink-predecessor cancellation lemma appears sound under its hypotheses.
- The sharp obstruction theorem and congruence-chain induction direction
  appear sound.

## Current outcome

Neither final outcome is proved in the current branch:

```text
A. Complete finite-rack domination proof: not yet proved.
B. Explicit normalized-law counterexample: not constructed.
```

The next real target is the uniform descent-separation and
endpoint-longitudinalization theorem above, or a counterexample extracting a
normalized-law sequence from its failure.
