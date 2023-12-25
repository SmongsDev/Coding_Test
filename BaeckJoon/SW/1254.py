s = input()
tmp = ''
for i in range(len(s)):
    result = s + tmp[::-1]
    mid = len(result) // 2
    if len(result) % 2 == 0:
        if result[:mid] == result[:mid-1:-1]:
            print(len(result))
            break
    else:
        if result[:mid] == result[:mid:-1]:
            print(len(result))
            break
    tmp += s[i]