"""
Problem
A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.
Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.
"""
"""
Sample Dataset
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT

Sample Output
4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4
"""
import sys
with open('./Datasets/rosalind_revp.txt', 'r') as file:
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

input = list(sequences[0])
compliment = {"A": "T", "G" : "C", "T": "A", "C": "G"}

def compli(input):
    comp = []
    for i in input:
        i = compliment[i]
        comp.append(i)
    return(comp[::-1])

for i in range(4,13):
    for j in range(len(input)-i+1):
        a = input[j:j+i]
        b = compli(input[j:j+i])
        if a == b:
            print(j+1,i)