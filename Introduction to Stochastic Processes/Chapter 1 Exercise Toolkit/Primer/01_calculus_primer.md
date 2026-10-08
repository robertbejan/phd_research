# 01 — Calculus you will actually use

**Read this if:** the self-test question 1 was hard, or if Taylor expansions,
integration by parts, or double integrals feel shaky.

## 1. Functions, limits, continuity

A **function** $f:\mathbb R\to\mathbb R$ is a rule assigning a number $f(x)$ to each
input $x$. The **limit** $\lim_{x\to a}f(x)=L$ means: as $x$ gets closer and closer to
$a$ (without necessarily equalling $a$), $f(x)$ gets arbitrarily close to $L$.
*Example:* $\lim_{h\to0}\frac{e^{h}-1}{h}=1$.

A function is **continuous at $a$** if $\lim_{x\to a}f(x)=f(a)$ — colloquially, "you
can draw it without lifting your pen".

> **Where you need it.** "Continuous paths" and "continuous modification"
> (Exercise 18) use exactly this word. Brownian motion has continuous paths;
> the Poisson process does not.

## 2. Derivatives

The **derivative** is the instantaneous rate of change:
$$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}=\text{slope of the tangent line}.$$

**Notation zoo** (all mean the same thing): $f'(x)$; $\frac{df}{dx}$; $\dot f$ (for
time); $\frac{d^2f}{dx^2}=f''$ (second derivative = rate of change of the slope).
The symbol $\partial$ ("partial") means: differentiate with respect to one variable
while **holding the others fixed**, e.g. for $F(t,s)=t^2s$,
$$\frac{\partial F}{\partial t}=2ts,\qquad \frac{\partial F}{\partial s}=t^2.$$

**The rules you need** ($a,\alpha$ constants):

| Rule | Statement |
|------|-----------|
| Power | $\frac{d}{dx}x^n=nx^{n-1}$ |
| Exponential | $\frac{d}{dx}e^{\alpha x}=\alpha e^{\alpha x}$ |
| Log | $\frac{d}{dx}\ln x=1/x$ |
| Trig | $\frac{d}{dx}\sin x=\cos x$, $\frac{d}{dx}\cos x=-\sin x$ |
| Sum | $(f+g)'=f'+g'$ |
| Product | $(fg)'=f'g+fg'$ |
| Quotient | $(f/g)'=\frac{f'g-fg'}{g^2}$ |
| **Chain** | $\frac{d}{dx}f(g(x))=f'(g(x))\,g'(x)$ |

*Worked:* $\frac{d}{dt}e^{-\alpha t}\cos(\beta t)
=-\alpha e^{-\alpha t}\cos(\beta t)-\beta e^{-\alpha t}\sin(\beta t)$ (product + chain).

## 3. Taylor series — the most useful tool in this book

**In words.** Near a point $a$, almost any nice function looks like a polynomial.
The polynomial is built from the derivatives at $a$.

**Exactly.**
$$f(a+x)=f(a)+f'(a)x+\frac{f''(a)}{2!}x^2+\frac{f'''}{3!}x^3+\cdots$$
At $a=0$ this is the **Maclaurin series**. Learn these five:
$$e^{x}=1+x+\frac{x^2}{2}+\frac{x^3}{6}+\cdots,\qquad
\sin x=x-\frac{x^3}{6}+\frac{x^5}{120}-\cdots$$
$$\cos x=1-\frac{x^2}{2}+\frac{x^4}{24}-\cdots,\qquad
\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}-\cdots$$
$$\frac{1}{1-x}=1+x+x^2+\cdots\ (|x|<1),\qquad
(1+x)^{\alpha}=1+\alpha x+\frac{\alpha(\alpha-1)}{2}x^2+\cdots$$

**Why you care.** (i) It evaluates limits. (ii) It lets you compute expectations of
exponentials of Gaussians (Exercises 5, 9, 10). (iii) It gives the error bar: the
first omitted term *is* (approximately) the error.

*Worked:* $\lim_{x\to0}\dfrac{1-\cos x}{x^2}
=\lim_{x\to0}\dfrac{1-(1-x^2/2+\cdots)}{x^2}=\dfrac{1}{2}.$

## 4. Asymptotic shorthand

