import sys; input = sys.stdin.readline
n, m = map(int, input().split())
character = []

def binary_search(target):
    result = 0
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end) // 2
        if target <= character[mid][1]:
            end = mid - 1
            result = mid
        else:
            start = mid + 1
    return result

for _ in range(n):
    name, power = input().split()
    character.append((name, int(power)))
for _ in range(m):
    x = int(input())
    result = binary_search(x)
    print(character[result][0])