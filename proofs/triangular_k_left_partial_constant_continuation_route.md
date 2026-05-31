# Triangular K-left partial-constant continuation route

Date: 2026-05-31

This note follows
`proofs/triangular_k_left_partial_constant_closure.md`.

It does not prove `[Resolution: A]` or construct `[Resolution: B]`.  It routes
the universal seed edges from partial-constant missing triangular rows into
the already isolated continuation/descent channel.

## Executable object

The helper

```text
missing_triangular_partial_constant_continuation_route_audit(I)
```

starts with the rows from

```text
missing_triangular_partial_constant_closure_audit(I)
```

and records:

```text
side
left_color
right_color
fixed_input
domain_color
collapsed_inputs
companion_output_color
companion_outputs
continuation_seed_witnesses
continuation_seed_closure_kinds
partial_edge_contained_in_seed_closure
status
```

The route status is one of:

```text
routed_to_universal_continuation_seed
routed_to_continuation_seed_closure
companion_outputs_not_separated
no_continuation_seed_witness
continuation_seed_closure_missing_partial_edge
```

The post-linear finite-system wrapper reports the K-relevant part as:

```text
missing_triangular_partial_constant_continuation_routes
missing_triangular_partial_constant_unrouted_continuation_rows
```

## Lemma: partial-constant edges create continuation seeds

[Proved] In left rack-base convention, every partial-constant missing
triangular kernel edge has a nontrivial continuation seed in the same local
row.

Proof for the left-side case.  Let

```text
T_{a,b}(x,y) = (u,v)
```

with base row `R(a,b)=(a*b,a)`.  Suppose a left coordinate section is
constant on two distinct inputs:

```text
L_x(y0)=L_x(y1)=u,
y0 != y1.
```

Write

```text
T_{a,b}(x,y_i)=(u,v_i).
```

Since the full local row is bijective and `x` is fixed, the companion outputs
are distinct:

```text
v0 != v1.
```

The base is in left rack convention, so `v0,v1,x` all lie in the same fibre
`A_a`.  Because `v0 != v1`, at least one `v_i` differs from `x`.  For that
input, the row has a continuation seed

```text
x ~ v_i.
```

The right-side case is dual.  If a right coordinate section is constant on
distinct `x0,x1`, write

```text
T_{a,b}(x_i,y)=(u_i,v).
```

Then `u0 != u1` by bijectivity, and at least one of `x0,x1` differs from the
continuing output `v`; hence one continuation seed `x_i ~ v` appears.  QED.

## Lemma: universal continuation closure contains the partial edge

[Proved] If the continuation seed closure is universal, then it contains the
partial-constant collapsed input edge.

Proof.  Universal closure means every pair in every fibre is related in the
generated admissible family.  The partial-constant edge is one such fibre
pair.  QED.

The executable audit records the stronger finite check actually needed in
practice:

```text
partial_edge_contained_in_seed_closure
```

so the route can also be certified when a supplied continuation seed closure
is not labelled universal but still contains the partial edge.

## Consequence for System K

Partial-constant hidden missing triangular rows are now routed to the
continuation/descent repair channel:

```text
partial-constant kernel edge
  -> separated companion output
  -> nontrivial continuation seed
  -> continuation seed generated closure.
```

In a local-minimal remaining interval, any nontrivial continuation seed has
universal generated closure.  Therefore a partial-constant universal seed edge
is not an independent K-left endpoint and is not a closed K row.  The
post-linear wrapper records it in
`continuation_routed_k_missing_latin_row_defects` and moves the finite system
to `system_c_universal_continuation_endpoint`, the universal-continuation
endpoint layer already handled by the descent-endpoint repair contract
target.

## Remaining burden

[Open] This does not construct the missing fixed readout or endpoint
`V_beta` witnesses.  It proves only that the partial-constant K-left residue
feeds into the existing continuation/descent system.  The remaining A-route is
therefore to prove the uniform descent-endpoint theorem for those universal
continuation seed closures, or to upgrade a failure of that theorem to the
normalized-law B sequence required by the original problem.
