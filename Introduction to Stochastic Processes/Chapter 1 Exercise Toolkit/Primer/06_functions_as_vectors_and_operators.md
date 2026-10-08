# 06 — Functions as vectors, and operators

**Read this if:** $L^2$, "inner product of two functions", "eigenfunction",
"self-adjoint", "Hilbert–Schmidt" or "Mercer" are unfamiliar. This file unlocks
Exercises 20–28.

## 1. The big idea

Anything you can do with vectors you can do with **functions**, by replacing
- finite sums $\sum_i\ \longrightarrow$ integrals $\int dt$,
- dot products $\sum_i u_iv_i\ \longrightarrow\ \int u(t)v(t)\,dt$.

So **a function is a vector with infinitely many coordinates**, one per time $t$.

## 2. The space $L^2(0,1)$

$$L^2(0,1)=\Big\{f:\ \int_0^1f(t)^2dt<\infty\Big\}.$$
"$f\in L^2$" = "$f$ is **square-integrable**" = "$f$ has finite energy". (A random
variable is "in $L^2$" if $\mathbb EX^2<\infty$.)

**Inner product and norm** (the $\sum\to\int$ translation):
$$\langle f,g\rangle=\int_0^1f(t)\,\overline{g(t)}\,dt,\qquad
\left\|f\right\|^2=\langle f,f\rangle=\int_0^1f(t)^2dt .$$
For real functions $\overline g=g$ and you may drop the bar — but always write it,
because Fourier objects are complex.

**Orthonormal sequence** $\{e_n\}$: $\langle e_n,e_m\rangle=\delta_{nm}$, i.e.
$\int_0^1e_n(t)e_m(t)dt=1$ if $n=m$, $0$ otherwise.

**Expansion.** If $\{e_n\}$ is **complete** (nothing is missing), then
$$f=\sum_n\langle f,e_n\rangle e_n,\qquad
\left\|f\right\|^2=\sum_n\left|\langle f,e_n\rangle\right|^2\ \ (\text{Parseval}).$$
*Example:* the Fourier families of file 07 §2.

> **Normalisation checklist.** Compute $\int_0^1e_n^2$; if it is not $1$, divide by
> its square root. This is pitfall #1 of the whole chapter.

## 3. Operators

An **operator** $T$ sends functions to functions; it is **linear** if
$T(af+bg)=aTf+bTg$. Our operator (Eq. (1.32)) is the **integral operator with
kernel** $R(t,s)$:
$$\boxed{\ (Rf)(t)=\int_0^1R(t,s)f(s)\,ds\ }$$
**In words:** $R$ blends all values $f(s)$ together, weighting $f(s)$ by how
strongly times $t$ and $s$ are correlated. If $R(t,s)=R(s,t)$ (symmetric kernel),
everything stays real.

## 4. Adjoint, self-adjoint, positivity

The **adjoint** $T^*$ is defined by $\langle Tf,g\rangle=\langle f,T^*g\rangle$ for
all $f,g$ — the operator twin of "transpose of a matrix". $T$ is **self-adjoint**
(symmetric) if $T^*=T$. For a kernel operator, swapping the order of a double
integral shows
$$R\ \text{self-adjoint}\iff R(t,s)=R(s,t)\ \text{(symmetric kernel)} .$$
*Read toolkit file 06 §T2 with this definition in hand.*

$T$ is **nonnegative** if $\langle Tf,f\rangle\ge0$ for all $f$ — the operator twin
of PSD (file 05 §6). With $R(t,s)=\mathbb E[X_tX_s]$,
$$\langle Rf,f\rangle=\int\!\!\int R(t,s)f(t)f(s)\,dt\,ds
=\mathbb E\Big(\int_0^1X_tf(t)\,dt\Big)^2\ \ge 0,$$
a variance. **That is Exercise 20.**

## 5. Eigenvalues and eigenfunctions

Exactly as for matrices (file 05 §3), but with functions:
$$Re_n=\lambda_ne_n\quad\iff\quad\boxed{\ \int_0^1R(t,s)e_n(s)\,ds=\lambda_ne_n(t)\ }$$
$\lambda_n$ = **eigenvalue** (a number), $e_n$ = **eigenfunction** (a function).

**Spectral theorem (function version) — the most important fact here.**
> If $R$ is continuous, symmetric and nonnegative on $[0,1]^2$, then
> 1. the $\lambda_n$ are **real and $\ge0$**, decreasing to $0$;
> 2. the $e_n$ can be chosen **orthonormal** in $L^2(0,1)$;
> 3. $\{e_n\}$ is **complete**: any $f\in L^2$ expands in it.

