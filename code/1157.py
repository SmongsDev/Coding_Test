s = input()

count = {}

for i in s.lower():
    count[i] = count.get(i, 0) + 1

    keys = sorted(count.keys())

c = 0

for i in keys:
    if count[i] == max(count.values()):
        c += 1
    
max_key = max(count, key=count.get)

if c >= 2:
    print('?')

else:
    print(max_key.upper())