# Product-Like Subsolution-Fibre Transport Gauge

Status: answered from GPT-5.5 Pro on 2026-06-04, pasted by the user.

Answer summary:

- Verdict supplied by Pro: Question A true under the stated
  transport-isomorphism hypothesis.
- Verdict supplied by Pro: Question B false, with the size-four affine Type A
  model as a product-like but non-transport-isomorphic counterexample.
- Repo-side action: Question B is promoted to the product-like transport
  boundary audit.  Question A is being audited further because the supplied
  proof uses a split-tower domination step and an identity-gauge normalization
  step whose hypotheses must be made certificate-explicit.

Prompt:

```text
Continue in the same chat. Please answer this exact branch question decisively. Assume no repo access; all definitions and current evidence are included here.

Let X be a finite bijective set-theoretic Yang-Baxter solution with r_X(x,y)=(u,v). A finite rack Y dominates X if

    ker(B_n acting on Y^n) <= ker(B_n acting on X^n)

for every n.

Known positive branches:

1. finite left-nondegenerate YBE solutions are rack-dominated by the derived rack;
2. finite involutive solutions are dominated by the two-point flip rack;
3. domination is closed under flip-across disjoint unions;
4. point-separating families of proper total YBE quotients glue safely;
5. a finite active-factor/transducer certificate proves domination if the combined equivariant output code is injective in every arity.

Now suppose theta is a proper YBE congruence on X, with blocks F_a indexed by the quotient Z=X/theta. Assume every block F_a is a crossing-closed subsolution, and assume Z and all block subsolutions F_a are already rack-dominated.

For distinct quotient blocks a,b, write

    r_Z(a,b)=(c,d).

The mixed fibre crossing

    r_X: F_a x F_b -> F_c x F_d

is called direct-product-like if there are maps

    phi_{a,b}:F_a -> F_c,    psi_{a,b}:F_b -> F_d

with

    r_X(x,y)=(phi_{a,b}(x), psi_{a,b}(y)).

It is called swapped-product-like if there are maps

    phi_{a,b}:F_b -> F_c,    psi_{a,b}:F_a -> F_d

with

    r_X(x,y)=(phi_{a,b}(y), psi_{a,b}(x)).

Because r_X is bijective, these one-variable maps are bijections in the relevant product-like cases. Call such a mixed row transport-isomorphic if the chosen one-variable maps are isomorphisms of the internal block subsolutions: for example a map t:F_a -> F_c satisfies

    r_X(t(x),t(y)) = (t(u),t(v)) whenever r_X(x,y)=(u,v) inside F_a.

Current repo-side evidence:

- The size-four Type B degenerate non-involutive examples are flip-across unions. Their subsolution-fibre mixed rows are swapped-product-like and transport-isomorphic; the flip-across domination theorem proves them rack-dominated.
- The size-four Type A affine examples have a proper subsolution-fibre congruence whose mixed rows are swapped-product-like bijections, but the one-variable transports are NOT isomorphisms of the internal block subsolutions. Type A is still rack-dominated, but by a separate parity/fibre coordinate gauge equivalent to a two-element cyclic rack action.

Question A. Prove or refute the following restricted theorem:

    If theta has crossing-closed blocks, Z is rack-dominated, all blocks are rack-dominated, and every mixed row is product-like and transport-isomorphic, then X is rack-dominated.

A proof must explicitly construct finite rack detectors or a finite active-factor/transducer certificate and prove all-arity injectivity/equivariance. A refutation must give a finite YBE table satisfying the hypotheses but not rack-dominated, or at least satisfying the hypotheses while defeating the proposed construction.

Question B. Does finite YBE locality force every product-like mixed row to be transport-isomorphic after refining theta or changing block gauges, or is the Type A phenomenon a genuine obstruction to this restricted theorem being enough? Give a precise proof or counterexample. It is acceptable to use the Type A affine model as the counterexample if you prove it has product-like non-isomorphic transports and cannot be made transport-isomorphic by a harmless refinement that preserves a proper subsolution-fibre quotient.

Please do not answer with another broad finite-search criterion. I need either a theorem proof for Question A, or a concrete obstruction/counterexample, and a clear verdict on whether Question B is true.
```
