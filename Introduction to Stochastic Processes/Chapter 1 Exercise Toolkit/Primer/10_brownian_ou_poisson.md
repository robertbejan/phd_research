# 10 — Brownian motion, OU, Poisson, white noise

**Read this if:** you want these three processes built from their definitions, with
every property used in the chapter explained.

## 1. Brownian motion (Wiener process) $W_t$

**Definition.** $W$ is a stochastic process with
1. $W_0=0$;
2. **independent increments:** $W_{t_1}-W_{t_0},\dots,W_{t_n}-W_{t_{n-1}}$ mutually
   independent;
3. **Gaussian, stationary increments:** $W_t-W_s\sim\mathcal N(0,t-s)$, $t>s$;
4. **continuous paths**.

**Consequences (all used in the exercises).**
- $W_t\sim\mathcal N(0,t)$, and every finite vector $(W_{t_1},\dots,W_{t_n})$ is
  Gaussian — so $W$ is a **Gaussian process** (file 04 §6).
- $$\boxed{\ \operatorname{Cov}(W_s,W_t)=\min(s,t)\ }$$
  *Derivation:* assume $s\le t$ and write $W_t=W_s+(W_t-W_s)$. The two pieces are
  independent, so $\mathbb E[W_sW_t]=\mathbb EW_s^2+\mathbb E[W_s(W_t-W_s)]=s+0=s$.
  **This is self-test question 10 and the hinge of Exercises 5, 6, 13, 14.**
- $\mathbb E(W_t-W_s)^2=t-s$, so $\mathbb E(W_t-W_s)^4=3(t-s)^2$ (Gaussian 4th
  moment, file 04 §5). Kolmogorov's criterion therefore holds with
  $\alpha=4,\beta=1$ — **BM has continuous paths**.
- **Self-similarity:** $(W_{ct})\overset{\text{law}}{=}(\sqrt c\,W_t)$.
  *Proof:* both are centred Gaussian; compare covariances:
  $\min(cs,ct)=c\min(s,t)=(\sqrt c)^2\min(s,t)$. ✓ (Exercises 11, 17.)
- Also BM: $W_{1-t}-W_1$, $-W_t$, and $tW_{1/t}$ (with the value $0$ at $t=0$).
- Paths are continuous but **nowhere differentiable**; $W$ has **quadratic variation**
  $\sum_i(W_{t_{i+1}}-W_{t_i})^2\to t$. Intuition: $\left|\Delta W\right|\approx
  \sqrt{\Delta t}$, so $\Delta W/\Delta t\approx1/\sqrt{\Delta t}\to\infty$.

**Brownian bridge** ($t\in[0,1]$): $B_t=W_t-tW_1$, BM **pinned to $0$ at $t=1$**.
- Centred Gaussian, $\operatorname{Cov}(B_s,B_t)=\min(s,t)-st$,
  $B_t\sim\mathcal N(0,t(1-t))$ — the variance vanishes at both ends.
- Equivalent description: $B_t\overset{\text{law}}{=}(1-t)W_{t/(1-t)}$.
- **General pinning recipe** (toolkit file 03 §T6): to pin a Gaussian process $X$ to
  $0$ at time $T$, subtract its best linear prediction of $X_T$:
  $$X_t-\frac{\operatorname{Cov}(X_t,X_T)}{\operatorname{Var}(X_T)}X_T .$$

**Fractional BM** (Exercise 17): the centred Gaussian process with
$$\mathbb E[W_s^HW_t^H]=\tfrac12\left(s^{2H}+t^{2H}-\left|t-s\right|^{2H}\right),
\qquad H\in(0,1)\ \text{(Hurst parameter)}.$$
$H=\tfrac12$ recovers BM (check: $\tfrac12(s+t-\left|t-s\right|)=\min(s,t)$).

## 2. White noise and the Wiener integral

**White noise** is the formal "derivative" $\xi_t=dW_t/dt$: flat spectrum, infinite
pointwise variance, $\mathbb E[\xi_t\xi_s]=\delta(t-s)$. It is a shorthand, not a
process. It is *why* the Langevin equation $dY=-\gamma Ydt+\sigma dW$ has a
"random force" interpretation.

**Wiener integral** $\int_0^tf(s)dW_s$ for **deterministic** $f$ (the only stochastic
integral Chapter 1 needs). Two rules:
1. **It is Gaussian with mean zero** — it is a limit of Gaussian Riemann sums
   $\sum_if(s_i)(W_{s_{i+1}}-W_{s_i})$ (file 04 §5 fact 2).
2. **Itô isometry:**
   $$\boxed{\ \mathbb E\Big(\int_0^tf(s)\,dW_s\Big)^2=\int_0^tf(s)^2ds\ }$$
   *How to remember it:* "$dW$ squared $=dt$".
Everything about such integrals follows from these two rules plus independence of
increments — no Itô calculus required.

*Worked.* $\int_0^tW_sds$ (Exercise 13) is **not** a Wiener integral (the integrand
is random) but it is still Gaussian, being a limit of linear combinations of the
Gaussian variables $W_{s_i}$; its covariance follows from Fubini plus
$\mathbb E[W_uW_v]=\min(u,v)$ (toolkit file 03 §T4).

