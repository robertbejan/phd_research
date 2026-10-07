# Chapter 1 Exercise Toolkit

**Book:** G. A. Pavliotis, *Stochastic Processes and Applications: Diffusion
Processes, the Fokker–Planck and Langevin Equations* (Springer, 2014).
**Chapter 1** = "Stochastic Processes". The exercises live in **§1.7** (pp. 23–27),
and there are **28** of them.

This folder is a **toolkit**, *not* a solution manual. Each file collects the
**concepts, theorems and algebraic tools** you need in order to attack a group of
exercises **yourself**. Every toolkit contains:

- **Which exercises** it covers, and where they sit in the book.
- **Tools** – the definitions, theorems and identities the exercise relies on,
  quoted with the book's own numbering (e.g. Definition 1.5, Eq. (1.15)).
- **Warm-ups** – short, *solved* problems that are **analogous but not identical**
  to the real exercise. Do these first to build the muscle.
- **Game plan** – a recipe plus guiding questions, with the *first step or two*
  only. The finish is left to you.
- **Pitfalls** – the traps that commonly eat an afternoon.
- **Numerical check** – a Python idea to confirm your algebra (optional).

## How to use this folder

1. Read the relevant section of the book (1.1–1.6) **first**. The toolkit assumes
   you have seen the material once.
2. Open the matching toolkit file below.
3. Attempt the exercise using the **Game plan** – don't peek at anything else.
4. When stuck, use the **Tools** and **Warm-ups**, then try again.
5. Verify with the **Numerical check** (NumPy / SciPy). If the numbers agree with
   your pen-and-paper result, you are done.

> ⚠️ No file here contains the final answer to an exercise. That is deliberate.
> Struggle productively first; the tools are scaffolding, not a ladder to the roof.

## Map: exercise ➜ toolkit file

| Exercise | Topic | Toolkit file |
|---------:|-------|--------------|
| 1 | iid sequence $X_n=Y_n$: stationarity, ergodicity | `01_stationarity_and_ergodicity.md` |
| 2 | constant process $X_n=Z$: strict stationarity | `01_stationarity_and_ergodicity.md` |
| 3 | harmonic (trigonometric) process: weak stationarity | `01_stationarity_and_ergodicity.md` |
| 4 | moving-average process: covariance, weak stationarity | `01_stationarity_and_ergodicity.md` |
| 5 | Brownian expectations (char. functions, 2nd moment) | `02_brownian_gaussian_expectations.md` |
| 6 | Brownian bridge | `02_brownian_gaussian_expectations.md` |
| 7 | sum of exponentials: spectrum, Green–Kubo, $N\to\infty$ | `04_spectra_and_green_kubo.md` |
| 8 | position of a Brownian particle (integral of OU) | `03_ornstein_uhlenbeck_and_integrals.md` |
| 9 | $\mathbb E e^{\sigma W(t)}$, $\mathbb E[\sin\cdot\sin]$ | `02_brownian_gaussian_expectations.md` |
| 10 | geometric Brownian motion: mean, var, pdf | `02_brownian_gaussian_expectations.md` |
| 11 | prove Proposition 1.5 (BM symmetries) | `02_brownian_gaussian_expectations.md` |
| 12 | distribution function of stationary OU | `03_ornstein_uhlenbeck_and_integrals.md` |
| 13 | integral of BM: mean and correlation | `03_ornstein_uhlenbeck_and_integrals.md` |
| 14 | $\int_t^{t+1}(W_s-W_t)\,ds$: second-order stationary | `03_ornstein_uhlenbeck_and_integrals.md` |
| 15 | the Ornstein–Uhlenbeck bridge | `03_ornstein_uhlenbeck_and_integrals.md` |
| 16 | damped oscillator: spectrum, mean-square displacement | `04_spectra_and_green_kubo.md` |
| 17 | scaling property of fractional BM | `02_brownian_gaussian_expectations.md` |
| 18 | Poisson process: no continuous modification | `05_continuity_and_poisson.md` |
| 19 | continuity of the correlation function | `05_continuity_and_poisson.md` |
| 20 | integral operator: self-adjoint, nonnegative | `06_integral_operators_and_spectral_theory.md` |
| 21 | the operator is Hilbert–Schmidt | `06_integral_operators_and_spectral_theory.md` |
| 22 | trace identity $\sum_n\lambda_n = T\,R(0)$ | `06_integral_operators_and_spectral_theory.md` |
| 23 | KL expansion for $R(t,s)=ts$ | `07_karhunen_loeve_analytical.md` |
| 24 | KL expansion of the Brownian bridge | `07_karhunen_loeve_analytical.md` |
| 25 | KL expansion of a transformed process | `07_karhunen_loeve_analytical.md` |
| 26 | KL expansion for $R(s,t)=\cos(2\pi(t-s))$ | `07_karhunen_loeve_analytical.md` |
| 27 | simulate BM / bridge / OU from their KL expansion | `08_karhunen_loeve_computational.md` |
| 28 | exponential covariance field: KL + numerics | `08_karhunen_loeve_computational.md` |

## The study loop

```
read section (book)  →  read toolkit  →  attempt (Game plan)  →  verify (Python)
        ↑                                                                    │
        └────────────────────  revisit Tools / Warm-ups  ←──────────────────┘
```

## Notation used here

- $W_t$ (or $W(t)$) — standard one-dimensional Brownian motion; $\mathbb E W_t=0$,
  $\operatorname{Cov}(W_s,W_t)=\min(s,t)$, increments $W_t-W_s\sim\mathcal N(0,t-s)$
  independent.
- $\mathcal N(m,\sigma^2)$ — normal with mean $m$ and variance $\sigma^2$.
- $C(t)$ / $R(t)$ — autocovariance / autocorrelation of a (mean-zero) stationary
  process; $R(t,s)$ is the general two-time covariance.
- $\hat f(\omega)=\int e^{-i\omega t}f(t)\,dt$ — Fourier transform.
- $\langle\cdot,\cdot\rangle$ — inner product in $L^2$.
