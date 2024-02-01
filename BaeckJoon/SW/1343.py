import sys; input = sys.stdin.readline
s = input().rstrip()
s = s.replace('XXXX', 'AAAA')
s = s.replace('XX', 'BB')
if 'X' in s:
    print(-1)
else:
    print(s)