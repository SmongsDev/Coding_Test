import sys

n, m, o = map(int, sys.stdin.readline().split())        

print((n + m) % o)
print(((n % o) + (m % o)) % o)
print((n * m) % o)
print((n % o) * (m % o) % o)