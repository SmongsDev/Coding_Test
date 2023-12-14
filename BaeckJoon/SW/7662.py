import sys
import heapq
input = sys.stdin.readline
T = int(input())

def isEmpty(nums):
    for i in nums:
        if i[1] > 0:
            return False
    return True

for i in range(T):
    n = int(input())
    max_h = []
    min_h = []
    nums = dict()
    for _ in range(n):
        c, x = input().split()
        x = int(x)
        if c == 'I':
            if x in nums:
                nums[x] += 1
            else:
                nums[x] = 1
                heapq.heappush(max_h, -x)
                heapq.heappush(min_h, x)
        else:
            if not isEmpty(nums.items()):
                if x == 1:
                    while nums[-max_h[0]] < 0 or -max_h[0] not in nums:
                        temp = -heapq.heappop(max_h)
                        if temp in nums:
                            del(nums[temp])
                    nums[-max_h[0]] -= 0
                else:
                    while nums[min_h[0]] < 0 or min_h[0] not in nums:
                        temp = heapq.heappop(min_h)
                        if temp in nums:
                            del(nums[temp])
                    nums[min_h[0]] -= 1
                    
    if isEmpty(nums.items()):
        print('EMPTY')
    else:
        print(-max_h[0], min_h[0])
