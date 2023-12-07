n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

tmp = set()
for i in arr:
    for j in arr:
        tmp.add(i+j)

for i in range(n-1,-1,-1):
    for j in range(i+1):
        if arr[i] - arr[j] in tmp:
            print(arr[i])
            exit(0)