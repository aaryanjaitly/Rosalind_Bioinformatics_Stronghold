"""
Problem
As is the case with point mutations, the most common type of sequencing error occurs when a single nucleotide from a read is interpreted incorrectly.

Given: A collection of up to 1000 reads of equal length (at most 50 bp) in FASTA format. Some of these reads were generated with a single-nucleotide error. For each read s in the dataset, one of the following applies:
    -> s was correctly sequenced and appears in the dataset at least twice (possibly as a reverse complement);
    -> s is incorrect, it appears in the dataset exactly once, and its Hamming distance is 1 with respect to exactly one correct read in the dataset (or its reverse complement).

    Return: A list of all corrections in the form "[old read]->[new read]". (Each correction must be a single symbol substitution, and you may return the corrections in any order.)
"""
"""
Sample Dataset
>Rosalind_52
TCATC
>Rosalind_44
TTCAT
>Rosalind_68
TCATC
>Rosalind_28
TGAAA
>Rosalind_95
GAGGA
>Rosalind_66
TTTCA
>Rosalind_33
ATCAA
>Rosalind_21
TTGAT
>Rosalind_18
TTTCC

Sample Output
TTCAT->TTGAT
GAGGA->GATGA
TTTCC->TTTCA
"""
from collections import defaultdict

def hamming(Seq1, Seq2):
    hamming_dist = 0
    for i in range(len(Seq1)):
        if(Seq1[i] != Seq2[i]):
            hamming_dist+=1
    return(hamming_dist)

def rc(seq):
    hash_map = {"A":"T", "T":"A", "G":"C", "C":"G"}
    seq = list(reversed(seq))
    for i in range(len(seq)):
        seq[i] = hash_map.get(seq[i]);    
    return("".join(seq))

Sequences = []
file = open("./Datasets/rosalind_corr.txt", "r")
for line in file:
    if(line.startswith(">")):
        continue
    else:
        Sequences.append(line.strip())

counts = defaultdict(int)
for seq in Sequences:
    counts[seq] += 1
    counts[rc(seq)] += 0

correct_reads = set()
for seq in counts:
    total = counts[seq] + counts[rc(seq)]
    if total >= 2:
        correct_reads.add(seq)
        correct_reads.add(rc(seq))

results = []
for seq in Sequences:
    if seq in correct_reads:
        continue
    found = False
    for correct in correct_reads:
        if hamming(seq, correct) == 1:
            results.append((seq, correct))
            found = True
            break
    if not found:
        for correct in correct_reads:
            if hamming(seq, rc(correct)) == 1:
                results.append((seq, rc(correct)))
                break

for wrong, correct in results:
    print(wrong,correct,sep="->")