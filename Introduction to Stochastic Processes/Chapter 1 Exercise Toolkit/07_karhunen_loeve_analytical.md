# 07 — Karhunen–Loève expansion (analytical)

**Covers Exercises 23, 24, 25, 26.**
Book sections: 1.5 (Theorem 1.4, the eigenvalue problem (1.32), Example 1.7 for
Brownian motion, eqs. (1.30)–(1.36)).

> **Prerequisites** (read these first if the maths is new):
> `Primer/06_functions_as_vectors_and_operators.md` §5–§9 — eigenfunctions, the
> spectral theorem, Mercer, and Sturm–Liouville;
> `Primer/08_odes_and_green_functions.md` §4–§5 — boundary value problems (Dirichlet
> vs Neumann), why boundary conditions quantise the eigenvalues, and how to convert
> an integral equation into an ODE by differentiating twice;
> `Primer/07_fourier_primer.md` §2 — sine vs cosine bases and the $\sqrt2$
> normalisation;
> `Primer/05_linear_algebra_primer.md` §3–§4 — the 2×2 eigenproblems you need for the
> rank-one/degenerate kernels.
> Techniques 8 and 9 of `Primer/11_recurring_techniques.md`.

---

## The tools

### T1 — What you are computing
For a mean-zero $L^2$ process on $[0,1]$ with continuous covariance $R(t,s)$, the
**KL expansion** is
$$X_t=\sum_{n=1}^\infty \xi_n\,e_n(t),\qquad
\xi_n=\int_0^1 X_t\,e_n(t)\,dt,\qquad \mathbb E[\xi_n\xi_m]=\lambda_n\delta_{nm},$$
where $\lambda_n,e_n$ solve the **integral eigenvalue problem** (1.32):
$$\boxed{\ \int_0^1 R(t,s)\,e_n(s)\,ds=\lambda_n\,e_n(t)\ }$$
with $\{e_n\}$ orthonormal in $L^2(0,1)$. For **Gaussian** processes,
$\xi_k=\sqrt{\lambda_k}\,\zeta_k$ with $\zeta_k\sim\mathcal N(0,1)$ iid, giving
$X_t=\sum_k\sqrt{\lambda_k}\,\zeta_k\,e_k(t)$ (1.35).

### T2 — The Sturm–Liouville reduction (Example 1.7 is the template)
When $R(t,s)=\min(t,s)$ the integral equation reduces to the ODE
$$-\psi_n(t)=\lambda_n\,\psi_n''(t),\qquad \psi_n(0)=\psi_n'(1)=0,$$
whose eigenvalues/eigenfunctions give $W_t=\sqrt2\sum_n \xi_n\,\frac{1}{(n-\frac12)\pi}
\sin\!\big((n-\tfrac12)\pi t\big)$. The recipe:
1. write the integral equation,
2. **differentiate once/twice** to kill the $\min$/piecewise kernel,
3. read off **boundary conditions**,
4. solve the ODE and **normalise**.

### T3 — Degenerate (finite-rank) kernels
If $R(t,s)=\sum_{i=1}^r f_i(t)g_i(s)$, the operator has **at most $r$ nonzero
eigenvalues**. Write $e(t)=\sum_{i=1}^r c_i f_i(t)$, plug into T1 and obtain an
$r\times r$ linear system for $c_i$ and $\lambda$. Orthogonalise any degenerate
eigenfunctions afterwards.

### T4 — The two cheap special cases
- **Rank one:** $R(t,s)=f(t)f(s)$ (with $f\not\equiv0$) has **one** nonzero
  eigenvalue, and $e(t)\propto f(t)$ — just normalise and read off $\lambda$.
- **Trigonometric rank two:** using $\cos(a-b)=\cos a\cos b+\sin a\sin b$,
  $$R(s,t)=\cos(2\pi(t-s))=\cos2\pi t\cos2\pi s+\sin2\pi t\sin2\pi s,$$
  a sum of two rank-one pieces — apply T3 with $r=2$.

### T5 — Weighted $L^2$ space for a transformed process (Exercise 25)
For $Y(t)=f(t)X_{\tau(t)}$ on $[0,S]$, the "correct" inner product is a **weighted**
one (weight built from $f$ and the change of variables $\tau$). Transform the
eigenvalue problem for $X$ into one for $Y$: substitute $s=\tau(u)$ and multiply by
$f$ so the kernel of $Y$ appears. The eigenfunctions of $Y$ are $f(t)\,e_k(\tau(t))$,
orthogonal **in the weighted space**. For the **OU** process, first write it as a
time change of BM (Lemma 1.6) and reuse the BM eigenfunctions.

### T6 — Everything you need about orthonormality
Check $\int_0^1 e_n(t)^2dt=1$ *before* you quote eigenvalues; a missing normalisation
factor is the single most common error.

---

## Warm-ups (solved)

