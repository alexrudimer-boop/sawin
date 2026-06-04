# Asymptotic Rigid-Core Endpoint Prompt

Status: ask_now / prepared for GPT-5.5 Pro on 2026-06-04.

Prompt:

```text
Please answer self-containedly. We are working on Sawin's MathOverflow problem:

Does every finite bijective set-theoretic Yang-Baxter solution X admit domination by a finite rack Y, meaning

    ker rho^Y_n <= ker rho^X_n

for every braid group B_n?

Known positive branches and local evidence:

1. Left- or right-nondegenerate finite solutions are dominated by the derived/guitar rack.

2. Finite involutive solutions are dominated by the two-point flip rack.

3. Flip-across/twisted unions of rack-dominated pieces are dominated by product racks.

4. Point-separating families of total YBE quotient factors glue safely: if the quotient maps are B_n-equivariant and jointly injective in every arity, the product of the quotient rack detectors dominates X.

5. Proper active-factor certificates also glue safely: if finitely many proper active factors into racks or smaller already dominated YBE solutions, with optional invariant observer channels, give a total left-to-right B_n-equivariant injective code X^n -> product factors in every arity, then X is rack-dominated.

6. Size <= 3 has no counterexample: degenerate non-affine size-3 examples are involutive, hence flip-rack dominated.

7. Size-4 degenerate non-involutive examples currently fall into closed model families:
   - Type A is affine over F_2^2 and has all-arity kernel equality with the two-element cyclic rack by a parity/fibre coordinate gauge.
   - Type B is genuinely non-affine over F_2^2 under every relabeling, but is a flip-across union of the two-point identity solution and the two-point toggle permutation solution, hence is product-rack dominated.

8. A strong affine F_2^3 pressure candidate is also positive. In shifted coordinates the correct local rule is

       (a,b,c),(A,B,C) ->
       ((b+A, a+A, C), (c+A+C, a+b+A+B, a+b+A+C)).

   The fifth coordinate is B'=a+b+A+B. With this correction, the all-n proof gives

       rho^X_n ~= rho^Y_n x id_{F_2^n}

   where Y is the four-element tetrahedral Alexander rack. Hence ker rho^X_n = ker rho^Y_n for all n.

9. The naive derived/quasi-rack route is incomplete as stated. A three-point degenerate non-affine involutive solution has lambda_0=(0,0,2), lambda_1=(1,1,2), lambda_2=(0,1,2), and fails the quasi-left-nondegenerate idempotent commutation condition because lambda_0 lambda_1=(0,0,2) but lambda_1 lambda_0=(1,1,2). It is nevertheless flip-rack dominated because it is involutive.

We now have a sharper endpoint based on fixed-arity rack cofinality.

Theorem 1 candidate: fixed-arity rack cofinality

Fix n >= 2. For every finite quotient representation theta:B_n -> H, there is a finite rack Y such that

    ker rho^Y_n <= ker theta.

In particular, for every finite bijective YBE solution X and every fixed n, there is a finite rack Y_n with

    ker rho^{Y_n}_n <= ker rho^X_n.

Proposed proof:

Use the Artin-form congruence subgroup property for braid groups: for the Artin embedding B_n -> Aut(F_n), every finite-index subgroup of B_n contains a principal congruence kernel

    ker(B_n -> Aut(F_n/K))

for some characteristic finite-index subgroup K <= F_n.

Given theta, set N=ker(theta). Choose K so that C_G=ker(B_n -> Aut(F_n/K)) <= N, and put G=F_n/K.

Let Y be the conjugation rack of G:

    a*b = a b a^{-1},
    r_Y(a,b)=(a b a^{-1}, a).

For the standard Artin action convention

    sigma_i:
    x_i     -> x_i x_{i+1} x_i^{-1},
    x_{i+1} -> x_i,
    x_j     -> x_j  for j not i,i+1,

the action on the tuple of quotient generators in G^n is exactly the conjugation rack crossing. Therefore, if beta is trivial on Y^n, it fixes every tuple in G^n, in particular the quotient generator tuple. Since those generators generate G, beta acts trivially on G, so beta in C_G <= N.

First task:

Audit this theorem carefully. Is the Artin-form congruence subgroup property being used correctly for full B_n, not just P_n or a mapping-class quotient? Are there small-n exceptions, center/inner-automorphism issues, or convention issues that weaken the conclusion? If the theorem is false as stated, identify the exact flaw and give a corrected statement.

If Theorem 1 is correct, it sharpens the negative condition.

Previously, a no-rack counterexample X had to satisfy:

    forall m exists n such that N_{m,n}(X) != 1,

where P_m is the product of the first m finite racks and

    N_{m,n}(X) = { g_X : (1,g_X) lies in the joint image of B_n on P_m^n x X^n }.

The sharpened condition is:

    forall m forall N exists n>N such that N_{m,n}(X) != 1.

Reason: if a fixed rack product P_m dominates X in all arities above N_0, fixed-arity cofinality supplies finite racks Q_n handling each 2 <= n <= N_0, and the finite product P_m x product Q_n dominates X in all arities.

So a genuine no-rack counterexample must be asymptotically rack-invisible: every finite rack prefix fails again at arbitrarily high arities.

Also add the following finite-table filter for any minimal counterexample. Write

    r(x,y)=(L_x(y), R_y(x)).

If X is outside the left/right-nondegenerate branches and has no proper crossing-closed subsolution, then every L_x and every R_x must be non-bijective.

Proof sketch: U_L={x: L_x bijective} is crossing-closed by the YBE identity

    L_{L_x(y)} L_{R_y(x)} = L_x L_y.

Thus U_L is empty, all of X, or a proper crossing-closed subsolution. The all-X case is left-nondegenerate; the proper case violates rigid-core assumptions. Similarly for U_R using

    R_z R_y = R_{R_z(y)} R_{L_y(z)}.

Second task:

Assuming Theorem 1 is correct, attack this sharpened endpoint:

    Asymptotic rigid-core exclusion theorem.
    There is no finite bijective YBE solution X that is both:
      (a) a rigid core, meaning it avoids all known positive decompositions/certificates above; and
      (b) asymptotically rack-invisible, meaning

          forall m forall N exists n>N with N_{m,n}(X) != 1.

Please do one of the following decisively:

A. Prove the asymptotic rigid-core exclusion theorem, or reduce it to one specific finite-table theorem strictly smaller than Sawin itself.

B. Give an explicit finite YBE table X satisfying the rigid-core filters, including the everywhere-singular coordinate filter, and explain why it is a serious candidate for asymptotic rack-invisibility.

C. Show that the fixed-arity cofinality theorem or the sharpened negative condition has a gap, and give the corrected endpoint.

D. Give a new structural positive branch forced by the everywhere-singular condition. For example, prove that a finite bijective YBE solution with every coordinate map singular must have a proper quotient, proper crossing-closed subsolution, invariant observer, flip-across decomposition, finite monodromy rackification, or proper active-factor certificate.

Avoid bounded-only evidence unless it comes with either a structural all-arity mechanism or an explicit next obstruction. If using external theorems, state the exact theorem and any small-n hypotheses.
```
