# Nondegenerate Cover Obstruction

Date: 2026-05-28

This note rules out a tempting global shortcut: prove Sawin domination by
placing every finite bijective YBE solution under a finite nondegenerate
solution, then applying the known guitar/rack domination theorem upstairs.
That route cannot handle genuinely degenerate solutions.

## Lemma

Let

```text
p : Y -> X
```

be a surjective braided-set homomorphism of finite bijective YBE solutions.
If `Y` is left nondegenerate, then `X` is left nondegenerate.  If `Y` is right
nondegenerate, then `X` is right nondegenerate.  Hence every quotient of a
finite nondegenerate solution is nondegenerate.

## Proof

Write

```text
R_X(x,z) = (x.z, x*z)
```

for the quotient coordinate operations.  Fix `x in X` and choose a lift
`y in Y` with `p(y)=x`.  To prove left nondegeneracy of `X`, take any
`u in X` and choose a lift `v in Y` with `p(v)=u`.  Since `Y` is left
nondegenerate, the map

```text
t |-> pr_1 R_Y(y,t)
```

is a bijection of `Y`.  Therefore there is some `t in Y` such that

```text
pr_1 R_Y(y,t) = v.
```

Applying the homomorphism condition gives

```text
pr_1 R_X(p(y),p(t)) = p(v) = u.
```

Thus the left coordinate map `z |-> x.z` is surjective on the finite set `X`,
and therefore bijective.  Since `x` was arbitrary, `X` is left
nondegenerate.

The right-handed proof is identical: fix `z in X`, lift it to `t in Y`, and
use bijectivity of

```text
y |-> pr_2 R_Y(y,t)
```

to show that `x |-> x*z` is surjective on `X`.

## Consequence

If `X` is degenerate, then no finite nondegenerate YBE solution can map onto
`X` as a braided-set quotient.  The known nondegenerate/guitar theorem cannot
be used by passing to a finite nondegenerate cover of `X`.

This does not obstruct the actual domination theorem, because the dominating
rack in Sawin's problem is not required to map onto `X`.  The sharp
obstruction theorem uses an indirect rack `A_G` whose kernel is an Artin
longitude detector.  Therefore degenerate local-minimal intervals still have
to be handled by quotient/residual finite-G detection, product-label
factorization, Green/corridor factorization, or a normalized-law
counterexample.

## Relation To Heredity

`proofs/hereditary_domination_closure.md` says domination passes downward to
quotients.  The present lemma says nondegeneracy also passes downward to
quotients.  Together they justify two search conventions:

- a positive proof may use nondegenerate domination only after proving the
  interval or total solution is actually nondegenerate;
- a negative search cannot manufacture a degenerate candidate as the quotient
  of a nondegenerate hidden cover.
