# 행렬 덧셈

import sys

n,m = map(int, sys.stdin.readline().split())

A = []
B = []
sumArr = []

def sum(arr):
  for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
  return arr

A = sum(A)
B = sum(B)

for i in range(n):
  sumArr.append([x+y for x,y in zip(A[i], B[i])])

for i in sumArr:
  for j in i:
    print(j, end=' ')
  print()