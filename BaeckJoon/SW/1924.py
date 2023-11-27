x, y = map(int, input().split())
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

total_day = y
for i in range(1, x):
    total_day += days[i]

print(day[total_day % 7])