import sys

input = sys.stdin.readline

m = int(input())
S = [0]*21

for _ in range(m):
    requests = input().strip()

    try:
        func, number = requests.split()
        x = int(number)

        if func == 'add':
            S[x] = 1
        elif func == 'remove':
            S[x] = 0 
        elif func == 'check':
            print(1 if S[x] == 1 else 0)
        elif func == 'toggle':
            if S[x] == 1:
                S[x] = 0
            else:
                S[x] = 1
    except:
        if requests == 'all':
            S = [1]*21
        elif requests == 'empty':
            S = [0]*21