n = int(input())
s = input()
arr = [ 31 ** i for i in range(n) ]
result = 0
for i in range(n):
    c = ord(s[i]) - 96
    result += c * arr[i]
print(result % 1234567891)