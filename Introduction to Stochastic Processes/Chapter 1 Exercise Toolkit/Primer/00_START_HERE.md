# START HERE — all the maths you need, from scratch

You said the toolkits assume too much. This folder fixes that. Everything the
Chapter 1 exercises use is built up here starting from school algebra. Nothing is
assumed except that you can rearrange an equation and that you have *seen* a
derivative and an integral before. We go slowly and we define every symbol.

The parent-folder files now begin with a **Prerequisites** line telling you exactly
which sections of this folder to read first.

## What is inside

| # | File | Gives you |
|---|------|-----------|
| 01 | `01_calculus_primer.md` | limits, derivatives, Taylor, integrals, integration by parts, double integrals, asymptotics |
| 02 | `02_complex_numbers_and_trig.md` | $i$, Euler's formula, every trig identity used |
| 03 | `03_probability_primer.md` | probability, random variables, expectation, variance, independence, convergence |
| 04 | `04_gaussian_primer.md` | the normal distribution in 1 and $n$ dimensions, Gaussian processes |
| 05 | `05_linear_algebra_primer.md` | vectors, matrices, eigenvalues, symmetric matrices, PSD, Cholesky |
| 06 | `06_functions_as_vectors_and_operators.md` | $L^2$, inner products of functions, operators, Mercer, Sturm–Liouville |
| 07 | `07_fourier_primer.md` | Fourier series and transform, spectra, Parseval |
| 08 | `08_odes_and_green_functions.md` | ODEs, boundary value problems, Green's functions |
| 09 | `09_stochastic_processes_primer.md` | processes, stationarity, ergodicity, mean-square calculus |
| 10 | `10_brownian_ou_poisson.md` | Brownian motion, OU, Poisson, white noise, Wiener integrals |
| 11 | `11_recurring_techniques.md` | the tricks that appear again and again |
| 12 | `12_prerequisite_map.md` | exercise ➜ which primer sections to read first |

**Deliberately not covered:** measure theory, Itô calculus, general functional
analysis. Where the book uses one of these, I give a *usable stand-in statement*
clearly labelled, and the stand-in is enough for **every** exercise here.

**Still not here:** final answers. The primers explain *how*; the work is yours.

## How each file is written

- **In words.** Plain-English meaning first, with a tiny example.
- **Exactly.** The formula, with every symbol decoded.
- **Worked micro-example.** Real numbers, nothing skipped.
- **Where you need it.** The toolkit file and exercise it feeds.
- **Micro-drills.** Questions with answers. Do them — they *are* the learning.

## Do this first: the 10-minute self-test

Do **not** read everything. Answer these. If you can do a line, skip that file.

1. What is $\int_0^\infty e^{-3t}\,dt$? *(→ 01)*
2. What is $\cos(a-b)$ in terms of $\cos a,\cos b,\sin a,\sin b$? *(→ 02)*
3. If $\operatorname{Var}(X)=4$, what is $\operatorname{Var}(3X+7)$? *(→ 03)*
4. If $X\sim\mathcal N(0,1)$, what is $\mathbb E e^{2X}$? *(→ 04)*
5. What are the eigenvalues of $\begin{pmatrix}2&0\\0&3\end{pmatrix}$? *(→ 05)*
6. What does "$\{e_n\}$ is orthonormal in $L^2(0,1)$" mean? *(→ 06)*
7. What is $\int_{-1}^{1}\cos(\pi t)\cos(2\pi t)\,dt$? *(→ 07)*
8. Solve $y'(t)=-2y(t)$ with $y(0)=5$. *(→ 08)*
9. What does "weakly stationary" mean? *(→ 09)*
10. Why is $\operatorname{Cov}(W_s,W_t)=\min(s,t)$? *(→ 10)*

If you can do 1, 3 and 9, you are in better shape than you think.

## Symbol dictionary

Every symbol used anywhere in this toolkit, in one place.

**Sets, logic, order**

| Symbol | Read as | Meaning |
|---|---|---|
| $\mathbb R$ | "R" | all real numbers |
| $\mathbb N$, $\mathbb Z$ | — | natural numbers, integers |
| $\mathbb C$ | — | complex numbers |
| $\in$, $\notin$ | "in", "not in" | element of a set |
| $\subset$, $\cup$, $\cap$ | — | subset, union, intersection |
| $\left|x\right|$ | "mod x" | absolute value / modulus |
| $[0,1]$ vs $(0,1)$ | — | closed (endpoints included) vs open |
| $a\wedge b$, $a\vee b$ | — | $\min(a,b)$, $\max(a,b)$ |
| $\forall$, $\exists$ | — | "for all", "there exists" |
| $\Rightarrow$, $\iff$ | — | implies, if and only if |
| s.t., WLOG | — | "such that", "without loss of generality" |
| a.s. | "almost surely" | with probability 1 |
| iid | — | independent and identically distributed |

**Sums, integrals, asymptotics**

