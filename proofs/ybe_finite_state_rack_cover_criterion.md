# YBE finite-state rack-cover criterion

Date: 2026-06-03

The direct rack-cover shortcut asks whether one can enlarge a finite
bijective YBE solution `X` by finitely many labels and make a rack whose braid
action projects to the YBE braid action.  The coordinatewise version is too
rigid.

Use the rack convention

```text
R_Y(a,b) = (a > b, a).
```

If a surjective coordinatewise map

```text
pi:Y -> X
```

intertwines the two-strand rack action with

```text
r(x,y) = (lambda_x(y), rho_y(x)),
```

then for all `a,b in Y`,

```text
(pi(a > b), pi(a)) =
(lambda_{pi(a)}(pi(b)), rho_{pi(b)}(pi(a))).
```

Therefore

```text
pi(a) = rho_{pi(b)}(pi(a)).
```

Since `pi` is surjective, this forces

```text
rho_y(x)=x
```

for all `x,y in X`.  With the opposite rack convention the same argument
forces the left action to be trivial.  Thus a general finite bijective YBE
solution cannot be dominated by a coordinatewise rack quotient.

## Fibre Labels

The same obstruction appears for a fibre product `Y=X x S` if the first
coordinate is required to project directly:

```text
(x,s) > (y,t) = (lambda_x(y), alpha_{x,y}(s,t)).
```

Rack bijectivity already requires each `lambda_x` to be bijective, so this
cannot cover genuinely left-degenerate solutions.  Even when the `lambda_x`
are bijective, rack self-distributivity gives the first-coordinate identity

```text
lambda_x lambda_y =
lambda_{lambda_x(y)} lambda_x.
```

The YBE relation gives instead

```text
lambda_x lambda_y =
lambda_{lambda_x(y)} lambda_{rho_y(x)}.
```

The rack identity would therefore require the future operator attached to the
copied strand `x` to be interchangeable with the future operator attached to
the updated strand `rho_y(x)`.  A coordinatewise label cannot repair this
first-coordinate equality.

Even in the special cases where that first-coordinate obstruction vanishes,
the labels must satisfy the nonabelian rack cocycle equation

```text
alpha_{x,lambda_y(z)}(s,alpha_{y,z}(t,u)) =
alpha_{lambda_x(y),lambda_x(z)}
  (alpha_{x,y}(s,t),alpha_{x,z}(s,u)).
```

The YBE identity alone does not provide such an `alpha`.

## Finite-State Decoder

The possible direct-cover formulation is therefore finite-state rather than
coordinatewise.  Let `Y` be a finite rack, let `Q` be a finite decoder state
set, and choose maps

```text
d: Q x Y -> X,
tau: Q x Y -> Q.
```

Starting from a fixed initial state `q0`, define a left-to-right decoder

```text
Phi_n(y_1,...,y_n) = (x_1,...,x_n),
x_i = d(q_{i-1},y_i),
q_i = tau(q_{i-1},y_i).
```

For the rack braid action to project to the YBE braid action, the following
local equations must hold for every `q in Q` and `a,b in Y`:

```text
d(q,a > b) =
lambda_{d(q,a)}(d(tau(q,a),b)),
```

```text
d(tau(q,a > b),a) =
rho_{d(tau(q,a),b)}(d(q,a)),
```

and

```text
tau(tau(q,a > b),a) =
tau(tau(q,a),b).
```

Together with the rack identity on `Y` and surjectivity of every `Phi_n`,
these equations are the finite-state marked rack-cover criterion.  The second
equation is the important escape hatch: although the rack physically copies
`a` into the second output, the decoder state after reading `a > b` may
reinterpret that copied symbol as the YBE value `rho_y(x)`.

## Structure-Group Warning

The same copied-strand obstruction occurs if one tries to use a finite group
quotient and its conjugation rack:

```text
(g,h) -> (g h g^-1, g).
```

The second output is still the old element `g`.  Without finite decoder
context, it cannot represent the updated YBE value `rho_y(x)` unless the
projection collapses those two states and loses the intended `X`-coordinate.

So the exact direct-cover pressure test is not "find a finite label set
attached to each element of `X`."  It is:

```text
find finite (Y,Q,d,tau) satisfying the displayed decoder equations
and making all Phi_n surjective.
```

The corresponding obstruction is the right-update defect

```text
Delta(x,y)=lambda_{rho_y(x)} lambda_x^-1
```

when the `lambda_x` are invertible, or the noninvertible form of the same
failure:

```text
lambda_{lambda_x(y)} lambda_{rho_y(x)}
!=
lambda_{lambda_x(y)} lambda_x.
```

Finite rack domination may still be true, but it cannot follow from the naive
coordinatewise rack-cover construction.  It requires finite context capable
of absorbing this right-update defect coherently for all future crossings.
