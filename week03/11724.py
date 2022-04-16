# 11724 연결 요소의 개수
# 15분 30초

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort()

visited = [False] * (N+1)
def dfs(graph, v):
    '''해당 노드를 첫 방문하는 것이면 return1 아니면 0을 해준다.'''
    if not visited[v]:
        visited[v] = True
        
        for p in graph[v]:
            if not visited[p]:
                dfs(graph, p)
        return 1
    return 0

cnt = 0

for i in range(1,N+1):
    # return은 1 or 0이라 그 값을 더해줘서 구한다.
    cnt += dfs(graph, i)

print(cnt)


################### 다른  풀이
# 이런식으로 dfs를 시작할 때 방문한 적이 없으면 체크를 해서 더해주는 방식도 있다.
for i in range(1,N+1):
    if not visited[i]:
        cnt += 1
        dfs(graph, i)

