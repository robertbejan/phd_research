# 07 — Fourier series and the Fourier transform

**Read this if:** $\hat f(\omega)$, $S(\omega)$, "spectral density", "Parseval", or
$\int_{-1}^{1}\cos(\pi t)\cos(2\pi t)dt$ are not routine.

## 1. The idea in one sentence

Fourier analysis writes a function as a **superposition of pure oscillations**
$e^{i\omega t}$; the "amount" of each frequency is the **spectrum**. Many hard
problems become easy in the spectrum.

- **Fourier series** — periodic functions / functions on an interval; frequencies
  are **discrete** ($\omega=n$).
- **Fourier transform** — functions on all of $\mathbb R$; frequencies are
  **continuous** ($\omega\in\mathbb R$).

(Series ↔ discrete spectrum is the same dichotomy as process ↔ discrete
Karhunen–Loève eigenvalues in file 08.)

## 2. Fourier series on $[0,1]$

The family
$$\{1,\ \sqrt2\cos(2\pi nt),\ \sqrt2\sin(2\pi nt),\ n=1,2,\dots\}$$
is **orthonormal in $L^2(0,1)$**. (Use the orthogonality integrals of file 02 §5;
note $\int_0^1\cos^2(2\pi nt)dt=\tfrac12$, not $1$.) So
$$f(t)=a_0+\sum_{n\ge1}\big[a_n\sqrt2\cos(2\pi nt)+b_n\sqrt2\sin(2\pi nt)\big],$$
with coefficients by **projection**: $a_n=\langle f,\sqrt2\cos(2\pi n\cdot)\rangle$.

**Where does $\sqrt2$ come from?** $\cos(2\pi nt)$ has squared norm $\tfrac12$;
multiplying by $\sqrt2$ makes it norm $1$. Forgetting this factor is the single
most common error in this chapter.

**Dirichlet vs Neumann — which basis?** On $[0,L]$:
- function must vanish at both ends, $f(0)=f(L)=0$ (**Dirichlet**): use **sines**
  $\sin(n\pi t/L)$;
- derivative must vanish at both ends, $f'(0)=f'(L)=0$ (**Neumann**): use
  **cosines**.

*Worked.* The Brownian-motion eigenfunctions are
$\sqrt2\sin\big((n-\tfrac12)\pi t\big)$: sines, but at **half-integer** frequencies,
so that $e(0)=0$ (Dirichlet at $0$) while $e'(1)=0$ (Neumann at $1$). Mixed
boundary conditions are exactly why the frequencies are half-integers, and why the
Brownian eigenvalues $\lambda_n=[(n-\tfrac12)\pi]^{-2}$ are *not* the bridge's
$\lambda_n=(n\pi)^{-2}$.

## 3. The Fourier transform and its properties

Book convention:
$$\hat f(\omega)=\int_{-\infty}^{\infty}e^{-i\omega t}f(t)\,dt,\qquad
f(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}e^{i\omega t}\hat f(\omega)\,d\omega .$$

| Operation on $f(t)$ | Effect on $\hat f(\omega)$ |
|---|---|
| $f$ real **and even** | $\hat f$ real and even |
| shift $f(t-a)$ | $e^{-i\omega a}\hat f(\omega)$ |
| scale $f(\alpha t)$ | $\left|\alpha\right|^{-1}\hat f(\omega/\alpha)$ |
| derivative $f'$ | $i\omega\hat f$ |
| convolution $f*g$ | $\hat f\,\hat g$ |

**The master transform (learn cold):**
$$\boxed{\ \int_{-\infty}^{\infty}e^{-i\omega t}e^{-\alpha\left|t\right|}dt
=\frac{2\alpha}{\alpha^2+\omega^2}\ }\qquad(\alpha>0)$$
**Derivation (do it once):**
$$\int_{-\infty}^{\infty}\!\!e^{-i\omega t}e^{-\alpha|t|}dt
=2\operatorname{Re}\int_0^\infty e^{-(\alpha+i\omega)t}dt
=2\operatorname{Re}\frac{1}{\alpha+i\omega}
=\frac{2\alpha}{\alpha^2+\omega^2},$$
using $\int_0^\infty e^{-zt}dt=1/z$ (verify by differentiating both sides in $t$).

