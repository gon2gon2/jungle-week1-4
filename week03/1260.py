# 양방향이라는 것을 놓쳤다 + 초기화 실수했다.
# 30분
import sys
from collections import deque
input = sys.stdin.readline

# 정점, 간선, 시작점
N, M, V = [*map(int, input().split())]
graph = [[] for _ in range(N+1)]
for _ in range(M):
    n1,n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for i in range(N):
    graph[i+1].sort()


def DFS(graph, v):
    '''깊이 우선 탐색, 스택이나 재귀를 사용한다'''
    
    visited[v] = True
    print(v, end=' ')
    
    for p in graph[v]:
        if not visited[p]:
            DFS(graph, p)

    return


def BFS(graph, s):
    '''너비 우선 탐색, 큐를 사용한다'''

    visited[s] = True
    queue = deque([s])

    while queue:
        x = queue.popleft()
        print(x, end=' ')

        for p in graph[x]:
            if not visited[p]:
                visited[p] = True
                queue.append(p)
    return 


visited = [False] * (N+1)
DFS(graph, V)
print()

visited = [False] * (N+1)
BFS(graph,V)
print()