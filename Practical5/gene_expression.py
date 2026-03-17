# create a dictionary called dict_genes
# add another gene into this directory
# install the installation package, then import and test it

dict_genes = {
    "TP53": 12.4, # pay attention that the mapping relationships in the dict should be separated by commas
    "EGFR": 15.1,
    "BRCA1": 8.2,
    "PTEN": 5.3,
    "ESR1": 10.7
    }
dict_genes["MYC"] = 11.6 # add another gene into the dict
print("Gene expression dictionary:" , dict_genes)
import numpy as np
import matplotlib.pyplot as plt

# Strp 1: create a vairable to store the number of genes(bars)
# Step 2: create variables to store the height, position and width of the bars respectively
# Step 3: retrieve values from the dictionary
# (create empty lists (because we need it to be dynamic, so do not use tuple))
# (use for to get into the dictionary and take out the keys and values inside in each cycle respectively)
# (add it to the right list)
# Step 4: give the title of x-axis and y-axis respectively
# Step 5: give the distance between the coordinates, make sure that on the x-axis, it is the same as the positions of the bars

N = len(dict_genes)
genes = []
expressions = []
for gene , expression in dict_genes.items():
    genes.append(gene)
    expressions.append(expression)
width = 0.35
x_coordinate = np.arange(N) # generate x-axis position for each gene
pl = plt.bar(x_coordinate , expressions , width) # the contents in the brackets represent the position, height and width of the bars respectively
plt.ylabel("Expressions")
plt.title("Expressions by gene")
plt.xticks(x_coordinate , genes) # display the numerical positions as label names
plt.yticks(np.arange(0 , 20 , 2)) # the contents in the brackets represent the start point, end point and step of the y-axis respectively
plt.show()

# create a variable called gene_of_interest
# jugde if it is one of the names in the dictionary
# if yes, print its expression
# if no, print an error message

gene_of_interest = "TP53" # this could be modified
if gene_of_interest in dict_genes: # search for the key in the dictionary
    print("the expression of" , gene_of_interest , "is" ,  dict_genes[gene_of_interest])
else:
    print("it is not in the gene list")

# calculate the sum of the expressions
# divide it by N

sum_expression = 0
for value_expression in dict_genes.values():
    sum_expression += value_expression
average_expression = sum_expression/N
print("the average gene expression level across all genes is" , average_expression)