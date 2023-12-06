import sys
input = sys.stdin.readline
key = input().rstrip()
str = input().rstrip()
_key = sorted(key)
dic = {}
for i,j in enumerate(_key):
    dic[i] = j
key_len = len(str) // len(key)
d = []
for i in range(0,len(str),key_len):
    d.append(str[i:i+key_len])
for i in range(len(d[0])):
    for k in key:
        for K, V in dic.items():
            if k == V:
                print(d[K][i], end='')
                break

# 테스트 케이스
BATBOY
EYDEMBLRTHANMEKTETOEEOTH