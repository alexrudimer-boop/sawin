# Coxeter Versus Full-Twist Guardrail

This note records a false-positive pattern for the central full-twist
obstruction.

Let

```text
delta_n = sigma_1 sigma_2 ... sigma_{n-1}.
```

Then the central full twist used in the rack obstruction is not `delta_n`,
but

```text
Delta_n^2 = delta_n^n.
```

The distinction matters even for small finite racks.  On the Alexander rack
over `F_3`

```text
x * y = -x + 2y,
r(x,y) = (x*y, x),
```

the positive Coxeter braid has growing checked orders

```text
ord rho(delta_n), n=2..7: 3, 6, 12, 10, 18, 14.
```

This growth is real, but it is not an obstruction to finite rack domination.
The central full twist on the same rack has checked orders

```text
ord rho(Delta_n^2), n=2..7: 3, 2, 3, 2, 3, 2,
```

and the rack theorem bounds every degree by `exp Inn(Y)=6`.

So a search routine or external computation that reports unbounded order for
`sigma_1 ... sigma_{n-1}` has not found the obstruction from
`proofs/rack_full_twist_order_bound.md`.  To defeat finite rack domination by
this route, the order growth must persist for the central element
`(sigma_1 ... sigma_{n-1})^n` itself.

The regression

```text
test_coxeter_braid_growth_is_not_full_twist_growth
```

locks this convention on the finite Alexander rack above.
