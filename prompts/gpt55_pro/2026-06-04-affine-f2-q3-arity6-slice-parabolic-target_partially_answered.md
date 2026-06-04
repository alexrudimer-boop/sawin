# Affine F2^3 Arity-6 Slice/Parabolic Target

Status: partially resolved locally on 2026-06-04.  The arity-6 matrix-group
test passes with order `39,813,120`; follow-up queued in
`2026-06-04-affine-f2-q3-alln-slice-parabolic-after-arity6_ask_now.md`.

Prompt:

```text
Continue in the same chat. Please focus on the exact affine F_2^3 YBE table X and exact 4-element tetrahedral/Alexander rack Y below. The previous answer reduced the next finite test to arity 6 matrix groups and the all-n proof to a tetrahedral-rack parabolic/slice theorem. I need a decisive resolution of one of those two tasks.

Background. Sawin asks whether every finite bijective set-theoretic YBE solution X is dominated by a finite rack Y, meaning

    ker(B_n acting on Y^n) <= ker(B_n acting on X^n)

for every n.

Candidate X. Let X=F_2^3. For x=(x1,x2,x3), y=(y1,y2,y3), define R_X(x,y)=(u,v) by

    u1 = x2 + y1
    u2 = x1 + y1
    u3 = y3 + 1
    v1 = x3 + y1 + y3 + 1
    v2 = x1 + x2 + y2
    v3 = x1 + x2 + y1 + y3

The affine part is linearized in arity n by the one-based position shift

    x_i -> x_i + (0,0,i mod 2).

In shifted coordinates the local linear block on (x1,x2,x3,y1,y2,y3) is

    M_X =
    010100
    100100
    000001
    001101
    110110
    110101

over F_2.

Candidate rack Y. Let Y=F_2^2 identified with labels 0,1,2,3 in identity bit order. Let T have row masks (2,3), so T^2+T+I=0. Define

    a*b = T b + (I+T)a.

The braid crossing is (a,b)->(a*b,a), with local F_2 matrix

    M_Y =
    1101
    1011
    1000
    0100

using the same row-mask convention.

Known finite evidence:

    n=2: |G_Y|=|G_X|=3
    n=3: |G_Y|=|G_X|=24
    n=4: |G_Y|=|G_X|=648
    n=5: |G_Y|=|G_X|=77760

The joint images also have these same orders through n=5, so kernels agree through n=5. D_3 fails at n=5, so this size-4 rack is the first plausible detector.

Expected n=6 image order, if the unitary pattern continues:

    41,057,280
    =
    2^10 * 3^6 * 5 * 11.

Task A: arity-6 finite matrix computation.

Compute or theoretically decide whether the joint image

    G_{Y,X}(6)=< (Y_i^(6), X_i^(6)) : 1<=i<=5 >
        <= GL_12(2) x GL_18(2)

has the same order as G_Y(6). Equivalently decide whether

    K_6 = { g_X : (I,g_X) in G_{Y,X}(6) }

is trivial.

If K_6 is nontrivial, give an explicit braid word in ker rho^Y_6 that moves X. If K_6 is trivial, give a rigorous computation/theoretical certificate of that fact.

Task B: all-n theorem for the rack/slice mechanism.

The repo found a stronger finite certificate through n=10. Over F_4=F_2[t]/(t^2+t+1), the full tetrahedral Alexander representation preserves

    L_n(z_1,...,z_n)=sum_{i=1}^n t^{i-1} z_i.

Each slice L_n=s has F_2 dimension 2n-2. For every 2<=n<=10, the induced X fibre action is affine-conjugate to rack Y restricted to at least one slice L_n=s. The matching slice constants found are:

    n=2: 0,1,t,t+1
    n=3: 1,t,t+1
    n=4: 0,1,t,t+1
    n=5: 0,1,t,t+1
    n=6: 0
    n=7: 0,1,t,t+1
    n=8: 0,1,t,t+1
    n=9: 1,t,t+1
    n=10: 0,1,t,t+1

Please prove or refute a uniform theorem explaining this slice conjugacy. A proof should give an explicit all-n affine change of variables, or a recurrence constructing it, and should also explain why this slice/fibre action faithfully controls the full shifted X action.

Task C: parabolic kernel generation.

If K_6=1, prove or refute the rack-only theorem

    ker rho^Y_n is normally generated in B_n by consecutive parabolic copies
    of ker rho^Y_k for k<=6, for every n>6.

If true, then the n<=6 kernel checks prove Y dominates this X in all arities. If false, give the first obstruction mechanism.

Please answer one of A, B, or C decisively. A concrete n=6 witness, a certified n=6 trivial-kernel computation, an all-n slice conjugacy proof, or a proof/refutation of width-6 parabolic kernel generation would all be decisive progress.
```
