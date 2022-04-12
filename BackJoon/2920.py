t = list(map(int, input().split()))

if t == sorted(t):
    print('ascending')

elif t == sorted(t, reverse=True):
    print('descending')

else:
    print('mixed')