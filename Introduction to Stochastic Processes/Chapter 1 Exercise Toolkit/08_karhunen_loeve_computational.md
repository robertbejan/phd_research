# 08 — Karhunen–Loève expansion (computational)

**Covers Exercises 27 and 28.**
Book sections: 1.1 (simulating Gaussian processes via the covariance square root),
1.5 (Theorem 1.4, (1.35), Example 1.7), and the analytic KL results you derived in
Exercises 23–26.

---

## The tools

### T1 — KL sampling (truncated Karhunen–Loève)
For a Gaussian process, the KL expansion is
$$X_t=\sum_{k=1}^\infty \sqrt{\lambda_k}\,\zeta_k\,e_k(t),\qquad
\zeta_k\sim\mathcal N(0,1)\ \text{iid}.$$
Truncate at $K$ terms. The **mean-square truncation error** is exactly the tail of
the spectrum:
$$\mathbb E\Big|\ X_t-\sum_{k=1}^{K}\sqrt{\lambda_k}\zeta_ke_k(t)\ \Big|^2
=\sum_{k>K}\lambda_k .$$
So "how many modes?" is answered by "until the tail sum of $\lambda_k$ is below your
tolerance".

### T2 — The Cholesky (covariance-square-root) sampler
The method you already used in `1_4.py`: build $\Gamma_{ij}=C(t_i,t_j)$, factor
$\Gamma=\Lambda\Lambda^\top$, and set $X=\mu+\Lambda\,\zeta$. Cost is $O(N^3)$ to
factor and it needs the **full** $N\times N$ matrix; the KL sampler needs only $K$
modes ($K\ll N$ often) but requires the eigenpairs.

### T3 — The Nyström method (numerical eigenpairs)
Discretise the integral eigenvalue problem $\int_0^1 R(t,s)e(s)ds=\lambda e(t)$ on a
uniform grid $t_i=i\Delta t$ using the trapezoidal rule. With weights $w_i$ equal to
$\Delta t$ in the interior and $\tfrac12\Delta t$ at the endpoints, solve the
**symmetric** matrix eigenproblem
$$w_i\sum_j R(t_i,t_j)w_j\,u^{(k)}_j=\lambda_k\,u^{(k)}_i .$$
The eigenfunction values are $e_k(t_i)=u^{(k)}_i/\sqrt{w_i}$. For a smooth kernel the
eigenvalues converge at $O(\Delta t^2)$; for a kernel with a corner
(e.g. $\min(t,s)$ or $e^{-a|x-y|}$) expect $O(\Delta t)$.

**Generic skeleton (adapt the kernel):**
```python
import numpy as np
N, L = 400, 0.5
t = np.linspace(0, L, N)
dt = t[1] - t[0]
w = np.full(N, dt); w[0] = w[-1] = dt/2          # trapezoidal weights

def R(x, y):                                      # <- your covariance kernel
    return np.exp(-1.0*np.abs(x - y))             # e.g. Ex.28: a = 1

X, Y = np.meshgrid(t, t, indexing='ij')
A = np.sqrt(w)[:, None] * R(X, Y) * np.sqrt(w)[None, :]   # symmetric
lam, U = np.linalg.eigh(A)                        # ascending eigenvalues
idx = np.argsort(lam)[::-1]                        # largest first
lam, U = lam[idx], U[:, idx]
e = U / np.sqrt(w)[:, None]                        # eigenfunction values e_k(t_i)
```

### T4 — First four moments of a Gaussian field (Ex. 28a)
If $X(x)$ is a mean-zero Gaussian field, then at any fixed $x$, $X(x)\sim\mathcal N(0,\gamma(x,x))$.
For $\gamma(x,x)=1$ the *stationary* moments are mean $0$, variance $1$, and (since
the field is Gaussian) all **odd** central moments vanish while the fourth central
moment equals $3\,(\text{var})^2$. Use these as exact targets for your simulation.

### T5 — Analytic eigenvalues for the exponential kernel (Ex. 28b)
The eigenproblem $\int_{-L}^{L}e^{-a|x-y|}f(y)dy=\lambda f(x)$ reduces (differentiate
**twice** in $x$, as in T2 of file 07) to a second-order ODE with matching/decay
conditions at $x=\pm L$. Reduce it to $f''=-k^2f$, read the boundary conditions off
the *first* derivative of the integral equation, and solve. This gives $\lambda$ and
$f$ in closed form; check against the Nyström numbers from T3.

---

## Warm-ups (solved)

