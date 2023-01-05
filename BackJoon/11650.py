n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

for i in sorted(lst):
    print(*i)
