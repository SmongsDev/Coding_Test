import sys

N = int(sys.stdin.readline())
room = 1
cnt = 1

while N > room:
    room += 6 * cnt
    cnt += 1
print(cnt)
