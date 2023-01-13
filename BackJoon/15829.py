import sys

l = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip()
result = 0
for i in range(l):
    Ascii = ord(string[i]) - 96
    result += Ascii * pow(31,i)
print(result % 1234567891)
