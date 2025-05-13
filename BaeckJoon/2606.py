# 바이러스

import sys

input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v = int(input())
e = int(input())

parent = [i for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

cnt = 0
for i in range(2,v+1):
    if find_parent(parent, i) == find_parent(parent, 1):
        cnt += 1

print(cnt)


'''

7
6
1 2
2 3
1 5
5 2
5 6
4 7

---
4

'''