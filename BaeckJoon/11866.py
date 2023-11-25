# 요세푸스 문제 0
import sys
from collections import deque

queue = deque()
result = []

n, k = map(int, sys.stdin.readline().split());

for i in range(1, n+1):
    queue.append(i)

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print("<", end='')
print(', '.join(map(str,result)), end='')
print(">")