**W1 (rank one, analogue of Ex. 26).** KL for $R(t,s)=1$ on $[0,1]$.
*Solution.* By T4, $R(t,s)=f(t)f(s)$ with $f\equiv1$. Then $e(t)\propto1$; normalise
$\int_0^1 e^2=1\Rightarrow e\equiv1$; $\lambda=\int_0^1 R(t,s)\cdot1\,ds=1$.
All other eigenvalues vanish; $X_t=\xi_1$ is constant in $t$ — exactly Example 1.2.

**W2 (rank two, analogue of Ex. 26).** KL for $R(t,s)=f(t)f(s)+g(t)g(s)$ with
$f,g$ orthonormal.
*Solution.* By T3 with $r=2$ and orthonormal $f,g$: the $2\times2$ matrix is the
identity, so $\lambda_1=\lambda_2=1$ with eigenfunctions $f,g$ (any ON basis of
$\mathrm{span}\{f,g\}$ works).

**W3 (checking a candidate).** Verify $e(t)=\sqrt2\sin(\pi t)$ solves the Brownian
bridge problem by evaluating $\int_0^1(\min(t,s)-ts)\sqrt2\sin(\pi s)ds$.
*Solution.* Split at $s=t$, integrate by parts; the result is
$\frac{1}{\pi^2}\sqrt2\sin(\pi t)$, i.e. eigenvalue $1/\pi^2$. (This confirms the
first bridge mode; do the same for $n=2,3,\dots$ to find the pattern.)

---

## Game plan

### Exercise 23 — $R(t,s)=ts$
- Recognise a **rank-one** kernel: $R(t,s)=t\cdot s=f(t)f(s)$ with $f(t)=t$. Use T4.
- Set up T1's equation: $\int_0^1 ts\,e(s)ds=\lambda e(t)$. The left side is
  $\big(\int_0^1 s\,e(s)ds\big)\,t$, a *constant times $t$*, so $e(t)\propto t$.
- Normalise $e$ and plug back to read off $\lambda$. (There is exactly one nonzero
  eigenvalue.)
- *Guiding question:* what does a rank-one covariance say about the process
  ($X_t$ proportional to a single random variable times a deterministic shape)?

### Exercise 24 — Brownian bridge, $R(t,s)=\min(t,s)-ts$
- Kernel is $\min(t,s)$ **minus** a rank-one part. Use **T2**: differentiate the
  integral equation twice to remove the $\min$, get a second-order ODE.
- **Boundary conditions:** $e(0)=0$ and $e(1)=0$ (pinned bridge) — derive them, don't
  assume.
- Solve; normalise. Compare the eigenvalue scale with Example 1.7 (the bridge modes
  are sines with *both* ends zero; the BM modes have $e'(1)=0$).
- *Guiding question:* how do the two boundary conditions encode "fixed at both ends"?

### Exercise 25 — transformed process $Y(t)=f(t)X_{\tau(t)}$
- Write down the covariance of $Y$:
  $R_Y(t,u)=f(t)f(u)\,R_X(\tau(t),\tau(u))$.
- Set up the eigenvalue problem in the **weighted** $L^2$ space of **T5**; transform
  $s=\tau(u)$; factor an $f(t)$.
- Conclude the eigenfunctions of $Y$ are $f(t)e_k(\tau(t))$ with the $X$-eigenvalues
  $\lambda_k$; orthonormalise in the weighted space.
- Apply to the **OU** process via the time change $V_t=e^{-t}W(e^{2t})$.
- *Guiding question:* what is the weight function, and why does the ordinary $L^2$
  inner product fail here?

### Exercise 26 — $R(s,t)=\cos(2\pi(t-s))$
- Use the trig identity (T4) to write $R$ as a sum of two rank-one terms
  $f(t)f(s)+g(t)g(s)$ with $f=\cos2\pi t$, $g=\sin2\pi t$.
- Note $\{f,g\}$ are **already orthogonal** but **not normalised** on $[0,1]$;
  compute $\int_0^1\cos^2=1/2$ etc. to see both eigenvalues are $1/2$ (T3), and the
  normalised eigenfunctions are $\sqrt2\cos2\pi t$, $\sqrt2\sin2\pi t$.
- *Guiding question:* is the process Gaussian? If so, write the KL expansion with
  iid $\mathcal N(0,1)$ coefficients.

---

## Pitfalls

- **Normalisation.** Divide by $\int_0^1 e_n^2$; the bridge/BM modes carry an extra
  $\sqrt2$.
- **Boundary conditions** in the S–L reduction must be *derived* (e.g. setting $t=0$
  or $t=1$ in the differentiated equation), not guessed.
- **Degenerate kernels have infinitely many zero eigenvalues.** List only the
  nonzero ones; the process lives in a finite-dimensional (random) subspace.
- **Weighted inner product** in Ex. 25 is mandatory; using plain $L^2$ gives the
  wrong orthogonality.

---

## Numerical check (optional)

Discretise any kernel on a grid, form the $N\times N$ matrix
$M_{ij}=\Delta t\,R(t_i,t_j)$, and call `numpy.linalg.eigh`. The top eigenvalues and
eigenvectors should match your analytic $(\lambda_n,e_n)$ up to the grid resolution.

