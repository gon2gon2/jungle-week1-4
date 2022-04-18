# 10:11 ~ 10:34
# easy

from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
for _ in range(M):
    row = [*map(int, input().split())][1:]
    for i in range(len(row) - 1):
        graph[row[i]].append(row[i + 1])
        in_degree[row[i + 1]] += 1

q = deque()
ans = []
for i in range(1, N + 1):
    if not in_degree[i]:
        q.append(i)
while q:
    now = q.popleft()
    ans.append(now)

    for i in graph[now]:
        in_degree[i] -= 1
        if not in_degree[i]:
            q.append(i)
if len(ans) != N:
    print(0)
else:
    for a in ans:
        print(a)