| Symbol | Means | Example |
|--------|-------|---------|
| $f\sim g$ $(x\to a)$ | $\dfrac{f}{g}\to1$ | $1-\cos x\sim x^2/2$ |
| $f\propto g$ | $f=cg$ for a **constant** $c$ (exact, not a limit) | $R(t)\propto e^{-t}$ |
| $f=O(g)$ | $|f|\le C|g|$ for some fixed $C$, near $a$ | $\sin x=O(x)$ as $x\to0$ |
| $f=o(g)$ | $f/g\to0$ | $x^2=o(x)$ as $x\to0$ |
| $f\approx g$ | approximately equal (informal) | $\mathbb E X_t^2\approx 2Dt$ |
| $\to$ | "tends to" / tends to (in some sense, stated) | $X_N\to\mu$ |
| $\Rightarrow$ | "implies" | $X=Y$ a.s. $\Rightarrow$ same law |
| $\iff$ | "if and only if" (both directions) | weak $\iff$ strict, for Gaussian |

$O(\Delta t^2)$ (used in file 08) simply means "the error is a constant times
$\Delta t^2$", so halving $\Delta t$ cuts the error by four.

## 5. Integrals

The **integral** $\int_a^bf(t)dt$ is the (signed) area under the curve; it is the
limit of Riemann sums $\sum_if(t_i)\Delta t$ — a fact we use constantly
("the integral is a limit of sums").

**Fundamental theorem of calculus (FTC):**
$$\int_a^bf'(t)dt=f(b)-f(a),\qquad
\frac{d}{dt}\int_a^tf(s)\,ds=f(t).$$
The second half is the one that turns integral equations into ODEs (file 08 §5).

**Substitution (change of variables):** $\int f(g(t))g'(t)dt=\int f(u)du$ with
$u=g(t)$. *Example:* $\int_0^Te^{-2t}dt=\tfrac12(1-e^{-2T})$.

**Integration by parts** (reverse of the product rule used backwards):
$$\boxed{\ \int_a^bu\,dv=uv\Big|_a^b-\int_a^bv\,du\ }$$
*Worked:* $\int_0^\infty te^{-\alpha t}dt$. Take $u=t$, $dv=e^{-\alpha t}dt$, so
$v=-e^{-\alpha t}/\alpha$, $uv\to0$ at both ends, and
$$\int_0^\infty te^{-\alpha t}dt=\frac{1}{\alpha}\int_0^\infty e^{-\alpha t}dt
=\frac{1}{\alpha^2}.$$
(You will need this in Exercise 16 and in the "$\int_0^\infty e^{-\alpha t}\cos$"
derivations.)

**The three integrals to know by heart:**
$$\int_0^\infty e^{-\alpha t}dt=\frac1\alpha\quad(\alpha>0),\qquad
\int_0^\infty te^{-\alpha t}dt=\frac{1}{\alpha^2},\qquad
\int_0^\infty t^2e^{-\alpha t}dt=\frac{2}{\alpha^3}.$$

**Improper integrals.** $\int_0^\infty$ means $\lim_{R\to\infty}\int_0^R$. It
**converges** (is finite) iff the limit exists. *"$f$ is integrable" / "$f\in L^1$"
just means $\int\left|f\right|<\infty$.*
- $e^{-\alpha t}$ decays fast ⇒ integrable.
- $1/(1+t)$ decays too slowly ⇒ $\int_0^\infty\frac{dt}{1+t}=\infty$.
- $\left|e^{-\alpha t}\cos(\beta t)\right|\le e^{-\alpha t}$ ⇒ integrable.

## 6. The Gaussian integral (do this proof once; you will use it often)

$$\boxed{\ \int_{-\infty}^{\infty}e^{-x^2/2}dx=\sqrt{2\pi}\ }$$
**Proof.** Call the integral $I$. Then
$$I^2=\int_{-\infty}^\infty\!\!\int_{-\infty}^\infty
e^{-(x^2+y^2)/2}dx\,dy
=\int_0^{2\pi}\!\!\int_0^\infty e^{-r^2/2}r\,dr\,d\theta
=2\pi\Big[-e^{-r^2/2}\Big]_0^\infty=2\pi .$$
So $I=\sqrt{2\pi}$. (The middle step is **polar coordinates**: area element
$dx\,dy=r\,dr\,d\theta$.)

