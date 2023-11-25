import sys

n, m = map(int, sys.stdin.readline().split())

if n > m:
    print(">")

elif n < m:
    print("<")

else:
    print("==")