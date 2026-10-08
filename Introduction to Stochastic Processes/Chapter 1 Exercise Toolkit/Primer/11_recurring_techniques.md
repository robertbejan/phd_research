# 11 — The recurring techniques

**Read this after** files 01–10. These are the dozen moves that solve most of the
28 exercises. Each is stated as a *procedure* you can follow mechanically.

## Technique 1 — The "$\min$ split"

Whenever a double integral or double sum contains $\min(s,t)$, **assume an order**
(e.g. $s\le t$) and split the integration region at $s=t$. Then restore the general
case using symmetry.

*Template.* $\displaystyle I(t)=\int_0^t\!\!\int_0^t\min(u,v)\,du\,dv$.
Assume $u\le v$; the region is a triangle; by symmetry
$$I(t)=2\int_0^t\!\!\int_0^v u\,du\,dv=2\int_0^t\frac{v^2}{2}dv=\frac{t^3}{3}.$$
*Used in:* Exercises 5c, 6, 8, 13, 14.

## Technique 2 — Fubini for expectations

$$\mathbb E\int\!\!\int F=\int\!\!\int\mathbb E F .$$
"We may swap expectation and integration because the integrand is integrable."
Always *say* it; it is never the interesting part but examiners look for it.
*Used everywhere there is a double integral of covariances: Exercises 8, 13, 14, 16.*

## Technique 3 — "Riemann sums of Gaussians are Gaussian"

If $X$ is a Gaussian process and $Y_t=\int_0^tf(s)X_sds$ (or a limit of linear
combinations $\sum_ic_iX_{t_i}$), then $Y$ is Gaussian. Because a Gaussian vector is
determined by its mean and covariance (file 04 §5), you only ever need to compute
those two things. *This retires Exercises 8, 13 and much of 6.*

## Technique 4 — Prove equality in law by matching mean and covariance

For two **centred Gaussian** processes:
$$X\overset{\text{law}}{=}Y\quad\iff\quad
\mathbb E[X_sX_t]=\mathbb E[Y_sY_t]\ \text{for all }s,t .$$
Procedure: (i) show both are Gaussian with mean $0$; (ii) compute both covariances;
(iii) compare. *Used in:* Exercises 6b, 11, 17. For **non-Gaussian** processes this
fails — there you must compare whole FDDs (Exercises 1, 2).

## Technique 5 — The double-integral reduction

For a **stationary** process and $X(t)=\int_0^tY$:
$$\mathbb E X(t)^2=\int_0^t\!\!\int_0^tC(u-v)\,du\,dv
=\int_{-t}^{t}(t-\left|h\right|)C(h)\,dh
=2\int_0^t(t-u)C(u)\,du .$$
The $=$ step is a change of variables $h=u-v$ and a picture of the square: for each
lag $h$, the number of pairs $(u,v)$ with $u-v=h$ is $t-\left|h\right|$.
*Used in:* Exercises 7b, 16b. Then $t\to\infty$ gives $\approx2Dt$ with $D=\int_0^\infty C$.

## Technique 6 — Expectation of $\cos/\sin$ via the characteristic function

$\mathbb E\cos(\sigma Z)=\operatorname{Re}\mathbb E e^{i\sigma Z}$ and
$\mathbb E\sin(\sigma Z)=\operatorname{Im}\mathbb E e^{i\sigma Z}$; for centred
Gaussian $Z$ these are $e^{-\sigma^2\operatorname{Var}Z/2}$ and $0$. Combined with
products-to-sums (file 02 §4) this handles every "$\mathbb E[\sin(\sigma W_s)
\sin(\sigma W_t)]$" question. *Used in:* Exercise 5, 9.

## Technique 7 — Time change

If $Y_t=(\text{deterministic factor})\times X_{\tau(t)}$ with $\tau$ increasing, then
$\operatorname{Cov}(Y_s,Y_t)=(\text{factors})\operatorname{Cov}(X_{\tau(s)},X_{\tau(t)})$.
BM time changes produce OU ($e^{-t}W_{e^{2t}}$) and bridges
($tW_{1/t}$, $(1-t)W_{t/(1-t)}$). *Used in:* Exercises 6, 8, 12, 15.

## Technique 8 — Kernel → ODE (Sturm–Liouville) reduction

