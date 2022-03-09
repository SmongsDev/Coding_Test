import sys

T = int(sys.stdin.readline())

for i in range(T):
    n, m = map(int, sys.stdin.readline().split())
    n = n % 10

    if n == 0:
        print(10)

    elif n == 1 or n == 5 or n == 6:
        print(n)

    elif n == 4 or n == 9:
        m = m % 2
        if m == 1:
            print(n)        
        else:
            print((n * n) % 10)

    else:
        m = m % 4
        if m == 0:
            print((n ** 4) % 10 % 10 % 10)        
        else:
            print((n ** m) % 10 % 10 % 10)

''' 시간 초과

for i in range(T):
    n, m = map(int, sys.stdin.readline().split())

    result = pow(n, m) % 10
    print(result)
'''