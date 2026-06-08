# Theoretical Review: Multi-Copy Augmented Rack Lift Reduction

Date: 2026-06-07.

## Verdict

This is theorem-level progress in the positive route, but it still does not
prove A.  It removes the finite algebraic totalization problem by allowing
multiple copies of each contextual class.  The remaining obstruction becomes a
coherent lift-separation problem.

## Universal Multi-Copy Rack

Let `P=P_X` be the finite contextual quotient of a finite bijective YBE
solution `X`.  Define

```text
Y = P x Sym(P)
```

with operation

```text
(p,g) * (q,h) = (g(q), g h g^{-1}).
```

This is a finite rack.  The left translation by `(p,g)` is the bijection

```text
(q,h) -> (g(q), g h g^{-1}).
```

The left translation of the product `(p,g)*(q,h)` is conjugation by
`g h g^{-1}`, hence

```text
L_{(p,g)*(q,h)} = L_{(p,g)} L_{(q,h)} L_{(p,g)}^{-1}.
```

So self-distributivity follows.

## Forced Crossings

For any forced compatible contextual product

```text
p*q = r
```

one can choose a permutation `g in Sym(P)` with `g(q)=r`.  More strongly, if a
forced partial translation

```text
lambda_p : D_p -> I_p
```

is injective, a total permutation `g` extending `lambda_p` exists because `P`
is finite and `|D_p|=|I_p|`.

Thus every forced contextual crossing can be represented locally in the finite
rack `P x Sym(P)`.  No one-copy assignment `p -> L_p` and no residual
finiteness theorem is required for algebraic rack totalization.

## Remaining Problem

Domination requires coherent global lifts, not merely local realizability.
One needs, for every arity `n`, a braid-equivariant relation

```text
Pi_n subseteq Y^n x X^n
```

such that:

```text
every x in X^n has at least one lift y in Y^n;
(y,x) in Pi_n => (rho^Y_n(beta)y, rho^X_n(beta)x) in Pi_n;
(y,x),(y,x') in Pi_n => x=x'.
```

If such `Pi_n` exists for all `n`, then

```text
ker rho^Y_n <= ker rho^X_n
```

for every `n`.

Indeed, if `beta` fixes `Y^n` and `(y,x) in Pi_n`, equivariance gives
`(y,rho^X_n(beta)x) in Pi_n`, and single-valuedness over `y` forces
`rho^X_n(beta)x=x`.

## Prompt Impact

The active positive target is no longer simply finite rack completion of the
contextual partial rack.  A canonical finite rack now exists:

```text
Y_X = P_X x Sym(P_X).
```

The remaining theorem is:

```text
For every finite bijective YBE solution X and every n, construct a
braid-equivariant, X-separating lift relation
Pi_n subseteq Y_X^n x X^n.
```

A negative route should now look for a fixed finite `X` where no such coherent
single-valued lift relation can exist, and then convert the resulting lift
collision into actual Brunnian detector-kernel braid witnesses.
