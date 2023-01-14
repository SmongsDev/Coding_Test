import sys

def fibonacci(n):
    if n <= 1:
        return n
    
    fri = 0
    sec = 1
    for i in range(0, n-1):
        next = fri + sec
        fri = sec
        sec = next
    return next

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    print(fibonacci(T))
