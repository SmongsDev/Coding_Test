import sys

n_1 = int(sys.stdin.readline())
M_1 = list(map(int, sys.stdin.readline().split()))
M_1.sort()
n_2 = int(sys.stdin.readline())
M_2 = list(map(int, sys.stdin.readline().split()))

for i in M_2:
    f_n, l_n = 0, n_1 - 1

    while 1:
        if f_n > l_n:
            print(0)
            break 
        c = (f_n + l_n) // 2

        if M_1[c] == i:
            print(1)
            break
        elif i < M_1[c]:
            l_n = c - 1
        else:
            f_n = c + 1
