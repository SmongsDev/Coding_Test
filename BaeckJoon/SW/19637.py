import sys; input = sys.stdin.readline
n, m = map(int,input().split())
titles = []
for _ in range(n):
    c, x = input().split()
    titles.append((c,int(x)))

for _ in range(m):
    power = int(input())
    idx = 0
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end) // 2
        
        if power <= titles[mid][1]:
            end = mid - 1
            idx = mid
        else:
            start = mid + 1
    print(titles[idx][0])