# 59분 -> 시간초과 ㅜ

import heapq
import sys
input = sys.stdin.readline
N, M = map(int,input().split())

problem = [[-1, i] for i in range(N)]

for _ in range(M):
    before, next = map(int,input().split())
    problem[next-1][0] = before-1

heapq.heapify(problem)
ans = []
while problem:
    p = heapq.heappop(problem)
    ans.append(p[1]+1)
    if p[1] != -1:
        for i in range(len(problem)): # 아마 이부분이 오래 걸리는 거 같다.
            if problem[i][0] == p[1]:
                problem[i][0] = -1
                break

    heapq.heapify(problem)
print(*ans)