n = int(input())
li1 = []

for i in range(n):
    li2 = list(map(int, input().split()))

    ar = sum(li2[1:])/li2[0]
    count = 0
    for j in li2[1:]:
        if j > ar:
            count += 1

    r = count / li2[0] * 100
    li1.append(round(r, 3))

for k in range(n):
    print("{:.3f}%".format(li1[k]))
