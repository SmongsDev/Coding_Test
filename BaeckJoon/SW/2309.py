import sys; input = sys.stdin.readline
from itertools import combinations
dwarfs = [int(input()) for _ in range(9)]

for i in list(combinations(dwarfs, 7)):
    if sum(i) == 100:
        print(*sorted(i), sep='\n')