import sys; input = sys.stdin.readline

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

v, e = map(int,input().split())
parent = [i for i in range(v+1)]

for _ in range(e):
    a, b = map(int,input().split())
    union_parent(parent, a,b)

for i in range(1,v+1):
    parent[i] = parent[parent[i]]

res = []
for i in parent[1:]:
    if i not in res:
        res.append(i)
print(len(res))