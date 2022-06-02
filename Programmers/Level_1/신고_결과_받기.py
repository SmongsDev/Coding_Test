def solution(id_list, report, k):
    answer = []
    dic = {}
    _dic = {}
    re = [i.split(" ") for i in set(report)]
    for i in range(len(id_list)):
        dic[id_list[i]] = 0
    for i in range(len(id_list)):
        _dic[id_list[i]] = 0
    for i in re:
        dic[i[1]] += 1
    for i in dic:
        if dic[i] >= k:
            answer.append(i)
    for i in re:
        if i[1] in answer:
            _dic[i[0]] += 1
    return [j for i, j in _dic.items()]