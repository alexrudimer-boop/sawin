# Size-4 Degenerate Non-Affine Derived Test Prompt

Status: ask_now / prepared for GPT-5.5 Pro on 2026-06-04.

Prompt:

```text
Please answer self-containedly. We are working on Sawin's MathOverflow problem:

Does every finite bijective set-theoretic Yang-Baxter solution X admit domination by a finite rack Y, meaning

    ker rho^Y_n <= ker rho^X_n

for every braid group B_n?

Current positive branches and evidence:

1. Left- or right-nondegenerate finite solutions are dominated by the derived/guitar rack.

2. Finite involutive solutions are dominated by the two-point flip rack.

3. Flip-across/twisted unions of rack-dominated pieces are dominated by product racks.

4. Size-4 degenerate non-involutive affine examples found so far are braid-kernel equivalent to small racks:
   - Type A: size-2 cyclic rack.
   - Type B: size-3 rack with L_0=L_1=id, L_2=(01).

5. A strong affine F_2^3 pressure candidate is also positive. In shifted coordinates the correct local rule is

       (a,b,c),(A,B,C) ->
       ((b+A, a+A, C), (c+A+C, a+b+A+B, a+b+A+C)).

   The fifth coordinate is B'=a+b+A+B. Omitting the A term breaks R_n-invariance and even the braid relation. With the corrected rule, exhaustive state checks through n=6 verify:

       P_n rho^X_n(sigma_i)=rho^Y_n(sigma_i) P_n,
       R_n rho^X_n(sigma_i)=R_n,
       Phi_n=(P_n,R_n):X^n -> Y^n x F_2^n is bijective,
       the X generators satisfy braid relations.

   The state counts checked were 8,64,512,4096,32768,262144 for n=1,...,6. The all-n proof gives

       rho^X_n ~= rho^Y_n x id_{F_2^n}

   where Y is the four-element tetrahedral Alexander rack, so ker rho^X_n = ker rho^Y_n for all n.

6. One-dimensional affine-line families over fields are symbolically closed. For

       r(x,y)=(a x+b y+c, d x+e y+f),

   bidegeneracy plus bijectivity forces b=d=0 and ae != 0. The YBE equations force a=e=1 and c=f=0. Thus the only bidegenerate bijective affine-line YBE map is the identity.

7. The left-nondegenerate cover route is sufficient but incomplete: if X is a quotient of a finite left-nondegenerate solution Z, then X is rack-dominated by transitivity through Z's derived/guitar rack. But some rack-dominated examples need not arise from such covers.

8. The naive derived/quasi-rack route is also incomplete as stated. The three-point degenerate non-affine involutive solution

       r_1 table:
       0,0 -> (0,0), 0,1 -> (0,1), 0,2 -> (2,0)
       1,0 -> (1,0), 1,1 -> (1,1), 1,2 -> (2,1)
       2,0 -> (0,2), 2,1 -> (1,2), 2,2 -> (2,2)

   has lambda_0=(0,0,2), lambda_1=(1,1,2), lambda_2=(0,1,2). It fails the quasi-left-nondegenerate idempotent commutation condition because lambda_0 lambda_1=(0,0,2) but lambda_1 lambda_0=(1,1,2). It is nevertheless dominated by the two-point flip rack because it is involutive.

So the next meaningful test is not size 3. It is size 4, genuinely degenerate, non-involutive, and preferably non-affine / outside the quasi-left-nondegenerate subclass.

Task:

Please do one of the following decisively.

A. Classify all size-4 bijective set-theoretic YBE solutions that are left- or right-degenerate and non-involutive up to relabelling. For each class, say whether it is:
   - affine or non-affine;
   - involutive or non-involutive;
   - quasi-left-nondegenerate in the quasi-rack sense;
   - rack-dominated, and by which finite rack or mechanism.

B. If full classification is too much, give one explicit size-4 degenerate non-involutive non-affine table X. Then compute enough structure to decide whether:
   - it is dominated by a finite rack, ideally with all-arity kernel equality;
   - it is explained by the derived/quasi-rack route;
   - or it is a genuine rigid-core candidate needing rack-prefix pressure tests.

C. If no non-affine size-4 degenerate non-involutive examples exist, prove that fact and explain why every size-4 degenerate non-involutive solution is affine/twisted-union/small-rack-equivalent.

Please provide explicit tables or explicit normal forms when possible. Bounded checks are useful only if accompanied by the structural mechanism likely to prove all-arity domination or by a precise next obstruction.
```
