# YBE Brunnian derivative gate audit

Date: 2026-06-03

This generated audit records the next Brunnian pressure-test.
The naive route from Brunnian pure braids to deletion-degree-2
obstructions is false: ordinary one-strand point-pushing derivatives
are section-gauge coboundaries.  The real target is the residual
double-deletion quotient after modding out one-strand derivatives,
bounded two-strand mutual data, and fixed-base pullback.

## Flags

- naive Brunnian pure-braid obstruction rejected: `True`;
- one-strand derivatives are gauge coboundaries: `True`;
- Brunnian point-push shadow is gauge: `True`;
- nonabelian derivative chain rule recorded: `True`;
- residual double-deletion quotient identified: `True`;
- Fadell-Neuwirth decomposition would kill high Brunnian classes: `True`;
- records Brunnian derivative gate: `True`.

## Formulas

- derivative: `nabla_q b = tau_q(b) inf_q(partial_q b)^-1`;
- gauge: `(delta u)_{p,q}^I = nabla_q b`;
- chain rule: `nabla_r(nabla_q b) = nabla_q(nabla_r b)`;
- residual quotient: `R_{p,q}^I = V_{p,q}^{I,Br} / <nabla_q V_p^{I,Br}, nabla_p V_q^{I,Br}, M_{p,q}^I, Pi^sharp V_{p,q,B}^{I,Br}>`;
- decomposition route: `a = nabla_q b_p nabla_p b_q m_{p,q} Pi^sharp(theta)`.

## Rows

### one_strand_derivative_gauge_gate

- role: `gauge_triviality`;
- statement: for b in the one-deletion vertical group V_p^I, the deletion derivative nabla_q b is the square coboundary of the 1-cochain with u_p^I=b;
- consequence: ordinary point-pushing derivatives land in deletion degree 2 but represent the trivial gauge class.

### pure_braid_brunnian_shadow_triviality

- role: `false_counterexample_removed`;
- statement: if a Brunnian pure braid is killed by deleting p and q, its transported two-deletion bisection is tau_q(b_beta)=nabla_q b_beta;
- consequence: Brunnian pure-braid subgroups can survive as vertical bisections without producing nonzero Br^2 classes.

### nonabelian_derivative_chain_rule

- role: `coherence_identity`;
- statement: the second derivatives nabla_r(nabla_q b) and nabla_q(nabla_r b) agree after the Peiffer and cube transport defects have been killed;
- consequence: YBE locality makes point-pushing derivatives satisfy the cocycle equation precisely because they are coboundaries.

### residual_double_deletion_quotient

- role: `true_obstruction_target`;
- statement: a nonzero high-arity Brunnian deletion 2-class must survive the quotient by one-strand derivatives, bounded mutual two-strand data, and fixed-base pullback;
- consequence: the counterexample search narrows to residual double-deletion vertical bisections, not arbitrary Brunnian pure braids.

### fadell_neuwirth_decomposition_route

- role: `positive_route`;
- statement: if every double-deletion vertical bisection decomposes as one-strand derivatives times a bounded mutual term and a fixed-base pullback, then the residual quotient is trivial;
- consequence: after finite labels for derivative images and bounded mutual terms, arbitrarily high Brunnian relative deletion 2-classes vanish.

## Meaning

Brunnian point-pushing can produce high-arity vertical bisections,
but their ordinary two-deletion shadows are gauge.  A genuine
relative deletion `2`-obstruction must survive the residual
quotient `R_{p,q}^I`.

Thus the positive route is now sharper: prove a Fadell-Neuwirth
decomposition of every double-deletion vertical bisection into
one-strand derivatives, bounded mutual terms, and fixed-base
pullback.  The negative route must construct a residual element
of `R_{p,q}^I`, not just a Brunnian pure braid.
