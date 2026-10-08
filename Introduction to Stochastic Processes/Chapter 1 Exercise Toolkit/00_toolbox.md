# 00 — Shared toolbox

These are the tools used again and again across Chapter 1. Learn them once and
most exercises become bookkeeping. Everything is stated for real-valued random
variables unless noted.

> **Prerequisites.** Every line here is used by *every* exercise, so this is the very
> first file to make sense of. If anything below is unclear, read
> `Primer/00_START_HERE.md` (symbol dictionary + glossary), then
> `Primer/03_probability_primer.md` §2–§6 (expectation, variance, covariance,
> independence, inequalities) and `Primer/04_gaussian_primer.md` §1–§5 (the normal
> distribution, characteristic functions, linear maps of Gaussians).

## 1. Expectation and covariance

- **Linearity** (always true): $\mathbb E[aX+bY]=a\,\mathbb EX+b\,\mathbb EY$.
- **Mean of a sum**: $\mathbb E\sum_i X_i=\sum_i \mathbb E X_i$.
- **Covariance**: $\operatorname{Cov}(X,Y)=\mathbb E[(X-\mu_X)(Y-\mu_Y)]=\mathbb E[XY]-\mu_X\mu_Y$.
- **Variance of a sum**:
  $$\operatorname{Var}\!\Big(\sum_i X_i\Big)=\sum_i\operatorname{Var}(X_i)+2\sum_{i<j}\operatorname{Cov}(X_i,X_j).$$
- **Independent $\Rightarrow$ uncorrelated** (the converse is *false*):
  $X\perp Y \Rightarrow \operatorname{Cov}(X,Y)=0$.
- **Bilinearity**: $\operatorname{Cov}(aX+bY,Z)=a\operatorname{Cov}(X,Z)+b\operatorname{Cov}(Y,Z)$.
- **Constant pulled out**: $\operatorname{Var}(aX)=a^2\operatorname{Var}(X)$.

### Warm-up
Let $\xi_1,\xi_2$ be uncorrelated, mean $0$, variance $\sigma^2$. Compute
$\operatorname{Var}(\xi_1+2\xi_2)$.
$\rhd$ $=\sigma^2+4\sigma^2=5\sigma^2$.

## 2. The two universal inequalities

- **Cauchy–Schwarz**: $(\mathbb E[XY])^2\le \mathbb E[X^2]\,\mathbb E[Y^2]$.
  *This single inequality proves Exercise 19 and powers many others.*
- **Jensen / Markov / Chebyshev**: for $X\ge0$, $\mathbb P(X\ge a)\le \mathbb E X/a$;
  $\operatorname{Var}(X)\to0$ $\Rightarrow$ $X\to\mathbb E X$ in $L^2$ (hence in probability).

## 3. Gaussian random variables (the workhorse)

For $X\sim\mathcal N(\mu,\sigma^2)$:

- **Density**: $p(x)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp\!\big(-\frac{(x-\mu)^2}{2\sigma^2}\big)$.
- **Characteristic function** (this is the key identity for Ex. 5, 6, 10):
  $$\mathbb E e^{i\theta X}=\exp\!\Big(i\theta\mu-\tfrac12\theta^2\sigma^2\Big),\qquad \theta\in\mathbb R.$$
- **Moment generating function** (take $\theta=-is$ formally):
  $$\mathbb E e^{sX}=\exp\!\Big(s\mu+\tfrac12\sigma^2 s^2\Big).$$
- **Second moment**: $\mathbb E X^2=\mu^2+\sigma^2$, hence $\operatorname{Var}(X)=\sigma^2$.
- **Wick's theorem / Isserlis**: for joint Gaussian, $\mathbb E[XY]=\operatorname{Cov}(X,Y)$
  when means vanish, and $\mathbb E[X_1X_2X_3X_4]=\sum$ over pairings of covariances.

### Multivariate Gaussian
If $X\sim\mathcal N(\mu,\Sigma)$ ($\Sigma$ = covariance matrix), then for a vector $t$:
$$\mathbb E\,e^{\,i\,t\cdot X}=\exp\!\Big(i\,t\cdot\mu-\tfrac12 t^\top\Sigma\,t\Big).$$
Gaussian vectors are characterised by $(\mu,\Sigma)$, and **linear maps of a Gaussian
vector are Gaussian**: $AX+b\sim\mathcal N(A\mu+b,A\Sigma A^\top)$.

### Warm-up
$X\sim\mathcal N(0,1)$, find $\mathbb E e^{i X}$ and $\mathbb E e^{2X}$.
$\rhd$ $e^{-1/2}$ and $e^{2}=e^{0+\frac12\cdot4}$.