For an integral eigenvalue problem with a piecewise/absolute-value kernel:
1. differentiate once in $t$ (the corner produces a discontinuity);
2. differentiate again to get a second-order ODE;
3. read **boundary conditions** off the original equation at $t=0$ and $t=1$;
4. solve the ODE (file 08 §4) and **normalise**.
*Used in:* Exercises 24, 25, 28b.

## Technique 9 — Rank-one / degenerate kernels

If $R(t,s)=\sum_{i=1}^rf_i(t)g_i(s)$, there are **at most $r$ nonzero eigenvalues**.
Write $e(t)=\sum_ic_if_i(t)$, substitute into $\int R(t,s)e(s)ds=\lambda e(t)$ and
solve an $r\times r$ linear system. Special case $r=1$: $R(t,s)=f(t)f(s)$ ⟹
$e\propto f$, $\lambda=\int f^2$.
*Used in:* Exercises 23, 26 (with $\cos(2\pi(t-s))$ split by the angle-difference
formula into two rank-one pieces).

## Technique 10 — Mercer / trace

For a continuous symmetric nonnegative kernel on $[0,T]$:
$$\sum_n\lambda_n=\int_0^TR(t,t)\,dt .$$
For a stationary process $R(t,t)=R(0)$, giving $\sum\lambda_n=TR(0)$ — Exercise 22.
The discrete version is $\operatorname{tr}A=\sum\lambda_i$ (file 05 §5).

## Technique 11 — Green–Kubo

$$D=\int_0^\infty C(t)dt,\qquad
\mathbb E\Big(\int_0^tX_sds\Big)^2\sim2Dt\ (t\to\infty),$$
valid when $C\in L^1(0,\infty)$ **— check this explicitly; it is part of
Exercises 7b and 16b** (and it is why $\gamma>0$ matters).

## Technique 12 — Proving stationarity

Two questions, always in this order:
1. **Strict?** Compare the whole joint law of a shifted vector (iid or
   deterministic-in-$\omega$ structure; Exercises 1, 2).
2. **Weak?** Compute $\mathbb EX_t$ and $\operatorname{Cov}(X_t,X_{t+\tau})$ and show
   they do not depend on $t$. If the result depends only on the **lag** $\tau$, you
   are done. Using products-to-sums, the dependence on $n$ cancels — that is the
   *mechanism* in Exercises 3, 4, 14.

## Technique 13 — Ergodic average of an oscillation

$\frac1N\sum_{n=0}^{N-1}\cos(n\omega)\to0$ unless $\omega$ is a multiple of $2\pi$
(sum a geometric series). Consequence: for a harmonic process, time averages pick out
only the "DC" part. *Used in:* comparison of time and ensemble averages in
Exercises 1, 3.

## Technique 14 — Normalisation checklist (do it every single time)

1. Is my candidate eigenfunction normalised: $\int_0^1e_n^2=1$?
2. Did I keep the $\tfrac{1}{2\pi}$ on the correct side of the Fourier pair?
3. Did I split $\min$ and handle **both** orders?
4. Did I state **independence** where I used it, and not "uncorrelated"?
5. Did I check the integrability hypothesis before quoting Green–Kubo/Mercer?

## Technique 15 — Write the "bookkeeping" first

Before doing any algebra, write down in a column:
1. what is **known** (definition of the process, its mean, its covariance);
2. what is **asked** (an expectation? a law? a covariance? an eigenpair?);
3. which **hypotheses** must be checked (integrability, continuity, Gaussianity).

Half of the marks in this chapter are for (3). Exercises 7(b), 16(b), 18, 19, 21 and 22
are essentially *only* about hypotheses.

## How to use these 15 techniques in practice

- Stuck for more than 10 minutes? Ask: *is my object Gaussian?* (→ 3, 4)
- See $\min$, $\left|t-s\right|$, or a corner in a kernel? (→ 1, 5, 8)
- See $e^{i\theta}$, $\cos$, $\sin$ of a random variable? (→ 6)
- See an integral equation? (→ 8, 9, 10)
- See "show that this is stationary/ergodic"? (→ 12, 13)
- Asked for the $t\to\infty$ behaviour? (→ 5, 11)

Then go back to the relevant chapter file in the parent folder and follow its
**game plan** line by line with the technique in hand.
