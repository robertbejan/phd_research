import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

dt = 0.01
N = 100
t = [i * dt for i in range(int(N))]
mu = np.zeros(N)
def C(s,t):
    length_scale = 0.5
    sigma_f = 1.0
    return sigma_f**2 * np.exp(-0.5 * (s-t)**2 / length_scale**2)

Gamma = np.zeros((N,N))
print(Gamma)
for i in range(N):
    for j in range(N):
        Gamma[i,j] = C(t[i], t[j])

print(Gamma)
print(Gamma.shape)

Lambda = np.linalg.cholesky(Gamma)

xi = np.random.normal(0,1,size=N)
X = mu + np.dot(Lambda, xi)

plt.figure()
plt.plot(t, X)
plt.show()

print(X)

# Explanation
# dt is the step size
# N is the number of steps
# t is the time vector
# X is the vector to store the stochastic process values
# mu is the vector of means
# Gamma is the covariance matrix
# Lambda is the Cholesky decomposition of the covariance matrix Gamma
# xi is a vector of standard normal random variables

# What I have learned from this exercise
# This is a realization of a Gaussian process with size N. The covariance function C(s,t) defines the relationship between the timesteps, from t = 1 to t = N.
# The Cholensky factorization is used to generate the correlated random variables from the standard normal random variables xi.
# The resulted vector X is a sample of size N from the Gaussian process defined by the sum between the mean vector of size N and the dot product of the lambda matrix and the sampled number from the standard normal distribution.
# This experiment shows how to generate a sample path of a Gaussian process.