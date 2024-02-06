import sys; input = sys.stdin.readline
n = int(input())
target = input().rstrip()
b_c = r_c = 0
if target[0] == 'B':
    b_c = 1
else:
    r_c = 1
for i in range(1,n):
    if target[i] != target[i-1]:
        if target[i] == 'B':
            b_c += 1
        else:
            r_c += 1
print(min(b_c,r_c)+1)