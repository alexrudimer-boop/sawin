# Readout descent-separation certificate

Date: 2026-05-29

This note follows `proofs/readout_kernel_admissibility.md`.  It does not prove
the Master Local-Minimal Residual Theorem.  It packages the current
descent-separation target into one finite local certificate.

The certificate says: fixed finite readout labels solve the non-strand
continuation problem exactly when their kernel is admissible and kills the
continuation seeds.  In that case the quotient row is strand-continuing, so
the transport-state rackification theorem applies to the remaining lower
motion.

## Setup

Let `pi:X->Z` be a local interval already placed in the rack-side convention,
so base rows have the form

```text
R_Z(a,b) = (a*b, a).
```

For a local row

```text
T_{a,b}(x,y) = (u,v),
```

the non-strand-continuing seed is

```text
x ~ v
```

whenever `v != x`.

Let finite interval-level readout labels be

```text
r_a : A_a -> E_a.
```

Write `Phi^r` for their kernel relation:

```text
x Phi^r_a y  iff  r_a(x)=r_a(y).
```

## Lemma

Assume:

1. every base row is in rack-side form `R_Z(a,b)=(a*b,a)`;
2. `Phi^r` is an admissible local congruence family;
3. every continuation seed satisfies `x Phi^r_a v`.

Then the quotient local row modulo `Phi^r` is strand-continuing:

```text
Tbar_{a,b}([x],[y]) = ([u],[x]).
```

Proof.  Since `Phi^r` is admissible, every local table descends to a bijective
row on equivalence classes:

```text
Tbar_{a,b}([x],[y]) = ([u],[v]).
```

The base row has second output colour `a`, so `x` and `v` lie in the same
fibre `A_a`.  By assumption, the continuation seed is killed by the readout
kernel:

```text
[v]=[x].
```

Therefore

```text
Tbar_{a,b}([x],[y]) = ([u],[x]).
```

The row is strand-continuing.  QED.

## Closure of the quotient residue

Once the quotient row is strand-continuing, the transport-state
rackification note applies.  The remaining lower state set is finite, and the
row has the form

```text
((a,r),(b,s)) |-> ((a*b,F_{a,b,r}(s)),(a,r)).
```

The finite set of transport states becomes a rack under

```text
(a,r) * (b,s) = (a*b,F_{a,b,r}(s)).
```

Its inner group is a fixed finite detector factor, independent of braid index.

## Code certificate

The helper

```text
readout_descent_separation_audit(interval, labels)
```

records:

- the `ReadoutKernelAudit`;
- the continuation congruence audit;
- the seed-propagation audits for the readout kernel;
- the row-level continuation seeds that survive in the quotient.

Its property

```text
proves_descent_separation_readout
```

is true exactly when:

1. the base rows are in rack-side form;
2. the readout kernel is admissible;
3. no continuation seed survives the quotient;
4. the generated seed closures propagate through the readout kernel.

The failure helper

```text
readout_descent_separation_failures(interval, labels)
```

returns the surviving continuation seed rows.

## Updated positive target

The remaining A-route theorem can now be written as a concrete construction
problem.

For every local-minimal interval in the `bi_free_universal_corridor_bottleneck`,
construct fixed interval-level labels from the Green, Schutzenberger, atom,
known-branch, and endpoint/unit detector factors such that

```text
readout_descent_separation_audit(interval, labels)
```

proves descent separation.

Then:

1. the non-strand-continuing part vanishes in the fixed readout quotient;
2. the quotient lower row is strand-continuing;
3. transport-state rackification supplies a fixed finite rack detector for the
   remaining lower gauge;
4. endpoint factorization and product assembly give one fixed group
   `H(pi,Q)`, independent of `n`;
5. the sharp obstruction theorem supplies the local rack `Q x A_H`.

This is not yet outcome A, because the construction of those labels from the
actual Green/Schutzenberger/atom/unit factors is still unproved.

## B-route meaning

A proposed label system can fail this certificate in only explicit finite
ways:

1. its kernel is not admissible;
2. the base row is not in rack-side form, so another side convention or higher
   readout is required;
3. one or more continuation seeds survive the quotient;
4. a seed closure does not propagate because the readout is not admissible or
   misses the seed.

Any such finite failure is only a B seed.  To prove outcome B it must still be
upgraded to a normalized-law sequence invisible to every finite group while
moving a residual tuple.
