n, m = map(int, input().split())
arr = [list(map(int,input())) for _ in range(n)]

def sqaure(s):
    for i in range(n-s+1):
        for j in range(m-s+1):
            if arr[i][j] == arr[i][j+s-1] == arr[i+s-1][j] == arr[i+s-1][j+s-1]:
                return True
    return False

for s in range(min(n,m),0,-1):
    if sqaure(s):
        print(s ** 2)
        break