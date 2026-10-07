import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

np.random.seed(0)
T = 10000000
phi = 0.7
sigma = 1.0

X = np.zeros(T)
for t in range (1, T):
    X[t] = phi * X[t-1] + np.random.normal(0, sigma)

average_x = np.mean(X)

def autocov(x, tau, mu):
    if tau == 0:
        return np.mean((x - mu) * (x - mu))
    return np.mean((x[tau:] - mu) * (x[:-tau] - mu))

t1, t2, s = 0, 8, 8
tau = t2 - t1

covariance_original = autocov(X, tau, average_x)

X_shifted = X[s:]
covariance_shifted = autocov(X_shifted, tau, average_x)

# print(covariance_original)
# print(covariance_shifted)

C0 = autocov(X, 0, average_x)
Ch = autocov(X, 20, average_x)
print(2*C0 - 2*Ch)