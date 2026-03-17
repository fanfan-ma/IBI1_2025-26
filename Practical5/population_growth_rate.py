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
    country["percent_change"] = percent_change
    print("The percentage change of" , country["country"] , "is" , country["percent_change"])
