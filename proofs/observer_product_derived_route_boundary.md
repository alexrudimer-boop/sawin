# Observer-Product Derived-Route Boundary

This generated audit records a concrete finite degenerate example
where the classical derived solution and quasi-rack derived route
do not apply, while rack domination is still immediate from an
active rack factor plus inert observer coordinates.

## Solution

`X={0,1} x S_3 with r((e,g),(f,h))=((e,ghg^{-1}),(f,g))`.

The `S_3` order used in the table is:

`['1', 't', 's', 'a', 'a^2', 'u']`.

The conjugation table is:

- `['1', 't', 's', 'a', 'a^2', 'u']`;
- `['1', 't', 'u', 'a^2', 'a', 's']`;
- `['1', 'u', 's', 'a^2', 'a', 't']`;
- `['1', 'u', 't', 'a', 'a^2', 's']`;
- `['1', 's', 'u', 'a', 'a^2', 't']`;
- `['1', 's', 't', 'a^2', 'a', 'u']`;

## Finite Checks

- YBE: `True`;
- involutive: `False`;
- lambda image sizes: `(6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6)`;
- rho image sizes: `(6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6)`;
- everywhere left singular: `True`;
- everywhere right singular: `True`;
- lambda fixed-point counts: `{'(0,1)': 6, '(0,t)': 2, '(0,s)': 2, '(0,a)': 3, '(0,a^2)': 3, '(0,u)': 2, '(1,1)': 6, '(1,t)': 2, '(1,s)': 2, '(1,a)': 3, '(1,a^2)': 3, '(1,u)': 2}`.

## Non-Affine Reason

For any affine model over an abelian group, every nonempty fixed set of lambda_x has cardinality |ker(1-B)|.  Here all lambda_x have fixed points, but the counts vary with S_3 centralizer sizes.

## Derived Route Failure

- classical derived status: `undefined: no lambda_x is surjective, so lambda_y^{-1}(x) is empty for half of the possible observer fibers`;
- quasi-left failure witness: `{'x': "(0, '1')", 'y': "(1, '1')", 'z': "(0, '1')", 'lambda_x0_lambda_y_z': "(0, '1')", 'lambda_y_lambda_x0_z': "(1, '1')", 'commutes': False}`.

## Rack Domination

- split equivariance check: `{'max_arity': 4, 'checked': True, 'first_failure': None}`;

Projection to S_3^n is the conjugation-rack action and projection to {0,1}^n is fixed pointwise.  Hence rho^X_n is rho^{S_3-conj}_n times a trivial observer factor, so the kernels are equal for all n.

## Conclusion

The example is finite, bijective, everywhere degenerate, non-involutive, and non-affine.  Classical and quasi-derived routes fail, but the solution is still rack-kernel equivalent to the S_3 conjugation rack via an inert observer product.

## Next Prompt

`prompts/gpt55_pro/2026-06-04-size5-6-everywhere-singular-core-search_ask_now.md`.
