# Minimal Rigid-Core Exclusion Proof Prompt

Status: partially_answered / Pro response incorporated on 2026-06-04.

Prompt:

```text
Please answer self-containedly. The goal is to resolve Sawin's MathOverflow problem:

Does every finite bijective set-theoretic Yang-Baxter solution X admit domination by some finite rack Y, meaning

    ker(B_n acting on Y^n) <= ker(B_n acting on X^n)

for every braid arity n?

Current state and known positive branches:

1. Left- or right-nondegenerate finite solutions are dominated by the derived/guitar rack.

2. Finite involutive solutions are dominated by the two-point flip rack.

3. Flip-across/twisted unions of rack-dominated pieces are dominated by the product rack. The proof is by colour-pattern decomposition: pure braids restrict to the same-colour substrand braid actions.

4. Size-4 degenerate non-involutive examples found so far are not counterexamples. They split into two types:
   - Type A is braid-kernel equivalent to the size-2 cyclic rack.
   - Type B is braid-kernel equivalent to a size-3 rack with L_0=L_1=id, L_2=(01).

5. A strong affine F_2^3 pressure candidate was also resolved positively. In shifted coordinates x_i -> x_i+(0,0,i mod 2), define X-coordinate i as (a_i,b_i,c_i) and

       C_0=[[1,0],[1,1]], C_1=[[1,1],[0,1]], C_2=[[0,1],[1,0]].

   Define

       z_1 = C_n(a_1,c_1),
       z_{i+1}=z_i+C_{n-i}(a_i+b_i+a_{i+1}, c_i+c_{i+1}),
       r_i=sum_{j<i}(a_j+c_j)+a_i+b_i.

   Then Phi_n=(z_1,...,z_n,r_1,...,r_n) is a bijection

       X^n -> Y^n x F_2^n

   where Y is the four-element tetrahedral Alexander rack, and Phi_n conjugates rho^X_n to rho^Y_n x id. Hence ker rho^X_n = ker rho^Y_n for every n.

6. Structured affine searches have not found a rigid counterexample:
   - Exact affine-linear search on F_2^2: 481 YBE tables, 24 terminal survivors, all 24 fail quotient-rigidity.
   - Exact affine-line search on F_3: 31 YBE tables, 0 terminal survivors.
   - Exact affine-line search on F_5: 221 YBE tables, 0 terminal survivors.
   - Exact affine-line search on F_7: 715 YBE tables, 0 terminal survivors.

   In fact the one-dimensional affine-line case is now symbolically closed over any field. For

       r(x,y)=(a x+b y+c, d x+e y+f),

   bidegeneracy means b=d=0 and bijectivity then means ae != 0. The YBE equations include

       a(a+bd-1)=0,
       e(1-e-bd)=0,
       e(cd+f)=0,

   and the middle constant equation

       -ace+aef-af-bf+cd+ce-c+f=0.

   With b=d=0 and ae != 0 these force a=e=1, f=0, and then c=0. Thus the only bidegenerate bijective affine-line YBE map is the identity r(x,y)=(x,y), so affine-line families over fields cannot contain a bi-degenerate non-involutive rigid core.

Guardrails / failed broad methods:

1. Product-like mixed rows do not automatically prove transport-isomorphic gluing. Nontrivial transport loop monodromy and non-fixed quotient-colour routing are real gaps.

2. Point-pushing bounded exponent is not a valid rack invariant. The valid rack-only point-pushing structure is a finite operator-label Hurwitz quotient with a bounded-exponent vertical kernel.

3. Bounded pullback-coskeletality is not forced by finite YBE locality alone. A positive theorem would need bounded-width finite operator labels and vanishing high-arity Brunnian deletion cross-effects.

4. Proper active-factor observability is stronger than rack domination. A rack kernel inclusion does not automatically produce a coordinatewise finite sequential reconstruction code.

The current exact endpoint is the following.

Definition. A finite bijective YBE solution X is a rigid core if:

1. X is left- and right-degenerate.
2. X is non-involutive.
3. X is not a rack and is not braid-kernel equivalent to a finite rack through a finite total sequential gauge.
4. X has no nontrivial total YBE quotient congruence.
5. X has no nonempty proper crossing-closed subsolution S with r(S^2)=S^2.
6. X has no nonconstant one-state invariant observer nu:X->I satisfying
       (nu(x),nu(y))=(nu(u),nu(v))
   whenever r(x,y)=(u,v).
7. X is not a flip-across/twisted union of proper dominated pieces.
8. X has no proper active-factor certificate into finite racks or strictly smaller already dominated YBE solutions, even with optional invariant observer channels, whose combined left-to-right output is injective on X^n for every n.

Strict theorem that would prove Sawin YES:

    Minimal rigid-core exclusion theorem:
    No finite bijective set-theoretic YBE solution is a rigid core.

If this theorem is true, Sawin YES follows by minimal counterexample: a smallest non-dominated X cannot be in any terminal positive branch; any proper quotient, proper subsolution/active factor, observer certificate, flip-across decomposition, or sequential rack gauge would dominate X by minimality and the safe gluing/certificate theorems. Therefore a minimal counterexample would be a rigid core, contradicting the theorem.

Exact negative target:

Enumerate finite racks as Y_1,Y_2,... and set P_m=Y_1 x ... x Y_m. For fixed m,n define

    Gamma_{m,n}(X)
      =
    < (rho^{P_m}_n(sigma_i), rho^X_n(sigma_i)) : 1 <= i < n >

and

    N_{m,n}(X) = { g_X : (1,g_X) in Gamma_{m,n}(X) }.

A genuine finite no-rack counterexample must be a rigid core and satisfy

    for every m there exists n with N_{m,n}(X) != 1.

Task:

Please decisively do one of the following.

A. Prove the minimal rigid-core exclusion theorem. The proof must handle bi-degenerate non-involutive solutions and must not assume left/right nondegeneracy. It should construct at least one proper quotient, proper subsolution, invariant observer, flip-across decomposition, transport/monodromy rackification, or proper active-factor certificate from any finite table outside the known terminal branches.

B. Give an explicit finite bijective YBE table X that is a rigid core, and prove either:
   B1. cofinal rack-prefix nonseparation, i.e. for every m there exists n with N_{m,n}(X) != 1, which would refute Sawin; or
   B2. X is nevertheless dominated by a finite rack by a mechanism not covered by the current certificate classes, which would expose a missing positive branch.

C. If neither A nor B is currently possible, sharpen the rigid-core definition into a smaller exact theorem that still implies Sawin YES with the known branches, or identify a finite structural condition from the YBE table that every minimal counterexample must satisfy and that is not already listed above.

Please do not answer only with bounded evidence, and do not re-analyze the affine F_2^3 tetrahedral row as if it were still open. It is already resolved by all-arity kernel equality with the tetrahedral rack. The requested output should be a proof, a concrete table with cofinal obstruction, or a strictly sharper theorem than minimal rigid-core exclusion.
```
