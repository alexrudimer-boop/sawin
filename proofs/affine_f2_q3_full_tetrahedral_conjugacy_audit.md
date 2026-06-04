# Affine F2^3 Full Tetrahedral Conjugacy Audit

The explicit maps P_n and R_n identify the shifted affine X action with the tetrahedral rack action plus n fixed observer bits in every checked arity.  The formulas are local-recursive in n, so the accompanying proof records the all-arity argument: Phi_n=(P_n,R_n) is bijective and B_n-equivariant from X^n to Y^n x F_2^n, with B_n acting trivially on the second factor.  Consequently the braid kernels of this X and the tetrahedral rack Y are equal in every arity.

## Maps

Work in shifted `X` coordinates `x_i=(a_i,b_i,c_i)`.  Let

```text
C_0=[[1,0],[1,1]], C_1=[[1,1],[0,1]], C_2=[[0,1],[1,0]].
```

Define `P_n:X^n -> Y^n` recursively by

```text
z_1 = C_n(a_1,c_1)
p_i = a_i+b_i+a_{i+1}
q_i = c_i+c_{i+1}
z_{i+1} = z_i + C_{n-i}(p_i,q_i).
```

Define invariant observer bits

```text
S_{i-1}=sum_{j<i}(a_j+c_j)
r_i=S_{i-1}+a_i+b_i.
```

Set `Phi_n=(P_n,R_n):X^n -> Y^n x F_2^n`.

## Checked Rows

| n | rank Phi | bijective | P equivariant | R invariant | conjugates generators |
|---|---:|---|---|---|---|
| 1 | 3 | True | True | True | True |
| 2 | 6 | True | True | True | True |
| 3 | 9 | True | True | True | True |
| 4 | 12 | True | True | True | True |
| 5 | 15 | True | True | True | True |
| 6 | 18 | True | True | True | True |
| 7 | 21 | True | True | True | True |
| 8 | 24 | True | True | True | True |
| 9 | 27 | True | True | True | True |
| 10 | 30 | True | True | True | True |
| 11 | 33 | True | True | True | True |
| 12 | 36 | True | True | True | True |
| 13 | 39 | True | True | True | True |
| 14 | 42 | True | True | True | True |
| 15 | 45 | True | True | True | True |
| 16 | 48 | True | True | True | True |
| 17 | 51 | True | True | True | True |
| 18 | 54 | True | True | True | True |
| 19 | 57 | True | True | True | True |
| 20 | 60 | True | True | True | True |
| 21 | 63 | True | True | True | True |
| 22 | 66 | True | True | True | True |
| 23 | 69 | True | True | True | True |
| 24 | 72 | True | True | True | True |
| 25 | 75 | True | True | True | True |
| 26 | 78 | True | True | True | True |
| 27 | 81 | True | True | True | True |
| 28 | 84 | True | True | True | True |
| 29 | 87 | True | True | True | True |
| 30 | 90 | True | True | True | True |

## Proof Skeleton

The generator check is local.  For a crossing at positions `i,i+1`, only `z_i,z_{i+1}` and the adjacent recurrence equations involving `i-1,i,i+1,i+2` change.  Substituting the shifted `X` local block and using `T C_r=C_{r+1}` and `(I+T)C_r=C_{r-1}` gives

```text
P_n rho^X_n(sigma_i) = rho^Y_n(sigma_i) P_n.
```

The same substitution shows each `r_i` is invariant.  Finally, `Phi_n` is inverted recursively: recover `z_i+z_{i+1}`, hence `p_i,q_i`; recover `(a_1,c_1)` from `z_1`; then recover `b_i`, `a_{i+1}`, and `c_{i+1}` successively from `r_i,p_i,q_i`.  Thus `Phi_n` is bijective for all `n`.

Therefore

```text
Phi_n rho^X_n(beta) = (rho^Y_n(beta) x id) Phi_n
```

for every braid `beta`, and

```text
ker rho^X_n = ker rho^Y_n
```

for every arity `n`.
