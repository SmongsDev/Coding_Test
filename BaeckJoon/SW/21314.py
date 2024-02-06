import sys; input = sys.stdin.readline
s = input().rstrip()
max_res = min_res = ''
m = 0
for i in s:
    if i == 'M':
        m += 1
    else:
        max_res += str(5 * (10 ** m))
        if m:
            min_res += str(10 ** m + 5)
        else:
            min_res += str(5)
        m = 0
if m:
    max_res += '1' * m
    min_res += str(10 ** (m-1))
print(max_res, min_res)