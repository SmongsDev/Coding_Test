n = int(input())
N_lst = list(map(int, input().split()))

lst = [False, False] + ([True] * 999)

def isPrime(i):
    for j in range(2, i**(1//2) + 1):
        if i % j == 0:
            return False
    return True

for i in range(2, 1001):
    if lst[i] and isPrime(i):
        for h in range(i*2, 1001, i):
            lst[h] = False
            
count = 0
for i in N_lst:
    if lst[i]:
        count += 1
print(count)
