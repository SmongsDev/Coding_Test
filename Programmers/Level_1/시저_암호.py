def solution(s, n):
    answer = ''
    Alp = list(map(chr, range(65, 91)))
    alp = list(map(chr, range(97, 123)))
    for i in s:
        o = ord(i)
        if i == " ":
            answer += " "
            continue
        
        elif o >= 65 and o <= 90:
            an = ((o % 65) + n ) % 26
            answer += Alp[an]
            
        else:
            an = ((o % 97) + n) % 26
            answer += alp[an]
        
    return answer
