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

The generated audit `proofs/sequential_primitivity_frontier_audit.md` adds the
current finite frontier.  Exhaustively, the size-three corpus has `73` YBE
tables and no sequential-primitivity candidate: all route to involutive,
permutation, rack-inner, or left-nondegenerate/guitar terminal branches.  The
same audit records that the named pressure representatives currently in the
repo are closed by explicit certificates:

- size-four affine Type A by a cyclic rack gauge plus parity observer;
- size-four Type B by two proper active quotient factors;
- the affine `F_2^3` hidden cyclic pressure row by a two-state cyclic rack
  gauge plus inert observer.

Thus the next falsifiable search frontier is not size three and not these
named pressure rows; it starts at larger nonterminal tables, such as size five
or structured affine-linear families beyond the hidden cyclic gauge.

The subsequent Pro refinement makes the negative-search target more concrete.
Sequential primitivity is still too weak: it defeats one induction method but
does not exhibit rack-prefix pressure.  The next table to search for is a
rigid pressure core, meaning a finite table that survives all terminal
filters, has no proper quotient, no crossing-closed subsolution, no
one-state invariant observer, no transport-isomorphic fibre splitting, and
then has actual small-rack-prefix pressure

```text
N_{m,n}(X) != 1
```

for a prefix containing the racks of size at most `3`.  The generated audit
`proofs/rigid_pressure_core_audit.md` makes these finite filters executable:
the exhaustive size-three corpus has no terminal survivor, and the current
size-four/affine pressure representatives all fail one of the rigidity
filters before rack-prefix pressure is even tested.

The affine-linear subsearch is now separated out in
`proofs/affine_rigid_pressure_core_audit.md`.  Exhaustively over affine maps
on `F_2^2`, there are `481` bijective YBE tables.  Of these, `24` survive the
terminal filters, but all `24` fail quotient-rigidity.  Thus the first
structured affine size-four frontier is also exhausted before the pressure
test.  The same audit exhausts affine-line maps over `F_5`: there are `221`
bijective affine YBE tables and no terminal survivor, so the first affine
size-five line frontier is also closed.

The next affine audit, `proofs/affine_f2_q3_rigid_pressure_core_audit.md`,
finds the first serious finite-prefix pressure candidates.  In the affine
`F_2^3` family, `226241` affine YBE tables occur.  Among them, `3360` rows
survive bidegeneracy, noninvolutivity, observer-rigidity,
subsolution-rigidity, and pair-generated quotient-rigidity.  The first
survivor has actual pressure against the product prefix containing all rack
representatives of size at most `3`: the detector has size `36`, and
`sigma_1^4` is trivial on it but moves the candidate in arity `2`.  This is
not a Sawin counterexample; it is now the concrete table whose all-`n` fate
must be proved.

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

The first finite approximation of that last line is now the rigid pressure
core target: find a table with nontrivial `N_{m,n}(X)` for the first small
rack prefix after all currently understood proper-factor, observer, and
split mechanisms have been blocked.
