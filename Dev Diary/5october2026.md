# What I have learned today

# Stationary process

I have learned about the existance of Stationary processes. 
A stationary process is a stochastic process that follows the principle:
P(X_tk in Ak) = P(X_tk+s in Ak) where s,t in T and s is considered an offset or shift.
Let Y0, Y1 a sequence of iid random variables and a sequence Xk=Yk. Xk is proven as being a stationary process because of iid.

A stationary process with P(X_tk in Ak) and one P(X_tk+s in Ak) share the same mean based on the law of large numbers
A stationary process with P(X_tk in Ak) equal to P(Z) share the same mean based on the law of large numbers if they have the same distribution

# Second-order stationary process

Let Xt be a random process with finite second movement E(abs(Xt))^2 finite and assume that it is strictly stationary.
Then we have E(X_t+s) = E(X_t)

from which we conclude that the covariance of X_t+s is equal to the covariance of X_t given by the following statement
E((X_t1+s - mu)(X_t2+s - mu)) = E((X_t1 - mu)(X_t2 - mu))

and implies that the covariance function depends only on the difference between the two times t and s
C(t,s) = C(t-s)

Soooo a second-order stationary process is a stochastic process if the first moment EX_t is a constant and covariance function E(X_t - mu)(X_s - mu) depends only on the difference between t and s.

EX_t = mu, E((X_t - mu)(X_s - mu)) = C(t-s)

We can analyse the covariance using Fourier transformation.

A very important aspect is the diffusion coefficient which is demonstrated to exist in the book. 
The diffusion coefficient is a value given by the following statement:
D = integral bounded by 0 and infinite of C(t)dt. Basically the sum of all the covariances throughout the stochastic process.
If the C(t) decays slowly, it means that the memory kernel has long memory and otherwise.

Also, we conclude that the average of areas of the squared random variables are aproximately 2Dt.
Also, that the average of squared positions are equal to 2Dt. The larger the D is, the faster the diffusion is.