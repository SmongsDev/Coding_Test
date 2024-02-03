import sys; input = sys.stdin.readline
s = input().rstrip().split('-')
nums = []
for i in s:
    j = map(int,i.split('+'))
    nums.append(sum(j))

res = nums[0]
for n in nums[1:]:
    res -= n
print(res)