# 02 — Brownian motion & Gaussian expectations

**Covers Exercises 5, 6, 9, 10, 11, 17.**
Book sections: 1.3 (Def. 1.8, eqs. (1.17), Prop. 1.5), 1.4 (Lemma 1.6, Brownian
bridge (1.23)–(1.25), fractional BM Def. 1.9, eqs. (1.26)–(1.27)).

> **Prerequisites** (read these first if the maths is new):
> `Primer/04_gaussian_primer.md` §1–§6 — the normal law, its characteristic function
> $\mathbb E e^{i\theta X}=e^{-\theta^2\sigma^2/2}$, multivariate Gaussians,
> "linear maps of Gaussians are Gaussian", "mean + covariance = the whole law";
> `Primer/02_complex_numbers_and_trig.md` §3–§4 — Euler's formula and the trig
> products-to-sums identities;
> `Primer/10_brownian_ou_poisson.md` §1 — Brownian motion built from its four
> defining properties (independent Gaussian increments, continuous paths).
> Technique 4 and 6 of `Primer/11_recurring_techniques.md`.

---

## The tools

### T1 — Characteristic function of a Gaussian (Ex. 5, 6)
For $X\sim\mathcal N(\mu,\sigma^2)$:
$$\boxed{\ \mathbb E e^{i\theta X}=e^{\,i\theta\mu-\frac12\theta^2\sigma^2}\ }$$
For Brownian motion $W_t\sim\mathcal N(0,t)$ this gives $\mathbb E e^{i\theta W_t}=e^{-\theta^2 t/2}$.

**Multivariate version (the real engine of Ex. 5c,d).** If $X=(X_1,\dots,X_n)$ is a
zero-mean Gaussian vector with covariance matrix $\Sigma_{ij}=\mathbb E X_iX_j$,
then for any real vector $c=(c_1,\dots,c_n)$:
$$\mathbb E\,e^{\,i\,c\cdot X}=\exp\!\Big(-\tfrac12 c^\top\Sigma c\Big)
=\exp\!\Big(-\tfrac12\sum_{i,j}c_ic_j\,\mathbb E[X_iX_j]\Big).$$

### T2 — Brownian covariance & the two-second-moment trick
$$\mathbb E[W_sW_t]=\min(s,t),\qquad \mathbb E[(W_t-W_s)^2]=t-s\ (t>s).$$
Therefore for a linear combination $\sum_i c_iW_{t_i}$:
$$\mathbb E\Big(\sum_i c_iW_{t_i}\Big)^2=\sum_{i,j}c_ic_j\min(t_i,t_j).$$
*This is exactly Exercise 5(c).*

### T3 — MGF / exponential moments (Ex. 9a, 10)
$$\mathbb E e^{\sigma W_t}=\exp\!\Big(\tfrac12\sigma^2 t\Big)
\quad\Longleftarrow\quad \mathbb E e^{sX}=e^{s\mu+\frac12 s^2\sigma^2}.$$
Because $W_t$ is Gaussian, $e^{\sigma W_t}$ is **log-normal**.

### T4 — Sine products (Ex. 9b)
Write $\sin$ in terms of exponentials, or use $\sin a\sin b=\tfrac12[\cos(a-b)-\cos(a+b)]$:
$$\mathbb E[\sin(\sigma W_{s_1})\sin(\sigma W_{s_2})]
=\tfrac12\mathbb E\cos\!\big(\sigma(W_{s_1}-W_{s_2})\big)-\tfrac12\mathbb E\cos\!\big(\sigma(W_{s_1}+W_{s_2})\big).$$
Now $W_{s_1}\pm W_{s_2}$ are **Gaussian** (explain why!) with mean $0$ and known
variance, and $\mathbb E\cos(\sigma Z)=\operatorname{Re}\mathbb E e^{i\sigma Z}$,
which T1 gives you.

### T5 — Linear maps of Gaussians are Gaussian
If $X$ Gaussian and $b_t$ is a fixed (deterministic) linear function of the path,
then $Y_t=b_t+\sum_i a_i(t)X_{s_i}$ (finite, or an $L^2$ limit) is Gaussian.
Covariance follows by bilinearity. This is why:
- the **Brownian bridge** $B_t=W_t-tW_1$ is Gaussian (Ex. 6a),
- the **integral** $\int_0^tW_s\,ds$ is Gaussian (Ex. 13),
- the **position** of the Brownian particle is Gaussian (Ex. 8).

### T6 — Time change (Lemma 1.7) and the bridge (Ex. 6b)
If $X(t)$ is Gaussian and $f$ strictly increasing, then $Y(t)=X(f(t))$ is Gaussian.
Use it to show $B_t=(1-t)W\!\big(\tfrac{t}{1-t}\big)$ equals the bridge in law:
match means and covariances. (For Ex. 6c, $B_t\sim\mathcal N(0,t(1-t))$ — square
that with T1.)

### T7 — Equality in law by matching first two moments (Ex. 11, 17)
For **centred Gaussian** processes, "equal in law" is equivalent to equal mean ($0$)
and equal covariance. So to prove e.g. rescaling/inversion/time-reversal (Prop. 1.5)
or the fractional-BM self-similarity (1.27):
1. show the candidate is Gaussian with mean $0$,
2. compute its covariance and check it equals $\min(s,t)$ (or the fBm covariance
   (1.26) $\tfrac12(s^{2H}+t^{2H}-|t-s|^{2H})$).

