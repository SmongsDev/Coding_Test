from itertools import product

def solution(users, emoticons):
    max_subscribes = 0
    max_sales = 0
    
    for discount in list(product([10, 20, 30, 40], repeat=len(emoticons))):
        total_sales = subscribes = 0
        for per, money in users:
            sales = 0
            for i, emotion in enumerate(emoticons):
                if per <= discount[i]:
                    sales += emotion * (1 - discount[i] / 100)
            if sales >= money:
                subscribes += 1
            else:
                total_sales += sales
        if max_subscribes < subscribes or (max_sales < total_sales and subscribes == max_subscribes):
            max_subscribes = subscribes
            max_sales = total_sales

    return [max_subscribes, int(max_sales)]