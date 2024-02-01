import sys; input = sys.stdin.readline
n,m = map(int,input().split())
move = 0
now = 1
for _ in range(int(input())):
    apple = int(input())
    if apple in range(now,now+m):
        continue
    elif apple > now:
        move += apple - (now + m-1)
        now = apple - (m-1)
    else:
        move += now - apple
        now = apple
print(move)