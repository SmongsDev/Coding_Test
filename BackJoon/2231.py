# 분해합

inputNum = int(input())
tmp = []

for i in range(inputNum):
  decompositionSum = i
  for j in range(len(str(i))):
    decompositionSum += int(str(i)[j])
  if decompositionSum == inputNum:
    tmp.append(i)

if tmp:
  print(min(tmp))
else:
  print(0)