**The scaled version:** $\int_{-\infty}^\infty e^{-\alpha x^2}dx=\sqrt{\pi/\alpha}$
for $\alpha>0$; and with a linear term (complete the square, file 05 §8),
$$\int_{-\infty}^{\infty}e^{-\frac{x^2}{2\sigma^2}+bx}dx
=\sqrt{2\pi\sigma^2}\,e^{\sigma^2b^2/2}.$$
*This last formula is literally how the characteristic-function identity
$\mathbb Ee^{i\theta X}=e^{-\theta^2\sigma^2/2}$ is proved* (put $b=i\theta$).

## 7. Double integrals, Fubini, and the "$\min$ split"

**In words.** $\int_a^b\int_c^df(t,s)\,ds\,dt$ adds up values over a rectangle. Do it
**one variable at a time** (inner integral first, treating the other variable as a
constant).

**Fubini/Tonelli.** You may **swap the order** of the two integrals:
$$\int_a^b\!\!\int_c^df(t,s)\,ds\,dt=\int_c^d\!\!\int_a^bf(t,s)\,dt\,ds,$$
provided $\int\!\!\int\left|f\right|<\infty$ (true for everything in this chapter;
state it and move on). The same statement holds with $\mathbb E$ in place of one of
the integrals: $\mathbb E\int\!\!\int X=\int\!\!\int\mathbb EX$ — this is used in
Exercises 8, 13, 14, 16.

**Non-rectangular regions.** If the region is a triangle, e.g.
$\{(u,v):0\le u\le v\le t\}$, then
$$\int_0^t\!\!\int_0^v f(u,v)\,du\,dv .$$

**The "$\min$ split" (you will use it five times).** To compute
$$I(t)=\int_0^t\!\!\int_0^t\min(u,v)\,du\,dv,$$
note the integrand is **symmetric** in $u\leftrightarrow v$, and that on the triangle
$u\le v$ we have $\min(u,v)=u$. Hence
$$I(t)=2\int_0^t\!\!\int_0^v u\,du\,dv
=2\int_0^t\frac{v^2}{2}dv=\frac{t^3}{3}.$$
*Moral: assume an order, integrate, double.*

## 8. Differentiating under the integral sign, and swapping limits

**Leibniz rule.** If $F(t)=\int_{a(t)}^{b(t)}f(t,s)ds$ then
$$F'(t)=f(t,b(t))b'(t)-f(t,a(t))a'(t)+\int_{a(t)}^{b(t)}\frac{\partial f}{\partial t}(t,s)\,ds .$$
For **fixed** limits it reduces to the friendly form
$$\frac{d}{dt}\int_a^bf(t,s)ds=\int_a^b\frac{\partial f}{\partial t}(t,s)ds .$$
*Worked:* $\frac{d}{dt}\int_0^1e^{ts}ds=\int_0^1se^{ts}ds$.

**Why this matters.** Turning an integral *equation* into an *ODE* is exactly this
rule applied to a kernel with a corner (file 08 §5) — that is Exercises 24/28.

**Swapping a limit and an integral** (an informal stand-in for dominated
convergence): if $\left|f_n(t)\right|\le g(t)$ with $\int g<\infty$, then
$$\lim_{n\to\infty}\int f_n=\int\lim_{n\to\infty}f_n .$$
You may use this freely here (e.g. to pass from Riemann sums to integrals in
Wiener-integral arguments).

## 9. Micro-drills

1. $\int_0^\infty e^{-4t}dt$, $\int_0^\infty te^{-4t}dt$. *Ans.* $1/4$; $1/16$.
2. $\int_0^1\!\!\int_0^1(t+s)\,dt\,ds$. *Ans.* $1$.
3. $\int_0^1\!\!\int_0^1\min(t,s)\,dt\,ds$. *Ans.* By symmetry
   $2\int_0^1\!\!\int_0^st\,dt\,ds=2\int_0^1\frac{s^2}{2}ds=\tfrac13$.
4. $\frac{d}{dt}\int_0^te^{-(t-s)}ds$. *Ans.* $1-\int_0^te^{-(t-s)}ds
   =1-(1-e^{-t})=e^{-t}$ (Leibniz with a moving limit).
5. $\int_{-\infty}^{\infty}e^{-x^2/2+3x}dx$. *Ans.* $\sqrt{2\pi}e^{9/2}$.
6. Is $\int_0^\infty e^{-t}\cos(10t)dt$ finite? *Ans.* Yes — bounded by
   $\int_0^\infty e^{-t}dt=1$; in fact it equals $1/(1+100)$.
