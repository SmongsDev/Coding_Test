# 개수 세기

import sys

inputNum = int(sys.stdin.readline().rstrip())
N_list = list(sys.stdin.readline().split())
findN = sys.stdin.readline().rstrip()

print(N_list.count(findN))