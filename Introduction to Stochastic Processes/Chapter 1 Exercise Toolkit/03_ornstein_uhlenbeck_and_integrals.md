# 03 — Ornstein–Uhlenbeck process & integrals of Brownian motion

**Covers Exercises 8, 12, 13, 14, 15.**
Book sections: 1.2 (Example 1.5, eqs. (1.9)–(1.11)), 1.4 (OU, Lemma 1.6, Brownian
bridge (1.23)–(1.25)).

> **Prerequisites** (read these first if the maths is new):
> `Primer/01_calculus_primer.md` §5–§7 — integrals, Fubini, and the "$\min$ split"
> of a double integral;
> `Primer/08_odes_and_green_functions.md` §2 — first-order linear ODEs, the origin of
> every $e^{-\alpha t}$;
> `Primer/09_stochastic_processes_primer.md` §6 — variance of an integral of a
> stationary process (the double-integral reduction);
> `Primer/10_brownian_ou_poisson.md` §1–§3 — Brownian motion, the Wiener integral and
> Itô isometry, and the Ornstein–Uhlenbeck process (SDE, solution, time change
> $V_t=e^{-t}W(e^{2t})$, stationary version).
> Techniques 1–5 and 7 of `Primer/11_recurring_techniques.md`.

---

## The tools

### T1 — The stationary Ornstein–Uhlenbeck process
A mean-zero Gaussian stationary process with correlation
$$C(t)=R(t)=\frac{D}{\alpha}e^{-\alpha|t|}\qquad(\alpha>0).$$
In this chapter the normalisation $\alpha=D=1$ gives $R(t)=e^{-|t|}$. It is used as
the **velocity** $Y_t$ of a Brownian particle. Correlation time $\tau_{cor}=\alpha^{-1}$.
Realisation via time change (Lemma 1.6): $V(t)=e^{-t}W(e^{2t})$ is OU with
$R(t)=e^{-|t|}$.

### T2 — Gaussian stability of the integral (Ex. 8, 13)
If $Y$ is a mean-zero Gaussian process and $Z_t=\int_0^tY_s\,ds$, then $Z_t$ is a
mean-zero **Gaussian** process (T5 of file 02: Riemann sums of Gaussians are
Gaussian). Only its **covariance** remains to be computed:
$$\mathbb E[Z_tZ_s]=\int_0^t\!\!\int_0^s \mathbb E[Y_uY_v]\,du\,dv.$$
For OU with $X_t=\int_0^tY_s\,ds$ and $\alpha=D=1$ the book gives (1.11)
$$ \mathbb E[X_tX_s]=2\min(t,s)+e^{-\min(t,s)}+e^{-\max(t,s)}-e^{-|t-s|}-1. $$

### T3 — Fubini for expectations (Ex. 13, 14)
$$\mathbb E\int\!\!\int \cdots = \int\!\!\int \mathbb E[\cdots],$$
legitimate when the integrand is integrable (true here). Then use
$\mathbb E[W_uW_v]=\min(u,v)$.

### T4 — The $\min$ kernel (a recurring computation)
For $Y_t=\int_0^tW_s\,ds$:
$$\mathbb E[Y_tY_s]=\int_0^t\!\!\int_0^s\min(u,v)\,du\,dv.$$
Handle it by assuming $s\le t$, then **splitting** the $v$-integral (or $u$) at the
point where the $\min$ switches. The result for $s\le t$ is a polynomial; use
$s\leftrightarrow t$ symmetry for the other case.

### T5 — Stationary increments $\Rightarrow$ stationarity (Ex. 14)
BM has **stationary** increments: the law of $W_{s+h}-W_{t+h}$ equals that of
$W_s-W_t$. For $Y_t=\int_t^{t+1}(W_s-W_t)\,ds$, show the covariance
$\mathbb E[Y_tY_{t+\tau}]$ depends only on $\tau$: shift the integration variable to
use increment-stationarity. A mean-zero process with a $\tau$-only covariance is
second-order stationary.

### T6 — Bridges by pinning a Gaussian process (Ex. 6, 15)
Given a Gaussian process $X_t$ on $[0,T]$, the **bridge** to a value at a fixed time
$T$ is obtained by subtracting the part explained by the endpoint:
$$\text{bridge}_t = X_t - \frac{\text{Cov}(X_t,X_T)}{\operatorname{Var}(X_T)}\,X_T
\quad(\text{when the pinned value is }0).$$
For the Brownian bridge this reduces to $W_t-tW_1$. For the OU bridge, replace
$X_t=W_t$ by the (stationary) OU process/appropriate time-changed process. The
result is again centred Gaussian; get its covariance by bilinearity.

