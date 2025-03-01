"""
Problem
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.
DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.
In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
"""
"""
Sample Dataset
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
Sample Output
Rosalind_0808
60.919540
"""
def Read_File(file_path):
    sequence_dict = {}
    with open(file_path) as file:
        for line in file:
            if line.startswith(">"):
                i = line[1:].strip("\n")
                sequence_dict[i] = []
            else:
                sequence_dict[i].append(line.strip("\n"))
        for j in sequence_dict.keys():
            sequence_dict[j] = "".join(sequence_dict[j])
    return(sequence_dict)

def GC_Count(sequence_dict):
    GC_count = {}
    for key, value in sequence_dict.items():
        GC_count[key] = 0
        for j in value:
            if(j == "G" or j == "C"):
                GC_count[key] += 1
        GC_count[key] = (GC_count[key] / (len(value))) * 100
        max_value = max(GC_count.values())
        if GC_count[key] == max_value:
            max_key = key 
    print(max_key)
    print(max_value)

GC_Count(Read_File("./Datasets/rosalind_gc.txt"))