# What does this piece of code do?
# Answer: This program calculates the sum of 11 randomly chosen integers between 1 and 10

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint # to import a function that can generate random numbers from a library

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil # Also to import a function, but I do not think this line has been used in this program

total_rand = 0
progress=0
while progress<=10: # to limit the number of operations to 11 times
	progress+=1
	n = randint(1,10) # to randomly choose a number between 1 and 10
	total_rand+=n # to calculate the sum of 11 randomly chosen numbers

print(total_rand) # print the final result

