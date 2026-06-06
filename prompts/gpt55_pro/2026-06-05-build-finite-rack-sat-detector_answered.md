# Build Finite Rack SAT Detector Prompt

Status: ask now / awaiting GPT-5.5 Pro response.

Prompt:

```text
Please answer self-containedly and concretely.  The associated-group route is
false: for every rack R, eta(u triangleright u)=eta(u), and a two-element
constant-action rack already gives finite rack separation not seen by
associated groups.

So the next route is the full finite rack detector, not conjugation-rack
detectors.

Rack convention:

    r_R(u,v)=(u triangleright v,u).

Contextual endpoint rack.

For finite X, finite quotient M of L_X, and r(x,y)=(x',y'), C_M(X) has
generators

    [p,x,s], p,s in M, x in X,

and relations:

    (T) [p,x,bar{y}s]=[p bar{x'},y',s],

    (R) [p,x,bar{y}s] triangleright [p bar{x},y,s]
        =
        [p,x',bar{y'}s].

Finite rack detector certificate for endpoint pair e,e':

    finite rack Q with table T;
    assignment alpha:M x X x M -> Q;
    all rack axioms for T;
    all (T),(R) relations for alpha;
    alpha(e) != alpha(e').

Task.

This is not an audit prompt.  Produce an implementable detector/search plan
that can actually be coded next.

1. Give exact finite constraints for the finite rack SAT problem.

   Variables:
       rack operation T on q elements;
       assignment alpha to endpoint generators.

   Constraints:
       left translations bijective;
       self-distributivity;
       contextual (T),(R);
       endpoint inequality.

   Present them in a solver-friendly form.

2. Optimize the finite rack SAT search.

   Include symmetry breaking, quotienting by endpoint T-equivalence classes,
   precomputing the closure of forced equalities, using known rack libraries or
   enumerating rack tables, and reducing variables before SAT.

3. Give exact algorithm to search small YBE solutions:

       enumerate finite bijective YBE tables on |X|<=m;
       compute P_X by rack-admissible partitions;
       compute principal bad triples up to arity n<=N via finite paired action
       group Gamma_n^{X,P};
       enumerate finite monoid quotients M up to size k;
       run rack SAT for endpoint pairs.

   The output should classify each candidate as:

       no principal bad triple found;
       bad triple found and separated by finite rack detector;
       strong-collapse candidate;
       residual-collapse candidate.

4. Provide sound finite certificates for each classification.

   For example:
       YBE table certificate;
       P_X partition certificate;
       bad triple certificate with braid word;
       monoid quotient M table;
       finite rack detector table;
       strong-collapse derivation certificate;
       residual-collapse certificate if possible.

5. Decide the first computational experiment.

   Specify exact bounds that are feasible:

       |X|<=2 or |X|<=3,
       arity bound N,
       monoid size bound k,
       rack size bound q.

   State what result would be meaningful:

       no principal invisibles up to bound;
       associated-group failure but rack SAT success;
       candidate strong collapse;
       candidate residual collapse.

6. If possible, prove a small-size theorem by hand:

       for |X|=2, all finite bijective YBE solutions either have no principal
       bad triples or every principal bad triple is separated by a small finite
       rack detector.

   If not, give the exact computation needed.

7. Required ending.

   End with one of:

   (I) a complete pseudocode implementation plan with data structures;
   (II) a hand proof for the first nontrivial size bound;
   (III) exact SAT/SMT encoding sufficient for implementation;
   (IV) a concrete obstruction candidate and how to certify it.

Guardrails.

- Do not use associated groups as a complete method.
- Do not rehash why Target A is hard.
- Do not leave the answer at "run a search"; give explicit variables,
  constraints, certificates, and first bounds.
- Do not claim residual collapse without a sound certificate.
- Keep the output implementation-ready.

Goal.

Turn the finite rack detector route into an executable search plan that can
test the pointwise Target A gate on small finite YBE solutions and produce
checkable certificates.
```
