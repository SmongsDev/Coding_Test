n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

for i in sorted(lst, key=lambda x:(x[1], x[0])):
    print(*i)
