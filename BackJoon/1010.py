import sys 

input = sys.stdin.readline

T = int(input())

def factorial(k):
    tmp = 1
    
    for i in range(1, k+1):
        tmp *= i
    return tmp

def combination(n, r):
    if n == r:
        print(1)
    else:
        result = factorial(n) // ( factorial(r) * factorial(n-r))
        print(result)

for _ in range(T):
    N, M = map(int, input().split())
    
    combination(M, N)
