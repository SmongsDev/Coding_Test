import sys; input = sys.stdin.readline
n = int(input())
oils = list(map(int,input().split()))
charges = list(map(int,input().split()))

res = 0
now = charges[0]
for i in range(n-1):
    res += now * oils[i]
    if now > charges[i+1]:
        now = charges[i+1]
    
print(res)