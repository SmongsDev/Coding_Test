def solution(cap, n, deliveries, pickups):
    answer = 0
    
    delivery = 0
    pickup = 0
    
    for i in range(n-1, -1, -1):
        cnt = 0
        
        delivery += deliveries[i]
        pickup += pickups[i]
        
        while delivery > 0 or pickup > 0:
            cnt += 1
            delivery -= cap
            pickup -= cap
        answer += (i + 1) * 2 * cnt
    return answer