import sys; input = sys.stdin.readline
s = list(input().rstrip())
t = list(input().rstrip())
res = 0
def dfs(t):
    global res
    if len(s) == len(t):
        if s == t:
            res = 1
        return        
    if t[-1] == 'A':
        dfs(t[:-1])
    if t[0] == 'B':
        dfs(t[:0:-1])
dfs(t)
print(res)