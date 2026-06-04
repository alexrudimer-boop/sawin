# Minimal Rigid Core Resolution Prompt

Status: answered / Pro response incorporated on 2026-06-04.

Prompt:

```text
Please answer self-containedly. The goal is to resolve Sawin's MathOverflow problem:

Does every finite bijective set-theoretic Yang-Baxter solution X admit domination by some finite rack Y, meaning

    ker(B_n acting on Y^n) <= ker(B_n acting on X^n)

for every braid arity n?

Known positive branches and current evidence:

1. If X is left-nondegenerate or right-nondegenerate, the derived/guitar rack machinery gives finite rack domination.

2. If X is finite involutive, the 2-point flip rack dominates X.

3. If X is a flip-across/twisted union of rack-dominated pieces, then the product rack dominates X. The proof uses the color-pattern decomposition: pure braids restrict to substrand braid actions on each color, so domination is functorial under flip-across union.

4. Size-4 degenerate non-involutive examples have been found. They split into two types and are braid-kernel equivalent to small racks:
   - Type A: equivalent to the size-2 cyclic rack.
   - Type B: equivalent to the size-3 rack with L_0=L_1=id, L_2=(01).

5. A stronger affine pressure candidate X over F_2^3 was tested. It is left- and right-degenerate, non-involutive, not handled by D_3, and initially looked like a rigid pressure core. It is now also positive. In shifted coordinates x_i -> x_i+(0,0,i mod 2), it is conjugate in every arity to the tetrahedral rack Y over F_2^2 plus n fixed observer bits:

   Let X-coordinate i be (a_i,b_i,c_i), let

       C_0=[[1,0],[1,1]], C_1=[[1,1],[0,1]], C_2=[[0,1],[1,0]].

   Define

       z_1 = C_n(a_1,c_1),
       z_{i+1}=z_i+C_{n-i}(a_i+b_i+a_{i+1}, c_i+c_{i+1}),
       r_i=sum_{j<i}(a_j+c_j)+a_i+b_i.

   Then Phi_n=(z_1,...,z_n,r_1,...,r_n) is a bijection

       X^n -> Y^n x F_2^n

   and conjugates rho^X_n to rho^Y_n x id. Therefore

       ker rho^X_n = ker rho^Y_n

   for all n.

Failed proof methods / guardrails:

1. Product-like mixed rows do not automatically give transport-isomorphic gluing. Nontrivial transport loop monodromy and non-fixed quotient-colour routing are real gaps.

2. Point-pushing bounded exponent is the wrong invariant. Finite racks may have unbounded point-pushing image complexity; the valid rack-only structure is a finite operator-label Hurwitz quotient with bounded vertical kernel.

3. Bounded pullback-coskeletality is not forced by finite YBE locality alone. A positive theorem needs bounded-width operator labels and vanishing high-arity Brunnian deletion cross-effects.

4. Active-factor observability is stronger than Sawin-positive. A rack domination certificate need not automatically produce a finite sequential active-factor code.

Current exact fork:

A positive proof would follow from a theorem of the following form:

    Every finite bijective YBE solution X that is not already in a terminal positive branch has a proper total YBE quotient, proper subsolution, invariant observer, flip-across decomposition, transport/monodromy finite rackification, or finite sequential active-factor/rack gauge whose outputs jointly reconstruct X^n in every arity.

A negative proof needs an explicit finite table X and a normalized-law no-rack sequence:

    for every finite rack prefix P_m, there exist n and beta in B_n such that
        rho^{P_m}_n(beta)=1
    but
        rho^X_n(beta) != 1.

Equivalently, X must be a rigid pressure core with cofinal rack-prefix nonseparation.

Please now decisively resolve one side:

A. Prove the positive theorem. Use a minimal-counterexample argument if possible: assume X is a smallest finite bijective YBE solution not dominated by a finite rack, and prove it must admit one of the proper quotient/subsolution/observer/active-factor mechanisms above, contradicting minimality. The proof must handle bi-degenerate non-involutive solutions and must not assume left/right nondegeneracy.

B. Give a concrete finite counterexample table X, together with a proof of the cofinal rack-prefix obstruction. It is not enough to defeat one bounded certificate class or one small rack; the proof must show that every finite rack prefix is eventually blind to some braid that moves X.

C. If neither A nor B is possible, give a strictly smaller theorem that would still decide Sawin when combined with the existing positive branches. It must be a precise mathematical statement whose truth would imply finite rack domination for all finite bijective YBE solutions, not merely another bounded-evidence search.

Avoid re-answering with the known examples above. The affine F_2^3 pressure candidate is already resolved positively by explicit conjugacy to the tetrahedral rack plus fixed observers. The needed step is a general theorem or a genuine finite-table counterexample with cofinal rack-prefix nonseparation.
```
