# Universal symmetric detector audit

Date: 2026-05-28

This generated audit tests the candidate global detector

```text
G_X = Sym(X)
```

for whole finite YBE solutions over the one-point quotient.  If the
candidate theorem were true, the rack `A_{Sym(X)}` would dominate `X`
directly, bypassing the congruence-chain local theorem.  The audit is
not a proof: bounded scans are finite search, and exact scans are only
fixed braid-index finite-image closures.

## Exact fixed-index scans

- size `2`, n `2`: solutions `5`, proved `5`, trivial action `1`, truncated `0`, failures `0`, max visited states `4`.
- size `2`, n `3`: solutions `5`, proved `5`, trivial action `1`, truncated `0`, failures `0`, max visited states `48`.
- size `3`, n `2`: solutions `73`, proved `73`, trivial action `1`, truncated `0`, failures `0`, max visited states `12`.
- size `3`, n `3`: solutions `73`, proved `1`, trivial action `1`, truncated `72`, failures `0`, max visited states `1001`. First nonproof: detector states `1001`, residual states `6`, truncated `True`.

## Bounded kernel scans

- size `2`, n `3`, length <= `4`: words `161`, Sym-invisible words `5`, solutions `5`, failures `0`.
- size `3`, n `3`, length <= `4`: words `161`, Sym-invisible words `1`, solutions `73`, failures `0`.
- size `2`, n `4`, length <= `4`: words `937`, Sym-invisible words `15`, solutions `5`, failures `0`.
- size `3`, n `4`, length <= `4`: words `937`, Sym-invisible words `9`, solutions `73`, failures `0`.

## Symbolic known-branch filter

This filter is not a search proof.  It records rows where a separate
all-`n` branch argument already implies direct `Sym(X)` detection:
rack inner group, involutive Artin-permutation quotient,
permutation-form twist subgroup, or left-nondegenerate guitar-derived
rack.  Exact detector-state enumeration may still truncate on such
rows because it tracks many irrelevant longitude states.

- size `2`: solutions `5`, unknown rows `0`, reason counts `{'involutive_artin_permutation': 2, 'permutation_twist_subgroup': 1, 'rack_inner_group_subgroup': 2}`.
- size `3`: solutions `73`, unknown rows `0`, reason counts `{'involutive_artin_permutation': 18, 'left_nondegenerate_guitar_derived_rack': 35, 'permutation_twist_subgroup': 7, 'rack_inner_group_subgroup': 13}`.

## Exact two-strand crossing-order gate

`proofs/two_strand_symmetric_gate.md` proves that the `B_2`
longitude kernel for `Sym(X)` has exact period
`2*lcm(1,...,|X|)`.  Therefore the two-strand part of the
direct symmetric detector succeeds exactly when the crossing
permutation order divides that number.  The following tiny
exhaustive scans record this exact gate.

- size `2`: solutions `5`, period `4`, bad rows `0`, order histogram `{'1': 1, '2': 2, '4': 2}`.
  Explanation counts: `{'involutive_order_two': 2, 'permutation_form_twist_order_2': 1, 'rack_inner_group_branch': 1, 'trivial_crossing_action': 1}`.
- size `3`: solutions `73`, period `12`, bad rows `0`, order histogram `{'1': 1, '2': 18, '3': 12, '4': 36, '6': 6}`.
  Explanation counts: `{'involutive_order_two': 18, 'left_nondegenerate_derived_rack_branch': 35, 'permutation_form_twist_order_2': 3, 'permutation_form_twist_order_3': 4, 'rack_inner_group_branch': 12, 'trivial_crossing_action': 1}`.

## Affine cyclic two-strand stress test

For `n=2`, the exact positive period of the finite-G longitude
kernel is `2*exp(G)`.  For `G=Sym(X)` this is
`2*lcm(1,...,|X|)`.  Thus a two-strand failure of the symmetric
detector route would require the crossing
permutation `R` to have order not dividing that number.  The audit
checks affine cyclic solutions

```text
R(x,y)=(a*x+b*y+e, c*x+d*y+f) mod m
```

for small `m`.

- m `2`: YBE affine tables `5`, max crossing order `4`, invisible power `4`, bad rows `0`.
- m `3`: YBE affine tables `31`, max crossing order `6`, invisible power `12`, bad rows `0`.
- m `4`: YBE affine tables `113`, max crossing order `8`, invisible power `24`, bad rows `0`.
- m `5`: YBE affine tables `221`, max crossing order `10`, invisible power `120`, bad rows `0`.
- m `6`: YBE affine tables `155`, max crossing order `12`, invisible power `120`, bad rows `0`.
- m `7`: YBE affine tables `715`, max crossing order `14`, invisible power `840`, bad rows `0`.
- m `8`: YBE affine tables `1793`, max crossing order `16`, invisible power `1680`, bad rows `0`.

## Consequence

No failure appears in these small scans.  This suggests a new
positive route:

> Universal symmetric detector candidate.  For every finite
> bijective YBE solution `X`, every `n`, and every braid `beta`,
> `Lambda_{Sym(X),n}(beta)=Lambda_{Sym(X),n}(1)` should imply
> `rho_{X,n}(beta)=1`.

If this candidate is proved, Sawin finite-rack domination follows
with the explicit finite rack `A_{Sym(X)}`.  If it is false, the
first counterexample gives a very direct B-route target: a finite
solution `X` and a braid invisible to `Sym(X)`-longitudes but moving
`X^n`; the diagonal normalized-obstruction lemma would still be
needed to upgrade one failure into an all-finite-group obstruction.

The next symbolic task is therefore to prove the universal symmetric
detector candidate by a context/Green factorization argument, or to
find an explicit finite solution where it fails.
