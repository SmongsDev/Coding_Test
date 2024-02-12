import sys; input = sys.stdin.readline
n = int(input())
res = []
idx = 666
while len(res) != n:
    if '666' in str(idx):
        res.append(idx)
    idx += 1
print(res[-1])