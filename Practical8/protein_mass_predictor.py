# create a dictionary to store the amu of each AA
# traverse each AA, then calculate its quantity, and subsuquently calculate its quantity
# return the final mass

amino_acid_dict = {
        "G": 57.02,
        "A": 71.04,
        "S": 87.03,
        "P": 97.05,
        "V": 99.07,
        "T": 101.05,
        "C": 103.01,
        "I": 113.08,
        "L": 113.08,
        "N": 114.04,
        "D": 115.03,
        "Q": 128.06,
        "K": 128.09,
        "E": 129.04,
        "M": 131.04,
        "H": 137.06,
        "F": 147.07,
        "R": 156.10,
        "Y": 163.06,
        "W": 186.08
    }
while True:
    amino_acid_sequence = input("Please enter the amino acid sequence of the protein: ")
    valid = True
    for amino_acid in amino_acid_sequence:
        if amino_acid not in amino_acid_dict.keys():
            print("Error: amino acid not found")
            valid = False
            break
    if not valid: # if the input is legal, then do not go to the continue step, if it is illegal, continue and input again
        continue
    break # exit the loop
def calculating_protein_mass(amino_acid_sequence , amino_acid_dict):
    mass = 0
    for amino_acid in amino_acid_sequence:
        mass += amino_acid_dict[amino_acid]
    return mass
protein_mass = calculating_protein_mass(amino_acid_sequence , amino_acid_dict)
print(f"The mass of the total protein in atomic mass units is {protein_mass}.")