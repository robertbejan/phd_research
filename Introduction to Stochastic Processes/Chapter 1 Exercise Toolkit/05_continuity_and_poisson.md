# 05 — Continuity, modifications & the Poisson process

**Covers Exercises 18 and 19.**
Book sections: 1.3 (Theorem 1.2 Kolmogorov, Theorem 1.3 Wiener, modifications),
1.5 (condition (1.28) and the continuity of $R(t,s)$).

> **Prerequisites** (read these first if the maths is new):
> `Primer/09_stochastic_processes_primer.md` §1–§2 — what a process is,
> finite-dimensional distributions, and the crucial distinction
> equivalent / modification / indistinguishable, plus Kolmogorov's continuity
> criterion;
> `Primer/10_brownian_ou_poisson.md` §1 and §4 — Brownian moments
> ($\mathbb E|W_t-W_s|^4=3(t-s)^2$) and the Poisson process (why its increments are
> linear, not super-linear, in $t-s$);
> `Primer/03_probability_primer.md` §6 — Cauchy–Schwarz, Markov and Chebyshev, which
> are the whole of Exercise 19.

---

## The tools

### T1 — What the three notions mean (get these exact)
- **Equivalent:** same finite-dimensional distributions (Def. 1.3).
- **Modification:** $\mathbb P(X_t=Y_t)=1$ **for each fixed** $t$.
- **Indistinguishable:** $\mathbb P(X_t=Y_t\ \forall t)=1$ (stronger).
A continuous modification is a modification whose paths are a.s. continuous.

### T2 — Kolmogorov's continuity criterion (Theorem 1.2)
If there exist $\alpha,\beta>0$ and, for each $T$, a constant $C(T)$ with
$$\mathbb E|X_t-X_s|^{\alpha}\le C(T)\,|t-s|^{1+\beta},\qquad 0\le s,t\le T,$$
then $X$ has a continuous modification.
- BM satisfies it with $\alpha=4,\ \beta=1$ (from $\mathbb E|W_t-W_s|^4=3|t-s|^2$).
- To show a process has **no** continuous modification, prove that for **every**
  $\alpha,\beta>0$ the inequality **fails**, i.e. no finite $C$ can work.

### T3 — Poisson process facts (Exercise 18)
$N_t-N_s\sim\text{Poisson}(\lambda(t-s))$ ($t>s$), so
$$\mathbb P(N_t-N_s=k)=e^{-\lambda(t-s)}\frac{[\lambda(t-s)]^k}{k!},\qquad
\mathbb E(N_t-N_s)=\lambda(t-s),\qquad \operatorname{Var}=\lambda(t-s).$$
Useful **lower bound** for any $\alpha>0$: since $\{|N_t-N_s|\ge1\}$ contributes at
least $1$,
$$\mathbb E|N_t-N_s|^{\alpha}\ \ge\ \mathbb P(N_t-N_s\ne0)=1-e^{-\lambda(t-s)}
\ \xrightarrow[\ t-s\to0\ ]{}\ \lambda(t-s).$$

### T4 — Cauchy–Schwarz (the engine of Exercise 19)
$$|\mathbb E[UV]|\le\sqrt{\mathbb E[U^2]\,\mathbb E[V^2]}.$$
Apply it to $U=X_t-X_{t'}$, $V=X_s$ to bound how much the correlation function
moves when you move one time argument.

### T5 — $L^2$ continuity (condition (1.28))
$$\lim_{h\to0}\mathbb E|X_{t+h}-X_t|^2=0.$$
This is given for the process in Ex. 19. Note also
$\mathbb E|X_{t+h}-X_t|^2=2(C(0)-C(h))$ for stationary processes (Eq. (1.4)).

---

## Warm-ups (solved)

**W1 (Cauchy–Schwarz bound, analogue of Ex. 19).**
Show that if $X_s\in L^2$ and $\mathbb E|X_{t'}-X_t|^2\to0$ as $t'\to t$, then
$\mathbb E[X_tX_s]-\mathbb E[X_{t'}X_s]\to0$.
*Solution.* $\big|\mathbb E[(X_t-X_{t'})X_s]\big|\le\sqrt{\mathbb E|X_t-X_{t'}|^2\,\mathbb E X_s^2}\to0$
by T4.

**W2 (Poisson moment, analogue of Ex. 18).**
For $N_t-N_s\sim\text{Poisson}(\lambda(t-s))$, compute $\mathbb E|N_t-N_s|$ and
$\mathbb E|N_t-N_s|^2$.
*Solution.* $=\lambda(t-s)$ and $=\operatorname{Var}+\text{mean}^2=\lambda(t-s)(1+\lambda(t-s))$.

**W3.** State why BM has a continuous modification but you must *prove*
(rather than assume) that $N_t$ does not.
*Solution.* BM satisfies T2 with $\alpha=4,\beta=1$. For $N_t$ you must show T2
fails for all $\alpha,\beta>0$.

---

## Game plan

### Exercise 18 (no continuous modification)
- Fix any $\alpha>0$. Use the **lower bound** in T3:
  $\mathbb E|N_t-N_s|^{\alpha}\ge 1-e^{-\lambda(t-s)}$.
- Suppose a continuous modification existed; then T2 would force
  $\mathbb E|N_t-N_s|^{\alpha}\le C(t-s)^{1+\beta}$. Combine with the lower bound and
  divide by $(t-s)^{1+\beta}$:
  $$\frac{1-e^{-\lambda(t-s)}}{(t-s)^{1+\beta}}\ \ge\ \frac{\lambda(t-s)}{2\,(t-s)^{1+\beta}}
  =\frac{\lambda}{2}(t-s)^{-\beta}\to\infty\ \ (t-s\to0).$$
  Contradiction with the bounded constant $C$. Hence no continuous modification.
- *Guiding questions:* why does the *jump structure* of $N_t$ make the left side blow
  up? Would the argument change if $N_t$ were continuous?

### Exercise 19 (continuity of $R(t,s)$)
- Prove $R(t,s)=\mathbb E[X_tX_s]$ is continuous in both arguments.
- Route: write
  $R(t,s)-R(t',s')=[R(t,s)-R(t',s)]+[R(t',s)-R(t',s')]$.
- Bound each bracket with **T4 (Cauchy–Schwarz)** exactly as in W1; the factors
  $\mathbb E|X_t-X_{t'}|^2$, $\mathbb E|X_s-X_{s'}|^2$ vanish by **T5** (condition
  (1.28)); the other factors are bounded by $\sup_u\mathbb E X_u^2<\infty$ on the
  compact time set.
- *Guiding question:* where do you use that the process is in $L^2$ and $L^2$-continuous?

---

## Pitfalls

- **Modification $\ne$ indistinguishable.** Kolmogorov's theorem gives a *modification*;
  for pathwise statements you need separability/indistinguishability arguments.
- **One value of $\alpha$ is not enough.** To disprove continuity you must defeat
  *all* $\alpha,\beta>0$ — the division trick above does that in one stroke.
- **In Ex. 19 keep the two arguments separate.** Moving $t$ and $s$ at once needs the
  two-bracket decomposition; a naive bound loses the limit.

---

## Numerical check (optional)

Simulate a Poisson process on a fine grid; the empirical
$t\mapsto$ jump indicator shows the discontinuity directly. Check
$\mathbb E|N_{t}-N_s|\approx\lambda(t-s)$ for small $\Delta$ and note it is linear,
not super-linear, in $\Delta$.

