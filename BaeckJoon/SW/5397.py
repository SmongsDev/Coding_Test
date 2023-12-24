import sys; sys.stdin.readline
n = int(input())
ban_word = ['<','>','-']
for _ in range(n):
    s = input().rstrip()
    stack = []
    tmp = []
    for i in s:
        if i == '<' and stack:
            tmp.append(stack.pop())
        elif i == '>' and tmp:
            stack.append(tmp.pop())
        elif i == '-' and stack:
            stack.pop()
        elif i not in ban_word:
            stack.append(i)
    result = stack + tmp[::-1]
    print(''.join(result))