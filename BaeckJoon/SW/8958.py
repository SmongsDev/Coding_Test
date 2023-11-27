n = int(input())

for i in range(n):
    s = input()
    score = 0
    cnt = 1
    for i in s:
        if i == 'O':
            score += cnt
            cnt += 1
        else:
            cnt = 1
    print(score)