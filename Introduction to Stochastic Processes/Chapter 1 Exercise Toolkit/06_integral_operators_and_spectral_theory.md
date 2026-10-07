# 06 — Integral operators & spectral theory

**Covers Exercises 20, 21, 22.**
Book sections: 1.5 (operator $R$ in (1.32), self-adjointness/nonnegativity,
Mercer's theorem, (1.30)/(1.32)/(1.35)).

---

## The tools

### T1 — The operator and the inner product
$$\langle f,g\rangle=\int_0^1 f(t)\overline{g(t)}\,dt,\qquad
(Rf)(t)=\int_0^1 R(t,s)f(s)\,ds .$$
For a real symmetric kernel ($R(t,s)=R(s,t)$) everything is real.

### T2 — Self-adjointness
$R$ is **self-adjoint** iff $\langle Rf,h\rangle=\langle f,Rh\rangle$ for all
$f,h$. Compute:
$$\langle Rf,h\rangle=\int_0^1\!\!\int_0^1 R(t,s)f(s)\overline{h(t)}\,ds\,dt
\ \stackrel{\text{swap}}{=}\ \int_0^1\!\!\int_0^1 f(s)\overline{R(t,s)h(t)}\,dt\,ds,$$
and identify the last expression with $\langle f,Rh\rangle$ using $R(t,s)=R(s,t)$.
**Symmetric kernel $\iff$ self-adjoint operator.**

### T3 — Nonnegativity
$R$ is **nonnegative** iff $\langle Rf,f\rangle\ge0$ for all $f$. The slick route:
$$\langle Rf,f\rangle=\int_0^1\!\!\int_0^1 R(t,s)f(t)f(s)\,dt\,ds
=\mathbb E\Big(\int_0^1 X_tf(t)\,dt\Big)^2\ \ge0,$$
using $R(t,s)=\mathbb E[X_tX_s]$ and Fubini.

### T4 — Consequence for the spectrum
Self-adjoint $\Rightarrow$ all eigenvalues **real**; nonnegative $\Rightarrow$ all
eigenvalues **$\ge0$**. Eigenfunctions of a self-adjoint operator belonging to
**distinct** eigenvalues are **orthogonal**: take
$\lambda_n\langle e_n,e_m\rangle=\langle Re_n,e_m\rangle=\langle e_n,Re_m\rangle
=\lambda_m\langle e_n,e_m\rangle$, so $(\lambda_n-\lambda_m)\langle e_n,e_m\rangle=0$.

### T5 — Hilbert–Schmidt (the given definition)
$R:H\to H$ is **Hilbert–Schmidt** if for a complete orthonormal sequence
$\{\varphi_n\}$,
$$\sum_{n=1}^\infty\|R\varphi_n\|^2<\infty .$$
Two facts you need:
1. **Kernel in $L^2$:** an integral operator with kernel $R(t,s)\in L^2([0,1]^2)$ is
   Hilbert–Schmidt, and its HS norm is
   $\|R\|_{HS}^2=\int_0^1\!\!\int_0^1 |R(t,s)|^2\,dt\,ds$.
2. **Continuous kernel $\Rightarrow$ $L^2$ kernel** (continuous on the compact square
   $\Rightarrow$ bounded), so Ex. 21 is a corollary of fact 1.

*Proof sketch of fact 1 (Parseval):* expand $\int_0^1R(t,s)\varphi_n(s)ds$ in the
complete sequence $\{\varphi_k\}$ (Parseval in $k$), then use completeness in $s$ to
collapse the double sum to $\int_0^1 R(t,s)^2ds$; finally integrate in $t$.

### T6 — Trace identity (Exercise 22)
For a Hilbert–Schmidt self-adjoint operator with continuous kernel, Mercer's theorem
gives $R(t,s)=\sum_n\lambda_ne_n(t)e_n(s)$ (absolutely, uniformly). Evaluating at
$t=s$ and integrating,
$$\sum_{n=1}^\infty\lambda_n=\int_0^1 R(t,t)\,dt .$$
For a **stationary** process on $[0,T]$, $R(t,t)=\mathbb E X_t^2=R(0)$ for every $t$,
so the right side is $T\,R(0)$ — which is Exercise 22.

---

## Warm-ups (solved)

**W1 (self-adjointness, analogue of Ex. 20).**
Show the operator with $\min(t,s)$ is self-adjoint.
*Solution.* The kernel is symmetric, $R(t,s)=\min(t,s)=\min(s,t)=R(s,t)$; apply T2.

**W2 (HS norm of a rank-one kernel, analogue of Ex. 21).**
For $R(t,s)=f(t)f(s)$ with $f\in L^2(0,1)$, compute the HS norm.
*Solution.* $\|R\|_{HS}^2=\int_0^1\int_0^1 f(t)^2f(s)^2\,dt\,ds=\big(\int_0^1f^2\big)^2$, finite.

**W3 (trace sanity check, analogue of Ex. 22).**
For $R(t,s)\equiv1$ on $[0,1]$ verify $\sum\lambda_n=\int_0^1R(t,t)dt$.
*Solution.* $R(t,t)=1$ gives $\int_0^1 1\,dt=1$. Indeed the only nonzero eigenvalue is
$\lambda=1$ (eigenfunction $e\equiv1$), and $\sum\lambda_n=1$. ✓

---

## Game plan

### Exercise 20
- Hypothesis: $X_t$ satisfies (1.28) — mean zero, $\mathbb E X_t^2<\infty$,
  $L^2$-continuous — so $R(t,s)=\mathbb E[X_tX_s]$ is symmetric.
- **Self-adjoint:** T2.
- **Nonnegative:** T3 (write $\langle Rf,f\rangle$ as a squared expectation).
- **Real, nonnegative eigenvalues:** cite T4.
- **Orthogonal eigenfunctions:** the one-line argument in T4.
- *Guiding question:* do you need the process to be *stationary* for any of this, or
  only $L^2$ with a continuous covariance?

### Exercise 21
- The kernel $R(t,s)$ is **continuous on the compact square** $[0,1]^2$, hence
  $\int_0^1\int_0^1 R^2<\infty$, i.e. $R\in L^2([0,1]^2)$.
- Apply **T5** fact 1 (with the Parseval sketch) to conclude $\sum_n\|R\varphi_n\|^2<\infty$.
- *Guiding question:* where exactly does continuity of $R$ enter, and why is a merely
  $L^2$ kernel *not* enough for a continuous eigenbasis?

### Exercise 22
- $X_t$ is second-order stationary on $[0,T]$, mean zero. So
  $R(t,t)=\mathbb E X_t^2$ is constant and equals $R(0)$.
- Use **T6 (Mercer)**: $\sum_n\lambda_n=\int_0^T R(t,t)dt=\int_0^T R(0)\,dt=T R(0)$.
- *Guiding questions:* which hypotheses (continuous covariance, self-adjointness)
  justify Mercer? Why is $R(0)$ the total variance?

---

## Pitfalls

- **Inner product conjugation.** For real kernels it is invisible, but write $\overline{g}$
  to keep the definition honest.
- **Nonnegative $\ne$ positive.** Some eigenvalues can be $0$ (e.g. constant kernel).
- **Completeness matters in T5.** $\sum_n\|R\varphi_n\|^2$ must use a *complete*
  orthonormal sequence; the value is the same for every such sequence (that is part
  of what you are proving).
- **Trace needs Mercer**, i.e. a continuous kernel — don't quote it for a merely
  $L^2$ kernel.

---

## Numerical check (optional)

Discretise $R(t,s)=\min(t,s)$ on a grid and use `numpy.linalg.eigh`. The eigenvalues
should match the analytic $\lambda_n=1/((n-\tfrac12)^2\pi^2)$ and their sum should
approach $\int_0^1 t\,dt=\tfrac12$ (the trace of $\min(t,s)$). This is a perfect
dress rehearsal for Exercises 23–28.

