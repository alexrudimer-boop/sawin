# Framed-to-Conjugation Cover Frontier and Remaining Uniformity Problem

The framed fan-envelope route gives a finite-rack strategy.  To upgrade it to
the stronger finite-conjugation-rack strategy for the Brunnian fan reduction,
one does not need the full framed-cover lemma.  The fan-only regular-module
detector theorem is enough.

The distinction is important:

```text
Uniform framed fan envelope
  => finite pointed rack detector
  => finite rack domination.

Uniform framed fan envelope + fan-only regular-module detector
  => finite conjugation-rack domination.
```

The desired covering theorem is:

```text
Framed-to-Conjugation Cover Lemma.

For every finite group G, there exists a finite group C(G) such that

    K_n(C(G)^conj) subset K_n(A_G^+)

for every n.
```

Here `A_G` is the framed Artin detector rack with labels `(g,u) in G x G`, and
`A_G^+` is its transparent-point extension.

The current candidate is recorded in

```text
proofs/regular_module_framed_to_conjugation_cover_theorem.md
```

with

```text
C(G) = F_2[G] semidirect G,
```

where `G` acts by the left regular action on the finite module `F_2[G]`.

The proof is not yet unconditional.  The missing point is a Fox-derivative
separation statement for Artin longitudes: vector terms in the regular module
must not be able to cancel every nontrivial longitude value.

However, the full cover is stronger than what the final Brunnian fan reduction
needs.

The sufficient fan-only theorem is proved in

```text
proofs/fan_only_regular_module_conjugation_detector_theorem.md
```

It says that if a Brunnian fan word has a nonidentity evaluation in a finite
group `H`, then it is detected by

```text
C_reg(H)^conj,
qquad C_reg(H)=F_2[H] semidirect H.
```

The proof labels the moving fan strand with group component `1`, so the vector
part of the lifted longitude cancels:

```text
(a,l)(v,1)(a,l)^{-1} = (l v,1).
```

Thus the regular module detects the nonidentity fan value without needing the
full Fox-separation lemma.

If that lemma holds, then every finite framed envelope

```text
P_X = A_{H_1}^+ x ... x A_{H_s}^+
```

can be replaced by the finite conjugation rack

```text
C(H_1)^conj x ... x C(H_s)^conj.
```

## Two-Strand Sanity Check

The executable probe

```text
proofs/framed_to_conjugation_b2_probe.md
```

checks the smallest framed detector `A_C2` in arity two.

For `B_2`, the kernel of a finite rack action is determined by the order of
`sigma_1`.  The probe records:

```text
A_C2:      ord(sigma_1)=4,
S3^conj:   ord(sigma_1)=12.
```

Therefore

```text
K_2(S3^conj) subset K_2(A_C2).
```

This matches the familiar mod-2/S3 bridge and shows that the framed correction
is compatible with the old cyclic detector in the smallest arity.

## Arity-3 Residual Check

The executable probe

```text
proofs/framed_c2_s3_arity3_cover_probe.md
```

checks the actual residual-image containment for the same framed detector in
arities `2` and `3`.  It records:

```text
n=2: joint image 12, kernel size 1, no nonidentity A_C2 action in K_2(S3^conj);
n=3: joint image 279936, kernel size 1, no nonidentity A_C2 action in K_3(S3^conj).
```

Thus the finite audit certifies

```text
K_n(S3^conj) subset K_n(A_C2)
```

for `n=2,3`.

## All-Arity C2 Cover

The note

```text
proofs/framed_c2_s3_all_arity_cover_proof.md
```

upgrades the `A_C2` probe to a theorem.  For `G=C2`, the framed detector
records only the Artin longitude matrix modulo `2`.  On pure braids this is
the pairwise linking matrix modulo `2`, so the `A_C2` action factors through

```text
M_n = B_n / (P_n' P_n^2).
```

Since `S3^conj` detects every nontrivial element of `M_n`, one gets

```text
K_n(S3^conj) subset K_n(A_C2)
```

for every arity `n`.

## Abelian Framed Cover

The note

```text
proofs/framed_abelian_dihedral_cover_theorem.md
```

extends the `C2` result to every finite abelian group `A`.  If `e=exp(A)`,
then the framed detector `A_A` records only the Artin longitude matrix modulo
`e`, i.e. pairwise linking modulo `e` on pure braids.  The generalized
dihedral group

```text
D_e = C_{2e} semidirect C_2
```

detects exactly this obstruction through its reflection sector.  Hence

```text
K_n(D_e^conj) subset K_n(A_A)
```

for every arity `n`.

## Remaining Boundary

There is now one remaining statement for the finite-group detector route.

The full framed-cover problem remains interesting:

```text
If an Artin longitude value is nonidentity in a finite group G, then the
corresponding braid is detected by (F_2[G] semidirect G)^conj.
```

But the final Brunnian fan reduction only needs the uniform finite fan-envelope
statement:

```text
For every finite bijective YBE solution X, find finite groups H_1,...,H_s
such that every X-visible Brunnian fan word has a nonidentity evaluation in
one of the H_i.
```

If the uniform statement holds, then

```text
P_X = A_{H_1}^+ x ... x A_{H_s}^+
```

is a finite framed envelope and `T_2 x P_X` dominates `X` as a finite rack.
By the fan-only regular-module theorem, the same fan evaluators give a finite
conjugation rack

```text
C_2^conj x C_reg(H_1)^conj x ... x C_reg(H_s)^conj
```

dominating `X`.

The exact criterion is recorded in

```text
proofs/finite_group_brunnian_fan_evaluation_basis_criterion.md
```

There the finite groups `H_1,...,H_s` are called a Brunnian
fan-evaluation basis for `X`.

## Correct Next Fork

There are now two nested final routes.

### Positive Route

Prove the Uniform Framed Fan-Envelope Theorem:

```text
Every X-visible Brunnian fan word has a nonidentity evaluation in one of
finitely many finite groups H_1,...,H_s.
```

Equivalently, prove that every finite `X` has a finite Brunnian
fan-evaluation basis.

Then

```text
T_2 x A_{H_1}^+ x ... x A_{H_s}^+
```

dominates `X` as a finite rack.

The fan-only theorem replaces each fan evaluator `H_i` by
`C_reg(H_i)^conj`, giving finite conjugation-rack domination.

### Counterexample Route

If the uniform framed envelope fails, the obstruction is a diagonal Brunnian
fan ghost: a sequence of X-visible Brunnian fan words whose arities tend to
infinity and which is eventually invisible to every fixed finite group, hence
to every fixed finite framed detector.

Thus the remaining finite-group-theoretic step is:

```text
Prove or refute the Uniform Framed Fan-Envelope Theorem,
equivalently exclude or construct a diagonal Brunnian fan ghost.
```
