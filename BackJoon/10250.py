# ACM 호텔

import sys, math

T = int(sys.stdin.readline().rstrip())

for i in range(T):
  H, W, N = map(int, sys.stdin.readline().split())
  y = N % H
  x = str(math.ceil(N / H))

  if N % H == 0: # H의 배수 ex) 6 % 6 == 0 (0층 없음)
    y = H

  print("{}{}".format(y, x.zfill(2)))