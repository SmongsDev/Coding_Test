list = list(map(int, input().split()))

for i in range(len(list)):
    list[i] = int(str(list[i])[::-1])

print(max(list))