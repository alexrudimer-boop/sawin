# Affine F2^3 Period-3 Shear / n=9 Target

Status: answered by GPT-5.5 Pro on 2026-06-04; promoted to
`proofs/affine_f2_q3_full_tetrahedral_conjugacy_audit.md`.

Prompt:

```text
Continue in the same chat. Please focus only on the period-3 shear obstruction for the exact affine F_2^3 table X and the tetrahedral rack Y below. Do not re-answer with the arity-6 computation.

Problem. Sawin asks whether every finite bijective set-theoretic YBE solution X is dominated by a finite rack Y:

    ker(B_n acting on Y^n) <= ker(B_n acting on X^n)

for every n.

Exact X. Let X=F_2^3. For x=(x1,x2,x3), y=(y1,y2,y3), define R_X(x,y)=(u,v):

    u1 = x2 + y1
    u2 = x1 + y1
    u3 = y3 + 1
    v1 = x3 + y1 + y3 + 1
    v2 = x1 + x2 + y2
    v3 = x1 + x2 + y1 + y3

The affine action is linearized by the one-based position shift

    x_i -> x_i + (0,0,i mod 2).

In shifted coordinates the local F_2 block is

    M_X =
    010100
    100100
    000001
    001101
    110110
    110101.

Exact rack Y. Let Y=F_2^2 with T row masks (2,3), so T^2+T+I=0, and

    a*b = T b + (I+T)a.

The braid crossing is (a,b)->(a*b,a), local F_2 block

    M_Y =
    1101
    1011
    1000
    0100.

Finite joint-kernel evidence:

    n=2: |G_Y|=|G_X|=|G_{Y,X}|=3
    n=3: |G_Y|=|G_X|=|G_{Y,X}|=24
    n=4: |G_Y|=|G_X|=|G_{Y,X}|=648
    n=5: |G_Y|=|G_X|=|G_{Y,X}|=77760
    n=6: |G_Y|=|G_X|=|G_{Y,X}|=39813120

Thus K_n={g_X:(1,g_X) in the joint image} is trivial through n=6.

Your previous response proposed the following reduction. I independently checked its linear algebra through arity 18.

Let shifted X coordinates at position i be (a_i,b_i,c_i). For 1<=i<n define

    p_i = a_i + b_i + a_{i+1},
    q_i = c_i + c_{i+1}.

Let

    C_0 = [[1,0],[1,1]],
    C_1 = [[1,1],[0,1]],
    C_2 = [[0,1],[1,0]].

Define

    D_n(x)_i = C_{n-i mod 3} (p_i,q_i).

Let Ybar be the tetrahedral rack representation reduced to adjacent differences eta_i=z_i+z_{i+1}. The repo verifies through n=18 that

    D_n X_i = Ybar_i D_n

for all braid generators. It also verifies:

    rank D_n = 2n-2,
    dim ker D_n = n+2,
    ker D_n is pointwise fixed by all shifted X generators,
    dim invariant linear observers = n+2,
    rank([D_n; Inv_n]) = 3n if 3 does not divide n,
    rank([D_n; Inv_n]) = 3n-2 if 3 divides n.

Therefore rack Y controls X for every arity n with 3 not dividing n. The only remaining possible mismatch is a two-dimensional period-3 shear when n=3k. Since n=3 and n=6 already pass, the first unresolved arity is n=9.

Please now resolve one of the following, decisively:

A. Prove the period-3 shear vanishing theorem:

    For every k>=1, if beta in ker rho^Y_{3k}, then rho^X_{3k}(beta)=1.

Equivalently, prove that the possible 2-dimensional shear cocycle on the missing quotient of [D_n; Inv_n] is zero on ker rho^Y_{3k} for all k.

B. Refute domination by producing or theoretically forcing a braid beta in B_9 such that

    rho^Y_9(beta)=1,
    rho^X_9(beta) != 1.

If possible, give a method to extract an explicit signed Artin-generator word.

C. Give a finite presentation / structural identification of the tetrahedral rack image and the shifted X image that explains why the joint image should or should not stay diagonal at all arities 3k.

The needed answer is not another bounded-evidence summary. I need an all-k proof of shear vanishing, or a concrete n=9 obstruction mechanism/word, or a structural presentation reducing n=9 and higher 3k to a finite check.
```
