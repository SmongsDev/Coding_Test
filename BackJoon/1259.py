# 팰린드롬수

import sys

while True:
  inputNum = int(sys.stdin.readline().rstrip());
  
  if (inputNum == 0): break
  
  if (inputNum == int(str(inputNum)[::-1])):
    print('yes')
  else:
    print('no')