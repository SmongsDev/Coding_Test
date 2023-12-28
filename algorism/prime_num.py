# 에라토스테네스의 체
import math
def solutions(n):
    check = [True for _ in range(n+1)]
    for i in range(2, int(math.sqrt(n))+1):
        if check[i]:
            j = 2
            while i * j <= n:
                check[i * j] = False
                j += 1
    return check

print(solutions(16)) # 16까지의 소수 판별