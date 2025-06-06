"""
Problem
A prefix of a length n string s is a substring s[1:j]; a suffix of s is a substring s[k:n].
The failure array of s is an array P of length n for which P[k] is the length of the longest substring s[j:k] that is equal to some prefix s[1:k−j+1], where j cannot equal 1 (otherwise, P[k] would always equal k). By convention, P[1]=0.

Given: A DNA string s (of length at most 100 kbp) in FASTA format.
Return: The failure array of s.
"""
"""
Sample Dataset
>Rosalind_87
CAGCATGGTATCACAGCAGAG

Sample Output
0 0 0 1 2 0 0 0 0 0 0 1 2 1 2 3 4 5 3 0 0
"""
Sequence= []
file = open("./Datasets/rosalind_kmp.txt")
for line in file:
    if line.startswith(">"):
        continue
    else:
        Sequence.append(line.strip("\n"))
Sequence =  "".join(Sequence)  

def compute_kmp_prefix(pattern):
    prefix = [0] * len(pattern)
    j = 0

    for i in range(1, len(pattern)):
        while(j > 0 and pattern[i] != pattern[j]):
            j = prefix[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix[i] = j
    return prefix

print(*compute_kmp_prefix(Sequence))