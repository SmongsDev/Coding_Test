# 대소문자 바꾸기

word = input()
result = ""

for i in word:
  if i.islower():
    result += i.upper()
  else:
    result += i.lower()

print(result)