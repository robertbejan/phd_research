# Introduction into stochastic processes
## Definition 1.1

Explanation:
- We have T which is an ordered set (ex. Z+ or R+)
- We also have a probability space with (omega, F, P), where omega is the sample space (all possible outcomes), F is the event space (collection of subsets that are allowed to be assigned probabilities to) and P which is the probability measure
- We also have the measurable space with (E, G) where E is the set of possible results and G is the collection of subsets that we can measure.

The stochastic process in a collection of random sampes X = {X_t, t in T} where each random sample X_t is from the probability space to the measure space.

Example:
``` python
T = {1, 2}
omega = {HH, TH, HT, TT}
X = {(HH, 2), (HT, 1), (TH, 1), (TT, 0)}
E = {0, 1, 2}
```

## Definition 1.2

Explanation: The finite-dimensional distributions FDDs of a stochastic process are the distributions of the Ek-valued random variables X(t_1), X(t_2), ... X(t_k) for an positive k and t_i in T, with i in 1,... k. 

F(x) = P(X_1 <= x_i, ...)

So basically, if we have a random variable, we have some thresholds x_i that are imposed in the evaluation of the CDF.
To calculate the CDF, we need a parameter like x_i for example.

The CDF represents the value of the probability that a random variable X is less than or equal to a specific value x.
- The joint CDF is the probability of multiple events happening. (F(xi) = {Xi<=xi}) => one value
- The FDD is the collection of probabilities of multiple events happening. (F(x1, x2, .., xk) = {X1<=x1, ...})

## Definition 1.3

Explanation:
If we have two processes X_t and Y_t are equivalent if they have same FDDs.
Pretty much what is says.

## Definition 1.4

Explanation: Let a finite-dimensional vector Xt_1, Xt_2, ..., Xt_k be a N(miu_k, K_k) have all of its elements a random variable with a mean miu_k and a variance K_k for all k = 1,2,... and for all t1, t2, ..., tk.

Basically, if all of the CDFs of all the random variables Xt_k are basically a gaussian distribution, then the process is a gaussian stochastic process.

Because we have the FDD, we can draw the actual PROBABILITY DENSITY FUNCTION of the gaussian distribution in finite-dimension. To get the PDFs, we simply derive the CDF.

Some other things noted here. Because this is a GAUSSIAN process x(t), this is characterised by:1
1. MEAN: m(t) := Ex(t) => the average of the set of the possible values
2. COVARIANCE (autocorrelation matrix): C(t,s) = E((x(t) - m(t)) * (x(s) - m(s)))  => the expectation of the direct product between the differences of the set of possible values and mean
3. VARIANCE: V(t) = E((x(t) - m(t))^2)

We can simulate a Gaussian process on a computer. We just need a generator that generates N(0,1) pseudo-random numbers. We can sample from a Gaussian stochastic process by calculation the square root of the covariance. How to do it in python:

''' python
dt = 0.1
N = 10
t = [i * dt for i in range(int(N/dt) + 1)]
X = zeros(1, len(t))
Xn = zeros(1, N)
miu_N = 0.5
std = 3

for X in XN:
    X = miu_N + std * N(0,1)
'''

# Stationary Processes
## Definition 1.5
Let Y0, Y1 be a sequence of independently identically distributed random variables and consider the stochastic process Xn = Yn. Then Xn is a strictly stationary process. Assume that EY0 = mu <+inf. Then, by the law of large numbers, we have that the average of the random variables Xn equals to the average of the random variables Yn and equals to the expectation of Y0 which also equals to mu (the mean). We can also have the same thing for a function f with Ef(Y0)=lim of average of f(Xj).

So basically, the expectation given one random variable, gives the mean or the average of all of the values of the random variables in the sequence almost surely.

The formal definition is:
P(X_t1 in A1, X_t2 in A2, ..., X_tk in Ak) = P(X_t1+s in A1, X_t2+s in A2, ..., X_tk+s in Ak)
When asked to prove it, use the independence and idetically distributed properties.
Independence: P(Y_i in A, Y_j in B) = P(Y_i in A) * P(Y_j in B)
Identically Distributed: P(Y_i in A) = P(Y_j in B)

