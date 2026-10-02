# What I have learned today

In general, I have reviewed what exactly is a stochastic process. Since I want to be able to understand mathmatically, I will try to explain as best as possible in math language.

## What is a stochastic process?
Let T be an ordrered set, (omega, F_curved, P) a probability space, and (E, G_curved) a measurable space. A stochastic process is a collection of random variables X = {X_t; t in T} s.t for each t in T, X_t is a random variable from the probability space to the measurable space. The sample space is omega, the F_curved is the event space, P is the probability measure, and E is the state space of the stochastic process X_t.

The common notation for the stochastic process is X(small_omega)_t = {X_t1, X_t2, ... X_tk}

The finite-dimensional distribution (FDD) is the collection of CDFs for the stochastic process. The collection is given by the following formula:
F(x) = P(X(t_i)<=x_i, i=1,...k), where x=(x1, ..., x_k)

Also, if we have two random processes with the same FDD then they are equivalent.

## What is a gaussian stochastic process
A gaussian stochastic process is a stochastic process that is ordered by the gaussian law. Let the stochastic process X_t. If all of the random variables in X_t are in N(mu_k, K_k) for some vector mu_k and nonnegative covariance matrix K_k for all positive integer k and for all t1, t2, ... tk then it is a Gaussian stochastic process. 

Because it is a gaussian process, it also has the following particularities:
1. MEAN given by the formula: m(t):= E(x(tk)) where E is the Expectation
2. COVARIANCE or autocorrelation matrix: C(t,s):= E((x(t)-m(t)*(x(s)-m(s))))

The algorithm for an example realization/trajectory of the gaussian process can be found at [this file](<../introduction to stochastic processes/1_4.py>)
