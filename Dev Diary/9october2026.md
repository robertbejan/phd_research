# What have I learned today?

Today I went through the Markovian Process and Chapman-Kolmogorov Equation.
In human langauge, the Markov process is a stochastic process in which each future state depends only on the present state. 
This is backed by a lot of maths easy to read. This markov process can be either in discrete-time or in continuous-time.

## The things I have found out about the Markov Process:
1. The simplest Markov Process can be expressed as a random walk.
2. The stochastic process is a MArkov process if the MArkov property is satisfied:
P(X_n+m = i_n+m | X_1 = i_1, ... X_n = i_n) = P(X_n+m = i_n+m | X_n = i_n)
3. The markov process has a conditional probability density.
4. The Brownian motion and the Ornstein-Uhlenbeck both have conditional probability densities
5. We can also deduce a transition matrix which has the probabilities to go from a state to another.
6. You can calculate each of the state we want given a intermediate state, basically using "2 sub-paths" from the main path.
7. We can also get a formula for the evolution of the vector mu, which contains the distribution at time t
8. THere exista a generator matrix G.

## The things I have found out about the Chapman-Kolmogorov:
In short, this basically describes the fact that you can describe the evolution of a process through intermediary events using two sub-paths.

1. In continuous time, the equation is an intergral and in discrete time this is a sum.
2. Another thing about the Markov process, is that the past is recorded in a filtration F, which basically is a collection of sigma-algebras contaning the history of all of the events.
3. The p(y,t|x,s) in the Chapman-Kolmogorov is called transition probability density and it describes the initial position and time x,s and the final position and time y, t.
4. The transition probability density can be split into two p() functions with an intermediary state.