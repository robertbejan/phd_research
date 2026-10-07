# 04 — Spectral density & the Green–Kubo formula

**Covers Exercises 7 and 16.**
Book sections: 1.2 (Bochner Thm 1.1, spectral density (1.7)–(1.8), correlation time,
Example 1.5, Green–Kubo (1.14)–(1.15)).

---

## The tools

### T1 — The Fourier pair (book convention)
$$S(\omega)=\frac{1}{2\pi}\int_{-\infty}^{\infty} e^{-i\omega t}C(t)\,dt,
\qquad
C(t)=\int_{-\infty}^{\infty} e^{i\omega t}S(\omega)\,d\omega .$$
$S(\omega)\ge0$ (Bochner), even in $\omega$ for real $C$.

### T2 — The master transform (learn this one cold)
$$\int_{-\infty}^{\infty} e^{-i\omega t}e^{-\alpha|t|}\,dt=\frac{2\alpha}{\alpha^2+\omega^2}.$$
Hence for $C(t)=\frac{D}{\alpha}e^{-\alpha|t|}$ (Example 1.5):
$$S(\omega)=\frac{D}{\pi}\,\frac{1}{\omega^2+\alpha^2}\quad(\text{Cauchy/Lorentz}).$$

### T3 — Linearity
$\mathcal F[C_1+C_2]=\mathcal F[C_1]+\mathcal F[C_2]$. So a **sum of exponentials**
gives a **sum of Lorentzians** (this is the whole of Exercise 7a).

### T4 — Cosine/sine integrals on the half-line
$$\int_0^\infty e^{-\alpha t}\cos(\beta t)\,dt=\frac{\alpha}{\alpha^2+\beta^2},
\qquad
\int_0^\infty e^{-\alpha t}\sin(\beta t)\,dt=\frac{\beta}{\alpha^2+\beta^2}.$$
For a product $e^{-\gamma t}\cos(\delta t)$ etc., combine with the evenness of $|t|$
and T2.

### T5 — Correlation time
$$\tau_{cor}=\frac{1}{C(0)}\int_0^\infty C(t)\,dt
=\frac{1}{\mathbb E X_0^2}\int_0^\infty\mathbb E[X_tX_0]\,dt .$$
Slower decay $\Rightarrow$ larger $\tau_{cor}$; non-integrable $C$ $\Rightarrow$
$\tau_{cor}=\infty$.

### T6 — Green–Kubo (the diffusion coefficient)
For a mean-zero second-order stationary $X_t$ with $C\in L^1(0,\infty)$ (the key
hypothesis — this is the assumption you must **check**):
$$D=\int_0^\infty C(t)\,dt=\int_0^\infty \mathbb E[X_tX_0]\,dt,
\qquad
\mathbb E\Big(\int_0^tX_s\,ds\Big)^2\approx 2Dt\ \ (t\to\infty).$$
*Exercise 7b* asks exactly for this with $X_t$ = the process with $R(t)$ given.
(Note: the exercise says "Theorem 1.3"; the relevant statement providing the
integrable-correlation hypothesis is the mean-square ergodic result of §1.2 —
Prop. 1.3. Cite the hypothesis $C\in L^1(0,\infty)$ explicitly.)

### T7 — Mean-square displacement from a correlation (Ex. 16b)
If $X(t)=\int_0^tY(s)\,ds$ with stationary velocity $Y$, then
$$\mathbb E\big(X(t)^2\big)=\int_0^t\!\!\int_0^t R(u-v)\,du\,dv
=2\int_0^t (t-u)R(u)\,du .$$
For large $t$ this tends to $2Dt$ with $D=\int_0^\infty R$ (T6). To study the
limit, insert $R$ and integrate by parts / use T4.

---

## Warm-ups (solved)

**W1 (analogue of Ex. 7a).** Spectral density of $C(t)=e^{-2|t|}$.
*Solution.* By T2 with $\alpha=2$, $D=1$: $\int e^{-i\omega t}e^{-2|t|}dt=\frac{4}{4+\omega^2}$,
so $S(\omega)=\frac{1}{2\pi}\cdot\frac{4}{4+\omega^2}=\frac{2}{\pi(4+\omega^2)}$.

