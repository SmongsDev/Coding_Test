wave = [1, 1, 1]
for i in range(3, 101):
        wave.append(wave[i-2] + wave[i-3])
T = int(input())
for _ in range(T):
    n = int(input())
    print(wave[n-1])
