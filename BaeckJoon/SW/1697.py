from collections import deque
MAX = 10 ** 5
n, k = map(int, input().split())
d = [0] * (MAX+1)

def bfs():
    que = deque([n])
    while que:
        x = que.popleft()
        if x == k:
            print(d[x])
            break
        for nx in [x-1, x+1, x*2]:
            if 0 <= nx <= MAX and not d[nx]:
                d[nx] = d[x] + 1
                que.append(nx)
bfs()