### T8 — Fractional Brownian motion (Ex. 17)
$W^H$ is centred Gaussian with
$$\mathbb E[W^H_sW^H_t]=\tfrac12\big(s^{2H}+t^{2H}-|t-s|^{2H}\big).$$
Self-similarity: $(W^H_{\alpha t})\overset{\text{law}}{=}(\alpha^H W^H_t)$.
Use **T7**: compare $\mathbb E[W^H_{\alpha s}W^H_{\alpha t}]$ with
$\alpha^{2H}\mathbb E[W^H_sW^H_t]$.

---

## Warm-ups (solved)

**W1 (analogue of Ex. 5a,b).** Compute $\mathbb E e^{iW_3}$ and
$\mathbb E e^{i(W_3+W_1)}$.
*Solution.* $W_3\sim\mathcal N(0,3)$, so $\mathbb E e^{iW_3}=e^{-3/2}$.
$W_3+W_1$ is Gaussian, mean $0$, variance $=3+1+2\min(3,1)=6$, so
$\mathbb E e^{i(W_3+W_1)}=e^{-3}$.

**W2 (analogue of Ex. 5c).** $\mathbb E(W_3-2W_1)^2$.
*Solution.* $=\mathbb E W_3^2-4\mathbb E W_3W_1+4\mathbb E W_1^2
=3-4\cdot1+4\cdot1=3$.

**W3 (analogue of Ex. 6a).** For $B_t=W_t-tW_1$, show $\mathbb E B_t=0$ and
$\mathbb E B_tB_s=\min(t,s)-ts$.
*Solution.* Mean $=0-t\cdot0=0$. Then
$\mathbb E B_tB_s=\mathbb E W_tW_s-t\mathbb E W_sW_1-s\mathbb E W_tW_1+ts\mathbb E W_1^2
=\min(t,s)-ts-st+ts=\min(t,s)-ts.$

**W4 (analogue of Ex. 10).** If $X\sim\mathcal N(m,v)$, find $\mathbb E e^{X}$.
*Solution.* $=e^{m+v/2}$ (T3). The distribution is log-normal.

**W5 (analogue of Ex. 11/17).** Show $X_t=\frac{1}{\sqrt c}W_{ct}$ is a standard BM.
*Solution.* Gaussian, mean $0$, and $\mathbb E X_sX_t=\frac1c\min(cs,ct)=\min(s,t)$.
By T7 it is BM.

---

## Game plan

### Exercise 5
- (a) Apply T1 with $W_t\sim\mathcal N(0,t)$.
- (b) $W_t+W_s$ is Gaussian (T5); its variance uses $\mathbb E W_sW_t=\min(s,t)$
  (T2). Then T1.
- (c) Direct application of T2.
- (d) Use the **multivariate characteristic function** T1 with
  $\Sigma_{ij}=\min(t_i,t_j)$.
- *Guiding questions:* in (d), why is $\sum_i c_iW_{t_i}$ Gaussian? What is its
  variance?

### Exercise 6
- (a) Linearity of Gaussian (T5) for the "Gaussian" part; compute mean and
  covariance by bilinearity (exactly like W3).
- (b) Match the law of $B_t=(1-t)W(t/(1-t))$ to the bridge using T6/T7; compute its
  variance and compare with (a), and check $B_0=B_1=0$.
- (c) With covariance known, $B_t\sim\mathcal N(0,t(1-t))$; write the CDF (an
  integral of the Gaussian density).
- *Guiding question:* which of the four BM symmetries (Prop. 1.5) underlies the
  time-change formula in (b)?

### Exercise 9
- (a) T3 with $t$ fixed.
- (b) T4: write $W_{s_1}\pm W_{s_2}$ as Gaussians, get their variances, and use
  $\mathbb E\cos(\sigma Z)=\operatorname{Re}\mathbb E e^{i\sigma Z}$ with T1.

### Exercise 10
- $S_t=e^{t\mu}e^{\sigma W_t}$; $t\mu$ is deterministic. Identify $\sigma W_t$ as
  $\mathcal N(0,\sigma^2t)$ and use T3 / log-normal tools.
- (a) mean and variance from the log-normal formulas.
- (b) the pdf is the log-normal density with the right $(m,v)$.

### Exercise 11
- For each of the four properties, follow **T7**: mean $0$ + covariance match.
  Beware: rescaling $X_t=c^{-1/2}W_{ct}$; time reversal $W_{1-t}-W_1$; inversion
  $tW_{1/t}$. Show Gaussianity and the covariance.
- *Guiding question:* where exactly is the independence of **increments** used in
  the shifting property (ii)?

### Exercise 17
- Substitute $s\mapsto\alpha s$, $t\mapsto\alpha t$ in the fBm covariance (1.26) and
  factor out $\alpha^{2H}$. Then invoke T7 (centred Gaussian, matching covariance).

---

## Pitfalls

- **Index order in $\min$** — $\min(t_i,t_j)$ is symmetric, but write both orders
  when $t_i>t_j$.
- **Variance of a sum is not the sum of variances** unless means/covariances are
  handled: use full bilinearity (T2).
- **$\mathbb E e^{\sigma W_t}\ne e^{\sigma\mathbb E W_t}$**; the $+\frac12\sigma^2 t$
  term is the whole point.
- **"Equal in law" ≠ "pathwise equal".** Prop. 1.5(ii) needs independence of the
  shifted increments from the past — covariance matching alone is not enough there.

---

## Numerical check (optional)

Sample many BM paths; for Ex. 5 compare the empirical
$\mathbb E e^{iW_t}$ against $e^{-t/2}$; for Ex. 6 check
$\operatorname{Cov}(B_t,B_s)$ on a grid against $\min(t,s)-ts$; for Ex. 10 check the
log-normal histogram against the density you derived.

