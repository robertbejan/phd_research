# 08 — Differential equations and Green's functions

**Read this if:** you cannot solve $y'=-2y$, do not know what a "boundary value
problem" is, or want to know why differentiating an integral equation helps.

## 1. What an ODE is

An **ordinary differential equation (ODE)** is an equation relating a function to
its derivatives, e.g. $y'(t)=-2y(t)$ ("the rate of decrease is proportional to the
amount"). Solving it means finding **all** functions satisfying the equation.
An **initial condition** pins down one of them.

**Order** = highest derivative present. We need orders 1 and 2 only.

## 2. First order, linear

**Form:** $y'(t)=a(t)y(t)+b(t)$.
- **Homogeneous** ($b=0$): $y'=ay$ $\Rightarrow$ $y(t)=Ce^{at}$. *Check by
  differentiating.*
- **Full equation:** solve by an **integrating factor** $e^{-\int a}$:
  $y(t)=e^{\int_0^ta}\left[y(0)+\int_0^te^{-\int_0^sa}b(s)\,ds\right]$.
- **Constant coefficients:** $y'=-\alpha y$ has $y(t)=e^{-\alpha t}y(0)$; if
  $\alpha>0$ it decays with **time constant** $1/\alpha$.

*Worked:* $y'=-2y$, $y(0)=5$ $\Rightarrow y(t)=5e^{-2t}$.

> **Where you need it.** The OU process solves $dV=-\gamma V\,dt+\sigma\,dW$; the
> deterministic part is exactly $V'=-\gamma V$, and its solution $e^{-\gamma t}$ is
> the origin of every $e^{-\alpha|t|}$ correlation in this chapter. The "Langevin"
> equation (Ex. 8, 12, 15, 16) is this ODE plus a random push.

## 3. Second order with constant coefficients

**Form:** $ay''+by'+cy=0$. Guess $y=e^{rt}$; this works iff
$$ar^2+br+c=0\qquad\text{(the **characteristic equation**)} .$$
- two real roots $r_1\ne r_2$: $y=C_1e^{r_1t}+C_2e^{r_2t}$;
- double root $r$: $y=(C_1+C_2t)e^{rt}$;
- **complex roots** $r=\pm i\delta$: $y=C_1\cos(\delta t)+C_2\sin(\delta t)$.

*Worked (the damped oscillator of Exercise 16).* For
$y''+2\gamma y'+ \omega_0^2y=0$ with $\gamma<\omega_0$, the roots are
$r=-\gamma\pm i\delta$, $\delta=\sqrt{\omega_0^2-\gamma^2}$, so the solution
**oscillates while decaying**:
$$y(t)=e^{-\gamma t}\big(A\cos\delta t+B\sin\delta t\big).$$
The velocity autocorrelation in Exercise 16 is precisely the decaying combination
$e^{-\gamma|t|}\big(\cos(\delta|t|)-\tfrac1\delta\sin(\delta|t|)\big)$. This is why
that formula looks odd: it is (a rescaled) solution of the oscillator equation.

**Damping regimes:** $\gamma>0$ ⇒ decay ⇒ the correlation is **integrable** (so the
diffusion coefficient $D$ is finite); $\gamma=0$ ⇒ pure oscillation ⇒
non-integrable correlation ⇒ $D$ does not exist. The condition $\gamma>0$ in
Exercise 16b is not decoration.

## 4. Boundary value problems (BVP)

An ODE plus conditions at **two different points**, e.g.
$$-e''(t)=\mu e(t),\qquad e(0)=0,\quad e(1)=0 .$$
Unlike initial-value problems, a BVP usually has solutions only for special
$\mu$ — those are the **eigenvalues** (file 06 §9). Solve by trying the boxed case:

*Worked.* $-e''=\mu e$ with complex roots $r=\pm i\sqrt\mu$ gives
$e(t)=A\cos(\sqrt\mu\,t)+B\sin(\sqrt\mu\,t)$. Condition $e(0)=0$ kills $A$;
condition $e(1)=0$ gives $\sin(\sqrt\mu)=0$, i.e. $\sqrt\mu=n\pi$. Therefore
$$\mu=n^2\pi^2,\qquad e_n(t)=\sqrt2\sin(n\pi t)\ \text{(normalised)} .$$
Note the pattern: **boundary conditions quantise the eigenvalues.** That is the
entire mechanism behind the Brownian bridge's $(\lambda_n,e_n)=(1/(n^2\pi^2),\sqrt2\sin(n\pi t))$.

