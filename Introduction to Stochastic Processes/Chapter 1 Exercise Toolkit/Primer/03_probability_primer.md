# 03 — Probability from scratch

**Read this if:** you cannot confidently explain *expectation*, *variance*,
*independence*, *covariance* or *convergence in $L^2$* to a friend.

## 1. The setup, in words

- An **experiment** has a set of possible outcomes $\Omega$ (the **sample space**).
- An **event** $A$ is a subset of $\Omega$; $\mathbb P(A)\in[0,1]$ is its
  **probability**. $\mathbb P(\Omega)=1$.
- A **random variable (RV)** $X$ is a function on $\Omega$: it assigns a **number**
  to each outcome. Written $X:\Omega\to\mathbb R$.

> Think of "rolling a die" once: $\Omega=\{1,\dots,6\}$, and $X=$ the number shown
> is the identity map. A random variable is just "a number determined by chance".

**Distribution**: the rule giving the probabilities of the values of $X$. Two ways:
- **CDF (cumulative distribution function):** $F_X(x)=\mathbb P(X\le x)$.
- **Density $p_X$** (continuous case): $F_X(x)=\int_{-\infty}^{x}p_X(u)\,du$, so
  $\mathbb P(a\le X\le b)=\int_a^b p_X(u)du$. A density must satisfy $p_X\ge0$ and
  $\int_{\mathbb R}p_X=1$.

*Standard example:* $X\sim\mathcal N(0,1)$ (see file 04) has
$p_X(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2}$.

## 2. Expectation ("average")

$$\mathbb E X=\int_{\mathbb R}x\,p_X(x)\,dx\qquad(\text{continuous case}).$$
**In words:** the long-run average of $X$ over many independent repetitions.

**Properties** (memorise these five):
1. **Linearity (always true, no assumptions):**
   $\mathbb E(aX+bY)=a\mathbb E X+b\mathbb E Y$, and $\mathbb E c=c$.
2. **LOTUS** ("law of the unconscious statistician"): $\mathbb E g(X)=\int g(x)p_X(x)dx$ —
   you do **not** need the density of $g(X)$.
3. If $X\ge0$ then $\mathbb E X\ge0$.
4. $\left|\mathbb E X\right|\le\mathbb E\left|X\right|$.
5. If $X,Y$ are independent, $\mathbb E[XY]=\mathbb E X\,\mathbb E Y$ (and conversely
   no — see below).

*Worked:* $\mathbb E X^2$ for $X\sim\mathcal N(0,1)$ is $1$ (file 04 shows why).

## 3. Variance, covariance, correlation

$$\operatorname{Var}(X)=\mathbb E\left[(X-\mathbb EX)^2\right]=\mathbb EX^2-(\mathbb EX)^2\ \ge0,$$
$$\operatorname{Cov}(X,Y)=\mathbb E\left[(X{-}\mathbb EX)(Y{-}\mathbb EY)\right]=\mathbb E[XY]-\mathbb EX\,\mathbb EY,$$
$$\operatorname{Corr}(X,Y)=\frac{\operatorname{Cov}(X,Y)}{\sqrt{\operatorname{Var}X\,\operatorname{Var}Y}}\in[-1,1].$$
**In words:** variance = "spread"; covariance = "do they move together?";
correlation = covariance measured on a $[-1,1]$ scale.

**The rules used everywhere:** $\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$;
$\operatorname{Cov}$ is **bilinear** (linear in each slot), e.g.
$$\operatorname{Cov}(aX+bY,Z)=a\operatorname{Cov}(X,Z)+b\operatorname{Cov}(Y,Z).$$
and $\operatorname{Cov}(X,X)=\operatorname{Var}(X)$. Hence
$$\operatorname{Var}\Big(\sum_i X_i\Big)=\sum_i\operatorname{Var}(X_i)+2\sum_{i<j}\operatorname{Cov}(X_i,X_j).$$

## 4. Independence

**Independent** means: knowing $X$ tells you nothing about $Y$. Exactly: for all
$a,b$, $\mathbb P(X\le a,\,Y\le b)=\mathbb P(X\le a)\mathbb P(Y\le b)$; for densities,
$p_{X,Y}(x,y)=p_X(x)p_Y(y)$.

