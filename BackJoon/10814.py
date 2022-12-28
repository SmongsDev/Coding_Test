import sys

N = int(sys.stdin.readline())
N_list = []

for i in range(N):
    num, name = map(str, sys.stdin.readline().split())
    num = int(num)
    N_list.append((num, name))
    
N_list.sort(key=lambda x:x[0])

for i in N_list:
    print(i[0], i[1])
