import math
import sys; input = sys.stdin.readline
num = 1299709
T = int(input())
visited = [True for _ in range(num+1)]
for i in range(2,int(math.sqrt(num))+1):
    if visited[i]:
        j = 2
        while i * j <= num:
            visited[i * j] = False
            j += 1
for i in range(T):
    n = int(input())
    if visited[n]:
        print(0)
    else:
        start = end = n
        while 1:
            start -= 1
            if visited[start]:
                break
        while 1:
            end += 1
            if visited[end]:
                break
        print(end - start)