**The crucial implication:**
$$\text{independent}\ \Rightarrow\ \operatorname{Cov}(X,Y)=0\ \ (\text{``uncorrelated''}),$$
but **not** the other way round. Counter-example: $X\sim\mathcal N(0,1)$,
$Y=X^2$: $\operatorname{Cov}(X,Y)=\mathbb EX^3-\mathbb EX\,\mathbb EX^2=0-0=0$,
yet $Y$ is a function of $X$, so they are utterly dependent.
*(The one exception: for **jointly Gaussian** variables, uncorrelated $\iff$
independent — file 04.)*

**Marginal vs joint.** If you only want $X$, "integrate out" the other:
$p_X(x)=\int p_{X,Y}(x,y)\,dy$.

## 5. Conditional expectation (lightly)

$\mathbb E[X\mid Y]$ = "best guess of $X$ given that you know $Y$". It is itself a
random variable (a function of $Y$). Two facts suffice here:
- **Tower property:** $\mathbb E\big[\mathbb E[X\mid Y]\big]=\mathbb E X$.
- If $X$ is independent of $Y$, $\mathbb E[X\mid Y]=\mathbb E X$.
- **Gaussian case:** for jointly Gaussian $X,Y$,
  $\mathbb E[X\mid Y]=\mathbb EX+\frac{\operatorname{Cov}(X,Y)}{\operatorname{Var}Y}(Y-\mathbb EY)$
  — a straight line. (Used for bridges, Exercises 6 and 15.)

## 6. Inequalities (the engine of several exercises)

- **Cauchy–Schwarz:** $(\mathbb E[XY])^2\le\mathbb E X^2\,\mathbb E Y^2$. *This single
  inequality proves Exercise 19.*
- **Markov:** $\mathbb P(X\ge a)\le \mathbb E X/a$ for $X\ge0$, $a>0$.
- **Chebyshev:** $\mathbb P(\left|X-\mathbb EX\right|\ge a)\le\operatorname{Var}(X)/a^2$.
- **Jensen:** for convex $\varphi$, $\varphi(\mathbb EX)\le\mathbb E\varphi(X)$.
- **Union bound:** $\mathbb P(A\cup B)\le\mathbb P(A)+\mathbb P(B)$.
- **Borel–Cantelli:** if $\sum_n\mathbb P(A_n)<\infty$ then only finitely many $A_n$
  occur, a.s. (used to pass from "for each $\varepsilon$" to "for one path, uniformly").

## 7. Characteristic functions (the tool behind half the exercises)

For a random variable $X$,
$$\varphi_X(\theta)=\mathbb E\,e^{i\theta X}\qquad(\theta\in\mathbb R).$$
**In words:** it is the Fourier transform of the distribution, and it *encodes the
whole law* (two random variables with the same $\varphi$ have the same distribution —
this is the **inversion/moment theorem**, you may quote it).

**Properties used here:**
1. $\varphi_X$ always exists for **real** $\theta$, and $\left|\varphi_X(\theta)\right|\le1$.
2. Derivatives at $0$ give moments: $\varphi'(0)=i\mathbb EX$,
   $\varphi''(0)=-\mathbb EX^2$.
3. **Independence factorises:** if $X\perp Y$ then
   $\varphi_{X+Y}(\theta)=\varphi_X(\theta)\varphi_Y(\theta)$.
4. **Linearity:** if $Y=aX+b$ then $\varphi_Y(\theta)=e^{i\theta b}\varphi_X(a\theta)$.
5. $\mathbb E\cos(\theta X)=\operatorname{Re}\varphi_X(\theta)$,
   $\mathbb E\sin(\theta X)=\operatorname{Im}\varphi_X(\theta)$.

*Worked 1.* $X\sim\mathcal N(0,1)$: $\varphi_X(\theta)=e^{-\theta^2/2}$, so
$\mathbb E\cos X=e^{-1/2}$ and $\mathbb E\sin X=0$.

