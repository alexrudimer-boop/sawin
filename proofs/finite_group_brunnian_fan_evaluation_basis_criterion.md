# Finite-group Brunnian fan evaluation basis criterion

This note records the current exact finite-group detector reduction.

The earlier reductions show that Sawin domination is controlled by ordinary
Brunnian fan words:

```text
Br_m subset L_m = ker(P_m -> P_{m-1}) ~= F_{m-1}.
```

The fan-only regular-module theorem

```text
proofs/fan_only_regular_module_conjugation_detector_theorem.md
```

shows that any nonidentity finite-group evaluation of such a fan word can be
turned into detection by a finite conjugation rack.

Therefore the remaining finite-group detector problem is exactly a finite
basis problem for fan-word evaluations.

## Definition: finite fan-evaluation basis

Let `X` be a finite bijective YBE solution.

A finite family of finite groups

```text
H_1,...,H_s
```

is a Brunnian fan-evaluation basis for `X` if, for every `m` and every

```text
w in Br_m subset L_m ~= F_{m-1},
```

the implication holds:

```text
rho_m^X(w) != 1
    =>
exists i, exists (h_1,...,h_{m-1}) in H_i^{m-1}
such that w(h_1,...,h_{m-1}) != 1.
```

In words: every `X`-visible Brunnian fan word has a nonidentity evaluation in
one of finitely many fixed finite groups.

Equivalently, after replacing the finite family by its direct product, this
can be stated with one finite group `H_X`.  The sharpened single-group version
and the exact diagonal law-ghost negation are recorded in

```text
proofs/uniform_brunnian_fan_evaluation_frontier.md
```

## Theorem: basis implies finite-group domination

If `X` has a finite Brunnian fan-evaluation basis

```text
H_1,...,H_s,
```

then `X` is dominated by a finite conjugation rack.

More explicitly, set

```text
C_reg(H_i) = F_2[H_i] semidirect H_i
```

and

```text
G_X = C_2 x C_reg(H_1) x ... x C_reg(H_s).
```

Then

```text
K_n(G_X^conj) <= K_n(X)
qquad for every n.
```

## Proof

By the fan-only regular-module theorem, if a Brunnian fan word has a
nonidentity evaluation in `H_i`, then the corresponding braid is detected by
`C_reg(H_i)^conj`.

Thus the finite group

```text
C_reg(H_1) x ... x C_reg(H_s)
```

detects every `X`-visible Brunnian fan word.  Equivalently,

```text
Br_m cap K_m((C_reg(H_1) x ... x C_reg(H_s))^conj)
    subset K_m(X)
```

for every `m`.

Now apply the pointed-Brunnian detector reduction.  The identity element makes
every conjugation rack pointed, and the extra `C_2^conj` factor is the
two-element trivial rack, which forces braid purity.  Therefore

```text
K_n(G_X^conj) <= K_n(X)
```

for every `n`.

This proves finite-group domination.

## Converse in obstruction form

If no finite Brunnian fan-evaluation basis exists, then there is a diagonal
Brunnian fan ghost:

```text
eta_j in Br_{m_j},       m_j -> infinity,
rho_{m_j}^X(eta_j) != 1,
```

such that for every fixed finite group `H`,

```text
eta_j(h_1,...,h_{m_j-1}) = 1
```

for all sufficiently large `j` and all tuples in `H^{m_j-1}`.

Indeed, enumerate all finite groups

```text
Q_1,Q_2,Q_3,...
```

and, for each arity `q`, include the fixed-arity finite detector group
`D_q^X = G_q^X`, where `G_q^X = rho_q^X(L_q)`.  Since no finite basis exists,
for each `j` there is an `X`-visible Brunnian fan word invisible on all groups

```text
Q_1,...,Q_j,D_2^X,...,D_j^X.
```

The inclusion of the fixed-arity detectors forces its arity to be larger than
`j`.  Hence the arities tend to infinity.  And because every fixed finite group
appears among the `Q_i`, the sequence is eventually a law on every fixed finite
group.

Thus failure of the basis theorem is exactly the diagonal ghost obstruction.

## Final remaining theorem

The finite-group detector route is now reduced to:

```text
Uniform Brunnian Fan-Evaluation Basis Lemma.

Every finite bijective YBE solution X admits a finite Brunnian fan-evaluation
basis.
```

If this lemma holds, Sawin's finite-rack domination problem is solved in the
stronger finite-conjugation-rack form.

If it fails, the counterexample is explicit: a finite `X` with a diagonal
sequence of `X`-visible all-variable Brunnian fan words that is eventually a
law on every fixed finite group.
