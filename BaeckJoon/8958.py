n = int(input())

for i in range(n):
    data = list(input())

    sum = 0
    count = 1

    for j in data:
        if j == 'O':
            sum += count
            count += 1
        else:
            count = 1
        
    print(sum)