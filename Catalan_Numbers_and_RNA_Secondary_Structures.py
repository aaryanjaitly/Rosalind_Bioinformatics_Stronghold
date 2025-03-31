"""
Problem
In this problem, we will consider counting noncrossing perfect matchings of basepair edges. As a motivating example of how to count noncrossing perfect matchings, let cn denote the number of noncrossing perfect matchings in the complete graph K2n. After setting c0=1, we can see that c1 should equal 1 as well. As for the case of a general n, say that the nodes of K2n are labeled with the positive integers from 1 to 2n. We can join node 1 to any of the remaining 2n−1 nodes; yet once we have chosen this node (say m), we cannot add another edge to the matching that crosses the edge {1,m}. As a result, we must match all the edges on one side of {1,m} to each other. This requirement forces m to be even, so that we can write m=2k for some positive integer k.
There are 2k−2 nodes on one side of {1,m} and 2n−2k nodes on the other side of {1,m}, so that in turn there will be ck−1⋅cn−k different ways of forming a perfect matching on the remaining nodes of K2n. If we let m vary over all possible n−1 choices of even numbers between 1 and 2n, then we obtain the recurrence relation cn=∑nk=1ck−1⋅cn−k. The resulting numbers cn counting noncrossing perfect matchings in K2n are called the Catalan numbers, and they appear in a huge number of other settings. See Figure 4 for an illustration counting the first four Catalan numbers.

Given: An RNA string s having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'. The length of the string is at most 300 bp.
Return: The total number of noncrossing perfect matchings of basepair edges in the bonding graph of s, modulo 1,000,000.
"""
"""
Sample Dataset
>Rosalind_57
AUAU

Sample Output
2
"""

with open("./Datasets/rosalind_cat.txt", "r") as file:
    sequences = [line.strip() for line in file]

sequence = "".join(sequences[1:])

hash_map = {
    "A": "U",
    "U": "A", 
    "G": "C",
    "C": "G"
}

dp = {}

def catland(low, high, rna, dp):
    if low >= high or high < 0:
        return 1
    
    mid = high - low + 1
    if mid % 2 != 0:
        return 0
    
    if (low, high) in dp:
        return dp[(low, high)]
    
    total_ways = 0
    lower = rna[low]
    upper = hash_map.get(lower, None)
    
    if upper:
        for i in range(low + 1, high + 1, 2):
            if rna[i] == upper:
                left = catland(low + 1, i - 1, rna, dp)
                right = catland(i + 1, high, rna, dp)
                total_ways += left * right
    
    dp[(low, high)] = total_ways % 1000000
    return dp[(low, high)]

print(catland(0, len(sequence) - 1, sequence, dp))