"""
Problem
For DNA strings s1 and s2 having the same length, their transition/transversion ratio R(s1,s2) is the ratio of the total number of transitions to the total number of transversions, where symbol substitutions are inferred from mismatched corresponding symbols as when calculating Hamming distance (see “Counting Point Mutations”).
Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
Return: The transition/transversion ratio R(s1,s2).
"""

"""
Sample Dataset
>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT

Sample Output
1.21428571429
"""
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


def Transitions_Transversions(ntd1,ntd2,Transitions,Transversions):
    if((ntd1 == "A" and ntd2 == "G") or (ntd1 == "C" and ntd2 == "T")):
        Transitions+=1
    elif((ntd1 == "G" and ntd2 == "A") or (ntd1 == "T" and ntd2 == "C")):
        Transitions+=1
    else:
        Transversions+=1
    return(Transitions,Transversions)

def Hamming_Check(Seq1,Seq2):
    Transitions = 0
    Transversions = 0
    for i in range(0,min(len(Seq1),len(Seq2))):
        if(Seq1[i] != Seq2[i]):
            Transitions,Transversions = Transitions_Transversions(Seq1[i],Seq2[i],Transitions,Transversions)
    
    return(Transitions/Transversions)

print(Hamming_Check(sequences[0],sequences[1]))