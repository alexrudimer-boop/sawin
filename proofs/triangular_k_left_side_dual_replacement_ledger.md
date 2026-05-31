# Triangular K-left side-dual replacement ledger

Date: 2026-05-31

This note refines the side-dual part of K-left.  It does not prove
`[Resolution: A]` or construct `[Resolution: B]`.  It replaces the coarse
phrases

```text
side_dual_right_triangular_nonlatin
no_side_dual_right_latin_replacement
```

by a finite replacement ledger.

## Executable object

For each missing left Latin colour pair, the post-linear finite-system audit
now reports:

```text
k_left_side_dual_replacement_rows
```

Each row has the form:

```text
((a,b), status, right_defects, right_missing_profiles)
```

with `status` one of:

```text
side_dual_right_latin_available
side_dual_right_triangular_nonlatin
no_side_dual_right_triangular_replacement
```

The `right_defects` field is the right-side Latin defect ledger for the same
colour pair.  The `right_missing_profiles` field is the missing-triangular
profile when no right triangular replacement exists.

## Consequence

[Proved relative to the recorded ledgers] A K-left side-dual failure is not a
new kind of row.  It is one of the already audited right-side finite systems:

```text
1. right Latin is available:
   closed by side-opposite YBE consistency and right-rack diagonal
   cancellation;

2. right triangular but non-Latin:
   apply the same structural, kernel-closure, and recovery-routing ledgers to
   the right-side non-Latin row;

3. no right triangular replacement:
   apply the missing-triangular row profile to the right side.
```

Thus the side-dual replacement problem has no separate algebraic content
after these ledgers.  It is a pointer to a right-side instance of the same
finite row systems, or to System U when the right-side kernel route is
triangular recovery.

The post-linear wrapper now enforces this bookkeeping point in the active
ledger.  The labels

```text
side_dual_right_triangular_nonlatin
no_side_dual_right_latin_replacement
```

are recorded in `missing_left_latin_row_defects` and in
`k_left_side_dual_replacement_rows`, but they are not included in
`live_k_missing_latin_row_defects`.  A right triangular non-Latin replacement
is live only through its right-side active defect rows; a missing right
triangular replacement is live only through the right-side missing-row
profile.  The left ledger therefore no longer double-counts side-dual
pointers as independent K defects.

## Remaining pressure

This note does not close System U and does not prove that every missing
right-side profile is impossible.  It only prevents K-left from hiding behind
an unspecified "no side-dual replacement" phrase.  Any remaining row must now
name the right-side defect or profile explicitly.