*Worked 2.* $W_t\sim\mathcal N(0,t)$, so $\varphi_{W_t}(\theta)=e^{-t\theta^2/2}$.
But you may **not** multiply $\varphi_{W_t}$ and $\varphi_{W_s}$ to get
$\varphi_{W_t+W_s}$: rule (3) needs **independence**, and for $t\ne s$ the variables
$W_t$ and $W_s$ are correlated. Use the multivariate version (file 04 §4) instead,
with $\Sigma_{ij}=\min(t_i,t_j)$.

**Moment generating function:** $M_X(s)=\mathbb EXe^{sX}$ behaves the same way
($M_{X+Y}=M_XM_Y$ for independent variables) and is the same object with $\theta=is$.
It gives **exponential moments** like $\mathbb Ee^{\sigma W_t}=e^{\sigma^2t/2}$
(Exercise 9a) — remember $\mathbb Ee^{sX}\ne e^{s\mathbb EX}$.

## 8. Convergence of random variables (four different meanings)

| Mode | Notation | Meaning |
|---|---|---|
| **Almost sure** | $X_n\to X$ a.s. | for (almost) every outcome $\omega$, the numbers $X_n(\omega)\to X(\omega)$ |
| **In probability** | $X_n\xrightarrow{P}X$ | $\mathbb P(\left|X_n-X\right|>\varepsilon)\to0$ for each $\varepsilon>0$ |
| **In $L^2$ (mean square)** | $X_n\xrightarrow{L^2}X$ | $\mathbb E\left|X_n-X\right|^2\to0$ |
| **In distribution** | $X_n\xrightarrow{d}X$ | the CDFs converge: $F_{X_n}(x)\to F_X(x)$ |

**Implications** (the ones used here):
$$L^2\ \Rightarrow\ \text{probability}\ \Rightarrow\ \text{distribution},\qquad
\text{a.s.}\ \Rightarrow\ \text{probability}\ \Rightarrow\ \text{distribution}.$$
None of the arrows reverses in general.

**Chebyshev bridge:** $L^2$ convergence of $X_n$ to $\mu$ is checked by showing
$\operatorname{Var}(X_n)\to0$; then $\mathbb P(\left|X_n-\mu\right|>\varepsilon)\le
\operatorname{Var}(X_n)/\varepsilon^2\to0$ gives convergence in probability.

**Laws of large numbers (LLN).** For iid $Y_i$ with mean $\mu$ and finite variance,
$\frac1N\sum_{i=1}^NY_i\to\mu$ a.s. and in $L^2$. **Central limit theorem (CLT):**
$\frac{1}{\sqrt N}\sum_{i=1}^N(Y_i-\mu)\xrightarrow{d}\mathcal N(0,\sigma^2)$.

> **Where you need it.** Exercise 1 (stationarity + LLN + $L^2$ averaging),
> Exercise 4 (variance of a moving average), Exercise 19 (Cauchy–Schwarz to control
> $\mathbb E[X_tX_s]$), and every "the Riemann sums converge to the integral" argument
> for Wiener integrals.

## 9. Micro-drills

1. $\operatorname{Var}(3X+7)$ for $\operatorname{Var}(X)=4$. *Ans.* $36$.
2. $X,Y$ uncorrelated, $\operatorname{Var}X=1$, $\operatorname{Var}Y=2$:
   $\operatorname{Var}(X-2Y)$. *Ans.* $1+8=9$.
3. $X\sim\mathcal N(0,1)$: find $\mathbb E\cos(2X)$ and $\mathbb E\sin(2X)$.
   *Ans.* $e^{-2}$ and $0$.
4. If $\mathbb E(X_n-\mu)^2=1/n$, which modes of convergence do you get? *Ans.*
   $L^2$ and in probability (via Chebyshev); not a.s. without more work.
5. Why is "uncorrelated" *not* enough to conclude independence? *Ans.* Because
   covariance only sees linear dependence; e.g. $Y=X^2$ is uncorrelated with a
   symmetric $X$ but perfectly dependent.
6. State the Cauchy–Schwarz inequality and one use. *Ans.*
   $(\mathbb E[XY])^2\le\mathbb EX^2\,\mathbb EY^2$; it bounds
   $\left|\mathbb E[(X_t-X_{t'})X_s]\right|$ in Exercise 19.
