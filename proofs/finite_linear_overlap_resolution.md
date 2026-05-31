# Finite-linear overlap resolution

Date: 2026-05-31

This note closes the finite-linear overlap obstruction from the continuation
prompt.  The argument is purely symbolic: it uses only the seven block
Yang-Baxter identities and does not use finite search, semisimplicity, finite
order, or the auxiliary overlap inclusion `im S <= U`.

## Setup

Let

```text
R = [ A  B ]
    [ C  D ]
```

be an invertible block-linear Yang-Baxter gate.  The block equations are:

```text
(1) A^2 + BAC = A
(2) AB + BAD = BA
(3) CA + DAC = AC
(4) CB + DAD = ADA + BC
(5) DB = ADB + BD
(6) CD = CDA + DC
(7) D  = CDB + D^2
```

Define the middle overlap defect

```text
S = CB + (DA - A + I)(D - I).
```

Equivalently,

```text
S = CB + DAD - AD - DA + A + D - I.                  (8)
```

Using `(4)`, also

```text
S = ADA + BC - AD - DA + A + D - I.                  (9)
```

The system is invariant under the side-opposition

```text
A <-> D,   B <-> C.
```

Expression `(9)` is fixed by that opposition, modulo `(4)`.

## The defect is forced into an invariant summand

[Proved] For every block solution of `(1)`-`(7)`,

```text
AS = SA = DS = SD = 0,
BS = SB,
CS = SC.
```

Proof.

First compute `AS` using `(9)`:

```text
AS = A^2DA + ABC - A^2D - ADA + A^2 + AD - A.
```

By `(1)`, `A^2 = A - BAC`, hence

```text
AS = -BACDA + ABC + BACD - BAC.
```

By `(2)` multiplied on the right by `C`,

```text
ABC = BAC - BADC,
```

so

```text
AS = -BACDA - BADC + BACD.
```

By `(6)`, `CDA = CD - DC`, and therefore

```text
BACDA = BACD - BADC.
```

Substitution gives `AS = 0`.

Next compute `SD` using `(8)`:

```text
SD = CBD + DAD^2 - AD^2 - DAD + AD + D^2 - D.
```

By `(7)`, `D^2 = D - CDB`, hence

```text
SD = CBD - DACDB + ACDB - CDB.
```

By `(3)` multiplied on the right by `DB`,

```text
ACDB = CADB + DACDB,
```

so

```text
SD = CBD + CADB - CDB.
```

By `(5)` multiplied on the left by `C`,

```text
CDB = CADB + CBD,
```

and therefore `SD = 0`.

Applying the side-opposition `A <-> D, B <-> C` to `AS = 0` gives `DS = 0`,
and applying it to `SD = 0` gives `SA = 0`.

It remains to show that `B` and `C` preserve `im S`.  Using `(8)`,

```text
BS - SB =
  BCB - CB^2 + BDAD - DADB - BAD + ADB
  + BD - DB - BDA + DAB + BA - AB.
```

By `(2)`, `BA - AB = BAD`, so the terms `-BAD + BA - AB` cancel.  By `(5)`,
`DB = ADB + BD`, so the terms `ADB + BD - DB` cancel.  Thus

```text
BS - SB = BCB - CB^2 + BDAD - DADB - BDA + DAB.
```

Multiplying `(4)` on the right by `B` gives

```text
CB^2 + DADB = ADAB + BCB,
```

hence

```text
BS - SB = BDAD - ADAB - BDA + DAB.
```

Use `(2)` inside the middle term:

```text
ADAB = AD(AB) = AD(BA - BAD) = ADBA - ADBAD.
```

Therefore

```text
BS - SB = BDAD - ADBA + ADBAD - BDA + DAB.
```

Multiplying `(5)` on the right by `A` gives

```text
DBA = ADBA + BDA,
```

so

```text
BS - SB = BDAD + ADBAD + DAB - DBA.
```

Multiplying `(5)` on the right by `AD` gives

```text
DBAD = ADBAD + BDAD,
```

hence

```text
BS - SB = DBAD + DAB - DBA
        = D(BAD + AB - BA)
        = 0
```

by `(2)`.  Thus `BS = SB`.

Applying the side-opposition gives `CS = SC`.  This proves the lemma.  QED.

## Consequence for irreducible two-sided-degenerate candidates

[Proved] There is no finite-linear overlap obstruction satisfying the listed
requirements with `B,C` singular, `V` irreducible under `<A,B,C,D>`, and
`S != 0`.

Proof.  The identities above show:

```text
A(im S) = 0,
D(im S) = 0,
B(im S) = im(BS) = im(SB) <= im S,
C(im S) = im(CS) = im(SC) <= im S.
```

Thus `im S` is a common invariant subspace for `A,B,C,D`.  If `S != 0`,
then `im S` is nonzero.  Irreducibility forces

```text
im S = V.
```

Since `S` is then surjective, `AS = 0` and `DS = 0` force

```text
A = 0,
D = 0.
```

The block matrix becomes

```text
R = [ 0  B ]
    [ C  0 ].
```

Such an anti-diagonal block matrix is invertible only if both `B` and `C`
are invertible: from

```text
R(x,y) = (By, Cx),
```

injectivity of `R` forces injectivity of both `B` and `C`, and in finite
dimension injectivity is invertibility.  This contradicts the required
singularity of both `B` and `C`.

Therefore no data

```text
(F,V,A,B,C,D)
```

can satisfy the finite-linear obstruction with `S != 0`, regardless of
semisimplicity, nilpotence, the overlap space `U`, or braid-survival
requirements.  QED.

## Branch verdict

[Proved] The semisimple finite-order finite-linear overlap obstruction cannot
exist.

[Proved] The higher-nilpotent finite-linear overlap obstruction cannot exist
in the stated primitive irreducible form.

[Proved] The entire finite-linear overlap branch is A-controlled vacuously:
there is no finite-linear primitive overlap gate with `S != 0`, `B,C`
singular, and irreducible `V`.  Consequently no finite-linear overlap data can
produce the requested B-side braid survival.
