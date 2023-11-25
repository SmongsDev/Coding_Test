n = int(input())
m = n
len = 0

while True:
    sum = n//10 + n%10
    n1 = (n%10)*10 + sum%10
    len += 1
    n = n1
    if m == n:
        break

print(len)
