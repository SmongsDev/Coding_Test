n, m = map(int,input().split())
arr = []

def back(depth):
    if len(arr) == m:
        print(' '.join(map(str,arr)))
        return
    else:
        for i in range(depth, n+1):
            arr.append(i)
            back(i)
            arr.pop()
back(1)