import sys; input = sys.stdin.readline
n = int(input())
hits = []
for _ in range(n):
    a, b, c = input().split()
    hits.append((a, int(b), int(c)))

def check(target):
    for hit, s, b in hits:
        strk = ball = 0
        for i in range(3):
            if hit[i] == target[i]:
                strk += 1
            elif target[i] in hit:
                ball += 1
        if s != strk or b != ball:
            return False
    return True

res = 0
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i == j or j == k or i == k:
                continue
            now = str(i) + str(j) + str(k)
            if check(now):
                res += 1
print(res)