# 02 — Complex numbers and trigonometry

**Read this if:** self-test question 2 was hard, or if $i$, $e^{i\theta}$, or
"$\mathbb E\cos=\operatorname{Re}\mathbb E e^{i\cdot}$" make you nervous.

## 1. Why complex numbers appear at all

We never *need* them physically here, but they make the algebra **much** shorter.
The trick: instead of carrying $\cos$ and $\sin$ around, we carry one symbol
$e^{i\theta}$ that contains both.

## 2. The basics

- $i$ is defined by $i^2=-1$. A **complex number** is $z=a+bi$ with $a,b$ real.
- $a=\operatorname{Re}z$ (**real part**), $b=\operatorname{Im}z$ (**imaginary part**).
- **Conjugate:** $\overline{z}=a-bi$. Note $z\overline z=a^2+b^2$.
- **Modulus ($\left|z\right|$)** = distance from $0$: $\left|z\right|=\sqrt{a^2+b^2}$.
- Arithmetic: add parts; multiply like brackets and use $i^2=-1$, e.g.
  $(1+i)(2-i)=2-i+2i-i^2=3+i$.
- If $z=a+bi$ then $zz^{-1}=1$ etc. — but we will only ever need the above.
- **Real test:** $z$ is real $\iff \operatorname{Im}z=0$; and always
  $\operatorname{Re}z\le\left|z\right|$.

## 3. Euler's formula (the one formula to memorise)

$$\boxed{\ e^{i\theta}=\cos\theta+i\sin\theta\ }$$
Consequences you will use constantly:
$$\cos\theta=\operatorname{Re}\left(e^{i\theta}\right),\qquad
\sin\theta=\operatorname{Im}\left(e^{i\theta}\right),\qquad
e^{i\pi}=-1,\qquad \left|e^{i\theta}\right|=1 .$$
**Polar form:** $a+bi=re^{i\theta}$ with $r=\sqrt{a^2+b^2}$ and
$\tan\theta=b/a$.

Adding exponents multiplies the trig functions — this *is* how all the trig
identities below are derived:
$$e^{i(a+b)}=e^{ia}e^{ib}.$$

> **Where you need it.** The characteristic function $\mathbb E e^{i\theta X}$
> (file 03 §7) is the single most used object in Exercises 5, 6, 9, 10. Every
> "$\mathbb E\cos/\sin$ of a Gaussian" is done by writing it as a real/imaginary
> part of $e^{i\theta X}$.

## 4. Every trig identity used in this chapter

**Angle sum / difference** (derive from Euler if you forget):
$$\cos(a\pm b)=\cos a\cos b\mp\sin a\sin b,\qquad
\sin(a\pm b)=\sin a\cos b\pm\cos a\sin b .$$
**Products to sums** (this is what turns a covariance into a $\cos$ of the *lag*):
$$\cos a\cos b=\tfrac12\left[\cos(a-b)+\cos(a+b)\right],$$
$$\sin a\sin b=\tfrac12\left[\cos(a-b)-\cos(a+b)\right],$$
$$\sin a\cos b=\tfrac12\left[\sin(a+b)+\sin(a-b)\right].$$
**Double angle:** $\cos2a=\cos^2a-\sin^2a=1-2\sin^2a$, $\sin2a=2\sin a\cos a$.
**Pythagoras:** $\cos^2a+\sin^2a=1$.
**Even/odd:** $\cos(-a)=\cos a$, $\sin(-a)=-\sin a$.

*Worked (this is Exercise 3's core step).* With $X_n=A\cos(n\omega)+B\sin(n\omega)$,
$A\perp B$:
$$\cos(n\omega)\cos((n+\tau)\omega)+\sin(n\omega)\sin((n+\tau)\omega)
=\cos\big[(n+\tau)\omega-n\omega\big]=\cos(\tau\omega).$$
The $n$ cancels — *that is why the process is stationary.*

## 5. Orthogonality integrals (needed for Fourier, files 06–08)

For integers $m,n$:
$$\int_{0}^{2\pi}\!\!\cos(mt)\cos(nt)\,dt=\pi\delta_{mn},\qquad
\int_{0}^{2\pi}\!\!\sin(mt)\sin(nt)\,dt=\pi\delta_{mn},$$
$$\int_{0}^{2\pi}\!\!\cos(mt)\sin(nt)\,dt=0 ,$$
where $\delta_{mn}=1$ if $m=n$ and $0$ otherwise (**Kronecker delta**). On $[0,1]$
the same integrals with $\cos(2\pi nt)$ give $\tfrac12$ instead of $\pi$.

## 6. Micro-drills

1. Compute $e^{i\pi/2}$, $e^{i\pi/4}$, and $\left|3+4i\right|$.
   *Ans.* $i$; $\tfrac{\sqrt2}{2}+i\tfrac{\sqrt2}{2}$; $5$.
2. Write $\cos3\theta$ in terms of $\cos\theta$. *Ans.* $4\cos^3\theta-3\cos\theta$.
3. Evaluate $\int_0^{2\pi}\sin t\cos t\,dt$. *Ans.* $0$ (orthogonality, $m=n$ case of
   the third formula: $\sin t\cos t=\tfrac12\sin2t$, which integrates to $0$).
4. Express $\mathbb E\left[\cos(\sigma Z)\right]$ using a characteristic function.
   *Ans.* $\operatorname{Re}\mathbb E e^{i\sigma Z}$.

## Where this leads

You now have enough to read **every** toolkit file in the parent folder. Next:

1. `03_probability_primer.md` and `04_gaussian_primer.md` — these two unlock
   Exercises 1–19, i.e. two thirds of the chapter.
2. `09_stochastic_processes_primer.md` and `10_brownian_ou_poisson.md` — the
   three workhorse processes.
3. `05` → `06` → `07` → `08` — the operator/Fourier/ODE chain for Exercises 20–28.
4. `11_recurring_techniques.md` — the procedure list to keep beside you when solving.
5. `12_prerequisite_map.md` — the per-exercise reading order.

**One habit that matters more than any single formula:** when a line of the book or
of the toolkit does not make sense, write down *which symbol you do not know* and
look it up in the symbol dictionary at the top of this file. Almost always it is
one symbol, not the whole argument.
