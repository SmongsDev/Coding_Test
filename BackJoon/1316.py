n = int(input())
count = n

for i in range(n):
    ch = input()

    for j in range(len(ch)-1):
        if ch[j] != ch[j+1]:
            if ch[j] in ch[j+1:]:
                count -= 1
                break
            else:
                pass


print(count)
