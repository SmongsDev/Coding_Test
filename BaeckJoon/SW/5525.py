import sys; input = sys.stdin.readline
n = int(input())
m = int(input())
s = input()
pos, cnt, result = 0, 0, 0

while pos < m-1:
    if s[pos:pos+3] == 'IOI':
        pos += 2
        cnt += 1
        if cnt == n:
            result += 1
            cnt -= 1
    else:
        cnt = 0
        pos += 1
print(result)