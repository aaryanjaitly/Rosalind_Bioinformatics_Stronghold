"""
Problem
A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.
Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
"""
"""
Sample Dataset
3

Sample Output
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""
from itertools import permutations
input = int(input())

result = 1
for i in range(1,input+1):
    result *= i

seq = []
for i in range(1,input+1):
    seq.append(str(i))
Seq  = "".join(seq)

perms = [' '.join(p) for p in permutations(Seq)]

print(result)
for i in perms:
    print(i)