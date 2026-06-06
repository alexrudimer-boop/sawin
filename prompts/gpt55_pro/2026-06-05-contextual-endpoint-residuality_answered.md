# Contextual Endpoint Residuality Prompt

Status: answered by GPT-5.5 Pro on 2026-06-05.

Response summary:

- Pointwise endpoint-faithfulness is not a formal consequence of the
  definitions of `P_X`, `L_X`, and `C_M(X)`.
- It is exactly finite-residual injectivity of contextual endpoint profiles on
  `K_n(P_X)`-fiber monodromy.
- Local YBE identities prove braid coherence and contextual endpoint transport,
  but not finite rack residual separation of endpoint generators.
- A principal endpoint-invisible bad triple remains possible under current
  Target A machinery: closed in `P_X`, nonclosed in `X`, and closed in every
  finite residual contextual endpoint rack.
- Assuming pointwise, fixed arity is uniform because the transition set
  `T_n={(a,c): c!=a, c=beta a for some beta in K_n(P_X)}` is finite and
  `D_M` depends only on `(a,c)`.
- Failure of pointwise kills the current endpoint-detector Target A route, but
  it does not disprove Sawin or produce Target B.
- The next missing theorem is a no-principal-holonomy / contextual endpoint
  residuality theorem.

Prompt:

```text
Please answer self-containedly and mathematically.  We are working on Sawin's
finite rack-domination problem:

    For every finite bijective set-theoretic YBE solution X, does there exist
    a finite rack Y with ker rho_n^Y <= ker rho_n^X for every n?

Current Target A decomposition.

Let kappa:X->P_X be the universal finite rack shadow.  Let B be the set of
witnessed kernel-fiber bad triples

    b=(n,a,beta),
    a in X^n,
    beta in K_n(P_X),
    beta a != a.

For a finite quotient M of L_X, let

    D_M={
      b=(n,a,beta) in B :
      exists i<=n with epsilon_i^M(a) not equiv_M epsilon_i^M(beta a)
    }.

The quotient family is directed and D_M is monotone under refinement.

We have now split endpoint-faithfulness into:

    Pointwise endpoint-faithfulness:
        B = union_M D_M.

    Uniform endpoint-faithfulness:
        exists M_* with B = D_{M_*}.

Pointwise excludes principal harmful ultrafilters.  Uniform excludes both
principal and nonprincipal harmful ultrafilters.  Pointwise implies fixed-arity
uniformity, so any nonprincipal harmful ultrafilter under pointwise must
escape to unbounded arity.

Task.

1. Audit pointwise endpoint-faithfulness as a standalone theorem:

       beta in K_n(P_X), beta a != a
       => exists finite M and i<=n with
          epsilon_i^M(a) not equiv_M epsilon_i^M(beta a).

   Is this actually provable from the definitions of P_X, L_X, and C_M(X)?
   Or can there be a principal endpoint-invisible bad triple?

2. Reformulate pointwise endpoint-faithfulness in algebraic terms using the
   finite residual congruence of C_M(X):

       s equiv_M t iff every finite rack quotient of C_M(X) identifies d_s,d_t.

   Is there a natural map from X-fiber monodromy to a residual completion of
   contextual endpoint racks whose injectivity would imply pointwise
   faithfulness?

3. For fixed arity n, characterize the finite transition set

       T_n={(a,c): c!=a and exists beta in K_n(P_X) with c=beta a}.

   Can T_n be detected by one finite quotient assuming pointwise?  Does the
   detecting quotient depend on the braid witness or only on (a,c)?

4. Study principal obstruction patterns.  What would a finite bad triple

       (n,a,beta)

   invisible to every finite contextual rack detector have to look like?
   Write the exact constraints on r_X, kappa, beta, and the endpoint pairs.

5. Check whether local YBE identities rule out principal invisibility.  Use
   the component identities for r(x,y)=(L_x(y),R_y(x)) and the contextual rack
   relations.  Identify the first step where local identities stop proving
   endpoint residuality.

6. Study special branches for pointwise residuality:

       racks,
       left-nondegenerate solutions,
       nondegenerate involutive/symmetric solutions,
       degenerate involutive solutions,
       constant-action/permutation solutions,
       product/padding branches.

   Which branches prove pointwise directly, and what exact structure is used?

7. If pointwise endpoint-faithfulness fails, does that already obstruct the
   contextual Target A route completely?  Could direct finite rack absorption
   still happen by a detector not expressible through the D_M construction, or
   is D_M already the full endpoint-detector framework?

8. If pointwise fails, can the principal invisible bad triple be converted into
   Target B, an independent active factor?  State the finite coordinatewise YBE
   data that would be needed and explain whether the invisible triple supplies
   it.

9. If pointwise is true in all known branches but not formal in general,
   propose the weakest additional hypothesis that proves it.  Examples:

       finite residual faithfulness of contextual endpoint racks;
       a separating family of enriched but word-defined rack labels;
       a local-to-global endpoint residuality theorem;
       a no-principal-holonomy theorem.

10. State the sharpest valid theorem after this audit, separating:

    - what is proved for fixed arity assuming pointwise;
    - what pointwise itself requires;
    - what uniformity still requires after pointwise;
    - what belongs to Target B rather than Target A.

Guardrails.

- Do not confuse pointwise with uniform.
- Do not use the residual endpoint quotients E_M as active factors.
- Do not claim finite rack residuality of C_M(X) unless it is proved or added
  as a hypothesis.
- Do not count path-dependent holonomy unless it becomes word-defined finite
  rack endpoint data.
- Do not derive Target B without finite coordinatewise YBE data and global
  orbit-injectivity.

Goal.

Determine whether contextual endpoint residuality, the pointwise half of
endpoint-faithfulness, is provable from current YBE/contextual machinery, or
whether principal endpoint-invisible bad triples remain a genuine possible
obstruction.
```
