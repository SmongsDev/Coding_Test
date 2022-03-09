

# 시간 초과 뜨는 코드
import sys

T = int(sys.stdin.readline())

for i in range(T):
    n, m = map(int, sys.stdin.readline().split())

    result = pow(n, m) % 10
    print(result)
