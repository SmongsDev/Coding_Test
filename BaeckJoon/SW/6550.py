while 1:
    try:
        s, t = input().split()
        pos = 0
        for i in t:
            if i == s[pos]:
                pos += 1
                if len(s) == pos:
                    print('Yes')
                    break
        else:
            print('No')
    except:
        break