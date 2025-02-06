def solution(survey, choices):
    answer = ''
    dic = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for surv, choice in zip(survey, choices):
        score = (choice) % 4
        f, s = surv[0], surv[1]
        
        if choice < 4:
            if choice == 1:
                score = 3
            elif choice == 3:
                score = 1
            dic[f] += score 
        else:
            dic[s] += score
    keys = list(dic.keys())
    for i in range(0,len(keys),2):
        if dic[keys[i]] >= dic[keys[i+1]]:
            answer += keys[i]
        else:
            answer += keys[i+1]
    return answer