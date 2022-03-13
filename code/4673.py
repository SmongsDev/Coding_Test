def again(n):   
    result = n
    while n != 0:
        result += n%10
        n //= 10
    return result

li = []
for i in list(range(1, 10001)):
    li.append(again(i))
    if i not in li:
        print(i)
