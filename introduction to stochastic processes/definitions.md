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

## Definition 1.5
