"""
Problem
A subsequence of a string is a collection of symbols contained in order (though not necessarily contiguously) in the string (e.g., ACG is a subsequence of TATGCTAAGATC). The indices of a subsequence are the positions in the string at which the symbols of the subsequence appear; thus, the indices of ACG in TATGCTAAGATC can be represented by (2, 5, 9).
As a substring can have multiple locations, a subsequence can have multiple collections of indices, and the same index can be reused in more than one appearance of the subsequence; for example, ACG is a subsequence of AACCGGTT in 8 different ways.

Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.
Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.
"""
"""
Sample Dataset
>Rosalind_14
ACGTACGTGACG
>Rosalind_18
GTA

Sample Output
3 8 10
"""
import sys
with open('input.txt', 'r') as file:
    lines = file.readlines()

sequences = []
current_sequence = ""

for line in lines:
    line = line.strip()  
    if line.startswith(">"): 
        if current_sequence: 
            sequences.append(current_sequence)
        current_sequence = ""  
    else:
        current_sequence += line  

if current_sequence:
    sequences.append(current_sequence)

Seq1 = list(sequences[0])
Seq2 = list(sequences[1])

result = []
k=0

for i in range(0,len(Seq2)):
    for j in range(k,len(Seq1)):
        if Seq2[i] == Seq1[j]:
            result.append(j+1)
            k = j+1
            break

print(*(result))