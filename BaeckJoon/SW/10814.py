h = []
for _ in range(int(input())):
    age, name = input().split()
    h.append((int(age), name))
h.sort(key=lambda x: x[0])
for a, b in h:
    print(a,b)