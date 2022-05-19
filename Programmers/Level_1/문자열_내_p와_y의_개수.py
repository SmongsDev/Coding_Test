def solution(s):
    arr = [0, 0]
    for i in s:
        if "p" == i or "P" == i:
            arr[0] += 1
        elif "y" == i or "Y" == i:
            arr[1] += 1
    if arr[0] == arr[1]:
        return True
    else:
        return False