| Symbol | Meaning |
|---|---|
| $\sum_{j=0}^{N-1}$, $\prod_i$ | sum, product |
| $\int_a^b$, $\int_0^\infty$, $\int_{\mathbb R}$ | definite, half-line, whole-line integral |
| $\int\!\!\int$ | double integral (file 01 §7) |
| $\partial f/\partial t$ | partial derivative (others held fixed, file 01 §2) |
| $\delta_{nm}$ | Kronecker delta: $1$ if $n=m$, else $0$ |
| $\delta(t-s)$ | Dirac delta (a notation, file 07 §6) |
| $\propto$ | "proportional to" (exact, constant factor) |
| $\sim$ | "asymptotically equivalent" (ratio $\to1$) |
| $O(\Delta t^2)$, $o(1)$ | size/error notation (file 01 §4) |
| $\approx$ | approximately equal (informal) |
| $\to$, $\xrightarrow{N\to\infty}$ | tends to (with the sense stated) |
| $\overset{\text{law}}{=}$ | equal in law / distribution |

**Probability**

| Symbol | Meaning |
|---|---|
| $\mathbb P(A)$ | probability of event $A$ |
| $\Omega$, $\omega$ | sample space; an outcome |
| $F_X$, $p_X$ | CDF, density of $X$ (file 03 §1) |
| $X\sim\mathcal N(\mu,\sigma^2)$ | $X$ is normal with mean $\mu$, variance $\sigma^2$ |
| $\mathbb E X$, $\mathbb E[X\mid Y]$ | expectation; conditional expectation |
| $\operatorname{Var}$, $\operatorname{Cov}$, $\operatorname{Corr}$ | variance, covariance, correlation |
| $X\perp Y$ | independent (or, for Gaussians, uncorrelated) |
| $L^2$ | finite second moment / square-integrable (file 06 §2) |
| $\Phi$ | standard normal CDF |
| $\zeta_k$ | an iid standard normal, $\zeta_k\sim\mathcal N(0,1)$ |
| $\xi_n$ | a Karhunen–Loève coefficient (random) |

**Processes**

| Symbol | Meaning |
|---|---|
| $X_t$ / $X(t)$ | a stochastic process (file 09 §1) |
| $W_t$ / $W(t)$ | standard Brownian motion (file 10 §1) |
| $B_t$ | Brownian bridge, $W_t-tW_1$ |
| $N_t$ | Poisson process (file 10 §4) |
| $Y_t$, $V_t$ | OU velocity / stationary OU |
| $W^H_t$ | fractional Brownian motion, Hurst $H$ |
| $C(t)$, $R(t)$ | autocovariance / autocorrelation of a stationary process |
| $R(t,s)$ | general two-time covariance, $R(t,s)=\mathbb E[X_tX_s]$ |
| $S(\omega)$ | spectral density (file 07 §4) |
| $D$ | diffusion coefficient, $\int_0^\infty C$ |
| $\tau_{cor}$ | correlation time |
| $\lambda,\gamma,\sigma,\alpha,\omega_0,\delta$ | rate/damping/noise/frequency constants (locals) |
| $e_n$, $\lambda_n$ | eigenfunctions and eigenvalues of a kernel (file 06 §5) |
| $\langle f,g\rangle$, $\left\|f\right\|$ | $L^2$ inner product, norm (file 06 §2) |
| $\hat f(\omega)$ | Fourier transform (file 07 §3) |
| $T^*$, $(Rf)(t)$ | adjoint; the integral operator (file 06 §3) |

## Glossary of the "maths words" that trip people up

- **iff** — "if and only if": the statement holds in **both** directions.
- **kernel** — two meanings! (i) the function $R(t,s)$ inside $\int R(t,s)f(s)ds$;
  (ii) for an integral operator, the same thing. Not the same as the "null space".
- **eigenvalue / eigenfunction** — the special scaling factor / shape where an
  operator just multiplies (file 05 §3, file 06 §5).
- **spectrum** — the collection of eigenvalues, or (in Fourier) the distribution over
  frequencies. Context tells you which.
- **self-adjoint / symmetric** — "the same when you swap the two arguments"
  (operator twin of "$A=A^\top$").
- **positive (semi-)definite** — "never gives a negative variance" (file 05 §6).
- **integrable / $L^1$** — the integral **converges** to a finite number.
- **continuous modification** — a version of the process with continuous paths
  (file 09 §2).
- **modification vs indistinguishable** — "for each $t$" vs "for all $t$ at once"
  (file 09 §2).
- **stationary** — the statistics do not change with time (file 09 §3).
- **ergodic** — one long path reveals all the statistics (file 09 §4).
- **compact operator** — "behaves like a finite matrix"; gives discrete eigenvalues
  (file 06 §7).
- **in law / in distribution** — the probability distributions agree, even if the
  random objects themselves differ.
- **$O(\Delta t^2)$** — "the error is at most a constant times $\Delta t^2$".
