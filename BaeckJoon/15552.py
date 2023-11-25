# 빠른 A + B

import sys

forNum = int(sys.stdin.readline().rstrip())

for i in range(forNum):
  a, b = map(int, sys.stdin.readline().split())
  print(a+b)