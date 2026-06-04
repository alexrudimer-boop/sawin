# Affine F2^3 Size-4 Rack Target

Status: superseded on 2026-06-04 by
`2026-06-04-affine-f2-q3-tetrahedral-module-target_answered.md`.

Prompt:

```text
Continue in the same chat. The affine F_2^3 candidate below is not dominated by D_3, but a specific 4-element rack matches its braid image through arity 5. Please focus on proving or refuting domination by this exact rack.

Problem. For a finite bijective set-theoretic Yang-Baxter solution X, Sawin asks whether there is always a finite rack Y such that

    ker(B_n acting on Y^n) <= ker(B_n acting on X^n)

for every n.

Candidate X. Let X=F_2^3. Write x=(x1,x2,x3), y=(y1,y2,y3), and define R_X(x,y)=(u,v) by the affine formula over F_2

    u1 = x2 + y1
    u2 = x1 + y1
    u3 = y3 + 1
    v1 = x3 + y1 + y3 + 1
    v2 = x1 + x2 + y2
    v3 = x1 + x2 + y1 + y3

Equivalently, the matrix rows and offset are

    010100
    100100
    000001
    001101
    110110
    110101

    t=001100.

Structural finite checks: X is bijective YBE, bi-degenerate, non-involutive, not rack-type, has universal one-state observer partition, no nonempty proper crossing-closed subsolution, and is quotient-rigid by pair-generated congruence closure.

The 3-element dihedral rack D_3 fails at arity 5:

    n=5: |G_D3|=51840, |G_X|=77760,

and there is an explicit length-25 braid in ker(D_3) moving X.

Now the promising rack Y has elements {0,1,2,3} and rack operation table rows

    [0,2,3,1]
    [3,1,0,2]
    [1,3,2,0]
    [2,0,1,3]

meaning row a gives a*b for b=0,1,2,3. This is the tetrahedral-looking 4-element rack/quandle: each left translation fixes a and cycles the other three points.

Native mixed-image checks compare tuple permutations on Y^n with affine transformations on X^n. They give exact image equality and no detector-kernel obstruction through arity 5:

    n=2: |G_Y|=|G_X|=3
    n=3: |G_Y|=|G_X|=24
    n=4: |G_Y|=|G_X|=648
    n=5: |G_Y|=|G_X|=77760

Question. Please do one of the following decisively:

A. Prove that this 4-element rack Y dominates X for every n. Ideally prove kernel equality. A useful proof could identify both braid images as the same finite-field representation or construct a finite-state/affine gauge from Y to X.

B. Refute domination by finding the first arity n and braid word beta with rho^Y_n(beta)=1 but rho^X_n(beta)!=1. If possible, explain the structural reason the equality holds through n=5 and fails later.

C. Identify an all-n image-order formula for both actions. The first values are 3, 24, 648, 77760. A matching formula would strongly guide A; a mismatch would guide B.

D. If neither A nor B is possible, give the next exact computation that should be implemented. The computation must be specific: arity, representation, expected state size, and what kernel/image condition to check.

Please keep the answer self-contained and grounded in the exact tables above. Bounded evidence alone is not a final answer unless it is presented as a precise next computation.
```
