import sys; input = sys.stdin.readline
n = int(input())
for i in range(1,n):
    num = sum(map(int,str(i)))
    num += i
    if num == n:
        print(i)
        break
else:
    print(0)