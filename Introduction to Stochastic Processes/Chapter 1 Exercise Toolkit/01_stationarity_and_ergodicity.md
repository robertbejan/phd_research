# 01 — Stationarity & ergodicity (discrete time)

**Covers Exercises 1, 2, 3, 4.**
Book sections: 1.1 (Definition 1.1), 1.2 (Definitions 1.5–1.6, eqs. (1.1)–(1.3)),
Examples 1.1–1.4.

> **Prerequisites** (read these first if the maths is new):
> `Primer/03_probability_primer.md` §1–§4, §6, §8 — random variables, expectation,
> variance, covariance, independence, modes of convergence;
> `Primer/09_stochastic_processes_primer.md` §1, §3, §4 — what a process is,
> stationarity, ergodicity and time averages;
> `Primer/02_complex_numbers_and_trig.md` §4 — the trig product-to-sum identities.
> Techniques 12 and 13 of `Primer/11_recurring_techniques.md`.

---

## The tools

### T1 — Two definitions to keep side by side
- **Strictly stationary (Def. 1.5).** For every $k$ and all times $t_1,\dots,t_k$,
  the joint law of $(X_{t_1},\dots,X_{t_k})$ equals that of
  $(X_{t_1+s},\dots,X_{t_k+s})$ for every shift $s$.
  *Practice:* "shifting time does not change the joint distribution".
- **Weakly / second-order stationary (Def. 1.6).** $\mathbb E X_t=\mu$ is
  **constant**, and $\operatorname{Cov}(X_t,X_s)=C(t-s)$ depends only on the
  **difference** $t-s$.

Strict + finite second moment $\Rightarrow$ weak. For **Gaussian** processes weak
$\iff$ strict (because the mean and covariance determine the whole law).

### T2 — How to *prove* strict stationarity (Ex. 1a, 2)
Show that the joint law of the shifted vector equals the original. Two standard
routes:
1. **iid route:** if $X_n=Y_n$ with $(Y_n)$ iid, the shifted vector
   $(Y_{n_1+s},\dots,Y_{n_k+s})$ has *the same marginal law for each coordinate*
   and the coordinates are still independent — identical joint law.
2. **Deterministic-in-$\omega$ route:** if $X_n=Z$ (same $Z$ for every $n$), the
   joint law of any finite vector is the law of $(Z,\dots,Z)$, which is shift
   invariant.

### T3 — Time averages, ergodicity and $L^2$ (Ex. 1b, 1c)
The ergodic (Birkhoff) theorem, Eq. (1.1): for an ergodic strictly stationary
sequence, $\frac1N\sum_{j=0}^{N-1} f(X_j)\to \mathbb E f(Y_0)$ a.s. (hence in
$L^2$ if $f(Y_0)$ has finite second moment). To **prove** the $L^2$ statement,
compute the mean-square error directly:
$$\mathbb E\Big|\frac1N\sum_{j=0}^{N-1}X_j-\mu\Big|^2
=\frac{1}{N^2}\sum_{j,k}\operatorname{Cov}(X_j,X_k).$$
For **uncorrelated** terms the cross-covariances vanish and you get $\propto 1/N$.

### T4 — Handling a sum of uncorrelated variables (Ex. 3, 4)
If the "$A$'s and $B$'s" (or "$\xi$'s") are uncorrelated with mean $0$ and
variances $\sigma_i^2$:
$$\operatorname{Cov}\!\Big(\sum_i a_i Z_i,\ \sum_j b_j Z_j\Big)
=\sum_i a_i b_i\,\sigma_i^2 \quad\text{(only "matched" index pairs survive).}$$

### T5 — Trig identities you will need (Ex. 3)
$$\cos a\cos b=\tfrac12[\cos(a-b)+\cos(a+b)],\quad
\sin a\sin b=\tfrac12[\cos(a-b)-\cos(a+b)],$$
$$\sin a\cos b=\tfrac12[\sin(a+b)+\sin(a-b)].$$

---

## Warm-ups (solved)

**W1 (strict stationarity, analogue of Ex. 1a/2).**
Let $Y_0,Y_1,\dots$ be iid and set $X_n=Y_n+Y_{n-1}$. Is $X_n$ stationary?
*Solution.* The vector $(X_{n_1},\dots,X_{n_k})$ is a fixed linear map of
$(Y_{\cdot})$; translating all indices by $s$ shifts the *indices* but, being iid,
the joint law of the $Y$'s is translation invariant; a fixed map of a
translation-invariant vector is translation invariant. Hence yes (this is the
role of Example 1.1).

