"""
Problem
For a collection of strings, a larger string containing every one of the smaller strings as a substring is called a superstring.
By the assumption of parsimony, a shortest possible superstring over a collection of reads serves as a candidate chromosome.

Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent reads deriving from the same strand of a single linear chromosome). The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.
Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).
"""
"""
Sample Dataset
>Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC

Sample Output
ATTAGACCTGCCGGAATAC
"""
import sys
with open('./Datasets/rosalind_long.txt', 'r') as file:
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

def Overlap(seq1, seq2):
    max_Length = -1
    seq = ""
    for i in range(1, len(seq1)+1):
        if(seq1[len(seq1)-i:] == seq2[:i]):
            if(max_Length < i):
                max_Length = i
                seq = seq1 + seq2[i:]

    for i in range(1, len(seq2)+1):
        if(seq2[len(seq2)-i:] == seq1[:i]):
            if(max_Length < i):
                max_Length = i
                seq = seq2 + seq1[i:]
    return max_Length,seq


def findShortestSuperstring(arr, n):
    while n != 1:

        max_len = -sys.maxsize   
        l, r = 0, 0    
        res_str = ""    
      
        for i in range(n):
            for j in range(i+1, n):
                str_ = ""
                res, str_ = Overlap(arr[i], arr[j])

                if max_len < res:
                    max_len = res
                    res_str = str_
                    l, r = i, j
                    
        n -= 1   

        if max_len == -sys.maxsize:
            arr[0] += arr[n]
        else:
            arr[l] = res_str
            arr[r] = arr[n]
    
    return arr[0]        

print(findShortestSuperstring(sequences, len(sequences)))