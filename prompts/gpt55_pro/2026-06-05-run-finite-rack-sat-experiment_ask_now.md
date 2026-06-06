# Run the finite rack SAT detector program to closure

We are no longer asking for an audit of Target A. Treat the finite rack
detector route as an implementation-and-proof task.

## Current state

The associated-group separability theorem is false. The obstruction is
\(\eta_R(u\triangleright u)=\eta_R(u)\), and the two-element constant-action
rack

\[
X=\{0,1\},\qquad r(i,j)=(1-j,i)
\]

already separates endpoint generators by a finite rack detector while every
associated-group detector collapses them.

So the only acceptable Route A detector is rack-valued, not group-valued.

For a finite quotient \(M\) of \(L_X\), the contextual endpoint rack
\(C_M(X)\) has generators \([p,x,s]\), and for
\(r(x,y)=(x',y')\) the defining detector relations are:

\[
[p,x,\bar y s]=[p\bar{x'},y',s],
\]

\[
[p,x,\bar y s]\triangleright[p\bar x,y,s]=[p,x',\bar{y'}s].
\]

A finite detector certificate is a finite rack table \(Q\), an assignment
\(\alpha:M\times X\times M\to Q\), and an endpoint inequality
\(\alpha(e)\ne\alpha(e')\).

## Task

Close as much of the finite program as possible. Do not return another
philosophical audit unless it contains a theorem, counterexample, or exact
algorithmic certificate.

1. Give a fully specified bounded experiment for \(|X|\le 2\), arity
   \(n\le 5\), \(|M|\le 4\), and \(|Q|\le 4\), with no hidden heuristics.
2. State exactly what output would constitute a machine-checkable theorem and
   what output would constitute a genuine obstruction candidate.
3. If you can prove that the \(|X|=2\) case has no unbounded bad triples, do it.
   If not, identify the precise missing lemma and give a finite counterexample
   search designed to attack that lemma directly.
4. Strengthen the detector core where possible: add sound saturation rules,
   exact \(q=2\) parity tests, canonical rack-table enumeration, or a proof
   that a smaller search bound suffices.
5. If a residual-collapse candidate appears, specify the finite certificate
   that would distinguish "bounded no detector" from true residual collapse.

Required output:

- A concrete theorem/counterexample/search result, not merely a restatement.
- If the theorem is conditional, isolate the condition in a form we can
  implement or falsify.
- If the answer is computational, include verifier-level certificate fields.
