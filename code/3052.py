cha = []

for i in range(10):
    n = int(input())
    cha.append(n % 42)

print(len(set(cha)))
