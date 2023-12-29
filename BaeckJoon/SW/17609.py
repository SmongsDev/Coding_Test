import sys; input = sys.stdin.readline
n = int(input())

def palindrome(start,end,s):
    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            if s[start] == s[end-1]:
                tmp = s[start:end]
                if tmp == tmp[::-1]:
                    return 1
            if s[start+1] == s[end]:
                tmp = s[start+1:end+1]
                if tmp == tmp[::-1]:
                    return 1
            return 2
    return 0

for _ in range(n):
    s = input().rstrip()
    start = 0
    end = len(s) - 1
    print(palindrome(start,end,s))