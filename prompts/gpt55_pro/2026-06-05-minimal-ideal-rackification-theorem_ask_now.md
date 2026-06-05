# Minimal-Ideal Rackification Theorem Prompt

Status: ask_now / prepared for GPT-5.5 Pro on 2026-06-05.

Prompt:

```text
Please answer self-containedly and mathematically. Do not give a bounded search
plan as the main result. The goal is to move Sawin's finite-rack domination
problem forward.

Problem:

Let X be a finite bijective set-theoretic Yang-Baxter solution, with

    r(x,y) = (L_x(y), R_y(x)).

Sawin asks whether every finite X is dominated by a finite rack Y:

    ker rho^Y_n <= ker rho^X_n      for all n.

Current endpoint:

Known positive branches handle one-sided nondegenerate solutions, involutive
solutions, quotient/subsolution/flip-across decompositions, transport or
periodic observer-rack certificates, and several affine/small pressure examples.
Fixed-arity rack cofinality is known, so a genuine counterexample must defeat
every finite rack prefix at arbitrarily large arities.

Thus a minimal counterexample outside known branches should be an
everywhere-singular rigid core: every L_x and every R_y is non-bijective, with
no proper quotient, no proper crossing-closed subsolution, no nonconstant
one-state observer, no flip-across/twisted union, and no known active
rack/observer factor.

Important correction:

A rack cover route is dead. If p:Y -> X is a surjective solution morphism and Y
is a rack solution r_Y(a,b)=(a*b,a), then X must itself satisfy R_y(x)=x for all
x,y. Hence an everywhere-singular X cannot be a rack quotient. Domination, if
true, must come from a detector/factor/code, not a surjective rack cover.

Finite semigroup content:

Let

    S_L = <L_x : x in X>,      S_R = <R_y : y in X>

be the nonempty-product transformation semigroups. If every L_x is singular,
then every element of S_L is singular. The minimal ideal K_L consists of
minimal-rank maps and contains idempotents. For an idempotent e in K_L, the
local monoid e S_L e = e K_L e is a finite group acting faithfully on
Omega_e=im(e). Each generator L_x maps minimal-rank images bijectively to
minimal-rank images.

But the canonical object is not one group H_e. It is the minimal-ideal transport
groupoid:

    objects: minimal-rank images im(e) for idempotents e in K_L;
    morphisms: restrictions of elements of K_L giving bijections between these
               images;
    vertex groups: e K_L e.

The right side gives a second transport groupoid from K_R. A serious positive
route probably needs the combined left/right groupoids and their YBE
compatibility.

What is not proved:

This groupoid does not yet give a finite rack detector or a braid-equivariant
factorization of X^n. It also is not the classical structure group; in the
left-nondegenerate case it collapses only to the finite left-permutation group
image.

Task:

Try to prove or refute the following precise theorem.

Minimal-ideal rackification theorem.

For every finite everywhere-singular bijective YBE solution X that survives the
known rigid-core filters, the combined left/right minimal-ideal transport
groupoids admit a finite rack Y and finite observer data I_n such that, for
every n, there is an injective braid-equivariant code

    Phi_n : X^n -> Y^n x I_n

where B_n acts trivially on I_n. Consequently Y dominates X.

Please do one of the following:

A. Prove the theorem, or prove a nontrivial special case that would apply to a
   minimal counterexample. The proof must construct the rack Y and the
   all-arity code Phi_n, not merely identify finite semigroup groups.

B. Show how the left/right minimal-ideal transport groupoids combine into an
   augmented rack or conjugation/action rack. Give the actual rack operation and
   prove the local braid equivariance relation.

C. Prove a no-go theorem for this route: construct formal left/right
   minimal-ideal transport groupoids satisfying the semigroup consequences and
   YBE-compatible local transport laws, but for which no such rack/observer code
   can exist. State exactly which condition blocks the code.

D. Identify the exact missing lemma in proof-level form. It should be a precise
   statement about cross-coordinate escapes, kernel-family transport, Green/Rees
   data, or the middle YBE identity. It should be strong enough that proving it
   would give a finite rack detector, not just another finite invariant.

Important:

- Do not claim that a local group eK_L e is canonical; the canonical object is
  the groupoid.
- Do not claim domination until a finite rack detector or injective all-arity
  observer-rack code is explicitly constructed.
- Use the coordinate YBE identities and finite transformation semigroup theory.
- Separate a true Sawin-positive theorem from a new positive branch.
```
