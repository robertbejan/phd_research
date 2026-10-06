import random
import numpy as np
import plotly.express as px

def simulate_1d_bm(nsteps=1000, t=0.01):
    steps_y = [ np.random.randn()*np.sqrt(t) for i in range(nsteps) ]
    y = np.cumsum(steps_y)
    x = [t*i for i in range(nsteps)]
    return x, y

def simulate_2d_bm(nsteps=1000000, t=0.01):
    steps_y = [ np.random.randn()*np.sqrt(t) for i in range(nsteps) ]
    steps_x = [ np.random.randn()*np.sqrt(t) for i in range(nsteps) ]
    tau = 10
    print(np.mean(np.array([steps_y[1], steps_y[2]])))
    y = np.cumsum(steps_y)
    x = np.cumsum(steps_x)
    return x, y

simulation_data = {}
x, y = simulate_2d_bm()
simulation_data['y{col}'] = y
simulation_data['x'] = x

fig = px.line(simulation_data)
fig.show()