"""
Problem
A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".
Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
"""
"""
Sample Dataset
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA

Sample Output
AC
"""
def read_file(file_path):
    sequence_dict = {}
    with open(file_path, 'r') as file:
        current_key = None
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                current_key = line[1:]
                sequence_dict[current_key] = []
            else:
                sequence_dict[current_key].append(line)
    
    sequences = ["".join(seq) for seq in sequence_dict.values()]
    
    seq1 = sequences[0]
    kmer_min = 2
    kmer_max = len(seq1)
    kmers = {seq1[i:i+k] for k in range(kmer_min, kmer_max+1) for i in range(len(seq1)-k+1)}

    common_kmers = kmers
    for seq in sequences[1:]:
        seq_kmers = {seq[i:i+k] for k in range(kmer_min, kmer_max+1) for i in range(len(seq)-k+1)}
        common_kmers &= seq_kmers 

    longest_kmer = max(common_kmers, key=len, default="")  
    print(longest_kmer)

read_file("./Datasets/rosalind_lcsm.txt")