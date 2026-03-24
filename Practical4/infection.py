# give the initial number of infected students and the growth rate over 24 hrs
# write the formula for calculating the number of newly infected students each day
# reassign the original variable to represent the current number of infected students, print it
# compare this value with 91. If it >= 91, terminate the loop
i = 1 # to record the date
a = 5 # the initial number of infected students is 5
r = 0.4 # the growth rate is 0.4
print("The number of infected students is" , a , "at day" ,i) # recording the initial number
while a < 91:
    a += r*a
    i += 1
    if a > 91:
        a = 91
    print("The number of infected students is" , a , "at day" ,i)
print("it takes" , i , "days to infect all")

    
