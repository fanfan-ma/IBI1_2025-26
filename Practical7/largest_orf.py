seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

# import re
# find all substrings with a start code and end with any end code
# step 1: give the start code
# step 2: give any end code
# step 3: between them should be multiples of 3

import re
ORF = re.findall(r'AUG(?:...)*?(?:UAA|UAG|UGA)' , seq)

# find the longest one in ORF
# jugde if ORF is not an empty list
# print the longest OPF and its length

longest_orf = max(ORF , key = len)
if ORF:
    print("The longest ORF is" , longest_orf , "and its length is" , len(longest_orf))
else:
    print("ORF not found")