**W2 (variance decay, analogue of Ex. 1b).**
Let $\xi_j$ be uncorrelated, mean $\mu$, variance $\sigma^2$. Show
$\mathbb E\big(\frac1N\sum_{j=0}^{N-1}\xi_j-\mu\big)^2\to0$.
*Solution.* The sum has mean $N\mu$; subtracting $\mu$ and using T3:
$\operatorname{Var}(\frac1N\sum \xi_j)=\frac{1}{N^2}\cdot N\sigma^2=\sigma^2/N\to0$.

**W3 (a single harmonic mode, analogue of Ex. 3).**
Let $X_n=A\cos(n\omega)+B\sin(n\omega)$ with $A,B$ uncorrelated, mean $0$,
$\mathbb E A^2=\mathbb E B^2=\sigma^2$. Find $\mathbb E X_n$ and
$\operatorname{Cov}(X_n,X_{n+\tau})$.
*Solution.* Mean $=0$. Using T5 and $A\perp B$:
$$\operatorname{Cov}(X_n,X_{n+\tau})=\sigma^2[\cos(n\omega)\cos((n{+}\tau)\omega)
+\sin(n\omega)\sin((n{+}\tau)\omega)]=\sigma^2\cos(\tau\omega),$$
which depends only on $\tau$ — weak stationarity. Exercise 3 is the sum over $k$
of several such modes with *distinct* frequencies.

---

## Game plan

### Exercise 1
- (a) Route **T2-1**: write the shifted joint law and note iid.
- (b) Use **T3**: expand $\mathbb E|\frac1N\sum X_j-\mu|^2$; the uncorrelatedness of
  distinct $Y$'s kills every cross term; you are left with $N$ identical diagonal
  terms; conclude $\to0$.
- (c) Same computation with $f(X_j)$; you need $\mathbb E f^2(Y_0)<\infty$ to have
  finite variance. *Guiding question:* what is $\operatorname{Cov}(f(Y_j),f(Y_k))$
  for $j\ne k$?

### Exercise 2
- Route **T2-2**: the finite-dimensional law of $(X_{n_1},\dots,X_{n_k})$ is the law
  of $(Z,\dots,Z)$, unchanged by a shift.

### Exercise 3
- Compute $\mathbb E X_n$ (linearity). Then $\operatorname{Cov}(X_n,X_{n+\tau})$
  using **T4** (cross terms between different frequencies vanish since
  $A_i,B_i$ are uncorrelated) and **T5**. Show the result depends only on $\tau$.
- *Guiding question:* why do we need the frequencies to be **distinct**? What would
  happen if $\omega_i=\omega_j$?

### Exercise 4
- (a) $X_n=\sum_{k=1}^m a_k\xi_{n-k+1}$. Apply **T4** to get the variance
  ($\Delta=0$) and covariance ($\Delta\ne0$). Fix a lag $\Delta$ and ask: which
  *pairs* $(k,k')$ have $\xi_{n-k+1}$ and $\xi_{n+\Delta-k'+1}$ sharing the same
  $\xi$-index? Only $k'=k+\Delta$ contributes.
- (b) Insert $a_k=1/\sqrt m$. Study $m=1$ (white noise) and $m\to\infty$. The
  covariance becomes a triangular/"tent" function of the lag; identify its
  continuous limit.

---

## Pitfalls

- **Don't confuse the two stationarities.** Ex. 2 is *strict*; Ex. 3/4 are *weak*.
- **Independence is stronger than uncorrelatedness.** In Ex. 1 the $Y$'s are iid
  (independent); in Ex. 3/4 they are only uncorrelated — that is exactly enough.
- **Lag bookkeeping.** For $\operatorname{Cov}(X_n,X_{n+\tau})$ count the
  *overlap* of the index sets; a shifted index outside the support contributes $0$.
- **In Ex. 1(c)** remember $\operatorname{Var}(f(Y_0))=\mathbb E f^2(Y_0)-(\mathbb E f(Y_0))^2$.

---

## Numerical check (optional)

Simulate $X_n=Y_n$ ($Y_n\sim\mathcal N(\mu,\sigma^2)$) with a large $N$ and check
that $\operatorname{Var}\big(\tfrac1N\sum X_j\big)\approx \sigma^2/N$, and for
Ex. 4 that the empirical autocovariance matches your formula at a few lags. Reproduce
the MA($m$) covariance with `numpy.correlate`.

