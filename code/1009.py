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
            
|0|10|
|1|1|
|2|2 4 8 6|
|3|9 7 1|
|4|4 6|
|5|5|
|6|6|
|7|9 3 1|
|8|8 4 2 6|
|9|9 1|

# 시간 초과 뜨는 코드
import sys

T = int(sys.stdin.readline())

for i in range(T):
    n, m = map(int, sys.stdin.readline().split())

    result = pow(n, m) % 10
    print(result)
