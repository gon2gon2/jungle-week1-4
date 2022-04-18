# 13분, 위상정렬 아니까 바로 풀렸다.
import heapq
import sys

input = sys.stdin.readline
queue = []
ans = []

N, M = map(int, input().split())
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    indegree[v] += 1

for i in range(1, N + 1):
    if not indegree[i]:
        heapq.heappush(queue, i)

while queue:
    now = heapq.heappop(queue)
    ans.append(now)

    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(queue, i)

print(*ans)
