# 8:46 ~ 9:42
# 야호 혼자 풀었땅
import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for t in range(T):
    # 건물 수, 규칙 수
    N, K = map(int, input().split())
    in_degree = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    duration = [0] + [*map(int, input().split())]
    for _ in range(K):
        u, v = map(int, input().split())
        graph[u].append(v)
        in_degree[v] += 1

    victory_tower = int(input())
    q = deque()
    result = [0] * (N + 1)
    for i in range(1, N + 1):
        if not in_degree[i]:
            q.append(i)
            result[i] = duration[i]

    while q:
        x = q.popleft()

        for i in graph[x]:
            result[i] = max(result[x] + duration[i], result[i])
            in_degree[i] -= 1
            if not in_degree[i]:
                q.append(i)

    print(result[victory_tower])
