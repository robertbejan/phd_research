# 09 — Stochastic processes from scratch

**Read this if:** "stationary", "ergodic", "mean-square continuous" or
"modification" are words you nod at without being sure.

## 1. What a stochastic process is

**In words.** A stochastic process is a **random function of time**: for each time
$t$ you get a random variable $X_t$; run the experiment once and you get a whole
curve $t\mapsto X_t(\omega)$, called a **path** (or **realisation**,
**trajectory**).

**Exactly.** A stochastic process is a family $(X_t)_{t\in T}$ of random variables on
a common probability space. $T$ is the **index set**: $T=\{0,1,2,\dots\}$ (discrete
time — Exercises 1–4) or $T=[0,\infty)$ (continuous time — Exercises 5–28).

**Finite-dimensional distributions (FDDs):** for any $t_1,\dots,t_n$, the joint law
of $(X_{t_1},\dots,X_{t_n})$. Two processes with the same FDDs are **equivalent**
(they have the same law).

## 2. Three words that are often confused (Exercise 18)

- **Equivalent:** same FDDs. "Same statistics at every fixed set of times."
- **Modification:** $\mathbb P(X_t=Y_t)=1$ **for each fixed $t$** separately; the
  exceptional null set may depend on $t$.
- **Indistinguishable:** $\mathbb P(X_t=Y_t\text{ for all }t)=1$; strictly stronger.
- A **continuous modification** is a modification whose paths are a.s. continuous.

**Why it matters.** Statistics (FDDs) are "cheap"; **path** regularity is extra
work. That is precisely the content of Exercise 18.

> **Kolmogorov's continuity criterion (Theorem 1.2).** If
> $\mathbb E\left|X_t-X_s\right|^{\alpha}\le C\left|t-s\right|^{1+\beta}$ for some
> $\alpha,\beta>0$ and all $s,t$ in a compact interval, then $X$ has a **continuous
> modification**. *Moral: enough moments of small increments ⇒ continuous paths.*

## 3. Stationarity

**Strict (strong) stationarity (Def. 1.5).** For all $n$, all $t_1,\dots,t_n$ and all
shifts $s$:
$$(X_{t_1},\dots,X_{t_n})\ \overset{\text{law}}{=}\ (X_{t_1+s},\dots,X_{t_n+s}).$$
*In words: shifting the clock does not change the statistics.*

**Weak (second-order) stationarity (Def. 1.6).** Only the first two moments matter:
$$\mathbb EX_t=\mu\ \text{(constant)},\qquad
\operatorname{Cov}(X_t,X_s)=C(t-s)\ \text{(depends only on the lag)} .$$
- Strict + finite variance $\Rightarrow$ weak. The **converse is false** in general
  but **true for Gaussian** processes (file 04 §5).
- Always: $C(0)=\operatorname{Var}(X_t)\ge0$, $C(-t)=C(t)$,
  $\left|C(t)\right|\le C(0)$ (Cauchy–Schwarz), and $C$ is PSD (file 06 §8).

**Stationary increments:** $(X_{t_2}-X_{t_1})\overset{\text{law}}{=}
(X_{t_2+s}-X_{t_1+s})$. This is what makes Exercise 14 work.

## 4. Ergodicity and time averages

**In words.** A stationary process is **ergodic** if along a **single** long path the
time average converges to the theoretical average:
$$\frac1N\sum_{j=0}^{N-1}f(X_j)\ \xrightarrow[N\to\infty]{}\ \mathbb E f(X_0).$$
If it is *not* ergodic, one path can have "locked-in" randomness that never averages
out (e.g. $X_n=Z$ for all $n$: the time average is always $Z$, never $\mathbb EZ$).

**Birkhoff's ergodic theorem (Eq. (1.1)).** For a strictly stationary ergodic
sequence the time averages converge **almost surely** (and in $L^2$ when
$\mathbb Ef(X_0)^2<\infty$).

**The $L^2$ computation you actually do** (this is Exercise 1b/1c). For weakly
stationary $X$ with mean $\mu$:
$$\mathbb E\Big|\frac1N\sum_{j=0}^{N-1}X_j-\mu\Big|^2
=\frac{1}{N^2}\sum_{j,k=0}^{N-1}C(j-k)
=\frac1N\sum_{\left|h\right|<N}\Big(1-\frac{\left|h\right|}{N}\Big)C(h).$$
So the time average converges in $L^2$ **iff $C(h)\to0$** as $\left|h\right|\to\infty$.
*For uncorrelated $X_j$: $C(h)=\sigma^2\delta_{h0}$, and the right side is
$\sigma^2/N$ — the textbook $\sigma^2/N$.*

