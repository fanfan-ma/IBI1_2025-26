# create a dictionary containg countries, pop_2020, pop_2024
# iterate through the values to obtain each sub-dictionary
# calculate the change
# add it to the corresponding sub-dictionary
# calculate the percent_change and add it to the corresponding sub-dictionary

dict_population = {
    "country1": {
        "country": "UK",
        "pop_2020": 66.7,
        "pop_2024": 69.2
    },
     "country2": {
        "country": "China",
        "pop_2020": 1426,
        "pop_2024": 1410
    },
     "country3": {
        "country": "Italy",
        "pop_2020": 59.4,
        "pop_2024": 58.9
    },
     "country4": {
        "country": "Brazil",
        "pop_2020": 208.6,
        "pop_2024": 212.0
    },
     "country5": {
        "country": "USA",
        "pop_2020": 331.6,
        "pop_2024": 340.1
    }
}
for country in dict_population.values():
    change = country["pop_2024"] - country["pop_2020"]
    country["pop_change"] = change
    percent_change = country["pop_change"]/country["pop_2020"]*100
    percent_change = round(percent_change , 2)
    country["percent_change"] = percent_change # calculate population change and percentage change for each country
    print("The percentage change of" , country["country"] , "is" , country["percent_change"])

# Alternative approach (manual sorting using max and remove):

# list_change = []
# list_change_ordered = []
# for country in dict_population.values():
#     list_change.append(round(country["pop_change"] , 2))
# list_change_copy = list_change.copy()
# for country in dict_population.values():
#     list_change_ordered.append(max(list_change_copy))
#     list_change_copy.remove(max(list_change_copy))
# print(list_change_ordered)

# This method was replaced by sorted() for better efficiency and readability

# sort the dictionaries, use lambda to give the temporary dictionary name, take pop_change as the sorting criterion
# get a loop into the ordered list and print them line by line
# take out the first and the last line

print("\n")
print("Below is the population changes in descending order:")
countries = list(dict_population.values()) # change the sub-dictionaries into a list
countries_ordered = sorted(countries, key = lambda x: x["pop_change"], reverse = True) # sort in descending order
for c in countries_ordered:
    print(c["country"] , ": " , round(c["pop_change"] , 2))
largest_increase_country = countries_ordered[0]
largest_decrease_country = countries_ordered[-1]
print("The country with the largest increase in population is" , largest_increase_country["country"])
print("The country with the largest decrease in population is" , largest_decrease_country["country"])

# import
# use N to give the positions
# create variables for country names, pop_change and width
# give the title of the x- and y-axis
# give the start, end and step of the y-axis

import numpy as np
import matplotlib.pyplot as plt
N = len(countries)
population_change = []
country_name = []
for c_bar in countries:
    population_change.append(c_bar["pop_change"])
    country_name.append(c_bar["country"])
ind = np.arange(N)
width = 0.35
pl = plt.bar(ind , population_change , width)
plt.ylabel("Population Changes")
plt.title("Population Changes by country")
plt.xticks(ind , (country_name))
plt.yticks(np.arange(-20 , 11 , 2)) # it does not include the stop point
plt.axhline(0, color='black', linewidth = 0.5)
plt.show()