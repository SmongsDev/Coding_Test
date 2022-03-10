n = int(input())

for i in range(n):
    a, b = input().split()

    S = ""
    for j in b:
        S += j * int(a)
    
    print(S)
