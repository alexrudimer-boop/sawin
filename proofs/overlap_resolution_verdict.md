# Overlap resolution verdict

Date: 2026-05-31

This note is the requested six-part verdict for the overlap obstruction prompt.
It relies on the symbolic finite-linear proof in
`proofs/finite_linear_overlap_resolution.md`.

## 1. Semisimple overlap resolution

[Proved] No semisimple finite-order, two-sided-degenerate, irreducible
finite-linear overlap gate with `S != 0` exists.

In fact the proof does not use semisimplicity.  For every block solution

```text
R = [ A  B ]
    [ C  D ]
```

of the seven linear Yang-Baxter block equations, the middle defect

```text
S = CB + (DA - A + I)(D - I)
```

satisfies

```text
AS = SA = DS = SD = 0,
BS = SB,
CS = SC.
```

Therefore `im S` is a common invariant subspace for `A,B,C,D`.  If `S != 0`
and `V` is irreducible, then `im S=V`, so `S` is onto.  The identities
`AS=DS=0` force `A=D=0`.  Then

```text
R(x,y) = (By,Cx)
```

is invertible only if both `B` and `C` are invertible, contradicting the
required singularity of `B,C`.

Thus the semisimple finite-linear algebraic system has no solutions.

## 2. Higher-nilpotent overlap resolution

[Proved] No higher-nilpotent finite-linear primitive overlap gate with
`S != 0`, singular `B,C`, and irreducible `V` exists.

The same identities for `S` are purely formal consequences of the block YBE
equations.  They do not use finite order, diagonalizability, or nilpotence.
So the higher-nilpotent filtered linear branch is killed before passing to
associated graded layers: a nonzero defect image is already an invariant
subspace, and irreducibility again contradicts the singularity of `B,C`.

## 3. Finite-extension control

[Proved] The finite-linear overlap branch is A-controlled vacuously.

There is no primitive finite-linear overlap datum satisfying the obstruction
hypotheses, hence no finite-linear braid-survival condition remains to be
controlled by a finite extension group.  Equivalently, every linear primitive
candidate either has `S=0` and lies in the already known
operator-Alexander/non-overlap route, or fails the obstruction hypotheses.

This statement is deliberately limited to the finite-linear branch.  It does
not claim that every nonlinear endpoint/unit gauge cocycle has a fixed
finite-extension witness.

## 4. Nonlinear overlap resolution

[Open] The nonlinear primitive overlap branch is not closed by the
finite-linear argument alone.

The obstruction that remains is not a finite-linear block system.  A genuine
nonlinear counterexample would have to survive all of the following reductions
already recorded in the proof ledger:

```text
local-minimality,
semisplit refinement,
known rack/involutive/permutation/nondegenerate branches,
product and coboundary finite-G routes,
Green/Schutzenberger first-output defect decomposition,
terminal gauge telescoping,
transport-state rackification of strand-continuing rows.
```

After these reductions, the exact remaining nonlinear target is the failure
of the uniform descent-endpoint theorem from
`proofs/descent_endpoint_repair_contract.md`:

```text
construct a quotient-minimal bi-free universal-corridor interval for which no
fixed descent-separating readout, fixed endpoint groups, faithful
reconstruction rule, and all-n V_beta endpoint witnesses exist; then upgrade
that finite failure to a normalized-law braid sequence invisible to every
finite group while moving an explicit residual tuple.
```

No such nonlinear primitive cocycle or normalized-law sequence is constructed
in the current worktree.

The reduction note
`proofs/nonlinear_overlap_reduction_after_linear_closure.md` records this in
the prompt's language: after finite-linear closure, any nonlinear survivor is
an elementary universal-continuation seed in a local-minimal
`bi_free_universal_corridor_bottleneck` interval, together with terminal
endpoint/gauge motion not killed by any fixed finite detector.

## 5. Global closure

[Conditional] If the nonlinear descent-endpoint theorem holds for every
local-minimal bi-free universal-corridor interval, then the existing sharp
obstruction theorem and congruence-chain induction give the positive
finite-rack domination theorem.

[False] A B-side conclusion follows from the finite-linear branch.  The
finite-linear branch has no primitive overlap candidates, so it cannot supply
a counterexample.

[Open] Global outcome A or B is not proved by this note, because the
nonlinear descent-endpoint theorem remains unproved and no nonlinear
counterexample has been supplied.

## 6. Final verdict

[Proved] The finite-linear overlap obstruction cannot exist.

[Proved] The semisimple and higher-nilpotent finite-linear systems in the
prompt are solved on the A side.

[Open] The exact remaining obstruction is nonlinear:

```text
a quotient-minimal finite residual fibre cocycle with a nonzero middle-carrier
overlap defect, not reducible to the killed finite-linear block system, whose
terminal endpoint/gauge readout escapes every fixed finite V_beta witness and
produces a normalized-law sequence in Br_n cap C^lambda_M(n) with nontrivial
residual action for every M.
```

Thus this work supplies a valid resolution of the finite-linear obstruction,
but it does not mark `[Resolution: A]` or `[Resolution: B]` for the full
finite-rack domination problem.
