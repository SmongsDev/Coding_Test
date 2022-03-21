a = 1
list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for _ in range(3):
    a *= int(input())

for i in str(a):
    if i == '0':
        list[0] += 1
    elif i == '1':
        list[1] += 1
    elif i == '2':
        list[2] += 1
    elif i == '3':
        list[3] += 1
    elif i == '4':
        list[4] += 1
    elif i == '5':
        list[5] += 1
    elif i == '6':
        list[6] += 1
    elif i == '7':
        list[7] += 1
    elif i == '8':
        list[8] += 1
    elif i == '9':
        list[9] += 1

# unpacking operator *
print(*list, sep='\n') # sep 옵션은 인자에 원하는 구분자를 넣어 요소들 '사이'에 출력할 수 있다.
# end 옵션은 출력하고 나서 작동됨