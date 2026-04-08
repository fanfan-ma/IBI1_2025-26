# create a dictionary to store the amu of each AA

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

# define a function to calculate mass and judge if the suquence is valid

def calculating_protein_mass(amino_acid_sequence , amino_acid_dict):
    """
    Input: a sequence of amino acid
    Return: the mass of the protein (if the amino acid does not exist, return None)
    """
    mass = 0
    for amino_acid in amino_acid_sequence:
        if amino_acid not in amino_acid_dict.keys():
            return None
        else:
            mass += amino_acid_dict[amino_acid]
    return mass

# get into a loop to get valid input, use the function to judge and calculate

if __name__ == "__main__": # ensure that the test program will only be executed when directly run this file
    while True:
        amino_acid_sequence = input("Please enter the amino acid sequence of the protein: ")
        valid = True
        protein_mass = calculating_protein_mass(amino_acid_sequence , amino_acid_dict)
        if protein_mass == None:
            print("Error: amino acid not found")
            valid = False
        if not valid: # if the input is legal, then do not go to the continue step, if it is illegal, continue and input again
            continue
        print(f"The mass of the total protein in atomic mass units is {protein_mass:.2f}.")
        break # exit the loop