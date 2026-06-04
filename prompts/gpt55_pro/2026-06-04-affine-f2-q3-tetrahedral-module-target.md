# Affine F2^3 Tetrahedral Module Target

Status: answered by GPT-5.5 Pro on 2026-06-04; follow-up queued in
`2026-06-04-affine-f2-q3-arity6-slice-parabolic-target.md`.

Prompt:

```text
Continue in the same chat. Please focus on the exact finite affine YBE table and exact 4-element rack below. The decisive question is now whether the observed fibre-module/rack equivalence holds for all braid arities.

Background problem. Sawin asks whether every finite bijective set-theoretic Yang-Baxter solution X is dominated by a finite rack Y, meaning

    ker(B_n acting on Y^n) <= ker(B_n acting on X^n)

for every n.

Candidate X. Let X=F_2^3. Write x=(x1,x2,x3), y=(y1,y2,y3), and define R_X(x,y)=(u,v) by the affine formula over F_2:

    u1 = x2 + y1
    u2 = x1 + y1
    u3 = y3 + 1
    v1 = x3 + y1 + y3 + 1
    v2 = x1 + x2 + y2
    v3 = x1 + x2 + y1 + y3

Equivalently, with input coordinates (x1,x2,x3,y1,y2,y3), the local affine matrix rows and offset are

    010100
    100100
    000001
    001101
    110110
    110101

    t = 001100.

This X is bijective YBE, bi-degenerate, non-involutive, not rack-type, observer-rigid in the one-state sense, has no nonempty proper crossing-closed subsolution, and is quotient-rigid by pair-generated congruence closure.

The 3-element dihedral rack D_3 does not dominate X. It matches through arity 4 but fails at arity 5:

    |G_D3(5)| = 51840,
    |G_X(5)|  = 77760.

A B_5 word in the D_3 kernel that moves X is

    [1,1,2,1,1,3,2,4,3,3,2,1,4,3,2,2,1,3,2,4,3,3,2,4,3]

under positive-generator convention.

The current rack target is the 4-element rack Y with operation table rows

    [0,2,3,1]
    [3,1,0,2]
    [1,3,2,0]
    [2,0,1,3]

where row a gives a*b for b=0,1,2,3. Under the identity labelling {0,1,2,3}=F_2^2, this is the Alexander rack

    a*b = T b + (I+T)a

with T row masks (2,3), i.e.

    T(e1) = e2,
    T(e2) = e1+e2

in the bit-row convention. The braid crossing is

    (a,b) -> (a*b,a).

Native computations show exact marked image equality through arity 5:

    n=2: |G_Y|=|G_X|=3
    n=3: |G_Y|=|G_X|=24
    n=4: |G_Y|=|G_X|=648
    n=5: |G_Y|=|G_X|=77760

and the joint images also have the same orders, so this is kernel equality through arity 5, not just equal cardinalities.

New structural observation. For X^n, the affine offsets generate an explicit 2n-2 dimensional fibre module W_n. Write each X-strand coordinate as (a_i,b_i,c_i). A basis for W_n is given by two vectors for each edge k=1,...,n-1:

If k is odd:

    p_k = c_1 + b_2 + ... + b_k + a_{k+1},
    q_k = a_1 + b_1 + b_2 + ... + b_{k+1} + c_{k+1}.

If k is even:

    p_k = a_1 + b_1 + b_2 + ... + b_k + a_{k+1},
    q_k = c_1 + b_2 + ... + b_{k+1} + c_{k+1}.

For example:

    n=2:
      c1+a2,
      a1+b1+b2+c2

    n=3:
      c1+a2,
      a1+b1+b2+c2,
      a1+b1+b2+a3,
      c1+b2+b3+c3

The local affine X generators preserve W_n up to the affine offsets, so they induce affine transformations on W_n. Through arity 5, the following six marked images all have the same order in each arity:

    rack Y image,
    full X affine image,
    induced affine W_n image,
    rack-Y / full-X joint image,
    rack-Y / W_n joint image,
    W_n / full-X joint image.

The common orders for n=2,3,4,5 are

    3, 24, 648, 77760.

Question. Please prove or refute the all-n statement:

    ker(B_n acting on Y^n) <= ker(B_n acting on X^n)

for this exact X and this exact 4-element Alexander rack Y.

The preferred route is to prove that the affine W_n action of X and the rack-Y action have the same marked kernel for every n, perhaps by identifying both as the same reduced Burau/Alexander/unitary quotient at a primitive third root over F_4, plus explaining why the full affine X action is faithful to its W_n induced affine action.

If the statement is false, give a concrete first possible arity and a theoretical reason a rack-kernel word can still move X despite the n<=5 equality. If the statement is true, give a proof detailed enough to be converted into a repo note: define the common quotient or explicit conjugacy, handle the n=2 and n=3 low-rank cases, and show all braid relations/kernels agree for every n.
```
