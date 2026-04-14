# import necessery libraries

import numpy as np
import matplotlib.pyplot as plt

# define basic variables
# create arrays to record the change

S = 9999
I = 1
R = 0
N = 10000
β = 0.3
γ = 0.05
S_history = [9999]
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

time = np.arange(1001)
plt.figure(figsize = (6 , 4) , dpi = 150)
plt.plot(time, S_history, label="susceptible")
plt.plot(time, I_history, label="infected")
plt.plot(time, R_history, label="recovered")
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model")
plt.xticks(np.arange(0 , 1000 , 200))
plt.yticks(np.arange(0 , 10000 , 2000))
plt.legend()
plt.savefig("simple_SIR_model.png")