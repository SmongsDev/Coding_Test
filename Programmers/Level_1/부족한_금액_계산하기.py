def solution(price, money, count):
    result = sum(map(lambda x: x * price, range(1, count+1)))
    return result - money if money < result else 0