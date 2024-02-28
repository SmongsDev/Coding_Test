import sys; input = sys.stdin.readline
N, K, P, X = map(int,input().split())
nums = {'0': [1,1,1,1,1,1,0],
        '1': [0,1,1,0,0,0,0],
        '2': [1,1,0,1,1,0,1],
        '3': [1,1,1,1,0,0,1],
        '4': [0,1,1,0,0,1,1],
        '5': [1,0,1,1,0,1,1],
        '6': [1,0,1,1,1,1,1],
        '7': [1,1,1,0,0,0,0],
        '8': [1,1,1,1,1,1,1],
        '9': [1,1,1,1,0,1,1]}
X = str(X).zfill(K)
x_transform = [nums[x] for x in X]

res = 0
for n in range(1,N+1):
    elevator = str(n).zfill(K)
    ele_transform = [nums[e] for e in elevator]

    diff_cnt = 0
    for x, e in zip(x_transform, ele_transform):
        for i, j in zip(x, e):
            if i != j:
                diff_cnt += 1
        if diff_cnt > P:
            break
    if 0 < diff_cnt <= P:
        res += 1
print(res)