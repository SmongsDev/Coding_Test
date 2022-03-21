s = input()

count = {}

# 다음에는 counter 모듈을 사용하자!! <- 문자열의 알파벳 글자 수를 세어주는 모듈
for i in s.lower():
    count[i] = count.get(i, 0) + 1

    keys = sorted(count.keys())

c = 0

for i in keys:
    if count[i] == max(count.values()):
        c += 1
    
max_key = max(count, key=count.get)

if c >= 2:
    print('?')

else:
    print(max_key.upper())