**The orthogonality one-liner** (memorise):
$$\lambda_n\langle e_n,e_m\rangle=\langle Re_n,e_m\rangle=\langle e_n,Re_m\rangle
=\lambda_m\langle e_n,e_m\rangle
\ \Rightarrow\ (\lambda_n-\lambda_m)\langle e_n,e_m\rangle=0 .$$
Same idea as the matrix proof in file 05 §4 — with $\int$ instead of $\sum$.

## 6. Mercer's theorem and the trace identity

Mercer upgrades "expansion of functions" to "expansion of the kernel itself":
$$R(t,s)=\sum_{n}\lambda_ne_n(t)e_n(s),$$
converging absolutely. **Set $t=s$ and integrate** (term by term):
$$\boxed{\ \sum_{n}\lambda_n=\int_0^1R(t,t)\,dt\ }$$
That is the trace identity. Adding $R(t,t)=\mathbb EX_t^2=R(0)$ for a stationary
process on $[0,T]$ turns it into **Exercise 22**.

*Sanity check:* for $R\equiv1$ the only nonzero eigenvalue is $1$ (with $e\equiv1$),
and $\int_0^1R(t,t)dt=1$. ✓

## 7. Compactness, Hilbert–Schmidt, and why eigenvalues are discrete

- An operator is **compact** if it maps bounded sets to "nearly finite-dimensional"
  ones. **An integral operator with a continuous kernel is compact.** The spectral
  theorem above holds for compact self-adjoint operators, and *that* is why the
  eigenvalues form a **discrete** decreasing list $\lambda_1\ge\lambda_2\ge\cdots\to0$
  instead of a continuum — and hence why the Karhunen–Loève expansion is a **sum**.
- $R$ is **Hilbert–Schmidt** if $\sum_n\left\|R\varphi_n\right\|^2<\infty$ for a
  complete orthonormal sequence $\{\varphi_n\}$. For integral operators:
  $$\left\|R\right\|_{HS}^2=\int_0^1\!\!\int_0^1R(t,s)^2\,dt\,ds,$$
  so "kernel $\in L^2([0,1]^2)$" $\iff$ "$R$ is Hilbert–Schmidt". That is Exercise 21.
  A **continuous** kernel on the compact square is bounded, hence in $L^2$ — one line.
- **Parseval sketch** for the HS norm: expand $R\varphi_n$ in the complete sequence
  $\{\varphi_k\}$, use Parseval in $k$, then completeness in $s$ to collapse the double
  sum to $\int R(t,s)^2ds$, then integrate in $t$.

## 8. "Kernel" = "covariance": the dictionary

| Matrix world (file 05) | Function world (here) |
|---|---|
| symmetric matrix | symmetric kernel $R(t,s)=R(s,t)$ |
| covariance matrix $\Sigma$ | covariance function $R(t,s)$ |
| PSD matrix | PSD kernel: $\int\!\!\int R(t,s)f(t)f(s)\ge0$ for all $f$ |
| eigenvectors, $\Sigma=\sum_k\lambda_kq_kq_k^\top$ | eigenfunctions, $R(t,s)=\sum_n\lambda_ne_n(t)e_n(s)$ |
| $\operatorname{tr}\Sigma=\sum_k\lambda_k$ | $\int R(t,t)dt=\sum_n\lambda_n$ |
| Cholesky simulation | Karhunen–Loève simulation |

Exercises 20–28 are simply one column translated into the other. Keep this table.

## 9. Sturm–Liouville in one paragraph

A **Sturm–Liouville problem** is an eigenvalue problem for a *differential*
operator, e.g. $-e''(t)=\mu e(t)$ with **Dirichlet** ($e(0)=e(1)=0$) or **Neumann**
($e'(0)=e'(1)=0$) boundary conditions. Its eigenfunctions are orthogonal, and its
solutions are sines/cosines. **Tactically:** if an integral equation has a piecewise
kernel like $\min(t,s)$, or one of the form $e^{-a\left|t-s\right|}$,
**differentiate it twice** to convert it into a Sturm–Liouville problem, then solve
the ODE (file 08 §4–§5). This is the master move behind toolkit file 07 §T2.

## 10. Micro-drills

1. Normalise $f(t)=t$ on $[0,1]$. *Ans.* $\int_0^1t^2dt=1/3$, so $\hat f=\sqrt3t$.
2. Show $\langle Rf,f\rangle\ge0$ for $R(t,s)=1$. *Ans.*
   $\langle Rf,f\rangle=\left(\int_0^1f\right)^2\ge0$.
3. For $R(t,s)=\min(t,s)$ on $[0,1]$, compute $\sum_n\lambda_n$. *Ans.*
   $\int_0^1t\,dt=\tfrac12$ — the value found in toolkit file 06's numerical check.
4. Why must $\lambda_n\to0$? *Ans.* The kernel is compact, so its spectrum is a
   sequence tending to $0$.
