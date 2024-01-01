import sys; input = sys.stdin.readline
n = int(input())
homes = sorted(list(map(int,input().split())))
print(homes[(n-1) // 2])