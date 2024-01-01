n, k = map(int, input().split())
visited = [True] * (n+1)

lst = []
for i in range(2, n+1):
    if visited[i]:
        j = 1
        while i * j <= n:
            if visited[i*j]:
                visited[i * j] = False
                lst.append(i*j)
            j += 1
print(lst[k-1])