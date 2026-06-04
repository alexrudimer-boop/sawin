# Subsolution-Fibre Gauge Compression

Status: queued for GPT-5.5 Pro on 2026-06-04.

Prompt:

```text
Continue in the same chat. Please answer this narrower branch question decisively. Assume no repo access; all definitions are included here.

Let X be a finite bijective set-theoretic Yang-Baxter solution with

    r_X(x,y)=(lambda_x(y), rho_y(x)).

A finite rack Y dominates X if ker(B_n acting on Y^n) is contained in ker(B_n acting on X^n) for every n.

Known allowed facts:
1. left-nondegenerate finite YBE solutions are rack-dominated by the derived rack;
2. finite involutive solutions are dominated by the two-point flip rack;
3. domination is closed under flip-across disjoint unions;
4. if a finite family of proper total YBE quotient maps pi_alpha:X -> Z_alpha has point-separating product X -> product_alpha Z_alpha, and all Z_alpha are rack-dominated, then X is rack-dominated;
5. fixed active-factor certificates prove domination: if there are already rack-dominated finite YBE factors T_alpha, finite Mealy state sets Q_alpha, transitions delta_alpha, and outputs omega_alpha:Q_alpha x X -> T_alpha satisfying the local equivariance equations

    r_{T_alpha}(omega_alpha(q,x), omega_alpha(delta_alpha(q,x),y))
      =
    (omega_alpha(q,u), omega_alpha(delta_alpha(q,u),v))

    whenever r_X(x,y)=(u,v), and the combined left-to-right output code X^n -> product_alpha T_alpha^n is injective for every n, then X is rack-dominated.

Question. Suppose X has a proper YBE congruence theta whose blocks are all crossing-closed subsolutions:

    x,y in B  =>  r_X(x,y) in B x B

for each theta-block B. Assume the quotient X/theta is rack-dominated and every block subsolution B is rack-dominated. This is exactly the situation where the quotient plus block restrictions look smaller, but mixed-block crossings may carry hidden fibre transition data.

The theorem I want you to decide is:

    Subsolution-fibre gauge theorem:
    Under the hypotheses above, X admits a proper active-factor compression using only X/theta, the block subsolutions B, finite-state transducers, and invariant observer outputs. Consequently X is rack-dominated.

Please either:

1. prove this theorem completely, including an explicit construction of the finite state sets and output maps and a proof of all-length injectivity; or
2. refute it with an explicit finite YBE table X, a proper congruence theta with crossing-closed rack-dominated blocks and rack-dominated quotient, but no such proper active-factor compression from these data; if the refutation is not a Sawin counterexample, say so clearly.

Do not restate that a bounded certificate search is finite. I am asking whether this specific subsolution-fibre branch is actually valid. The subtle point is the mixed-block transition cocycle: detectors on the quotient and inside the blocks may fail unless the finite-state gauge records enough mixed-transition data. Decide whether finite YBE locality always makes such a gauge finite and injective, or whether there is a genuine obstruction.
```
