k, n = map(int, input().split())
arr = [ int(input()) for _ in range(k) ]

def binary_search():
    start = 1
    end = max(arr)
    while start <= end:
        mid = (start + end) // 2
        cable = 0
        for i in arr:
            cable += i // mid
        if cable < n:
            end = mid - 1
        else:
            start = mid + 1
    return end
print(binary_search())    
