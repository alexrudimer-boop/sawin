# Y2 Minimal-Ideal Coupling Lemma Prompt

Status: partially_answered / GPT-5.5 Pro proved that everywhere-singular
solutions always have nonconstant finite product-semigroup observers in every
arity under the broad observer definition. The remaining issue is rackifying
or reducing along those observer fibers, not proving observer existence.

Prompt:

```text
Please answer self-containedly and mathematically. Do not give a bounded search
plan as the main result.

We are working on Sawin's finite-rack domination problem for finite bijective
set-theoretic Yang-Baxter solutions:

    Does every finite solution X admit a finite rack Y with
    ker rho^Y_n <= ker rho^X_n for every n?

Write

    r(x,y) = (L_x(y), R_y(x)).

Known status:

1. The rack-cover route is dead for everywhere-singular cores. A surjective
   morphism from a rack solution r_Y(a,b)=(a*b,a) to X forces R_y(x)=x for all
   x,y, so X must already be rack-type.

2. If every L_x is singular, the left transformation semigroup

       S_L=<L_x>

   contains no permutations. Its minimal ideal K_L consists of minimal-rank
   maps. Idempotents e in K_L give minimal images Omega_e=im(e), and the local
   groups eK_Le act faithfully on Omega_e.

3. The canonical finite object is not one group. It is the minimal-ideal
   transport groupoid:

       objects: minimal-rank images Omega_e;
       morphisms: restrictions of elements of K_L between these images;
       vertex groups: eK_Le.

   The right side gives an analogous groupoid from S_R=<R_y>.

4. Idempotents act constantly on the set of minimal images, but bijectively
   between the images themselves. Do not treat them as pointwise constant maps.

5. The combined L/R transformation semigroup matters for subsolutions. If a
   nonempty proper A subset X is invariant under every L_x and every R_y, then
   A is a crossing-closed subsolution. Left-invariance alone is insufficient.

6. The left and right product observers

       O^L_n(x_1,...,x_n)=L_{x_1}...L_{x_n},
       O^R_n(x_1,...,x_n)=R_{x_n}...R_{x_1}

   are braid-invariant finite observers. This follows from the first and third
   coordinate YBE identities.

7. Minimal-ideal groupoid flatness is automatic. For r(x,y)=(u,v) and
   s in K_L,

       L_u L_v s = L_x L_y s,

   so the two left transport paths through a local crossing agree. Dually,
   for t in K_R,

       R_v R_u t = R_y R_x t.

What remains open:

These finite observers and flat groupoids do not yet produce a rack detector.
Kernel containment is weaker than an equivariant surjection Y^n -> X^n, and an
injective observer-rack code

    X^n -> Y^n x I_n

requires actual coordinate rack colours, not just finite semigroup labels.

Task:

Attack the first missing theorem:

Y2 minimal-ideal coupling lemma.

In an everywhere-singular, quotient-rigid, subsolution-rigid, observer-rigid
finite bijective YBE solution, the middle YBE identity either:

    (a) forces the combined left/right minimal-ideal transport groupoids plus
        O^L_n,O^R_n to yield a finite rack Y and an injective all-arity code

            X^n -> Y^n x I_n,

        or

    (b) produces a proper quotient, proper crossing-closed subsolution,
        nonconstant observer, or explicit obstruction to minimal rigid-core
        existence.

Please do one of:

A. Prove a nontrivial version of this lemma. It is enough to prove it under an
   additional condition that every minimal counterexample must satisfy, but the
   condition must be justified.

B. Derive a precise Y2 compatibility law for the combined left/right
   minimal-image groupoids. State it in terms of objects Omega_e, vertex groups
   eK_Le, right-side objects Psi_f, and local row r(x,y)=(u,v). Explain whether
   it is strong enough to define rack colours.

C. Prove a no-go theorem showing that the flat left/right groupoids and product
   observers are insufficient even with the displayed Y2 compatibility. The
   no-go should identify the missing data needed for a rack/observer code.

D. Formulate the exact smaller theorem after Y2 coupling. It must be sharper
   than "active-factor observability" and strong enough to imply Sawin for a
   minimal rigid core if proved.

Important:

- Do not state that kernel containment is equivalent to an equivariant
  surjection.
- Do not claim that the minimal-ideal groupoid already gives domination.
- Use the middle YBE identity explicitly. The first and third identities only
  give flatness of O^L/O^R.
- Separate theorem-level conclusions from plausible conjectural mechanisms.
```
