# 04 — The Gaussian (normal) distribution, completely

**Read this if:** you want to understand why $\mathbb E e^{i\theta X}
=e^{-(\theta\sigma)^2/2}$ and why "linear maps of Gaussians are Gaussian".

## 1. Standard normal

$X\sim\mathcal N(0,1)$ means $X$ has the **density**
$$p(x)=\frac{1}{\sqrt{2\pi}}\,e^{-x^{2}/2},\qquad x\in\mathbb R .$$
**Why $\sqrt{2\pi}$?** Because the total probability must be $1$:
$$\int_{-\infty}^{\infty}e^{-x^{2}/2}dx=\sqrt{2\pi}.$$
(The proof is in file 01 §6 and is worth doing once.)

Facts to memorise: $\mathbb EX=0$, $\operatorname{Var}(X)=1$, $\mathbb EX^2=1$,
$p$ is symmetric so $\mathbb EX^3=0$, and $\mathbb EX^4=3$.

## 2. General normal $\mathcal N(\mu,\sigma^2)$

**Standardisation:** if $X\sim\mathcal N(\mu,\sigma^2)$ then
$$Z=\frac{X-\mu}{\sigma}\sim\mathcal N(0,1),\qquad\text{i.e. } X=\mu+\sigma Z .$$
So *everything* about any normal is computed by turning it into the standard one.
$$\text{density: }p(x)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp\!\Big(-\frac{(x-\mu)^2}{2\sigma^2}\Big).$$
$\mathbb EX=\mu$, $\operatorname{Var}(X)=\sigma^2$. The **CDF** is
$\Phi(x)=\int_{-\infty}^{x}p(u)du$ for the standard case; it has no elementary
formula, it is a table/`scipy.stats.norm.cdf` object.

*Worked:* $\mathbb E e^{\sigma W_t}$ where $W_t\sim\mathcal N(0,t)$. Here
$\mu=0$, and the variable is $\sigma X$ with $X\sim\mathcal N(0,t)$ (variance $t$).
Hence $\sigma X\sim\mathcal N(0,\sigma^2t)$ and by §3 below the answer is
$e^{\sigma^2t/2}$. *(This is Exercise 9a.)*

## 3. The two transform identities (the most used formulas in the chapter)

For $X\sim\mathcal N(\mu,\sigma^2)$ and any real $\theta$:
$$\boxed{\ \mathbb E\,e^{i\theta X}=\exp\!\Big(i\theta\mu-\tfrac12\theta^2\sigma^2\Big)\ }
\qquad\text{(characteristic function)}$$
$$\boxed{\ \mathbb E\,e^{sX}=\exp\!\Big(s\mu+\tfrac12s^2\sigma^2\Big)\ }
\qquad\text{(moment-generating function)}$$
The second is the first with $\theta=is$ (formally). **Both follow from the
Gaussian integral, not from Taylor.**

*Worked:* $\mathbb E e^{iW_3}=e^{-3/2}$; $\mathbb E e^{2X}=e^{2}$ for
$X\sim\mathcal N(0,1)$. Since $\left|\mathbb E e^{i\theta X}\right|\le1$ always, the
$\theta^2\sigma^2/2$ term must be non-negative — a free sanity check.

**Real part = cosine formula** (used in Exercise 9b):
$$\mathbb E\cos(\theta X)=e^{-\theta^2\sigma^2/2},\qquad
\mathbb E\sin(\theta X)=0 \quad\text{(when }\mu=0).$$

## 4. Multivariate (vector) Gaussian

A **random vector** $X=(X_1,\dots,X_n)$ is **Gaussian** if every linear combination
$c_1X_1+\cdots+c_nX_n$ is a normal random variable. Equivalently it is described by
just two objects:
- the **mean vector** $\mu_i=\mathbb EX_i$,
- the **covariance matrix** $\Sigma_{ij}=\operatorname{Cov}(X_i,X_j)$ (an
  $n\times n$ symmetric, positive semi-definite matrix — file 05 §6).

Density (when $\Sigma$ is invertible):
$$p(x)=(2\pi)^{-n/2}(\det\Sigma)^{-1/2}
\exp\!\Big(-\tfrac12(x-\mu)^\top\Sigma^{-1}(x-\mu)\Big).$$

**Characteristic function** (the version that never breaks, even if $\det\Sigma=0$):
$$\boxed{\ \mathbb E\,e^{\,i\,t\cdot X}=\exp\!\Big(i\,t\cdot\mu-\tfrac12\,t^\top\Sigma\,t\Big)\ }$$
where $t\cdot X=\sum_i t_iX_i$ and $t^\top\Sigma t=\sum_{i,j}t_i t_j\Sigma_{ij}$.

