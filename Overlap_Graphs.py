"""
Problem
A graph whose nodes have all been labeled can be represented by an adjacency list, in which each row of the list contains the two node labels corresponding to a unique edge.
A directed graph (or digraph) is a graph containing directed edges, each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge form its tail and head, respectively. The directed edge with tail v and head w is represented by (v,w) (but not by (w,v)). A directed loop is a directed edge of the form (v,v).
For a collection of strings and a positive integer k, the overlap graph for the strings is a directed graph Ok in which each string is represented by a node, and string s is connected to string t with a directed edge when there is a length k suffix of s that matches a length k prefix of t, as long as s≠t; we demand s≠t to prevent directed loops in the overlap graph (although directed cycles may be present).

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
Return: The adjacency list corresponding to O3. You may return edges in any order.
"""

"""
Sample Dataset
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG

Sample Output
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
"""


def read_fasta(file_path):
    sequence_dict = {}
    with open(file=file_path,mode='r') as file:
        for line in file:
            if line.startswith(">"):
                i = line[1:].strip("\n")
                sequence_dict[i] = []
            else:
                sequence_dict[i].append(line.strip("\n"))
        for j in sequence_dict.keys():
            sequence_dict[j] = "".join(sequence_dict[j])


        suffix = {}
        prefix = {}
        for key, val in sequence_dict.items():
            suffix[key] = val[len(val)-3:len(val)]
            prefix[key] = val[0:3]
           
    
        for key1, val1 in prefix.items():
            for key2, val2 in suffix.items():
                if key1 != key2:
                    if (prefix[key1] == suffix[key2]):
                        print(key2, key1)

    return(sequence_dict)

file = "./Datasets/rosalind_grph.txt"
read_fasta(file)