# 9분 컷
import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    in_degree[B] += 1

queue = deque()


for i in range(1, N + 1):
    if not in_degree[i]:
        queue.append(i)

ans = []
while queue:
    now = queue.popleft()
    ans.append(now)

    for i in graph[now]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            queue.append(i)
print(*ans)
