# import necessary libraries

import numpy as np
import matplotlib.pyplot as plt

# make array of all susceptible population

population = np.zeros((100 , 100))

# randomly choose a person to be infected
# change his/her number to 1

outbreak = np.random.choice(range(100) , 2)
population[outbreak[0] , outbreak[1]] = 1

# plot the picture

plt.figure(figsize = (6 , 4) , dpi = 150)
plt.imshow(population , cmap = "viridis" , interpolation = "nearest")
plt.xlabel("X coordinate")
plt.ylabel("Y coordinate")
plt.xticks(np.arange(0, 100, 20))
plt.yticks(np.arange(0, 100, 20))
plt.title("Initial infection")
plt.colorbar()
plt.savefig("Initial_infection.png")
plt.show()

# set up model parameters

β = 0.3
γ = 0.05

# get into a time loop
# find the infected people
# randomly recover
# randomly infect their neighbors

for t in range(101):
    S_x, S_y = np.where(population == 0)
    I_x, I_y = np.where(population == 1)
    R_x, R_y = np.where(population == 2)
    for x , y in zip(I_x , I_y):
        if np.random.rand() < γ:
            population[x , y] = 2
        for s in ([x-1 , y-1] , [x-1 , y] , [x-1 , y+1] , [x , y-1] , [x , y+1] , [x+1 , y-1] , [x+1 , y] , [x+1 , y+1]):
            nx , ny = s
            if 0 <= nx < 100 and 0 <= ny < 100:
                if population[nx , ny] == 0:
                    if np.random.rand() < β:
                        population[nx , ny] = 1

# draw the pictire at 0 , 10 , 50 , 100

    if t in [0, 10, 50, 100]:
        plt.figure(figsize = (6 , 4) , dpi = 150)
        plt.imshow(population, cmap = 'viridis', interpolation = 'nearest')
        plt.title(f"Time {t}")
        plt.xlabel("X coordinate")
        plt.ylabel("Y coordinate")
        plt.xticks(np.arange(0, 100, 20))
        plt.yticks(np.arange(0, 100, 20))
        plt.colorbar()
        plt.savefig(f"Time {t}.png")
        plt.show()