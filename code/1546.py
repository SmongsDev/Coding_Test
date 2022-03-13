n = int(input())
n_li = list(map(int, input().split()))

n_max = max(n_li)

sum = 0
for i in range(len(n_li)):
    sum = sum + n_li[i]

avrg = sum / n_max * 100

print(avrg/n)