*Worked:* for $X=(W_1,W_3)$ with $W$ Brownian, $\Sigma=\begin{pmatrix}1&1\\1&3\end{pmatrix}$,
so $\mathbb E e^{i(t_1W_1+t_3W_3)}=\exp\left(-\tfrac12(t_1^2+2t_1t_3+3t_3^2)\right)$.
*(This is Exercise 5d.)*

## 5. The five facts that make Gaussians easy

1. **A Gaussian vector is completely determined by $(\mu,\Sigma)$.** Mean and
   covariance *are* the whole law.
2. **Linear maps preserve Gaussianity.** If $X$ is Gaussian and $A$ is a fixed
   matrix, $b$ a fixed vector, then $Y=AX+b$ is Gaussian with
   $$\mu_Y=A\mu_X+b,\qquad \Sigma_Y=A\Sigma_XA^\top .$$
   *(No integration needed — that is the point.)*
3. **Uncorrelated $\iff$ independent** for *jointly* Gaussian variables
   ($\Sigma_{ij}=0$ for $i\ne j$ $\iff$ $p$ factorises).
4. **Sums and differences** of jointly Gaussian variables are Gaussian: e.g.
   $W_s+W_t\sim\mathcal N(0,s+t+2\min(s,t))$. Compute the variance by bilinearity.
5. **Wick/Isserlis:** for zero-mean jointly Gaussian variables,
   $\mathbb E[X_1X_2X_3X_4]=\mathbb E[X_1X_2]\mathbb E[X_3X_4]
   +\mathbb E[X_1X_3]\mathbb E[X_2X_4]+\mathbb E[X_1X_4]\mathbb E[X_2X_3]$
   (sum over the three ways of pairing). Hence $\mathbb E W_t^4=3t^2$.

## 6. Gaussian processes

A **Gaussian process** is a family $(X_t)$ such that **every finite collection**
$(X_{t_1},\dots,X_{t_n})$ is a Gaussian vector. It is therefore defined by two
functions:
- mean $m(t)=\mathbb EX_t$,
- **covariance function** $R(t,s)=\mathbb E[(X_t-m(t))(X_s-m(s))]$,

with $R$ symmetric and positive semi-definite (file 06 §8). **Kolmogorov's
extension theorem** says: pick any such $R$, and a Gaussian process exists. That is
why the book can *define* processes by giving $R$ alone (Exercises 1.23–1.26).

> **Handy slogan:** *"mean + covariance = everything"* for Gaussian processes. This
> single slogan proves Exercises 6b, 11, 17.

## 7. Micro-drills

1. $X\sim\mathcal N(3,4)$: find $\mathbb EX$, $\operatorname{Var}X$, $\mathbb Ee^{X}$.
   *Ans.* $3$; $4$; $e^{3+2}=e^5$.
2. $X\sim\mathcal N(0,1)$: compute $\mathbb E\cos(2X)$. *Ans.* $e^{-2}$.
3. If $X,Y$ jointly Gaussian with $\operatorname{Cov}(X,Y)=0$, are they independent?
   *Ans.* Yes (only for the *jointly* Gaussian case).
4. $Z_t=\int_0^tW_sds$: why Gaussian? *Ans.* Riemann sums are linear combinations of
   the Gaussian variables $W_{s_i}$, and limits of Gaussians are Gaussian (fact 2,
   plus closedness in $L^2$).

## Where you need all of this

| Fact | Toolkit file / exercise |
|---|---|
| Gaussian vector = (mean, covariance) | 02 §T1, T7 — Exercises 5, 6, 11, 17 |
| linear maps of Gaussians are Gaussian | 02 §T5, 03 §T2 — Exercises 6, 8, 13 |
| characteristic function $e^{i\theta\mu-\theta^2\sigma^2/2}$ | 02 §T1 — Exercises 5, 9 |
| MGF $e^{s\mu+s^2\sigma^2/2}$ | 02 §T3 — Exercises 9, 10 |
| sums/differences of Brownian variables | 02 §T2, §T4 — Exercises 5, 6, 9 |
| Gaussian process defined by a covariance $R(t,s)$ | 07 §T1, 08 §T1 — Exercises 23–28 |
| pinned Gaussian process = bridge | 03 §T6 — Exercises 6, 15 |
| Wick's theorem for 4th moments | Exercise 18's $\mathbb E|W_t-W_s|^4=3(t-s)^2$ |

**The one line to remember from this file:**
$$\text{constant mean }+\text{ covariance depending only on the lag}
\ \Longrightarrow\ \text{stationary, if Gaussian.}$$
