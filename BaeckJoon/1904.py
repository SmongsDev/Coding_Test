import sys

n = int(sys.stdin.readline())

li = [0,1,2]

for i in range(3, n+1):
    li.append((li[i-1] + li[i-2]) % 15746)

print(li[n])
