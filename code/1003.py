import sys

T = int(sys.stdin.readline())

def fibonacci(n):
    fi = [0, 1]
    if n == 0:
        print(1,0)
        return 0
    
    elif n == 1:
        print(0,1)
        return 1
    
    else:
        for i in range(1, n):
            fi.append(fi[i] + fi[i-1])
        print(fi[n-1], fi[n])

for i in range(T):
    n = int(sys.stdin.readline())
    fibonacci(n)