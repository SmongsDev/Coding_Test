def solution(cap, n, deliveries, pickups):
    answer = 0
    n -= 1
    while n != 0:
        pos_d = 0
        res_d = []
        for i in range(n,-1,-1):
            res_d.append((deliveries[i],i+1))
            res = 0
            for j in res_d:
                res += j[0]
            if res > cap:
                deliveries[i] -= (cap - res) + res_d.pop()[0]
                pos_d = i
                break
            deliveries[i] = 0
        pos_p = 0
        res_p = []
        for i in range(n,-1,-1):
            res_p.append((pickups[i], i+1))
            res = 0
            for j in res_p:
                res += j[0]
            if res > cap:
                pickups[i] -= (cap - res) + res_p.pop()[0]
                pos_p = i
                break
            pickups[i] = 0
        n = max(pos_d, pos_p)
        answer += max(res_d[0][1], res_p[0][1]) * 2
            
    return answer
print(solution(4,5,[1, 0, 3, 1, 2],[0, 3, 0, 4, 0]))
print(solution(2,7,[1, 0, 2, 0, 1, 0, 2],[0, 2, 0, 1, 0, 2, 0]))