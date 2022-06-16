from collections import Counter
def solution(participant, completion):
    answer = list(Counter(participant) - Counter(completion))
    return answer[0]