**W1 (truncation error).** The BM spectrum is $\lambda_n=1/((n-\tfrac12)^2\pi^2)$.
Estimate the number of modes $K$ so the mean-square error is below $10^{-3}$.
*Solution.* By T1 you need $\sum_{n>K}\frac{1}{(n-\frac12)^2\pi^2}\lesssim10^{-3}$.
Since $\sum_{n>K}(n-\tfrac12)^{-2}\approx 1/K$, this needs roughly
$K\gtrsim \frac{1}{\pi^2\cdot10^{-3}}\approx100$. (The slow $1/n^2$ decay is why BM
needs *many* modes.)

**W2 (Nyström sanity check).** Discretise $R(t,s)=1$ on $[0,1]$ with $N$ points and
confirm you recover $\lambda_1\approx1$.
*Solution.* The matrix has rank one, largest eigenvalue $\approx\int_0^1 1\,dt=1$;
`eigh` returns it up to $O(\Delta t^2)$.

**W3 (moment targets).** For the field in Ex. 28 with $a=1$, state the exact first
four central moments at a point.
*Solution.* $0,\ 1,\ 0,\ 3$ (Gaussian, variance $\gamma(x,x)=1$).

---

## Game plan

### Exercise 27 (generate BM, bridge, OU from their KL expansions)
- Use the **analytic eigenpairs** you produced in Exercises 23–24 and Example 1.7:
  - BM: $e_n=\sqrt2\sin\!\big((n-\tfrac12)\pi t\big)$, $\lambda_n=[(n-\tfrac12)\pi]^{-2}$.
  - Bridge: $\sqrt2\sin(n\pi t)$, $\lambda_n=(n\pi)^{-2}$.
  - OU on $[0,1]$: obtain via the time change of BM (file 03, T7 / file 07, T5).
- Sample with **T1**: pick $K$, draw $\zeta_k$, sum.
- **Convergence study:** raise $K$ and monitor the empirical statistics *and* the
  theoretical tail sum $\sum_{k>K}\lambda_k$ (T1). Report how many modes give
  accurate mean/variance/covariance.
- **Cost comparison:** count operations for the KL sampler ($N\!\times\!K$ storage,
  cheap evaluation) against the Cholesky sampler (T2: $O(N^3)$ factor, $O(N^2)$
  memory). Discuss when each wins.
- *Guiding questions:* why does the OU expansion converge *faster* than BM? What sets
  the decay rate of $\lambda_k$ (smoothness of the paths)?

### Exercise 28 (exponential covariance field, $\gamma(x,y)=e^{-a|x-y|}$)
- (a) **Simulate** on $[-L,L]$ either by Cholesky (T2) or by KL/Nyström (T1/T3);
  estimate the first four moments over many samples and compare with **T4**.
- (b) **Analytic eigenpairs** via **T5**: reduce the integral equation to an ODE,
  derive the boundary conditions at $x=\pm L$, solve for $(\lambda_k,e_k)$. With
  $a=1,L=0.5$ plot the first five eigenfunctions; investigate the KL accuracy as a
  function of the number of modes (use T1's tail-sum idea).
- (c) **Numerical method:** apply **T3 (Nyström)** to get the first few eigenpairs;
  simulate with them; compare against (b) and comment on eigenvalue/eigenfunction
  accuracy and cost.
- *Guiding questions:* how does the corner of $e^{-a|x-y|}$ at $x=y$ affect the
  convergence rate of the Nyström eigenvalues? Does increasing $a$ (shorter
  correlation length) need more or fewer modes?

---

## Pitfalls

- **Missing the $\sqrt{w}$ (or $\Delta t$) factor.** Without it the matrix eigenvalues
  are $\Delta t$ times the true ones, and eigenfunctions are un-normalised.
- **Trapezoidal endpoint weights.** The first and last weights are $\tfrac12\Delta t$,
  not $\Delta t$.
- **Symmetry.** Build the kernel matrix symmetrically ($R(x_i,x_j)$ vs $R(x_j,x_i)$);
  use `eigh`, not `eig`, so you get real, sorted eigenvalues.
- **Comparing statistics, not paths.** KL and Cholesky give different sample paths for
  the same seed — compare *distributions* (means, covariances, histograms).
- **Tolerance vs $K$.** Because spectra decay algebraically ($1/n^2$ etc.), doubling
  accuracy can cost many modes — check the tail sum, not just the first few $\lambda_k$.

---

## Numerical check (optional)

The `numpy.linalg.eigh` skeleton in T3 *is* the check: run it on the analytic kernels
of Exercises 23–26 and confirm the eigenvalues match your closed forms to $O(\Delta t^2)$
(smooth kernels) or $O(\Delta t)$ (kernels with a corner).

