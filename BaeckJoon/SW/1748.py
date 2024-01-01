import sys; input = sys.stdin.readline
n = input().rstrip()
length = 0
for i in range(1,len(n)):
    length += 9 * 10**(i-1) * i
length += (int(n) - 10**(len(n)-1)+1) * len(n)
print(length)