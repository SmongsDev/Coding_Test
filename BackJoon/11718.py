# 그래도 출력하기

while True:
  try:
    print(input())
  except EOFError: # 입력값이 없을 떄의 오류 
    break