import sys; input = sys.stdin.readline
answer = []
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    lst.reverse()

    max_value = lst[0]
    benefit = 0
    res = []
    for i in range(1,n):
        if max_value >= lst[i]:
            benefit += max_value - lst[i]
        else:
            max_value = lst[i]

    answer.append(benefit)
print(*answer, sep='\n')