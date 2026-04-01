# open the input and outpot file
# ask user to input the stop codon and judge if it is a valid string
# search for the farthest in-frame stop codon, and get the in-frame codons upstream
# get into a loop and find all the specific codon and count
# draw the pie chart and write it into the output file

input_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa' , 'r')
stop_codon = input("Please input one of the stop codons (TAA, TAG, TGA):")
n = 0
sequence = ""
codon_counts = { # store the initial numbers of codons
'AAA':0,'AAC':0,'AAG':0,'AAT':0,
'ACA':0,'ACC':0,'ACG':0,'ACT':0,
'AGA':0,'AGC':0,'AGG':0,'AGT':0,
'ATA':0,'ATC':0,'ATG':0,'ATT':0,
'CAA':0,'CAC':0,'CAG':0,'CAT':0,
'CCA':0,'CCC':0,'CCG':0,'CCT':0,
'CGA':0,'CGC':0,'CGG':0,'CGT':0,
'CTA':0,'CTC':0,'CTG':0,'CTT':0,
'GAA':0,'GAC':0,'GAG':0,'GAT':0,
'GCA':0,'GCC':0,'GCG':0,'GCT':0,
'GGA':0,'GGC':0,'GGG':0,'GGT':0,
'GTA':0,'GTC':0,'GTG':0,'GTT':0,
'TAC':0,'TAT':0,
'TCA':0,'TCC':0,'TCG':0,'TCT':0,
'TGC':0,'TGG':0,'TGT':0,
'TTA':0,'TTC':0,'TTG':0,'TTT':0
}
import re
import numpy as np
import matplotlib.pyplot as plt
if stop_codon in ["TAA" , "TAG" , "TGA"]:
    for line in input_file:
        if re.search(r'^>' , line):
            if sequence != "": # to skip during the first gene cycle
                matches = []
                for start in re.finditer(r'ATG', sequence):
                    i = start.start()
                    for j in range(i+3, len(sequence)-2, 3):
                        codon = sequence[j:j+3]
                        if codon in ['TAA','TAG','TGA']:
                            if codon == stop_codon:
                                matches.append(sequence[i:j+3])
                            break
                if matches:
                    n += 1
                    longest = max(matches, key = len) # compare the length of strings in the tuple
                    in_frame_codons_list = []
                    for i in range(0 , len(longest) - 3 , 3):
                        in_frame_codons_list.append(longest[i:i+3])
                    for in_frame_codon in ['AAA','AAC','AAG','AAT','ACA','ACC','ACG','ACT','AGA','AGC','AGG','AGT','ATA','ATC','ATG','ATT','CAA','CAC','CAG','CAT','CCA','CCC','CCG','CCT','CGA','CGC','CGG','CGT','CTA','CTC','CTG','CTT','GAA','GAC','GAG','GAT','GCA','GCC','GCG','GCT','GGA','GGC','GGG','GGT','GTA','GTC','GTG','GTT','TAC','TAT','TCA','TCC','TCG','TCT','TGC','TGG','TGT','TTA','TTC','TTG','TTT']:
                        codon_counts[in_frame_codon] += in_frame_codons_list.count(in_frame_codon)
            sequence = ""
        else:
            sequence += line.rstrip()
    matches = []
    for start in re.finditer(r'ATG', sequence):
        i = start.start()
        for j in range(i+3, len(sequence)-2, 3):
            codon = sequence[j:j+3]
            if codon in ['TAA','TAG','TGA']:
                if codon == stop_codon:
                    matches.append(sequence[i:j+3])
                break
    if matches:
        n += 1
        longest = max(matches, key = len) # compare the length of strings in the tuple
        in_frame_codons_list = []
        for i in range(0 , len(longest) - 3 , 3):
            in_frame_codons_list.append(longest[i:i+3])
        for in_frame_codon in ['AAA','AAC','AAG','AAT','ACA','ACC','ACG','ACT','AGA','AGC','AGG','AGT','ATA','ATC','ATG','ATT','CAA','CAC','CAG','CAT','CCA','CCC','CCG','CCT','CGA','CGC','CGG','CGT','CTA','CTC','CTG','CTT','GAA','GAC','GAG','GAT','GCA','GCC','GCG','GCT','GGA','GGC','GGG','GGT','GTA','GTC','GTG','GTT','TAC','TAT','TCA','TCC','TCG','TCT','TGC','TGG','TGT','TTA','TTC','TTG','TTT']:
            codon_counts[in_frame_codon] += in_frame_codons_list.count(in_frame_codon)
    for codon, count in codon_counts.items():
        print(codon, count)
    print("The number of genes is" , n)
    codons = list(codon_counts.keys())
    counts = list(codon_counts.values())
    labels = codons
    sizes = counts
    plt.figure(figsize=(10,10))
    plt.pie(sizes , labels = labels , autopct = '%1.1f%%' , shadow = False , startangle = 90 , labeldistance=1.2 , pctdistance=0.8 , textprops={'fontsize': 6})
    plt.title("Codon Usage in Longest ORFs", fontsize=14)
    plt.axis('equal')
    plt.savefig("codon_pie_chart.png" , dpi = 300 , bbox_inches = 'tight')
    plt.close()
else:
    print("Please enter the correct stop codon")
input_file.close()