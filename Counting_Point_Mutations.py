"""
Problem
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t.
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
"""

"""
Sample Dataset
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
Sample Output
7
"""
def Hamming_Distance(seq1, seq2):
    hamming_distance = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            hamming_distance += 1
    return hamming_distance

seq1 = input()
seq2 = input()
print(Hamming_Distance(seq1,seq2))