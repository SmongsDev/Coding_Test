data = [ int(input()) for i in range(1, 10) ]

max = max(data)

print(max)
print(data.index(max) + 1)