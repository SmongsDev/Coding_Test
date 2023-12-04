import sys
input = sys.stdin.readline
n = int(input())
n_lst = list(map(int, input().split()))
m = int(input())
m_lst = list(map(int, input().split()))

result = [0] * 20000000
for i in n_lst:
    result[i] = 1

for i in m_lst:
    print(result[i], end=' ')

# 다른 풀이

dic = {}
for i in n_lst:
    dic[i] = 1
for i in m_lst:
    print(1 if i in dic else 0, end=' ')