# 2606번 바이러스
# 8분컷
import sys
from collections import deque
input = sys.stdin.readline

N = int(input()) # 전체 노드 개수
graph = [[] for _ in range(N+1)]
M = int(input()) # 간선의 개수
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)

# 저번 문제에서 DFS로 했으니 이번엔 BFS로 해보자

def bfs(graph, s, cnt):
    '''s부터 너비우선 탐색'''

    queue = deque([s])
    visited[s] = True

    while queue:
        x = queue.popleft()
        for p in graph[x]:
            if not visited[p]:
                queue.append(p)
                visited[p] = True
                cnt += 1
    return cnt

print(bfs(graph, 1,0))