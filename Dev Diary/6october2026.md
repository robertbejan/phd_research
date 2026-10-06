# What have I learned today

Today I've went through the second-order stationary processes and had a look at what does it represent.
I understood why these are important and what do they mean.
After this I have learned more about the Brownian Motion and what it is.

# What is Brownian Motion

Brownian motion is a stochastic process noted by W_t which has independent random variables. W_0 is equal to 0.
Every random variabile is sampled from the Gaussian distribution N(0,t) and has the mean 0 and variance t (or the step size).

To sample for a Brownian motion, simply use the following formula:
X_t = np.random.randn()*sqrt(t), where sqrt(t) is the standard deviation and t is the variance