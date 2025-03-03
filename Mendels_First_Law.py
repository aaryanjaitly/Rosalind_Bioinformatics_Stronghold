"""
Problem
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""

"""
Sample Dataset
2 2 2
Sample Output
0.78333
"""
k = int(input())
m = int(input())
n = int(input())

t = m + k + n

P_Dom = ((k*(k-1) + (k*m)*2 + 2*(k*n) + (3/4)*(m*(m-1)) + 2*(1/2)*(m*n)))

print(P_Dom/(t * (t-1)))