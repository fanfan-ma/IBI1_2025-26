# open the origin file
# open the new, empty file
# create a variable called sequence and make it an empty string (to store the gene lines)
# get into the for loop and get all the lines respectively
# judge if the line is the head line (start with >)
# if yes, get the gene name and write it into the new FASTA file, update the sequence to empty string
# when in the HEAD line, judge if gene line (a-1) is correct, if yes, write head line (a-1) and gene line (a-1)
# if no, join the lines together, which means, cut the \n and add to the sequence
# find the start code in the new string after concentration
# judge if the string has in-frame stop codons (this is done when the loop get into next HEAD line)
# if yes, write the whole string into the new FASTA file
# if no, continue to the next line

input_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa' , 'r')
output_file = open('stop_genes.fa' , 'w')
sequence = ""
gene_name = ""
import re
for line in input_file:
    if re.search(r'^>' , line): 
        if re.search(r'ATG(?:...)*?(?:TAA|TAG|TGA)' , sequence):
            output_file.write('>' + gene_name + ';') # get the first string in the list
            stop_codons = re.findall(r'ATG(?:...)*(TAA|TAG|TGA)' , sequence)
            output_file.write(",".join(stop_codons) + '\n')
            for i in range(0, len(sequence), 60):
                output_file.write(sequence[i:i+60] + '\n')
        gene_name = re.findall(r'>(\S*)' , line)[0]
        sequence = ""
    else:
        sequence += line.rstrip()
if re.search(r'ATG(?:...)*?(?:TAA|TAG|TGA)' , sequence):
    stop_codons = re.findall(r'ATG(?:...)*?(TAA|TAG|TGA)' , sequence)
    output_file.write(",".join(stop_codons) + '\n')
    for i in range(0, len(sequence), 60):
        output_file.write(sequence[i:i+60] + '\n')
input_file.close()
output_file.close()