## 4. Log-normal (for Ex. 10)

If $X\sim\mathcal N(m,v)$ then $Y=e^{X}$ is **log-normal**:
$$\mathbb E Y=e^{m+v/2},\quad \operatorname{Var}(Y)=(e^{v}-1)e^{2m+v},\quad
p_Y(y)=\frac{1}{y\sqrt{2\pi v}}\exp\!\Big(-\frac{(\ln y-m)^2}{2v}\Big),\ y>0.$$

## 5. Brownian motion facts

- $W_0=0$; $W_t\sim\mathcal N(0,t)$; increments independent & stationary.
- $\mathbb E[W_sW_t]=\min(s,t)$.
- $\mathbb E[(W_s-W_t)^2]=|s-t|$; $\mathbb E[W_t^4]=3t^2$.
- **Gaussian stability of integrals**: $\int_0^t W_s\,ds$, $\int_0^t e^{-s}W_s\,ds$,
  etc., are limits of Gaussian Riemann sums, hence **Gaussian** processes. Store
  this; it answers Ex. 8 and 13 "for free".

## 6. Stationarity (Definitions to have at your fingertips)

- **Strict (Def. 1.5):** all finite-dimensional distributions are invariant under
  time shift $t\mapsto t+s$.
- **Weak / second-order (Def. 1.6):** $\mathbb E X_t=\mu$ constant and
  $\operatorname{Cov}(X_t,X_s)=C(t-s)$ depends only on the **time difference**.
- Strict + finite second moment $\Rightarrow$ weak. Converse holds for Gaussian.
- **Symmetry**: for a real process $C(-t)=C(t)$, $C(t,s)=C(s,t)$.

## 7. Fourier pair used by the book

The book fixes the convention (Eqs. (1.7)–(1.8)):
$$S(\omega)=\frac{1}{2\pi}\int_{-\infty}^{\infty} e^{-i\omega t}C(t)\,dt,
\qquad
C(t)=\int_{-\infty}^{\infty} e^{i\omega t}S(\omega)\,d\omega.$$
Bochner's theorem (Thm 1.1) guarantees $S(\omega)\ge0$.

**Integrals you will need repeatedly:**
$$\int_0^\infty e^{-\alpha t}\cos(\beta t)\,dt=\frac{\alpha}{\alpha^2+\beta^2},
\qquad
\int_0^\infty e^{-\alpha t}\sin(\beta t)\,dt=\frac{\beta}{\alpha^2+\beta^2}.$$
Consequence: $\displaystyle \int_{-\infty}^{\infty} e^{-i\omega t}e^{-\alpha|t|}\,dt
=\frac{2\alpha}{\alpha^2+\omega^2}$.

## 8. Green–Kubo / diffusion coefficient (Eqs. (1.14)–(1.15))

For a mean-zero second-order stationary $X_t$ with $C\in L^1(0,\infty)$,
$$D=\int_0^\infty C(t)\,dt=\int_0^\infty \mathbb E[X_tX_0]\,dt
\quad\text{and}\quad \mathbb E\Big(\int_0^t X_s\,ds\Big)^2\approx 2Dt.$$
This is *the* formula for Ex. 7(b) and Ex. 16(b).

## 9. $L^2$ / inner-product toolkit (for Ex. 20–26)

- $\langle f,g\rangle=\int_0^1 f(t)\overline{g(t)}\,dt$; $\|f\|^2=\langle f,f\rangle$.
- Operator $(Rf)(t)=\int_0^1 R(t,s)f(s)\,ds$.
- $R$ **self-adjoint** $\iff$ $\langle Rf,g\rangle=\langle f,Rg\rangle$ $\iff$
  kernel satisfies $R(t,s)=\overline{R(s,t)}$ (real symmetric kernel).
- $R$ **nonnegative** $\iff$ $\langle Rf,f\rangle\ge0$; then all eigenvalues $\ge0$.
- Eigenfunctions for distinct eigenvalues of a self-adjoint operator are orthogonal.

## 10. Pitfalls master-list

1. **Independent vs uncorrelated** — always justify which one you use.
2. **$\min(s,t)$ order** — when a sum/double integral involves $\min$, split the
   domain so that $s\le t$ and $s\ge t$ are handled separately.
3. **Fubini** — swapping $\mathbb E$ and $\int$ requires integrability; here it is
   always fine, but say it.
4. **$\frac{1}{2\pi}$ placement** — the book puts it in $S(\omega)$, not in $C(t)$.
5. **Normalising eigenfunctions** — check $\int_0^1 e_n^2=1$ before you use them.
6. **Strict vs weak stationarity** — a statement about *all* FDDs differs from a
   statement about the first two moments.
