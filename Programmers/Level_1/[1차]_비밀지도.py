def zero(n, arr):
    for i in range(len(arr)):
        while len(arr[i]) < n:
            arr[i] = '0' + arr[i]
    return arr

def solution(n, arr1, arr2):
    answer = []
    arr1 = [format(i, 'b') for i in arr1]
    arr2 = [format(i, 'b') for i in arr2]
    tmp = [str(int(arr1[i]) + int(arr2[i])) for i in range(n)]
    arr = zero(n, tmp)
    for i in arr:
        temp = ''
        for j in range(n):
            if i[j] != '0':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
    return answer