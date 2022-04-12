import math

def solution(n, m):
    answer = []
    a = math.gcd(n, m)
    answer.append(a)
    answer.append((n * m) // a)
    
    return answer