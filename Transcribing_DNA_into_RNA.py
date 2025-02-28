"""
Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.
Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
"""

"""
Sample Dataset
GATGGAACTTGACTACGTAAATT
Sample Output
GAUGGAACUUGACUACGUAAAUU
"""
def DNA_to_RNA(Sequence):
    for i in range (0,len(Sequence)):
        if Sequence[i] == 'T':
            Sequence[i] = 'U'
    return("".join(Sequence))

sequence = input()
print(DNA_to_RNA(list(sequence)))
