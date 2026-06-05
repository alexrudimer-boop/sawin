# Product-Hurwitz Separability Prompt

Status: ask_now / prepared for GPT-5.5 Pro on 2026-06-05.

Prompt:

```text
Please answer self-containedly and mathematically. Do not give only a bounded
computation. The goal is to decide whether the product-Hurwitz separability
criterion can cover residual finite bijective Yang-Baxter solutions in Sawin's
finite rack-domination problem.

Use the right-rack convention:

    r_Y(a,b)=(b,a triangleright b).

Let X be a finite bijective YBE solution,

    r_X(x,y)=(L_x(y),R_y(x)).

The broad product observers are known:

    Lambda_n(x_1,...,x_n)=L_{x_1}...L_{x_n},
    Gamma_n(x_1,...,x_n)=R_{x_n}...R_{x_1}.

They are inert B_n-observers, but they do not by themselves imply rack
domination.  Indeed, for any finite solution Z and any finite identity solution
E with |E|>=2, the product X=E x Z is everywhere singular and

    ker rho_n^X = ker rho_n^Z

for every n.  Thus product observers alone can hide arbitrary Z-dynamics in
their fibers.

The useful sufficient theorem is product-Hurwitz separability.

Let S_L^1 be the left product semigroup with identity.  Suppose there are a
finite rack Y, maps

    c_t:X -> Y       (t in S_L^1),

and inert observer data J_n such that, for all x,y in X and t in S_L^1, writing

    u=L_x(y),  v=R_y(x),

one has

    c_{L_v t}(u) = c_t(y),                                      (LH1)
    c_t(v) = c_{L_y t}(x) triangleright c_t(y).                 (LH2)

For a word x=(x_1,...,x_n), define suffix products

    s_{n+1}=1,
    s_i=L_{x_i}s_{i+1},

and rack labels

    C_n(x)=
      (c_{s_2}(x_1), c_{s_3}(x_2), ..., c_{s_{n+1}}(x_n)).

Then C_n is B_n-equivariant.  If

    F_n(x)=(C_n(x), Lambda_n(x), J_n(x))

is injective for every n, then

    ker rho_n^Y <= ker rho_n^X

for every n.

There is a dual right-product version with maps d_p:X -> Y and equations

    d_p(u) = d_{R_x p}(y),                                      (RH1)
    d_{R_u p}(v) = d_p(x) triangleright d_{R_x p}(y).           (RH2)

Task:

1. Audit the product-Hurwitz theorem.
   - Are (LH1),(LH2) exactly the right local equations for right-rack
     equivariance?
   - Is the injectivity argument with inert observers correct?
   - Is the E x Z no-go theorem correct and sufficient to show product
     observers alone do not reduce Sawin?

2. Main target: prove or refute the residual-core separability statement.

   Residual-core product-Hurwitz separability:
   Every finite residual rigid core outside the known positive branches admits
   either left or right product-Hurwitz separability, possibly after adding
   inert observers J_n coming from quotients, orbits, semigroup endpoints, or
   finite minimal-ideal object data.

   If true, give a proof that does not assume Sawin.  If false, give a concrete
   structural obstruction or a candidate finite table pattern.

3. Relate this criterion to the minimal-ideal escape-rack construction.

   Earlier route:
   - Build C=G_L x G_R^op from left/right minimal-ideal transport groupoids.
   - Define elementary arrows eta(x;A,B):(A,R_xB)->(L_xA,B).
   - Quotient the groupoid action rack Y_0=Arr(C) by escape relations
       b'~a, a'~a*b
     to obtain Y_esc.
   - This yields an equivariant map Psi_n:X^n -> (Y_esc^Omega)^n.
   - Domination follows if Psi_n is injective on every braid orbit.

   Decide whether product-Hurwitz separability is equivalent to, stronger than,
   or weaker than this escape-rack strand-separation route.  In particular:
   - Can the escape-rack labels be rewritten as suffix-local maps c_t?
   - Does orbit-injectivity of Psi_n imply product-Hurwitz injectivity?
   - Does product-Hurwitz separability imply strand separation for some
     escape-rack quotient?

4. Address the sandwich obstruction.

   Minimal-ideal local groups do not automatically inherit YBE products:

       eL_uL_ve = eL_xL_ye

   does not imply

       eL_ueL_ve = eL_xeL_ye.

   Explain whether suffix-local labels c_t carry exactly the missing sandwich
   data, and whether this can be formalized using Rees matrix coordinates,
   holonomy groups, or transformation semigroup flows.

5. If the theorem fails, state the exact corrected endpoint:
   - a finite obstruction to product-Hurwitz labels;
   - a same-fiber hidden active factor theorem;
   - or a sharper class of residual cores where separability must be checked.

Important constraints:

- Do not claim product observers alone prove domination.
- Do not assume every equivariant kernel containment comes from an injective
  observer-rack code.
- Distinguish broad arity-dependent observers from one-state coordinate
  observers.
- If the answer is conditional, state the missing lemma precisely.
```

