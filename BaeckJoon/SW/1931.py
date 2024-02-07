import sys; input = sys.stdin.readline
n = int(input())
schedules = [list(map(int,input().split())) for _ in range(n)]
schedules.sort(key=lambda x: (x[1],x[0]))

end = schedules[0][1]
cnt = 1
for j in range(1,n):
    if end <= schedules[j][0]:
        cnt += 1
        end = schedules[j][1]
print(cnt)