## 5. Turning an integral equation into an ODE

Why it works: the **fundamental theorem of calculus** says
$\frac{d}{dt}\int_0^tf(s)ds=f(t)$; and for a **piecewise** kernel like $\min(t,s)$
the integrand changes form at $s=t$, so a single differentiation produces two
regime-dependent terms.

*Worked (the template for Exercise 24 and 28b).* Suppose
$$\int_0^1\min(t,s)e(s)\,ds=\lambda e(t).$$
Write the integral as $\int_0^tse(s)ds+\int_t^1te(s)ds$. Differentiate in $t$
(product rule on the second piece, and the fundamental theorem on the first):
$$\lambda e'(t)=\int_0^t s\,e'(s)ds + \text{(terms that cancel)} .$$
Differentiate again: the corner gives $\lambda e''(t)=-e(t)$, i.e.
$$-e''(t)=\frac1\lambda e(t),$$
and evaluating the equation at $t=0$ and $t=1$ yields the boundary conditions
$e(0)=0$ and $e'(1)=0$. So the integral equation $\to$ a Sturm–Liouville problem
(file 06 §9), which you solve as in §4. **This single move solves Exercises 24, 25
and 28(b).**

## 6. Green's functions and eigenfunction expansions

**The problem:** solve $-u''(t)=f(t)$ with $u(0)=u(1)=0$.
**The method:** expand everything in the eigenfunctions of the *homogeneous*
problem ($e_n=\sqrt2\sin(n\pi t)$, $-e_n''=n^2\pi^2e_n$). Writing
$f=\sum f_ne_n$ and $u=\sum u_ne_n$ gives, term by term,
$$n^2\pi^2u_n=f_n\quad\Rightarrow\quad u_n=\frac{f_n}{n^2\pi^2},$$
i.e. $u(t)=\int_0^1G(t,s)f(s)ds$ with
$$G(t,s)=\sum_n\frac{e_n(t)e_n(s)}{n^2\pi^2}.$$
$G$ is the **Green's function**: "the response at $t$ to a unit push at $s$".
**Moral:** a differential operator inverted is an integral operator, and its kernel
is built from the **eigenfunctions**. That is the bridge between files 06–07 (KL
eigenfunctions of a covariance) and file 08's ODEs.

## 7. Micro-drills

1. Solve $y'=3y$, $y(0)=2$. *Ans.* $2e^{3t}$.
2. Solve $y''+4y=0$. *Ans.* $A\cos2t+B\sin2t$.
3. For $y''+2\gamma y'+\omega_0^2y=0$, $\gamma<\omega_0$: write the general solution.
   *Ans.* $e^{-\gamma t}(A\cos\delta t+B\sin\delta t)$, $\delta=\sqrt{\omega_0^2-\gamma^2}$.
4. Solve $-e''=\mu e$, $e'(0)=e'(1)=0$, and give the eigenfunctions.
   *Ans.* $\mu=n^2\pi^2$, $e_n=\sqrt2\cos(n\pi t)$ ($n\ge0$, with the constant mode
   normalised).

## 10. Where each piece is used

| Piece | Toolkit file / exercise |
|---|---|
| $y'=-\alpha y\Rightarrow e^{-\alpha t}$ | 03 §T1, §T7; 04 §T6 — Exercises 8, 12, 15 |
| damped oscillator, $\delta=\sqrt{\omega_0^2-\gamma^2}$ | 04 §Game plan Ex. 16 — Exercise 16 |
| $\int_0^\infty e^{-\alpha t}\cos(\beta t)dt$ | 04 §T4 — Exercises 7, 16 |
| boundary conditions quantise eigenvalues | 07 §T2 — Exercise 24 |
| differentiate an integral equation twice | 07 §T2 — Exercises 24, 28(b) |
| Green's function = inverted operator | 06 §T6 — Exercises 22–28 |

**The one line to remember from this file:** *every $e^{-\alpha|t|}$ correlation in
this chapter is the decaying solution of a first- or second-order ODE, and its
Fourier transform is $2\alpha/(\alpha^2+\omega^2)$.*
