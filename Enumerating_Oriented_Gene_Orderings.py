"""
Problem
A signed permutation of length n is some ordering of the positive integers {1,2,…,n} in which each integer is then provided with either a positive or negative sign (for the sake of simplicity, we omit the positive sign). For example, π=(5,−3,−2,1,4) is a signed permutation of length 5.

Given: A positive integer n≤6.
Return: The total number of signed permutations of length n, followed by a list of all such permutations (you may list the signed permutations in any order).
"""
"""
Sample Dataset
2

Sample Output
8
-1 -2
-1 2
1 -2
1 2
-2 -1
-2 1
2 -1
2 1
"""
from itertools import permutations, product
import numpy as np

input = int(input())
Perm_list = []

for i in range(1,input+1):
        Perm_list.append(i)

Perm_list = list(permutations(Perm_list,input))
signs =  list(product([-1,1], repeat=input))

Perm_list =  np.array(Perm_list)
signs = np.array(signs)

result = []

for i in range(len(Perm_list)):
        for j in range(len(signs)):
                result.append((Perm_list[i] * signs[j]))

print(len(result))
for i in result:
        print(*i)