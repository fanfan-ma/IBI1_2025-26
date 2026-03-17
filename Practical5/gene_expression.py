# create a dictionary called dict_genes
# add another gene into this directory
# install the installation package, then import and test it

dict_genes = {
    "gene1": {
        "name": "TP53", # pay attention that the mapping relationships in the dict should be separated by commas
        "expression": 12.4
    }, # whatever the value type is (even also a dict), there should be a comma
    "gene2": {
        "name": "EGFR",
        "expression": 15.1
    },
    "gene3": {
        "name": "BRCA1",
        "expression": 8.2
    },
    "gene4": {
        "name": "PTEN",
        "expression": 5.3
    },
    "gene5": {
        "name": "ESR1",
        "expression": 10.7
    }
}
dict_genes["gene6"] = { # add another gene into the dict
    "name": "MYC",
    "expression": 11.6
}
import numpy as np
import matplotlib.pyplot as plt

# create a vairable to store the quantity of bars
# create variables to store the height, position and width of the bars respectively
# how to do this? firstly, create empty lists (because we need it to be dynamic, so do not use tuple)
# use for to get into the dictionary and take out the dictionaries inside in each cycle respectively
# use key to get the value we need in each dictionary
# add it to the right list
# give the title of x-axis and y-axis respectively
# give the distance between the coordinates, make sure that on the x-axis, it is the same as the positions of the bars

N = 6
genes = []
expressions = []
for gene_reference in dict_genes.values():
    genes.append(gene_reference["name"])
    expressions.append(gene_reference["expression"])
width = 0.35
x_coordinate = np.arange(N) # np.arange means generating a sequence of consecutive numbers starting from 0 and ending at N
pl = plt.bar(x_coordinate , expressions , width) # the contents in the brackets represent the position, height and width of the bars respectively
plt.ylabel("Expressions")
plt.title("Expressions by gene")
plt.xticks(x_coordinate , genes) # display the numerical positions as label names
plt.yticks(np.arange(0 , 20 , 2)) # the contents in the brackets represent the start point, end point and step of the y-axis respectively
plt.show()