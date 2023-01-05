n = int(input())

check = 665
count = 0

def sixTrueFalse(check):
    return True if '666' in str(check) else False

while count != n:
    check += 1
    if sixTrueFalse(check):
        count += 1
    
print(check)
