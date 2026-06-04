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
finds the first structurally rigid affine `F_2^3` survivors.  In this family,
`226241` affine YBE tables occur.  Among them, `3360` rows survive
bidegeneracy, noninvolutivity, observer-rigidity, subsolution-rigidity, and
pair-generated quotient-rigidity.  The first survivor has pressure against a
bounded ordered rack prefix of size `36`, but this was a cutoff artifact: the
prefix had not yet included the relevant three-element dihedral rack.  Exact
checks with that rack show matching braid image orders and no kernel
obstruction through arity `4`.  Thus the concrete all-`n` task is now to prove
or refute the dihedral-rack repair for this affine table.

The native-image audit
`proofs/affine_f2_q3_dihedral_native_image_audit.md` refutes that repair at
the next arity.  Working with the affine `F_2` action of `X` and the linear
`F_3` action of `D_3`, it computes

```text
n=5: |G_D3|=51840, |G_X|=77760.
```

It also gives a length-`25` positive braid word in the `D_3` kernel that
moves the zero tuple of `X^5`.  Thus the first structurally rigid affine
survivor is not dominated by `D_3`; the next target is a larger finite rack
detector or a cofinal rack-prefix obstruction.

The small-rack native detector audit
`proofs/affine_f2_q3_small_rack_native_detector_audit.md` tests the viable
individual rack representatives of size at most `4` at arity `5`.  All but
one viable rack either fail by a detector-kernel witness or truncate at the
state limit.  The survivor is rack representative `24`, a four-element rack
with operation table rows

```text
[0,2,3,1]
[3,1,0,2]
[1,3,2,0]
[2,0,1,3]
```

For this rack, the joint, detector, and `X` image orders agree through
arities `2,3,4,5` as `3,24,648,77760`, with no obstruction.  This is now the
main positive target for the affine survivor.

The companion native module audit
`proofs/affine_f2_q3_tetrahedral_module_audit.md` identifies this rack as the
Alexander rack on `F_2^2`

```text
a*b = T b + (I+T)a,        T rows = (2,3),
```

with braid crossing `(a,b) -> (a*b,a)`.  For the affine `F_2^3` survivor, the
affine offsets generate an explicit `2n-2` dimensional fibre module with basis
given by alternating prefix sums in the strand coordinates.  Through arity
`5`, the rack24 image, the full `X` image, the induced affine fibre image, and
all pairwise joint images have the same orders

```text
3, 24, 648, 77760.
```

Thus the current all-`n` positive target is sharper: prove that this
fibre-module identification with the tetrahedral Alexander rack persists
uniformly in `n`.  A direct arity-`6` tuple closure is not the right primitive
check; the expected image is already too large for naive enumeration.

The next Pro audit adds two refinements.  First, the affine `X` action is
globally linear after the one-based position shift

```text
x_i |-> x_i+(0,0,i mod 2).
```

Thus the arity-`6` test is a joint matrix-group computation in
`GL_12(2) x GL_18(2)`.  The focused audit
`proofs/affine_f2_q3_arity6_matrix_group_audit.md` runs this check using
matrix actions on the underlying vector spaces and SymPy Schreier-Sims.  It
finds

```text
|G_Y(6)| = |G_X(6)| = |G_{Y,X}(6)| = 39,813,120.
```

So the direct arity-`6` joint kernel `K_6` is trivial.  This also corrects the
provisional unitary-pattern guess `41,057,280`.

Second, the native module audit now checks a cheaper representation
certificate: the full tetrahedral Alexander representation over `F_4`
preserves

```text
L_n(z_1,...,z_n)=sum_i t^{i-1}z_i,
```

and the induced `X` fibre action is affine-conjugate to rack24 restricted to
an invariant slice `L_n=s` for every `2 <= n <= 10`.  This does not yet replace
the all-`n` proof, but it gives a concrete uniform theorem to try to prove:
existence of such a slice conjugacy for all `n`, plus faithfulness of the full
linearized `X` action to that fibre/slice action.

The follow-up coset audit
`proofs/affine_f2_q3_slice_coset_coverage_audit.md` strengthens the finite
evidence in exactly the faithfulness direction.  Since the shifted-linear `X`
action is identity on `V_n/W_n`, every quotient coset carries an affine action
on `W_n`.  Through arity `8`, every such coset action is affine-conjugate to
rack24 on at least one invariant slice `L_n=s`.  So the remaining positive
claim can be stated as an all-coset slice-coverage theorem, not merely a
single preferred fibre theorem.

The period-3 reduction audit
`proofs/affine_f2_q3_period3_reduction_audit.md` records the next sharpening.
It verifies the explicit edge-defect map

```text
p_i=a_i+b_i+a_{i+1},   q_i=c_i+c_{i+1},
D_n(x)_i=C_{n-i mod 3}(p_i,q_i)
```

through arity `18`, and checks that `D_n X_i = Ybar_i D_n`, where `Ybar_i`
is the reduced tetrahedral action on adjacent differences.  The kernel of
`D_n` is pointwise fixed by the shifted `X` generators, and `D_n` together
with all invariant linear observers has full rank exactly when `3` does not
divide `n`; when `n=3k` it misses two dimensions.  Thus rack24 domination is
now reduced to a period-3 shear problem, with the first unresolved arity
after the checked `n=3,6` cases being `n=9`.

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
