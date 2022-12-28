import sys

N = int(sys.stdin.readline())

for i in range(N):
    PS = sys.stdin.readline().rstrip()
    V_list = []
    for i in PS:
        if i == '(':
            V_list.append(i)
        elif i == ')':
            if V_list:
                V_list.pop()
            else:
                print("NO")
                break
    else:
        if V_list:
            print("NO")
        else:
            print("YES")
