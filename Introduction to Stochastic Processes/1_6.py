import numpy as np
import matplotlib.pyplot as plt
import matplotlib

dt = 0.01
N = 800  # time steps
M = 300  # particles
gamma = 1  # friction
sigma = 1  # noise strength
np.random.seed(42)

t = np.arange(N) * dt
print(t)

# Normal diffusion - Ornstein-Uhlenbeck velocity
# dv = - gamma v dt + sigma dW
# C(t) = (sigma^2 / 2gamma) exp(-gamma t)
# D = sigma^2 / (2 gamma^2)

v_ou = np.zeros((M,N))
v_ou[:,0] = np.random.randn(M) * np.sqrt(sigma**2 / (2*gamma))

for n in range(N - 1):
    v_ou[:, n+1] = v_ou[:, n] - gamma * v_ou[:, n] * dt + np.sqrt(dt) * np.random.randn(M)

C_ou = np.array([np.mean(v_ou[:, :N-tau] * v_ou[:, tau:]) for tau in range(N)])

D_ou = np.cumsum(C_ou) * dt

x_ou = np.cumsum(v_ou, axis=1) * dt
msd_ou = np.mean((x_ou -x_ou[:, 0:1]) **2, axis=0)

print(f"C_ou {C_ou[-1]}")
print(f"D_ou {D_ou[-1]}")

C_ou_theory = (sigma**1 / (2*gamma)) * np.exp(-gamma * t)
D_ou_theory = 1 / (2*gamma**2)
msd_ou_theory = 2 * D_ou_theory * t

print(f"C_ou_theory {C_ou_theory[-1]}")
print(f"D_ou_theory {D_ou_theory}")