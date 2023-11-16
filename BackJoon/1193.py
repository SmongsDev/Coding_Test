import math

n = int(input())

group = math.ceil(((1+8*n)**(1/2) - 1) / 2)
max_group_value = (group * (group+1)) // 2

k = max_group_value - n

if group % 2 == 0:
    x = group - k
    y = k + 1
else:
    x = k + 1
    y = group - k

print(x,'/',y,sep='')