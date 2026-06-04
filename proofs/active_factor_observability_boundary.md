# Active-Factor Observability Boundary

Date: 2026-06-04

This note records the current boundary after the Pro response to the
active-factor observability prompt.  It is not a proof of Sawin's problem and
not a counterexample.

## Verdict

The candidate active-factor observability theorem is not currently proved.
No explicit finite YBE table with a cofinal rack-prefix obstruction is known
from the current data.

The safe implication remains:

```text
proper active-factor observability
  => finite rack domination.
```

The converse is not known.  Rack domination is a kernel-inclusion statement:

```text
ker rho^Y_n <= ker rho^X_n        for all n.
```

Active-factor observability asks for much more: a coordinatewise, left-to-right
finite symbolic reconstruction of every word in `X^n` through racks,
strictly smaller dominated YBE factors, quotient channels, and invariant
observer channels.  A quotient of finite braid representations does not
automatically arise from such a finite Mealy code.

Thus a failure of active-factor observability would refute the proposed
induction method, but would not automatically refute Sawin.

## Sequential Primitivity

For a finite solution `X`, call `X` sequentially primitive relative to a
chosen terminal class if every finite equivariant left-to-right code into:

- finite racks;
- strictly smaller already dominated YBE active factors;
- proper quotient factors;
- invariant observer alphabets;

has an all-length collision.  Equivalently, for every such candidate
certificate `C`, there exist `n` and distinct words

```text
x != y in X^n
```

with

```text
C_n(x)=C_n(y).
```

Sequential primitivity is the exact obstruction to the active-factor
observability theorem.  It is not the exact obstruction to finite rack
domination.

The generated audit `proofs/active_factor_observability_audit.md` shows that
the current transport-gluing proof-gap witnesses are not sequentially
primitive:

- the identity-base cyclic monodromy witness is closed by a three-state
  position gauge into the cyclic rack, plus colour observer;
- the flip-base cyclic monodromy witness is closed by a proper fibre active
  factor over the flip quotient;
- the dihedral quotient-colour routing witness is closed by the quotient rack
  plus inert-fibre observer.

These examples remain proof-mechanism guardrails rather than negative
evidence.

## Cofinal Rack-Prefix Obstruction

A genuine negative answer to Sawin needs more than sequential primitivity.
Enumerate finite racks as `Y_1,Y_2,...` and let

```text
P_m = Y_1 x ... x Y_m.
```

For a fixed finite solution `X`, define the finite joint braid image

```text
Gamma_{m,n}(X)
  =
< (rho^{P_m}_n(sigma_i), rho^X_n(sigma_i)) : 1 <= i < n >
<= Sym(P_m^n) x Sym(X^n)
```

and the detector-kernel image

```text
N_{m,n}(X) = { g_X : (1,g_X) in Gamma_{m,n}(X) }.
```

Then `X` is not dominated by any finite rack exactly when

```text
forall m exists n,        N_{m,n}(X) != 1.
```

Equivalently, there is a normalized-law no-rack sequence: for each rack prefix
`P_m`, a braid invisible to `P_m` in some arity still moves `X`.

## Exact Remaining Obstruction

The combined target is:

```text
proper sequential primitivity
  + cofinal rack-prefix nonseparation.
```

Condition one refutes the proper active-factor induction route.  Condition two
refutes Sawin.  Neither is currently supplied by the known examples.

A positive proof by this route must construct proper active factors or
observer channels for every non-terminal finite YBE table and prove
all-length injectivity by the pair-automaton criterion.  A negative proof must
exhibit a concrete finite table `X` and prove the cofinal nontriviality of
`N_{m,n}(X)`.

## Current State

The active-factor route remains the sharpest positive certificate language in
the repo, but it is still a certificate theorem.  The exact next search
target is a finite table that is:

- not left- or right-nondegenerate;
- not involutive;
- not flip-across decomposable;
- without point-separating proper quotient factors;
- without a finite proper active-factor/observer certificate;
- and with nontrivial `N_{m,n}(X)` for every rack prefix `P_m`.

No such table is currently known.
