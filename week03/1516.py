# 9:52 ~ 10:11
# 쉽당.

import sys
from collections import deque

input = sys.stdin.readline
# 건물 수
N = int(input())
graph = [[] for _ in range(N + 1)]
duration = [0] * (N + 1)
result = [0] * (N + 1)
in_degree = [0] * (N + 1)
for b in range(1, N + 1):
    row = [*map(int, input().split())]
    duration[b] = row[0]
    for i in row[1:-1]:
        graph[i].append(b)
        in_degree[b] += 1
q = deque()
for i in range(1, N + 1):
    if not in_degree[i]:
        q.append(i)
        result[i] = duration[i]

while q:
    now = q.popleft()

    for i in graph[now]:

        result[i] = max(result[i], result[now] + duration[i])
        in_degree[i] -= 1
        if not in_degree[i]:
            q.append(i)
for a in result[1:]:
    print(a)