**Mean-square ergodicity, continuous time (Prop. 1.3 / Eq. (1.6)).** If $X$ is
second-order stationary and $C$ is continuous with
$$\int_{-\infty}^{\infty}\left|C(t)\right|dt<\infty\qquad(C\in L^1),$$
$$\text{then}\qquad
\mathbb E\Big(\frac1T\int_0^TX_t\,dt-\mu\Big)^2\ \xrightarrow[T\to\infty]{}\ 0 .$$
**The hypothesis "$C\in L^1$" is exactly what Exercise 7(b) asks you to check.**

## 5. Spectral density and the correlation time

For a second-order stationary process with $C\in L^1$ the **spectral density** is the
Fourier transform of $C$ (file 07 §4):
$$S(\omega)=\frac{1}{2\pi}\int_{-\infty}^{\infty}e^{-i\omega t}C(t)\,dt,\qquad
C(t)=\int_{-\infty}^{\infty}e^{i\omega t}S(\omega)\,d\omega .$$
**Bochner's theorem (Thm 1.1):** $S(\omega)\ge0$, even for real $C$, and
$\int S(\omega)d\omega=C(0)$. *Intuition:* $S(\omega)$ = "how much variance sits at
frequency $\omega$".

**Correlation time:** $\tau_{cor}=\frac{1}{C(0)}\int_0^\infty C(t)dt$ — how long the
process remembers itself. Slower decay ⇒ larger $\tau_{cor}$; if $C$ does not decay
(undamped oscillation), $\tau_{cor}=\infty$.

## 6. Green–Kubo: variance of an integral, and the diffusion coefficient

Integrating a stationary process and asking how fast a "particle" spreads gives
$$\boxed{\ D=\int_0^\infty C(t)\,dt\ }\qquad\text{(the diffusion coefficient)},$$
$$\mathbb E\Big(\int_0^tX_s\,ds\Big)^2=2\int_0^t(t-u)C(u)\,du\ \sim\ 2Dt\quad(t\to\infty).$$
**Where the double integral comes from** (you will do this by hand):
$$\mathbb E\Big(\int_0^t\!\!\int_0^tX_uX_v\,du\,dv\Big)
=\int_0^t\!\!\int_0^tC(u-v)\,du\,dv=2\int_0^t(t-u)C(u)\,du .$$
*Why:* for each lag $h=u-v$ the number of pairs $(u,v)$ with $u-v=h$ is $t-\left|h\right|$.
This is **Technique 5** in file 11 and the whole of Exercises 7(b) and 16(b).

## 7. Markov property, transition density, stationary distribution

- **Markov property:** "given the present, the future is independent of the past".
  Encoded by the **transition density** $p(t,x;y)$ via
  $\mathbb P(X_{t+dt}\in dy\mid X_t=x)=p(t,x;y)dy$.
- **Stationary distribution** (continuous-time Markov processes): a density $p_s$ with
  $\int p_s(x)p(t,x;y)dx=p_s(y)$ — the law is unchanged by the dynamics.
- **Fokker–Planck equation:** describes how the *density* of $X_t$ evolves;
  **backward Kolmogorov equation:** describes how $\mathbb E[\varphi(X_t)]$ evolves.
  For OU with $dX=-Xdt+\sqrt2dW$ the stationary law is $\mathcal N(0,1)$ — this **is
  Exercise 12**.
- *You do not need to solve these PDEs for Chapter 1's exercises*, but you should be
  able to state the property and the stationary law.

## 8. Micro-drills

1. Define weak stationarity in your own words for a **Gaussian** process. *Ans.*
   Constant mean and covariance depending only on the lag (weak $=$ strict here).
2. If $C(h)=(-1)^h$, is the process $L^2$-ergodic? *Ans.* No — $C(h)\not\to0$, so the
   time average does not settle down.
3. For $C(t)=e^{-\left|t\right|}$, find $D$ and $\tau_{cor}$. *Ans.* $D=1$,
   $\tau_{cor}=1$ (both are $\int_0^\infty e^{-t}dt$, and $C(0)=1$).
4. Why does $C\in L^1$ fail for $C(t)=\cos(\omega t)$? *Ans.* It never decays; the
   integral diverges, and time averages of a pure oscillation do not converge.
5. For $X_n=Z$ for all $n$, what is the time average, and is the process ergodic?
   *Ans.* The average is $Z$ itself, which $\ne\mathbb EZ$ in general — **not**
   ergodic. (This is Exercise 2's setting.)
