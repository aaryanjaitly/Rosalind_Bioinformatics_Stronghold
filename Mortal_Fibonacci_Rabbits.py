n = int(input())
k = int(input())

# # My recurrsion
# def fib(n,k):
#     if n == 0:
#         return 1
#     if n == 1 or n == 2: 
#         return 1
#     elif(n > k):
#         return((fib(n-1,k) + fib(n-2,k)) - fib(n-k-1,k))
#     else:
#         return(fib(n-2,k)+fib(n-1,k))
# print(fib(n,k))

# My Iteration of my recurrsion
def fib(n,k):
    if n == 1 or n == 2:
        return 1
    fib_values = [0] * (n+1)
    fib_values[0] = 1
    fib_values[1] = 1
    fib_values[2] = 1

    for i in range(3, n+1):
        if i > k:
            fib_values[i] = (fib_values[i-1] + fib_values[i-2]) - fib_values[i-k-1]
        else:
            fib_values[i] = fib_values[i-2]+fib_values[i-1]
    
    return(fib_values[n])

print(int(fib(n,k)))