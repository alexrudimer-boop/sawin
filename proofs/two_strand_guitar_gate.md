# Two-strand guitar gate

Date: 2026-05-28

This note closes the remaining conservative `passes_unclassified` labels in
the exhaustive size-`3` two-strand symmetric-detector audit.  The closure is
symbolic for the nondegenerate branch; the finite audit is only a regression
check that the branch label is applied where expected.

## Derived rack operation

Write a left-nondegenerate solution as

```text
R(x,y) = (sigma_x(y), rho_y(x)).
```

For `a,b in X`, define the derived operation

```text
a op b = sigma_a(rho_{sigma_b^{-1}(a)}(b)).
```

The standard guitar-map theorem for left-nondegenerate set-theoretic YBE
solutions says that this operation is a rack operation, and the associated
rack action is braid-action conjugate to the original nondegenerate solution.
In particular, for all braid indices `n`, the derived rack has the same
kernel as the original solution after conjugating `X^n` by the guitar map.

This is one of the known nondegenerate/guitar branches in the main ledger.
It is not a finite-search claim.

## Two-strand identity

For the direct two-strand gate, only the `n=2` shadow is needed.  Define

```text
J_2(x,y) = (sigma_x(y), x).
```

Then `J_2` is a bijection because every `sigma_x` is a bijection.  If
`R(x,y)=(u,v)`, then

```text
J_2(R(x,y)) = (sigma_u(v), u).
```

On the other hand, the rack crossing for the derived operation sends

```text
(u,x) -> (u op x, u).
```

Since `u=sigma_x(y)`, the defining formula gives

```text
u op x
  = sigma_u(rho_{sigma_x^{-1}(u)}(x))
  = sigma_u(rho_y(x))
  = sigma_u(v).
```

Therefore

```text
J_2 R_X = R_D J_2,
```

where `D` is the derived rack.  Thus the two-strand crossing permutation of
`X` is conjugate to the two-strand rack crossing permutation of `D`.

## Consequence for the direct Sym gate

Rack actions are detected by their finite inner group.  Since the derived
rack is a rack on the same finite set `X`, its inner group embeds in
`Sym(X)`, so its exponent divides

```text
exp(Sym(X)) = lcm(1,...,|X|).
```

The exact finite-group longitude calculation from
`proofs/two_strand_symmetric_gate.md` says that the `B_2` kernel for
`G=Sym(X)` is `2 exp(Sym(X)) Z`.  The derived rack crossing is trivial on
that power, hence the conjugate original crossing is also trivial.  Therefore
every finite nondegenerate solution satisfies the exact direct-Sym
two-strand gate:

```text
ord(R_X:X^2->X^2) divides 2 lcm(1,...,|X|).
```

## Executable certificate

The helper

```text
derived_rack_operation_table(X)
```

implements the operation above.  The helper

```text
two_strand_guitar_conjugacy_holds(X)
```

checks the identity `J_2 R_X = R_D J_2` against the derived rack solution.

The summary helper

```text
two_strand_symmetric_gate_summary(X)
```

now reports `nondegenerate_derived_rack_branch` for nondegenerate rows that
pass through this derived-rack certificate.  Regenerated audits should
therefore show no `passes_unclassified` rows in the exhaustive size-`3`
two-strand corpus; any future `passes_unclassified` row must be outside the
currently closed rack, involutive, permutation, and nondegenerate/guitar
two-strand branches.

## Remaining limitation

This note closes the nondegenerate contribution to the two-strand direct-Sym
gate.  It does not prove the arbitrary finite bijective YBE theorem.  A full
solution still needs either the all-`n` master local-minimal residual theorem
for arbitrary finite fibres and quotient colours, or an explicit normalized
law obstruction sequence.