So what is a strictly stationary process?
R: A strictly stationary process is a stochastic process for which there is more than one equal s-shifted stochastic processes.
It means that the joint probability of all of the random variables are equal. 
EX: Ideal Coin Toss. Any stochastic process will lead to the same probability (50/50)

## Definition 1.6
A stochastic process X_t in L^2 is called second-order stationary if the first moment EX_t is a constant and the covariance function E(X_t-mu)(X_s-mu) depends only on the difference t-s:

EX_t = mu, E((X_t-mu)(X_s-mu)) = C(t-s)

Let X_t be a strictly stationary stochastic process with finite second moment. If it's strictly stationary it implies that EX_t = mu, a constant, and E((X_t-mu)(X_s-mu)) = C(t-s). Hence, a strictly stationary process with finite second moment is also stationary in the wide sense;

If X_n = Y_n and we assume that EY_0 = 0 and EY_0^2=mu^2 <+inf, then X_n is a second-order stationary process with mean zero and correlation function R(k) = mu^2*delta_k0. We have no correlation among the values of the stochastic process at different times.

If X_n = Z and we assume that EZ_0 = 0 and EZ_0^2 = mu^2, then X_n becomes a second-order stationary process with mean zero and correlation function R(k) = mu^2. We have strongly correlated values in the stochastic process at different time steps.

Continuity in the stochastic process is when the limit of the expectation of the between the difference of X_t+h and X_t is 0.

### Lemma 1.1

The covariance function C(t) of a second-order stationary process is continuous for all t in R. The continuity of C(t) is equivalent to the continuity of the process X_t in the L^2 sense. 

E(X_t+h - X_t)^2 = 2(C(0)-C(h)) which converges to 0 as h-->0.

We can use the Fourier Transform on the covariance function of a seconod-order stationary process.

## Definition 1.7 

The covariance function of a second-order stationary process is a non-negative definite function.

## Theorem 1.1 (Bochner) for Fourier transformation of the autocorrelation function C(t)

C(t) = integral_on_R(e^iwt * sigma(dw))

The measure simga(dw) is called the spectral measure of the process Xt.

The correlation time = teta_cor. The slower of the decay of the correlation function, the larger the correlation time.

## Definition 1.8

W(t) : R+ -> R is a real-valued stochastic process (Brownian motion) with almost surely continuous paths such that:
1. W(0) = 0,
2. It has independent increments
3. for every t > s >= 0, the increment W(t)-W(s) has a gaussian distribution with mean = and variance t-s

The density of the random variable W(t) - W(s) is:
g(x;t,s) = (2*pi(t-s))^1/2 * exp(-x^2/(2(t-s))) - in one dimension
g(x;t,s) = (2*pi(t-s))^-d/2 * exp(-norm2(x)/2(t-s))

## Theorem 1.3 (Wiener)

There exists an almost surely continuous process Wt with independent increments such that W0=0 and for each t>=0, the random variable Wt is N(0,t). Furthermore, Wt is almost surely locally Holder continuous with exponent alpha for every alpha in (0,1/2)

## Proposition 1.5

1. Rescaling: X_t = 1/sqrt(c)*W(ct) => Brownian motion looks the same at each timestep
2. Shifting: X_t = W_c+t - W_c => Brownian motion restarts fresh at each time t. It doesn't depend on the past (Markovian).
3. Time reversal: X_t = W_1-t - W_1 => Recording a Brownian motion from 0 to T and then from T to 0 is statistically the same path.
4. Inversion: X0=0, X_t = tW(1/t). Then X0 and X_t look the same at 0 and inf

Brownian motion with drift mu and variance sigma^2 as the process: X_t = mu*t + sigma*W_t

The mean is E(X_t) = mu*t and the variance is E(X_t-E*X_t)^2 = sigma^2*t

# The Ornstein-Uhlenbeck

This chapter explains that the Ornstein-Uhlenbeck is basically a stochastic process with mean 0 and covariance function:
R(t) = e^-abs(t)
The function of the process is V(t)=e^-t*W(e^2t)
