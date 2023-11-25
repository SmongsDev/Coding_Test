import sys

n = int(sys.stdin.readline())
data = []

for i in range(n):
    t = sys.stdin.readline().split()
    
    if t[0] == "push":
        data.append(t[1])

    elif t[0] == "pop":
        if not data:
            print(-1)
        else:
            print(data.pop())

    elif t[0] == "size":
        print(len(data))

    elif t[0] == "empty":
        if not data:
            print(1)
        else:
            print(0)
    
    elif t[0] == "top":
        if not data:
            print(-1)
        else:
            print(data[-1])
