"""
Problem
A subsequence of a permutation is a collection of elements of the permutation in the order that they appear. For example, (5, 3, 4) is a subsequence of (5, 1, 3, 4, 2).
A subsequence is increasing if the elements of the subsequence increase, and decreasing if the elements decrease. For example, given the permutation (8, 2, 1, 6, 5, 7, 4, 3, 9), an increasing subsequence is (2, 6, 7, 9), and a decreasing subsequence is (8, 6, 5, 4, 3). You may verify that these two subsequences are as long as possible.

Given: A positive integer n≤10000 followed by a permutation π of length n.
Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.
"""
"""
Sample Dataset
5
5 1 4 2 3

Sample Output
1 2 3
5 4 2
"""
# # Greedy Algorithm 
# import numpy as np

# res_inc = [-1]
# def inc(input):
#     arr_inc = [0] * len(input)
#     if(res_inc[-1] >= input[0]):
#         return(input[1:])
#     for i in range(0,len(input)):
#         for j in range(i+1,len(input)):
#             if input[i] < input[j]:
#                 arr_inc[i] += 1

#     if(res_inc[-1] >= input[np.argmax(arr_inc)]):
#         while(res_inc[-1] > input[np.argmax(arr_inc)] and len(input) > 1):
#             arr_inc[np.argmax(arr_inc)] = 0

#     res_inc.append(input[np.argmax(arr_inc)])
#     new_input = input[np.argmax(arr_inc)+1:]
#     return(new_input)


# res_des = [9999999999999999999]
# def des(input):
#     arr_dec = [0] * len(input)
#     if(res_des[-1] <= input[0]):
#         return(input[1:])
#     for i in range(0,len(input)):
#         for j in range(i+1,len(input)):
#             if input[i] > input[j]:
#                 arr_dec[i] += 1

#     if(res_des[-1] <= input[np.argmax(arr_dec)]):
#         while(res_des[-1] < input[np.argmax(arr_dec)] and len(input) > 1):
#             arr_dec[np.argmax(arr_dec)] = 0
    
#     res_des.append(input[np.argmax(arr_dec)])
#     new_input = input[np.argmax(arr_dec)+1:]
#     return(new_input)
    

# input = input()
# input = list(map(int,input.split(" ")))
# a = input
# while(len(a) != 0):
#     a = inc(a)

# print(*res_inc[1:])

# a = input
# while(len(a) != 1):
#     a = des(a)

# print(*res_des[1:])


#Dynmaic Progrmaing
def lis(input,length):
    n = length
    dp = [1] * n 
    for i in range(1, n):
        for j in range(i):
            if input[i] > input[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    lis_sequence = []
    max_len = max(dp)
    for i in range(n-1, -1, -1):
        if dp[i] == max_len:
            lis_sequence.append(input[i])
            max_len -= 1
    return lis_sequence[::-1]

def lds(input,length):
    n = length
    dp = [1] * n 
    for i in range(1, n):
        for j in range(i):
            if input[i] < input[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    lds_sequence = []
    max_len = max(dp)
    for i in range(n-1, -1, -1):
        if dp[i] == max_len:
            lds_sequence.append(input[i])
            max_len -= 1
    return lds_sequence[::-1]

length = int(input())
input_list = list(map(int, input().split()))

lis_result = lis(input_list,length)
print(*lis_result)

lds_result = lds(input_list,length)
print(*lds_result)