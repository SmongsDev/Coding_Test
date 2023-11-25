n, k = map(int, input().split())

que = [ i for i in range(1, n+1) ]

result = []
pos = 0

for i in range(n):
    pos += k - 1
    if pos >= len(que):
        pos %= len(que)
    result.append(que.pop(pos))

print("<",", ".join(map(str,result)),">", sep='')