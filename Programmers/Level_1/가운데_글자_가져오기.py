def solution(s):
    l = len(s) // 2
    if len(s) % 2 == 0:
        return s[l-1]+s[l]
    else:
        return s[l]