# Rack-residual obstruction tower

This note records the exact finite-width obstruction tower obtained from the
latest Pro query.  It is sharper than failure of a chosen transducer class, but
it is still a criterion rather than a solved bounded-width theorem.

## Global tower

Enumerate finite racks up to isomorphism:

```text
R_1, R_2, R_3, ...
```

and let

```text
P_m = R_1 x ... x R_m.
```

For a finite bijective YBE solution `X` and arity `n`, define

```text
G_{m,n}(X)
  =
< (rho^X_n(sigma_i), rho^{P_m}_n(sigma_i)) : 1 <= i < n >
<= Sym(X^n) x Sym(P_m^n).
```

The fixed-width residual obstruction group is

```text
N_{m,n}(X)
  =
{ g_X in Sym(X^n) : (g_X,1) in G_{m,n}(X) }.
```

Equivalently, it is the projection to the `X` coordinate of the kernel of
`G_{m,n}(X) -> Sym(P_m^n)`.

For fixed `m,n`, this is a finite permutation-group computation.  The helper
`rack_residual_obstruction_audit(X,P_m,n)` implements the same check for any
supplied detector rack.

## Exact positive criterion

For fixed `m`,

```text
P_m dominates X
```

if and only if

```text
N_{m,n}(X)=1 for every n.
```

Therefore

```text
X is dominated by a finite rack
```

if and only if

```text
there exists m such that N_{m,n}(X)=1 for every n.
```

This is Sawin's positive answer in exact tower language.  It does not remove
the all-arity quantifier.

## Exact negative criterion

The negation is

```text
for every m there exists n with N_{m,n}(X) != 1.
```

Choosing a braid word witnessing each nontrivial `N_{m,n}(X)` gives

```text
beta_m in B_{n_m},
rho^{P_m}_{n_m}(beta_m)=1,
rho^X_{n_m}(beta_m) != 1.
```

After stabilizing by unused strands, one can force `n_m -> infinity`.  Since
every fixed finite rack occurs among the factors of some `P_m`, every fixed
finite rack is eventually blind to this sequence.  Thus the condition above
is exactly the normalized-law no-rack obstruction.

## Relative quotient version

If `pi:X->Z` is a quotient and `Z` is dominated by a rack `R_Z`, enumerate
finite hidden-fibre racks `S_1,S_2,...` and define

```text
P^Z_m = R_Z x S_1 x ... x S_m.
```

Then the same construction gives `N^Z_{m,n}(X)`.  Vanishing for some fixed
`m` and all `n` is exactly the existence of a finite relative rack detector
over `Z`; nonvanishing for every `m` in some arity is exactly the relative
hidden-fibre no-rack obstruction.

## Relation to transducer certificates

A finite Mealy/invariant transducer certificate over `pi:X->Z` proves that
`R_Z x S` dominates `X`.  Hence it implies vanishing of the relative
rack-residual tower for the corresponding finite detector.

The missing positive theorem is stronger than "find a good transducer":

```text
Transducer-completeness theorem.
If a finite relative rack detector over Z exists, then some finite
Mealy/invariant transducer certificate of the recorded form exists,
constructed from the quotient/fibre extension data.
```

Without this completeness theorem, failure of a transducer search is only a
gap.  Failure of every finite rack detector is the exact negative branch.

## Fixed-width executable audit

For a supplied detector rack `Y`, `rack_residual_obstruction_audit(X,Y,n)`
closes the finite subgroup

```text
< (rho^Y_n(sigma_i), rho^X_n(sigma_i)) >
<= Sym(Y^n) x Sym(X^n)
```

and checks whether the kernel over the `Y` coordinate has a nonidentity
projection to `Sym(X^n)`.  If it does, the audit returns a witness braid word
and a first moved `X^n` tuple.  This proves only fixed-width detector failure;
the Sawin problem is precisely the missing bounded-width/universal-detector
step.
