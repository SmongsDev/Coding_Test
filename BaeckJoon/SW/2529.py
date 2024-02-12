import sys; input = sys.stdin.readline
n = int(input())
sign = list(input().split())
visited = [0] * 10
res = []
def check(a, b, oper):
    if oper == '<':
        if a > b:
            return False
    else:
        if a < b:
            return False
    return True

def back(idx, s):
    if idx == n+1:
        res.append(s)
        return
    else:
        for i in range(10):
            if visited[i] == 0:
                if idx == 0 or check(int(s[-1]), i, sign[idx-1]):
                    visited[i] = 1
                    back(idx+1,s + str(i))
                    visited[i] = 0

back(0, '')
print(res[-1])
print(res[0])