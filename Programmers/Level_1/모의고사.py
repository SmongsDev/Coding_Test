def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3]
    
    dic = { 1 : 0, 2 : 0, 3 : 0 }
    
    for i in range(len(answers)):
        if answers[i] == p1[i % len(p1)]:
            dic[1] += 1
        if answers[i] == p2[i % len(p2)]:
            dic[2] += 1
        if answers[i] == p3[i % len(p3)]:
            dic[3] += 1
            
    _max = max(dic.values())
    for key, value in dic.items():
        if _max == value:
            answer.append(key)
    return answer