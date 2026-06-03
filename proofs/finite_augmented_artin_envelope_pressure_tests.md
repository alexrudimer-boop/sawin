# Finite augmented Artin-envelope pressure tests

Date: 2026-06-03

This note is the next route-(1) pressure test after
`proofs/finite_augmented_artin_envelope_route.md`.  It does not prove the
finite augmented Artin-envelope lemma.  It records exactly what kind of
finite label object would prove it, and what kind of finite computation would
begin to refute it.

The wrong test remains:

```text
exp Q_X(n) grows without bound.
```

Finite racks already allow unbounded whole point-pushing image complexity in
their finite group-Hurwitz quotient.  A real obstruction must defeat every
fixed finite group-Hurwitz base plus bounded-exponent vertical kernel.

## Positive envelope obligations

The rack baseline is already understood.  For a finite rack `Y`,

```text
C={L_y:y in Y} subset H=Inn(Y)
```

is closed under conjugation because

```text
L_{y*z}=L_y L_z L_y^{-1}.
```

The pure Artin conjugacy formula then evaluates every coordinate inside the
fixed finite group `H` over each operator-label fibre.

For a general finite bijective set-theoretic YBE solution

```text
r(x,y)=(lambda_x(y), rho_y(x)),
```

there are two natural positive candidates.

First candidate:

```text
label(x)=(lambda_x,rho_x) in Sym(X) x Sym(X).
```

This can only work if the labels of both outputs,

```text
lambda_x(y),        rho_y(x),
```

are functions of the two incoming labels.  Then the braid action has a finite
label quotient.  The remaining obligation is to prove that, after a pure
braid fixes the label tuple, every coordinate action belongs to one fixed
finite group independent of `n`.

Second candidate:

```text
label(x) = image of x in a finite structure-group or derived-action quotient.
```

This can only work if Artin words

```text
x_j |-> u_j x_j u_j^{-1}
```

admit a finite evaluation rule in the quotient labels for arbitrary braid
words, not just for rack self-distributive actions.

## Failure mechanisms

The generated audit records four ways the augmented-envelope lemma can fail.

### Non-conjugation-stable label failure

Two pairs with the same candidate incoming labels produce different outgoing
labels after a single crossing.  Then there is no well-defined finite
operator-label quotient of the chosen kind.

Finite probe:

```text
find x,y,x',y' with equal candidate labels but unequal labels of
lambda_x(y) or rho_y(x).
```

### Ordered-neighbor memory failure

A point-pushing word acts trivially on candidate labels, but the coordinate
motion depends on the ordered history of crossings and cannot be represented
as coordinatewise action by one fixed finite group.

Finite probe:

```text
inside Q_X(3), search the kernel of the label action for equal label-fibre
states with different vertical maps.
```

### Point-forgetting incompatibility

Normal vertical subgroups may exist separately at each arity but fail to be
compatible under the Fadell-Neuwirth maps.

Finite probe:

```text
compare alpha_{i,5} under point-forgetting with the marked alpha_{i,4}
generators and the proposed vertical kernels.
```

### Unbounded vertical-kernel failure

Even after every fixed finite label quotient is allowed, the kernel over that
quotient contains all-`n` compatible elements whose orders or chief layers
escape every fixed exponent bound.

Finite probe:

```text
compute candidate vertical kernels in Q_X(3) and Q_X(4), then test whether
the apparent escape is vertical rather than only a large group-Hurwitz
quotient.
```

## Generated audit

The executable ledger is

```text
finite_augmented_artin_envelope_pressure_audit()
```

and the generated report is

```text
proofs/finite_augmented_artin_envelope_pressure_audit.md
```

It records:

```text
rack_operator_conjugation_baseline
translation_pair_label_candidate
finite_structure_action_candidate
nonconjugation_stable_label_failure
ordered_neighbor_memory_failure
point_forgetting_incompatibility
unbounded_vertical_kernel_failure
```

The next useful computation for a concrete degenerate candidate `X` is not a
whole-image exponent calculation.  It is a labelled comparison of the
standard point-pushing generators in `Q_X(3)` and `Q_X(4)` against one of the
candidate finite label objects above.
