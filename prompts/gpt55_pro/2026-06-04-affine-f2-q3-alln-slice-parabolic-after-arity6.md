# Affine F2^3 All-n Slice/Parabolic Target After Arity 6

Status: queued for GPT-5.5 Pro on 2026-06-04.

Prompt:

```text
Continue in the same chat. The arity-6 matrix test for the exact affine F_2^3 table X and tetrahedral rack Y now passes. Please focus only on the remaining all-n theorem or a higher-arity obstruction.

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

Exact rack Y. Let Y=F_2^2 with T row masks (2,3), T^2+T+I=0, and

    a*b = T b + (I+T)a.

The braid crossing is (a,b)->(a*b,a), local F_2 block

    M_Y =
    1101
    1011
    1000
    0100.

Finite kernel equality evidence:

    n=2: |G_Y|=|G_X|=|G_{Y,X}|=3
    n=3: |G_Y|=|G_X|=|G_{Y,X}|=24
    n=4: |G_Y|=|G_X|=|G_{Y,X}|=648
    n=5: |G_Y|=|G_X|=|G_{Y,X}|=77760
    n=6: |G_Y|=|G_X|=|G_{Y,X}|=39813120

The n=6 computation was done as matrix/permutation groups on vector spaces, not tuple actions:

    G_Y(6) <= GL_12(2),
    G_X(6) <= GL_18(2),
    G_{Y,X}(6) <= GL_12(2) x GL_18(2).

Since the joint order equals |G_Y(6)|, the arity-6 joint kernel K_6 is trivial. This also corrects the earlier guessed order 41,057,280.

Additional finite structural certificate. Over F_4=F_2[t]/(t^2+t+1), the full tetrahedral Alexander representation preserves

    L_n(z_1,...,z_n)=sum_{i=1}^n t^{i-1} z_i.

Each slice L_n=s has F_2 dimension 2n-2. The repo verified by solving affine conjugacy equations that the induced X fibre action is affine-conjugate to rack Y restricted to at least one slice L_n=s for every 2<=n<=10. Matching slice constants:

    n=2: 0,1,t,t+1
    n=3: 1,t,t+1
    n=4: 0,1,t,t+1
    n=5: 0,1,t,t+1
    n=6: 0
    n=7: 0,1,t,t+1
    n=8: 0,1,t,t+1
    n=9: 1,t,t+1
    n=10: 0,1,t,t+1

Please now resolve one of these all-n questions:

A. Prove a uniform all-n slice-conjugacy theorem. Give an explicit affine change of variables, or a recurrence constructing one, showing that the induced X fibre action is affine-conjugate to tetrahedral rack Y on a slice L_n=s(n). Also prove that this fibre/slice action faithfully controls the full shifted X action, so that Y dominates X.

B. Prove the rack-only finite-to-infinite theorem: for the tetrahedral rack Y, ker rho^Y_n is normally generated in B_n by consecutive parabolic copies of ker rho^Y_k for k<=6, for every n>6. Since kernel equality is now checked through n=6, this would prove Y dominates X in all arities.

C. Refute domination by finding or theoretically forcing a higher-arity braid word beta in ker rho^Y_n but not in ker rho^X_n. Since n<=6 passes, the first obstruction must be n>=7.

Please do not re-answer with the n=6 computation; it is already done. The needed step is now a genuine all-n slice/parabolic proof or a higher-arity obstruction mechanism.
```
