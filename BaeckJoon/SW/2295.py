n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

# tmp = set()
# for i in arr:
#     for j in arr:
#         tmp.add(i+j)

# for i in range(n-1,-1,-1):
#     for j in range(i+1):
#         if arr[i] - arr[j] in tmp:
#             print(arr[i])
#             exit(0)

tmp = []
for i in arr:
    for j in arr:
        tmp.append(i+j)
result = 0
tmp.sort()
for i in range(n):
    for j in range(i, n):
        start = 0
        end = len(tmp) - 1
        sol = arr[j] - arr[i]
        while start <= end:
            mid = (start + end) // 2

            if sol > tmp[mid]:
                start = mid + 1
            elif sol < tmp[mid]:
                end = mid - 1
            else:
                result = max(result, arr[j])
                break
print(result)