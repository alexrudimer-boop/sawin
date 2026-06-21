# Impact of the uniform fan-evaluation prompt

This note records exactly how the current theoretical prompt relates to
Sawin's finite-rack domination problem.

## Prompt

The current finite-group route asks for:

```text
Uniform Brunnian Fan-Evaluation Group Lemma.

For every finite bijective YBE solution X, there exists one finite group H_X
such that every X-visible Brunnian fan word has a nonidentity evaluation in
H_X.
```

Equivalently, every Brunnian fan word that is a law on `H_X` is already
`X`-invisible.

## Positive outcome

A positive answer resolves Sawin, and does so in the stronger
finite-conjugation-rack form.

Indeed, if such `H_X` exists, let

```text
C_reg(H_X)=F_2[H_X] semidirect H_X.
```

The fan-only regular-module theorem gives

```text
Br_m cap K_m(C_reg(H_X)^conj) subset K_m(X)
```

for every `m`.  The pointed-Brunnian reduction then gives

```text
K_n((C_2 x C_reg(H_X))^conj) subset K_n(X)
```

for every `n`.

Thus

```text
(C_2 x C_reg(H_X))^conj
```

is a finite conjugation-rack detector for `X`.

## Negative outcome

A negative answer to the finite-group prompt gives a diagonal finite-group law
ghost:

```text
m_j -> infinity,
w_j in Br_{m_j},
rho_{m_j}^X(w_j) != 1,
```

where `w_j` is eventually a law on every fixed finite group.

This refutes the current finite-conjugation-rack route, but it is not by
itself a counterexample to Sawin.

To refute Sawin itself, the sequence must be stronger: it must be eventually
invisible to every fixed finite pointed rack, not merely a law on every fixed
finite group.

That is, one would need

```text
eta_j in Br_{m_j},      m_j -> infinity,
eta_j notin K_{m_j}(X),
```

and for every finite pointed rack `P`,

```text
eta_j in K_{m_j}(P)
```

for all sufficiently large `j`.

This is the pointed-rack Brunnian ghost.  It is the genuine Sawin
counterexample object.

## Correct fork

Therefore the current prompt has asymmetric impact:

```text
positive answer
    => finite conjugation-rack domination
    => Sawin.

negative finite-group answer
    => finite-group route obstruction,
       but not Sawin failure unless upgraded to pointed-rack invisibility.
```

The most useful next theorem is still the positive one.  The most useful
negative theorem must include an upgrade:

```text
finite-group law ghost
    =>
pointed-rack Brunnian ghost
```

or else construct the pointed-rack ghost directly.

## Practical implication

Computational evidence about growing fan-image groups, such as the rank-4
row-15 image of order `51840`, is relevant only if it produces Brunnian
all-variable words that are eventually laws on every fixed finite group.

Even that would only obstruct the finite-group route.  For a full Sawin
counterexample, the same words must eventually vanish on every fixed finite
pointed rack.

The rank-4 representative probe is recorded in

```text
proofs/nonperm3_rank4_fan_image_representative_probe.md
```

It gives a useful finite pressure point:

```text
rank 4, row 15 hard image order = 51840, exponent = 360.
```

But this is only pressure.  Large order and large exponent do not imply a
diagonal law ghost.  To matter for the prompt, the image must support
all-variable Brunnian words that are laws on every fixed finite group
eventually while remaining nontrivial on the marked row-15 fan tuple.