**Gaussian to Gaussian:** $\int e^{-i\omega t}e^{-t^2/2}dt=\sqrt{2\pi}e^{-\omega^2/2}$.

## 4. The book's convention for the spectral density

Equations (1.7)–(1.8) put $\tfrac{1}{2\pi}$ on the **forward** transform:
$$S(\omega)=\frac{1}{2\pi}\int_{-\infty}^{\infty}e^{-i\omega t}C(t)\,dt,\qquad
C(t)=\int_{-\infty}^{\infty}e^{i\omega t}S(\omega)\,d\omega .$$
- For real, even $C$ the transform is real and even, and using the cosine form,
  $$S(\omega)=\frac{1}{\pi}\int_0^\infty C(t)\cos(\omega t)\,dt .$$
- **Bochner / Wiener–Khinchin:** $S(\omega)\ge0$ and $\int S(\omega)d\omega=C(0)$
  (total variance). *"Spectrum = how the variance is spread over frequencies."*
- **Correlation time:** $\tau_{cor}=\frac{1}{C(0)}\int_0^\infty C(t)dt$ — the typical
  memory time of the process.

*Worked (Exercise 7a).* For $C(t)=e^{-2|t|}$ the master transform with $\alpha=2$
gives $4/(4+\omega^2)$, so $S(\omega)=\frac{1}{2\pi}\cdot\frac{4}{4+\omega^2}
=\frac{2}{\pi(4+\omega^2)}$.

## 5. Parseval, and the half-line integrals

**Parseval (Plancherel):** $\int\left|f\right|^2=\frac{1}{2\pi}\int\left|\hat f\right|^2$
— "energy is conserved". Discrete analogue:
$\sum_n\left|\langle f,e_n\rangle\right|^2=\left\|f\right\|^2$.

**Half-line integrals (used in toolkit file 04 — Exercises 7 and 16):**
$$\int_0^\infty e^{-\alpha t}\cos(\beta t)\,dt=\frac{\alpha}{\alpha^2+\beta^2},
\qquad
\int_0^\infty e^{-\alpha t}\sin(\beta t)\,dt=\frac{\beta}{\alpha^2+\beta^2}.$$
*Derivation of the first:* $\int_0^\infty e^{-(\alpha-i\beta)t}dt
=\frac{1}{\alpha-i\beta}=\frac{\alpha+i\beta}{\alpha^2+\beta^2}$; take real parts.

## 6. The delta "function" (a notation, used carefully)

$\delta$ is not a function; it is the rule $\int\delta(t-a)\varphi(t)dt=\varphi(a)$.
It is what "the transform of $f\equiv1$" means. Here it is pure bookkeeping: when a
kernel with a **corner** is differentiated twice, a delta appears, e.g.
$$\frac{\partial^2}{\partial t^2}e^{-a\left|t-s\right|}
=a^2e^{-a\left|t-s\right|}-2a\,\delta(t-s).$$
That is how the absolute-value kernels of Exercises 24, 28 become ODEs (file 08 §5).

## 7. Micro-drills

1. Compute $\int_0^1\cos(2\pi t)dt$ and $\int_0^1\cos^2(2\pi t)dt$.
   *Ans.* $0$ and $\tfrac12$ — hence the $\sqrt2$ normalisation.
2. Fourier transform of $e^{-3\left|t\right|}$. *Ans.* $6/(9+\omega^2)$.
3. Give $S(\omega)$ for $C(t)=\frac{D}{\alpha}e^{-\alpha\left|t\right|}$.
   *Ans.* $\frac{D}{\pi}\frac{1}{\omega^2+\alpha^2}$.
4. Why is the Neumann condition $e'(1)=0$ the natural one for $\min(t,s)$?
   *Ans.* Differentiating $\min(t,s)$ in $t$ gives a step function that is $0$ for
   $t>s$; matching the equation at $t=1$ forces $e'(1)=0$ (file 08 §5).
