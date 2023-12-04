n = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]
for i in range(1,len(arr)):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
print(len(dp))

# https://lgphone.tistory.com/129 