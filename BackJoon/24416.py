import sys

def fib(n):
    if n <= 1:
        return n
    fri = 0
    sec = 1
    for i in range(0, n-1):
        next = fri + sec
        fri = sec
        sec = next
    return next
    
T = int(sys.stdin.readline())
print(fib(T), T-2)
