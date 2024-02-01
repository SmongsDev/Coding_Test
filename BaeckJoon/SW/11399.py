import sys; input = sys.stdin.readline
n = int(input())
people = sorted(list(map(int,input().split())))

res = 0
prev = 0
for p in people:
    res += p + prev
    prev = p + prev
print(res)