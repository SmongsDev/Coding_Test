n = int(input())
f_d = 1
s_d = 1
for _ in range(1, n+1):
    next = f_d + s_d*2
    f_d = s_d
    s_d = next
print(next % 9901)