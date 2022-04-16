# 소요시간 31분
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)


# 2번부터 깊이우선으로 해서 마지막에 나오는 값을 출력하면 되는 건가 
# -> 탐색횟수 많았는데 시간초과에 걸려서 한번에 다 마킹하도록 바꿈
for i in range(1, N+1):
    graph[i].sort()

def dfs(graph, v):

    visited[v] = True

    for p in graph[v]:
        if not visited[p]:
            ans[p] = v
            dfs(graph, p)



ans = [1] * (N+1)
visited = [False] * (N+1)
dfs(graph, 1)
for i in ans[2:]:
    print(i)
