# Sequential Primitivity Challenge

Status: answered by GPT-5.5 Pro on 2026-06-04.

Answer summary:

- No proof of active-factor observability, no alternate proof of Sawin YES,
  and no concrete Sawin-negative table was supplied.
- Sequential primitivity alone remains too weak; the next falsifiable finite
  target should also exhibit actual small-rack-prefix pressure.
- The proposed search target is a rigid pressure core: a nonterminal,
  quotient-rigid, subsolution-rigid, observer-rigid, transport-split-rigid
  finite YBE table with `N_{m,n}(X) != 1` for a first small rack prefix.
- This answer is recorded in `proofs/active_factor_observability_boundary.md`
  and made executable by `tools/run_rigid_pressure_core_audit.py`.

Prompt:

```text
Continue in the same chat. Please focus on the exact remaining obstruction, not on previously closed examples.

Problem. For a finite bijective set-theoretic Yang-Baxter solution X, Sawin asks whether there is always a finite rack Y such that

    ker(B_n acting on Y^n) <= ker(B_n acting on X^n)

for every n.

Known positive terminal classes:

1. left- or right-nondegenerate solutions, by the guitar/derived-rack theorem;
2. involutive solutions, by the two-point flip rack;
3. flip-across/twisted unions of already dominated components;
4. explicit affine cyclic hidden-gauge examples, via finite sequential rack gauges.

Known safe certificate. If X admits finitely many total B_n-equivariant sequential active factors

    F^alpha_n:X^n -> T_alpha^n

where every T_alpha is a finite rack or a strictly smaller finite YBE solution already dominated by a rack, together with finite invariant observer channels, and the combined code is injective for all n, then X is rack-dominated.

The unresolved positive lemma is proper active-factor observability: every non-terminal finite X should admit such a proper certificate.

Define sequential primitivity relative to the known terminal classes as follows. X is sequentially primitive if every finite left-to-right equivariant code into:

    finite racks,
    strictly smaller already dominated YBE active factors,
    proper YBE quotient factors,
    invariant observer alphabets

has an all-length collision: for every candidate certificate C, there exist n and distinct words x,y in X^n with C_n(x)=C_n(y).

Sequential primitivity would refute the proper active-factor induction method. It would not by itself refute Sawin.

For a genuine Sawin-negative table, one additionally needs the cofinal rack-prefix obstruction. Enumerate finite racks Y_1,Y_2,... and set

    P_m = Y_1 x ... x Y_m.

For fixed m,n define

    Gamma_{m,n}(X)
      =
    < (rho^{P_m}_n(sigma_i), rho^X_n(sigma_i)) : 1 <= i < n >
    <= Sym(P_m^n) x Sym(X^n)

and

    N_{m,n}(X) = { g_X : (1,g_X) in Gamma_{m,n}(X) }.

Sawin-negative is exactly:

    forall m exists n, N_{m,n}(X) != 1.

Question. Can you now do one of the following?

A. Prove that sequential primitivity cannot occur for finite bijective YBE solutions outside the terminal classes, by constructing a proper active-factor/observer certificate from any such finite table.

B. Give a concrete finite bijective YBE table X that is sequentially primitive relative to the terminal classes. If you cannot prove the cofinal rack-prefix obstruction for it, say explicitly whether it is still rack-dominated by another mechanism.

C. Give a concrete finite bijective YBE table X with the full cofinal rack-prefix obstruction `forall m exists n, N_{m,n}(X)!=1`, thereby refuting Sawin.

D. Prove Sawin YES by another mechanism that bypasses active-factor observability but still produces one finite rack Y independent of n.

The answer should be decisive. A bounded search failure, a finite-width example, or a new certificate theorem without a universal construction does not resolve this. If none of A-D is currently possible, identify the smallest finite-table property that should be searched next and give explicit constraints that would make the search falsifiable.
```
