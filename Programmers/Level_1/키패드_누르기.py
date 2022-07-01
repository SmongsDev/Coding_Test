def solution(numbers, hand):
    num = { 1 : [0,0], 2 : [0,1], 3 : [0,2],
           4 : [1,0], 5 : [1,1], 6 : [1,2],
           7 : [2,0], 8 : [2,1], 9 : [2,2],
          '*' : [3,0], 0 : [3,1], '#' : [3,2] }
    answer = ''
    
    r = num['#']
    l = num['*']
    
    for i in numbers:
        now = num[i]
        
        if i in [1, 4, 7]:
            l = now
            answer += 'L'
        elif i in [3, 6, 9]:
            r = now
            answer += 'R'
        else:
            l_d = 0
            r_d = 0
            
            for x, y, z in zip(l, r, now):
                l_d += abs(x - z)
                r_d += abs(y - z)
            
            if l_d < r_d:
                l = now
                answer += 'L'
            elif l_d > r_d:
                r = now
                answer += 'R'
            else:
                if hand == 'right':
                    r = now
                    answer += 'R'
                else:
                    l = now
                    answer += 'L'
    return answer