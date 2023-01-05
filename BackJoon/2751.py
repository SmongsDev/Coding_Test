import sys

n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline().rstrip()))
    
print(*sorted(lst), sep="\n")
