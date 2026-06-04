# Derived Quasi-Rack Route Boundary

This generated note records the current state of the cover and
derived/quasi-rack routes.  The left-nondegenerate cover lemma is
sufficient, but the naive quasi-rack route does not automatically
cover every finite degenerate solution.

## Cover Lemma

If a finite YBE solution X is a homomorphic image of a finite left-nondegenerate solution Z, then X is dominated by a finite rack.

Proof sketch:

- A surjective solution morphism pi:Z->X makes pi^n:Z^n->X^n B_n-equivariant and surjective.;
- Therefore ker rho^Z_n <= ker rho^X_n for every n.;
- By the left-nondegenerate derived/guitar theorem, some finite rack Y has ker rho^Y_n <= ker rho^Z_n for every n.;
- Transitivity gives ker rho^Y_n <= ker rho^X_n for every n.;

Status: `sufficient but not known to be necessary`.

## Derived/Quasi-Rack Target

- kernel target: `construct a finite derived/quasi-rack object D(X) with ker rho^{D(X)}_n <= ker rho^X_n, or kernel equality after finite observer factors`;
- rack-domination target: `prove every finite D(X) is rack-dominated, for example by showing it is a Plonka sum, g-twist, or finite extension of actual racks with kernel-trivial fixed factors`;
- affine F_2^3 model: `the resolved affine F_2^3 candidate realizes this pattern: after a position-dependent twist, the moving factor is the tetrahedral rack and the remaining observer bits are fixed`.

## Quasi-Rack Gap Example

Name: `three_point_nonaffine_involutive_r1`.

Table rows:

- `['(0,0)', '(0,1)', '(2,0)']`;
- `['(1,0)', '(1,1)', '(2,1)']`;
- `['(0,2)', '(1,2)', '(2,2)']`;

- lambda rows: `{'lambda_0': (0, 0, 2), 'lambda_1': (1, 1, 2), 'lambda_2': (0, 1, 2)}`;
- quasi-left-nondegenerate failure: `lambda_0 lambda_1 = (0,0,2) but lambda_1 lambda_0 = (1,1,2), so the idempotent commutation condition fails`;
- domination status: `involutive, hence dominated by the two-point flip rack`;
- lesson: `quasi-rack literature covers an important degenerate subclass but does not automatically cover every finite bijective degenerate solution`.

## Non-Involutive Observer-Product Gap

Name: `observer_product_s3_conjugation`.

Formula: `X={0,1} x S_3, r((e,g),(f,h))=((e,ghg^{-1}),(f,g))`.

Properties:

- finite bijective YBE solution;
- everywhere left- and right-degenerate;
- non-involutive;
- non-affine over any abelian group by varying lambda fixed-point counts;
- classical derived solution undefined because no lambda_x is surjective;
- quasi-left-nondegenerate idempotent commutation fails;
- rack-kernel equivalent to the S_3 conjugation rack plus inert observer bits;

Proof artifact: `proofs/observer_product_derived_route_boundary.md`.

## Open Requirements

- define D(X) for genuinely degenerate finite bijective solutions without hidden nondegeneracy assumptions;
- prove or refute the all-arity kernel comparison between D(X) and X;
- prove or refute finite rack domination for the resulting quasi-rack class;
- test the construction on a genuinely degenerate non-affine finite table of size at least four that is non-involutive;
- replace the derived/quasi-rack route by an active rack factor plus invariant observer theorem, or find a rigid-core obstruction to such a theorem;

## Prompt

Next prompt: `prompts/gpt55_pro/2026-06-04-size5-6-everywhere-singular-core-search_ask_now.md`.

## Conclusion

The cover lemma gives a useful sufficient branch, but the naive derived quasi-rack route is not yet a theorem for all degenerate solutions.  The next decisive test is a size-four or larger degenerate non-involutive table outside the quasi-left-nondegenerate subclass.  The observer-product S_3 example shows that such tables can still be rack-dominated by an active rack factor plus inert observer channels.
