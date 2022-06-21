import datetime

def solution(a, b):
    week = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    date = datetime.date(2016, a, b).weekday()
    return week[date]