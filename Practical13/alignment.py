def read_files(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    header = lines[0].strip()
    sequence = ""
    for line in lines[1:]:
        sequence += line.strip()
    return header, sequence

mouse_header, mouse_sequence = read_files("P70396.fasta.txt")
human_header, human_sequence = read_files("P56178.fasta.txt")

amino_acids = "ACDEFGHIKLMNPQRSTVWY"
import random
length = 289
random_sequence = ""
for i in range(length):
    random_sequence += random.choice(amino_acids)

def compare_sequence(seq_1, seq_2, length):
    edit_distance = 0
    for i in range(len(seq_1)):
        if seq_1[i] != seq_2[i]:
            edit_distance += 1
    percentage = (length - edit_distance) / length * 100
    return edit_distance, percentage

HM_compare, HM_percentage = compare_sequence(human_sequence, mouse_sequence, length)
HR_compare, HR_percentage = compare_sequence(human_sequence, random_sequence, length)
MR_compare, MR_percentage = compare_sequence(mouse_sequence, random_sequence, length)

BLOSUM62_matrix = open("BLOSUM62_matrix.txt", "r")
lines = BLOSUM62_matrix.readlines()
headers = lines[0].split()
blosum = {}
for line in lines[1:]:
        parts = line.split()
        row_name = parts[0]
        blosum[row_name] = {}
        scores = parts[1:]
        for i in range(len(headers)):
            column_name = headers[i]
            score = int(scores[i])
            blosum[row_name][column_name] = score

def alignment_scores(seq_1, seq_2, blosum):
    score = 0
    for A1, A2 in zip(seq_1, seq_2):
        score += blosum[A1][A2]
    return score

HM_scores = alignment_scores(human_sequence, mouse_sequence, blosum)
HR_scores = alignment_scores(human_sequence, random_sequence, blosum)
MR_scores = alignment_scores(mouse_sequence, random_sequence, blosum)

print(f"HUMAN/MOUSE: The percentage of identical amino acids is {HM_percentage:.2f}%. The alignment score is {HM_scores}.")
print(f"HUMAN/RANDOM: The percentage of identical amino acids is {HR_percentage:.2f}%. The alignment score is {HR_scores}.")
print(f"MOUSE/RANDOM: The percentage of identical amino acids is {MR_percentage:.2f}%. The alignment score is {MR_scores}.")