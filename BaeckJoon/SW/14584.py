import sys
input = sys.stdin.readline
s = input()
n = int(input())
words = []
for _ in range(n):
    words.append(input())

for i in range(26):
    result = ''
    for j in s:
        result += chr(((ord(j)-97+i)%26 )+ 97)
    for word in words:
        if word[:-1] in result:
            print(result)
            break
    s = result