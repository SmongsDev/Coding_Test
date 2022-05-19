def solution(numbers):
    n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sum = 0
    for i in n:
        if i not in numbers:
            sum += i
            
    return sum