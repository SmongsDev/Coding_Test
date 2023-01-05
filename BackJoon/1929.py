m, n = map(int, input().split())

lst = [False, False] + ([True] * 999999)

def isPrime(i):
    for j in range(2, i**(1//2) + 1):
        if i % j == 0:
            return False
    return True

for i in range(2, 1000001):
    if lst[i] and isPrime(i):
        for h in range(i*2, 1000000, i):
            lst[h] = False

for i in range(m,n+1):
    if lst[i]:
        print(i)
