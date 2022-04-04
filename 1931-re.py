# 겹치면 안ㄷ ㅚㅁ
# 중단 X

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

# print(sorted(meetings, key=lambda x: (x[0],x[1])))

from itertools import combinations

maximum = 0
for i in range(N):
    for comb in combinations(meetings, i):
        last_start = 0
        for [start, end] in comb:
            if last_start > start:
                break
        else:
            maximum = max(maximum, len(comb))
print(maximum)

        