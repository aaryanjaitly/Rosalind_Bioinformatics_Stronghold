"""
Problem
Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.
Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.
"""

"""
Sample Dataset
>Rosalind_23
AGCUAGUCAU
Sample Output
12
"""
import math
input = list(input())
countAU = 0
countCG = 0 

for i in range(len(input)):
        if(input[i] == 'A'):
            countAU+= 1
        if(input[i] == 'G'):
            countCG+= 1
        
print(math.factorial(countAU) * math.factorial(countCG))