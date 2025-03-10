"""
Problem
A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.
Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents the number of times that C occurs in the jth position, and so on (see below).
A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
"""

"""
Sample Dataset
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
Sample Output
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
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

    sequence_list = []
    for key in sequence_dict.keys():
        sequence_list.append(list(sequence_dict[key]))
    return(sequence_list)

Profile = read_fasta("./input.txt")
length = len(Profile)

Profile_matrix = []
Row_dict = {}
Cons = []

for j in range(0,len(Profile[0])):
    A_counter = 0
    T_counter = 0
    G_counter = 0
    C_counter = 0
    for k in range(0, length):
        if (Profile[k][j]) == "A":
            A_counter += 1
        elif (Profile[k][j]) == "T":
            T_counter += 1
        elif (Profile[k][j]) == "G":
            G_counter += 1
        elif (Profile[k][j]) == "C":
            C_counter +=1 
    Profile_matrix.append(["A",A_counter, "C",C_counter, "G",G_counter, "T",T_counter,])
    Row_dict["A"] = A_counter
    Row_dict["C"] = C_counter
    Row_dict["T"] = T_counter
    Row_dict["G"] = G_counter
    max_value = max(Row_dict.values())
    for key, val in Row_dict.items():
        if max_value == Row_dict[key]:
            max_key = key
    Cons.append(max_key)

print("".join(Cons))

rowA = []
rowC = []
rowG = []
rowT = []
for i in Profile_matrix:
    str(rowA.append(str(i[1])))
    rowC.append(str(i[3]))
    rowG.append(str(i[5]))
    rowT.append(str(i[7]))

print("A:", " ".join(rowA))
print("C:", " ".join(rowC))
print("G:", " ".join(rowG))
print("T:", " ".join(rowT))