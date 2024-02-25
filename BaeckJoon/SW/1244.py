import sys; input = sys.stdin.readline
n = int(input())
switchs = [-1] +list(map(int,input().split()))

for _ in range(int(input())):
    gen, pos = map(int,input().split())
    if gen == 1:
        for i in range(pos,n+1,pos):
            switchs[i] = 1 if switchs[i] == 0 else 0
    else:
        switchs[pos] = 1 if switchs[pos] == 0 else 0
        for i in range(n//2):
            l = pos-i
            r = pos+i
            if l <= 0 or r > n or switchs[l] != switchs[r]:
                break
            switchs[l] = 1 if switchs[l] == 0 else 0
            switchs[r] = 1 if switchs[r] == 0 else 0
            
        
for i in range(1,n+1):
    print(switchs[i], end=' ')
    if i % 20 == 0:
        print()