**W2 (correlation time, analogue of Ex. 7a).**
*Solution.* $C(0)=1$ and $\int_0^\infty e^{-2t}dt=\tfrac12$, so $\tau_{cor}=\tfrac12$.

**W3 (Green–Kubo, analogue of Ex. 7b).**
$D$ for $C(t)=e^{-2|t|}$.
*Solution.* $D=\int_0^\infty e^{-2t}dt=\tfrac12$.

**W4 (a damped-cosine transform, warm-up for Ex. 16a).**
Compute $\int_0^\infty e^{-\gamma t}\cos(\delta t)\,dt$.
*Solution.* By T4, $=\gamma/(\gamma^2+\delta^2)$.

---

## Game plan

### Exercise 7
- (a) Apply **T3 + T2**: each term $\frac{\lambda_j^2}{\alpha_j}e^{-\alpha_j|t|}$ maps
  to $\frac{\lambda_j^2}{\pi}\frac{1}{\omega^2+\alpha_j^2}$. Sum them. Then
  $\tau_{cor}=\frac{1}{R(0)}\int_0^\infty R(t)dt$ (**T5**); integrate each exponential.
- (b) **Check the hypothesis** $R\in L^1(0,\infty)$ (exponentials decay — explain).
  Then **T6**: $D=\int_0^\infty R(t)dt$; integrate term by term.
- (c) Take $N\to\infty$: what condition on $\{\alpha_j,\lambda_j\}$ makes the sums
  $\sum\lambda_j^2/\alpha_j$ and $\sum\lambda_j^2/\alpha_j^2$ converge? (A
  summability condition.)

### Exercise 16
- The velocity autocorrelation is
  $R(t)=e^{-\gamma|t|}\big(\cos(\delta|t|)-\frac1\delta\sin(\delta|t|)\big)$,
  $\delta=\sqrt{\omega_0^2-\gamma^2}$ (verified from the book).
- (a) **Spectral density**: use T2/T4 on $e^{-\gamma|t|}\cos(\delta|t|)$ and
  $e^{-\gamma|t|}\sin(\delta|t|)$ (split $|t|$ into $\pm$). Combine into
  $S(\omega)=\frac1{2\pi}\int e^{-i\omega t}R(t)dt$. Expect a rational function of
  $\omega$; simplify using $\gamma^2+\delta^2=\omega_0^2$.
- (b) **Mean-square displacement** via **T7**: compute
  $\mathbb E(X(t)^2)=2\int_0^t(t-u)R(u)du$, then take $t\to\infty$; the slope is $2D$
  with $D=\int_0^\infty R(u)du$ (**T6**, and you can reuse the T4 integrals).
- *Guiding questions:* why must $\gamma>0$ for $D$ to be finite? What is the role of
  the $\cos/\sin$ combination — does it change the $t\to\infty$ slope?

---

## Pitfalls

- **Where the $\frac{1}{2\pi}$ lives.** Book convention: it multiplies the
  integral defining $S(\omega)$, *not* the one defining $C(t)$.
- **$|t|$ vs $t$.** All these $C$ are even; integrate over $t>0$ and double, or use T2
  directly, but keep track of the factor $2$.
- **Checking vs assuming integrability.** Ex. 7b asks you to *show* the hypothesis
  holds; don't skip it.
- **Algebraic simplification** in Ex. 16a is where marks are lost — factor
  $\omega^2+\gamma^2\pm\ldots$ carefully and use $\gamma^2+\delta^2=\omega_0^2$.

---

## Numerical check (optional)

Compute $S(\omega)$ numerically by FFT of a long simulated OU path and compare with
your closed form; for Ex. 16 integrate $R$ numerically (`scipy.integrate.quad`) to
confirm $D$ and the large-$t$ slope $2D$ from the simulated mean-square displacement.

