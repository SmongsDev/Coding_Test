numbers = {}
for i in range(10):
    numbers[str(i)] = 0
    
N = input()

for i in N:
    if i == '6' or i == '9':
        if numbers['6'] <= numbers['9']:
            numbers['6'] += 1
        else:
            numbers['9'] += 1
    else:
        numbers[str(i)] += 1
        
print(numbers[max(numbers, key=numbers.get)])