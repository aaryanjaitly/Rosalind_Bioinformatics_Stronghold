"""
Problem
Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.
Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.
"""
"""
Sample Dataset
2 1

Sample Output
0.684
"""
import scipy as sp
input = list(input().split(" "))
Genrations = int(input[0])
Outcomes = int(input[1])

"""
AaBb * AaBb ->      AB      Ab      aB      ab
              AB    AABB    AABb    AaBB    AaBb    
              Ab    AABb    AAbb    AaBb    AAbb
              aB    AaBB    AaBb    aaBB    aaBb
              ab    AaBb    Aabb    aaBb    aabb

              Probability
              AABB = 1/16
              AABb = 2/16
              AaBB = 2/16
              AaBb = 4/16 = 1/4
              AAbb = 1/16
              Aabb = 2/16
              aaBB = 1/16
              aaBb = 2/16
              aabb = 1/16
"""

tottal_after_k_gen = 2 ** Genrations
p_AaBb = 1/4

probability_at_least_Outcomes = 1 - sp.stats.binom.cdf(Outcomes - 1, tottal_after_k_gen, p_AaBb)

print(probability_at_least_Outcomes)