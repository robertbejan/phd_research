# 12 — Which maths do I need, exercise by exercise?

Use this as a **reading order**. For each exercise: read the listed primer sections
first, then the toolkit file. "Technique" numbers refer to file 11.

| Ex. | Topic | Primer sections to read first | Toolkit | Techniques |
|----:|-------|------------------------------|---------|-----------|
| 1 | iid sequence: stationarity, ergodicity | 03 §1–§4, §6; 09 §1, §3, §4 | `01_...md` | 12, 13 |
| 2 | constant process $X_n=Z$ | 03 §1, §4; 09 §1, §3 | `01_...md` | 12 |
| 3 | harmonic process | 02 §4; 03 §3, §4; 09 §3 | `01_...md` | 12, 13 |
| 4 | moving average | 02 §4; 03 §3, §4 | `01_...md` | 12 |
| 5 | Brownian expectations | 04 §1–§5, §7; 10 §1 | `02_...md` | 1, 6 |
| 6 | Brownian bridge | 04 §5, §6; 10 §1 | `02_...md` | 1, 4, 6, 7 |
| 7 | sum of exponentials: spectrum, Green–Kubo | 01 §6; 07 §2, §4, §5; 09 §5, §6 | `04_...md` | 5, 11 |
| 8 | integral of OU | 04 §5; 09 §6; 10 §3 | `03_...md` | 1, 2, 3, 7 |
| 9 | $\mathbb Ee^{\sigma W}$, sine products | 02 §3, §4; 04 §3; 10 §1 | `02_...md` | 6 |
| 10 | geometric BM | 01 §3; 04 §1–§3 | `02_...md` | 6 |
| 11 | BM symmetries (Prop. 1.5) | 04 §5, §6; 10 §1 | `02_...md` | 4, 7 |
| 12 | stationary OU law | 08 §2; 09 §7; 10 §3 | `03_...md` | 7 |
| 13 | integral of BM | 01 §7; 09 §6; 10 §2 | `03_...md` | 1, 2, 3 |
| 14 | sliding window of BM | 09 §3; 10 §1 | `03_...md` | 1, 12 |
| 15 | OU bridge | 04 §5; 09 §7; 10 §1, §3 | `03_...md` | 4, 7 |
| 16 | damped oscillator | 01 §6; 07 §4, §5; 08 §2, §3 | `04_...md` | 5, 11 |
| 17 | fractional BM scaling | 04 §5, §6; 10 §1 | `02_...md` | 4 |
| 18 | Poisson: no continuous modification | 03 §6; 09 §1, §2; 10 §4 | `05_...md` | 14 |
| 19 | continuity of $R(t,s)$ | 03 §6; 09 §3, §7 | `05_...md` | 14 |
| 20 | operator self-adjoint, nonnegative | 05 §2–§6; 06 §1–§5 | `06_...md` | 10 |
| 21 | Hilbert–Schmidt | 06 §2, §7 | `06_...md` | 10 |
| 22 | trace identity | 05 §5, §6; 06 §6 | `06_...md` | 10 |
| 23 | KL for $R(t,s)=ts$ | 05 §3, §4; 06 §2, §5 | `07_...md` | 9 |
| 24 | KL for the bridge | 07 §2; 08 §3, §4, §5; 06 §5, §9 | `07_...md` | 8 |
| 25 | KL for a transformed process | 05 §4; 06 §2; 10 §3 | `07_...md` | 7, 8 |
| 26 | KL for $\cos(2\pi(t-s))$ | 02 §4; 06 §2, §5; 07 §2 | `07_...md` | 9 |
| 27 | simulate BM/bridge/OU from KL | 05 §7; 06 §6; 11 §9 | `08_...md` | 3, 9 |
| 28 | exponential covariance field | 05 §7; 06 §6, §8; 08 §5 | `08_...md` | 8, 9 |

## Fastest route if you are short of time

1. **03** (probability) → **04** (Gaussian) → **09** (processes). These three unlock
   Exercises 1–19 and are the "core".
2. **05** (linear algebra) → **06** (operators) → **07** (Fourier) → **08** (ODEs).
   These unlock Exercises 20–28.
3. **11** (techniques) last, as a revision checklist.
4. **01**, **02** on demand — only if a specific computation or identity looks alien.

## The 6 ideas that carry the whole chapter

1. **Mean + covariance define a Gaussian process.**
2. **$\operatorname{Cov}(W_s,W_t)=\min(s,t)$, and split at the $\min$.**
3. **Integrals/limits of Gaussians are Gaussian and Itô isometry gives the variance.**
4. **Stationarity = the lag formula; ergodicity = "$C$ decays so time averages work".**
5. **Covariance kernel = integral operator; its eigenpairs are the Karhunen–Loève
   basis; $\sum\lambda_n=\int R(t,t)$ (trace/Mercer).**
6. **$e^{-\alpha|t|}$ is the universal correlation — from the OU/oscillator ODE, and
   its Fourier transform is $2\alpha/(\alpha^2+\omega^2)$.**
