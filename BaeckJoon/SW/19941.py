import sys; input = sys.stdin.readline
n, k = map(int,input().split())
s = input().rstrip()
visited = [False] * n
for i in range(n):
    if s[i] == 'P':
        for j in range(i-k,i+k+1):
            if j >= n or j < 0:
                continue
            if s[j] == 'H' and not visited[j]:
                visited[j] = True
                break
print(visited.count(True))