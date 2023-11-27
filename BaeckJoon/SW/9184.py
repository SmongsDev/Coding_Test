dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def recursion(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return recursion(20,20,20)
    elif dp[a][b][c]:
        return dp[a][b][c]
    elif a<b<c:
        dp[a][b][c] = recursion(a,b,c-1) + recursion(a,b-1,c-1) - recursion(a,b-1,c)
    else:
        dp[a][b][c] = recursion(a-1,b,c) + recursion(a-1,b-1,c) + recursion(a-1,b,c-1) - recursion(a-1,b-1,c-1)
    return dp[a][b][c]

while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break
    
    print('w({}, {}, {}) = {}'.format(a,b,c,recursion(a,b,c)))