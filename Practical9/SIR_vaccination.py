# import necessery libraries

import numpy as np
import matplotlib.pyplot as plt

# define basic variables
# create arrays to record the change

time = np.arange(1001)
plt.figure(figsize = (6 , 4) , dpi = 150)
p_vaccinated = [0 , 0.1 , 0.2 , 0.3 , 0.4 , 0.5 , 0.6 , 0.7 , 0.8 , 0.9 , 1]
for p in p_vaccinated:
    I = 1
    R = 0
    N = 10000
    β = 0.3
    γ = 0.05
    V = int(N * p)
    S = N - V - I
    if S < 0:
        S = 0
    S_history = [S]
    I_history = [1]
    R_history = [0]

# calculate the initiate porportion and p
# get into a loop
# use the random choice to calculate new SIR each time, record the data
# update p

    I_proportion = I / N
    p_infected = β * I_proportion
    for i in range(1000):
        I_new = sum(np.random.choice(range(2) , I , p = [γ , 1 - γ]))
        R += (I - I_new)
        S_new = sum(np.random.choice(range(2) , S , p = [p_infected , 1 - p_infected]))
        I = I_new + S - S_new
        S = S_new
        S_history.append(S)
        I_history.append(I)
        R_history.append(R)
        I_proportion = I / N
        p_infected = β * I_proportion

# give the time
# draw the figure

    plt.plot(time, I_history , label=f"{int(p*100)}%")
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model with different vaccination rates")
plt.xticks(np.arange(0 , 1001 , 200))
plt.yticks(np.arange(0 , 5001 , 1000))
plt.legend()
plt.savefig("vaccination_effect.png")