### T7 — Covariance of a time-changed process (Ex. 12, 15)
For $V_t=e^{-t}W(e^{2t})$:
$$\mathbb E[V_tV_s]=e^{-t-s}\min(e^{2t},e^{2s})=e^{-|t-s|}.$$
Reuse this pattern whenever a process is a deterministic rescaling/time-change of BM.

---

## Warm-ups (solved)

**W1 (analogue of Ex. 13).** For $Y_t=\int_0^tW_s\,ds$, find $\mathbb E Y_t$ and
$\operatorname{Var}(Y_t)$.
*Solution.* $\mathbb E Y_t=0$. Using T3/T4 with $s=t$:
$$\operatorname{Var}(Y_t)=\int_0^t\!\!\int_0^t\min(u,v)\,du\,dv
=2\int_0^t\!\!\int_0^v u\,du\,dv=2\int_0^t\frac{v^2}{2}\,dv=\frac{t^3}{3}.$$

**W2 (stationary increments, analogue of Ex. 14).**
Show $\operatorname{Cov}(W_{t+1}-W_t,\ W_{t+1+\tau}-W_{t+\tau})$ depends only on
$\tau$.
*Solution.* Both are increments over a window of length $1$; expand
$W_{t+1}-W_t$ and use $\mathbb E W_aW_b=\min(a,b)$; only the **offset** $\tau$
between the two windows survives. (Do the $\tau>1$ and $\tau<1$ cases separately —
this is where the split of the $\min$ appears.)

**W3 (time change, analogue of Ex. 12/15).**
For $V_t=e^{-t}W(e^{2t})$ show $V_t\sim\mathcal N(0,1)$ for each $t$.
*Solution.* $e^{2t}$ is deterministic, $W(e^{2t})\sim\mathcal N(0,e^{2t})$, so
$V_t\sim\mathcal N(0,e^{-2t}\cdot e^{2t})=\mathcal N(0,1)$.

---

## Game plan

### Exercise 8
- The velocity is the **stationary OU** process (T1). The position is
  $X_t=\int_0^tY_s\,ds$. By **T2** it is Gaussian and mean zero — *cite the Riemann-sum
  argument*.
- Compute the covariance by **T3/T4**: plug $\mathbb E[Y_uY_v]=e^{-|u-v|}$ (with the
  correct $D,\alpha$) into the double integral
  $\mathbb E[X_tX_s]=\int_0^t\int_0^s e^{-|u-v|}du\,dv$ and reproduce (1.11).
- *Guiding question:* why can you not just say "it's Gaussian" without checking the
  finite-dimensional distributions?

### Exercise 12
- Lemma 1.6 gives $V_t=e^{-t}W(e^{2t})$ as OU, and W3 tells you $V_t\sim\mathcal N(0,1)$
  for each $t$. Write down the CDF $\mathbb P(V_t\le x)$ as the standard normal CDF.

### Exercise 13
- Mean: linearity/Fubini, $\mathbb E W_s=0$.
- Covariance: **T3/T4** — compute $\int_0^t\int_0^s\min(u,v)\,du\,dv$; write the
  result piecewise in $t\le s$ and $t\ge s$.
- *Guiding question:* is the resulting process stationary? Justify from your formula.

### Exercise 14
- Change variables in the double integral for $\mathbb E[Y_tY_{t+\tau}]$ and use
  **stationary increments** (T5) to show it depends only on $\tau$.
- Note $Y_t=\int_0^1(W_{t+v}-W_t)\,dv$; expanding and using the $\min$ kernel is the
  cleanest route.

### Exercise 15
- **Define** the OU bridge as the process $V_t$ **pinned to $0$** at a fixed time,
  by analogy with the Brownian bridge (T6). Give the definition, then show it is
  centred Gaussian and compute its covariance (expected to interpolate between $0$
  endpoints).
- Study: mean, variance, path behaviour; compare with the plain OU and with the
  Brownian bridge.
- *Guiding question:* which time change maps the Brownian bridge to the OU bridge?

---

## Pitfalls

- **Never skip the "is the integral Gaussian?" argument** — it is part of the
  exercise, not a formality.
- **$\min$ splitting** in double integrals is the most common error; draw the
  $(u,v)$ square and mark the diagonal.
- **Bridges are not "conditioned paths" in a hand-wavy sense**: define them
  precisely via the covariance (T6).
- **$\alpha$ vs $D$** — the book's $\alpha=D=1$ normalisation only applies to (1.11);
  restore the general constants when using (1.9)/(1.15).

---

## Numerical check (optional)

Simulate OU velocity paths and integrate by `cumsum`; compare the empirical
variance of $\int_0^tY_s\,ds$ against your formula (e.g. $t^3/3$ for pure BM). For
Ex. 14, estimate the autocovariance of $Y_t$ at several lags and check it does not
depend on $t$.

