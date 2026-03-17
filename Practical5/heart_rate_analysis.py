# create a dictionary
# print a sentence with number of the patients
# calculate the average
# print the average

dict_heartrate = {
    "patient 1": 72,
    "patient 2": 60,
    "patient 3": 126,
    "patient 4": 85,
    "patient 5": 90,
    "patient 6": 59,
    "patient 7": 76,
    "patient 8": 131,
    "patient 9": 88,
    "patient 10": 121,
    "patient 11": 64
}
N = len(dict_heartrate)
print("There are" , N , "patients in the dataset.")
sum_heartrate = 0
for heartrate in dict_heartrate.values():
    sum_heartrate += heartrate
mean_heartrate = sum_heartrate/N
mean_heartrate = round(mean_heartrate , 2) # round to two decimal places
print("The mean heart rate is" , mean_heartrate)

# initialize the number of each category
# iterate through values
# determine the corresponding category, then count
# create a new dictionary for the categories
# judge which value is the largest

num_low = 0
num_normal = 0
num_high = 0
for heartrate_determine in dict_heartrate.values():
    if heartrate_determine < 60:
        num_low += 1
    elif heartrate_determine > 120:
        num_high += 1
    else:
        num_normal += 1
print("The number of patients in the low category is" , num_low)
print("The number of patients in the normal category is" , num_normal)
print("The number of patients in the high category is" , num_high)
dict_categories = {
    "low": num_low,
    "normal": num_normal,
    "high": num_high
}
max_category = max(dict_categories , key = dict_categories.get) # return the corresponding key based on the value's size
max_number = dict_categories[max_category]
print("The" , max_category , "category contains the largest number of patients, and the number is" , max_number)

# import
# give the ordered names and sizes
# give the explode og each pie
# give the direction of not having shadow
# give the stratangle as 90
# make sure the shape is correct

import matplotlib.pyplot as plt
categories = ["low" , "normal" , "high"] # define labels for the pie chart categories
numbers = [num_low , num_normal , num_high] # define the corresponding counts for each category
explode = (0 , 0 , 0)
plt.pie(numbers , explode = explode , labels = categories , shadow = False , startangle = 90 , autopct = "%1.1f%%")
plt.axis("equal")
plt.show() 
