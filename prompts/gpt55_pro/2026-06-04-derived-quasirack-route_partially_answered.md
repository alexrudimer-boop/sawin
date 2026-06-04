# Derived Quasi-Rack Route Prompt

Status: partially_answered / Pro response incorporated on 2026-06-04.

Prompt:

```text
Please answer self-containedly. We are working on Sawin's MathOverflow problem:

Does every finite bijective set-theoretic Yang-Baxter solution X admit domination by a finite rack Y, meaning

    ker rho^Y_n <= ker rho^X_n

for every braid group B_n?

Known positive branches and guardrails:

1. Left- or right-nondegenerate finite solutions are dominated by the derived/guitar rack.

2. Finite involutive solutions are dominated by the two-point flip rack.

3. Flip-across/twisted unions of rack-dominated pieces are dominated by product racks.

4. Size-4 degenerate non-involutive examples found so far are braid-kernel equivalent to small racks.

5. A strong affine F_2^3 pressure candidate is also positive. In shifted coordinates it is conjugate in every arity to the four-element tetrahedral Alexander rack plus n fixed observer bits, so ker rho^X_n = ker rho^Y_n for all n.

6. One-dimensional affine-line families over fields are symbolically closed. For

       r(x,y)=(a x+b y+c, d x+e y+f),

   bidegeneracy means b=d=0 and bijectivity means ae != 0. The YBE equations force a=e=1 and c=f=0, so the only bidegenerate bijective affine-line YBE solution is the identity. Thus affine-line families cannot contain a bi-degenerate non-involutive rigid core.

7. Direct cover by a finite left-nondegenerate solution would be sufficient but not necessary. If X is a quotient of finite left-nondegenerate Z, then a rack dominates Z by the derived/guitar theorem and hence dominates X. But trivial/inert examples can be rack-dominated without any useful nondegenerate cover, so the cover route is not complete.

The latest suggested route is:

    For every finite X, its derived solution D(X) should satisfy

        ker rho^{D(X)}_n <= ker rho^X_n

    or even kernel equality up to fixed observer factors, and every finite derived/quasi-rack solution should be rack-dominated.

This would subsume the degenerate affine F_2^3 example: after a position-dependent g-twist, the derived/quasi-rack part splits as a tetrahedral rack plus trivial fixed coordinates.

Task:

Please decisively analyze the derived/quasi-rack route.

A. Give a precise definition of the derived solution D(X) for a finite bijective set-theoretic YBE solution X that may be degenerate. Do not assume left/right nondegeneracy. If the construction is multivalued, partial, quotient-valued, or requires choices, say so explicitly.

B. Prove or refute:

       ker rho^{D(X)}_n <= ker rho^X_n      for all n

   for all finite bijective X, in the appropriate precise sense. If equality only holds after adding finite invariant observer factors or a g-twist, formulate that exact theorem.

C. Prove or refute:

       every finite derived/quasi-rack solution is dominated by a finite rack.

   If the theorem is only true for quasi-racks that are Płonka sums of racks, g-twists of racks, or another subclass, state the exact hypothesis and show whether every D(X) lands in that subclass.

D. If the general theorem is false, give a concrete finite degenerate non-affine YBE table X where the derived/quasi-rack route fails, and explain whether X is still rack-dominated by another mechanism or is a genuine rigid-core candidate.

Please avoid a high-level literature survey unless it produces exact definitions and kernel-inclusion statements. The needed output is a proof, a counterexample table, or a sharply stated theorem whose verification would imply Sawin YES with the known branches.
```