## 3. The Ornstein–Uhlenbeck process

**SDE form (Langevin equation):** $dY_t=-\gamma Y_t\,dt+\sigma\,dW_t$, with
$\gamma>0$ the **damping** and $\sigma$ the **noise strength**.
**Explicit solution:**
$$Y_t=e^{-\gamma t}Y_0+\sigma\int_0^te^{-\gamma(t-s)}dW_s .$$
*Verify* by differentiating (or by integrating factor, file 08 §2). The deterministic
part is the ODE $Y'=-\gamma Y$.

**Properties.**
- **Gaussian**, with mean $e^{-\gamma t}\mathbb EY_0$; centred when $Y_0=0$.
- Covariance (centred case):
  $$\operatorname{Cov}(Y_s,Y_t)=\frac{\sigma^2}{2\gamma}e^{-\gamma\left|t-s\right|}.$$
  **This is the $e^{-\alpha|t|}$ correlation of Example 1.5.**
- **Stationary version:** if $Y_0\sim\mathcal N(0,\sigma^2/2\gamma)$ then $Y$ is
  **stationary** with $C(t)=\frac{\sigma^2}{2\gamma}e^{-\gamma|t|}$, spectral density a
  **Lorentzian** $\frac{\sigma^2/2\gamma}{\pi}\frac{1}{\omega^2+\gamma^2}$, and hence
  $D=\int_0^\infty C=\sigma^2/(2\gamma^2)$ (Green–Kubo, file 09 §6).
- **Time change (Lemma 1.6):** $V_t=e^{-t}W_{e^{2t}}$ is the stationary OU process
  with $C(t)=e^{-\left|t\right|}$. *Check:* $V_t\sim\mathcal N(0,e^{-2t}\cdot e^{2t})=
  \mathcal N(0,1)$ and $\mathbb E[V_sV_t]=e^{-s-t}\min(e^{2s},e^{2t})=
  e^{-\left|t-s\right|}$. ✓ **Exercises 8, 12, 15 all start here.**
- **Ergodicity:** for $\gamma>0$ we have $C\in L^1$, so the process is ergodic with
  stationary law $\mathcal N(0,\sigma^2/(2\gamma))$ — that is Exercise 12.

## 4. The Poisson process $N_t$

**Definition.** $N_0=0$; increments independent; $N_t-N_s\sim\text{Poisson}(\lambda(t-s))$;
paths are right-continuous **step functions** jumping by $+1$.
$$\mathbb P(N_t-N_s=k)=e^{-\lambda(t-s)}\frac{[\lambda(t-s)]^k}{k!},\qquad
\mathbb E(N_t-N_s)=\operatorname{Var}(N_t-N_s)=\lambda(t-s).$$
- **Waiting times** between jumps are iid $\text{Exponential}(\lambda)$; the number of
  jumps in $[0,t]$ is $\text{Poisson}(\lambda t)$.
- **Why it has no continuous modification (Exercise 18).** *Intuition:* $N_t$ jumps by
  $1$ at random times, so $N_t-N_s$ is either $0$ or $\ge1$; it cannot be made small
  continuously. *Quantitatively,* for any $\alpha>0$,
  $$\mathbb E\left|N_t-N_s\right|^{\alpha}\ \ge\ \mathbb P(N_t\ne N_s)
  =1-e^{-\lambda(t-s)}\ \approx\ \lambda(t-s),$$
  which grows **linearly** in $t-s$ and so cannot be bounded by
  $C(t-s)^{1+\beta}$ with $\beta>0$. Kolmogorov's criterion therefore fails for
  **every** $\alpha,\beta$ — that is the required proof.
- **Useful fact for the argument:** the right-hand side is linear, whereas the
  criterion demands *super-linear* decay $(t-s)^{1+\beta}$. Dividing by
  $(t-s)^{1+\beta}$ and letting $t-s\to0$ gives $\infty$, contradicting a bounded $C$.

## 5. Micro-drills

1. Compute $\mathbb E[W_2W_5]$, $\operatorname{Var}(W_5-W_2)$, $\mathbb E(W_5-W_2)^4$.
   *Ans.* $2$ (the $\min$); $3$; $27$ (Gaussian 4th moment $3(t-s)^2$).
2. Is $2W_{t/4}$ a Brownian motion? *Ans.* Yes — self-similarity with $c=1/4$.
3. For OU with $\gamma=1,\sigma=\sqrt2$: give $C(t)$, the stationary variance and $D$.
   *Ans.* $e^{-\left|t\right|}$; $1$; $D=1$.
4. Give two reasons $N_t$ is not Gaussian. *Ans.* It is integer-valued, and its
   $t$-marginal is Poisson, not normal.
5. Why is $\int_0^1W_sds$ Gaussian even though $W_s$ is random? *Ans.* It is the
   $L^2$-limit of sums $\sum_iW_{s_i}\Delta s$, each Gaussian; limits of Gaussian
   variables are Gaussian (file 04 §5).
