# 과제 안 내신 분,,?

import sys

checkList = list(range(1,31))
attendanceList = []

for i in range(28):
  num = int(sys.stdin.readline().rstrip())
  checkList.remove(num)

for i in checkList:
  print(i)