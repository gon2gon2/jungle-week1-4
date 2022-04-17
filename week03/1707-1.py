import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(v, c):
    visited[v] = c 

    for p in graph[v]:
        if not visited[p]:
            if not dfs(p,-c): # 조건을 확인하면서 실행시키는 부분을 놓쳤다.
                return False
        else:
            if visited[p] == c:
                return False
    return True
    

K = int(input())
for k in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for e in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * (V+1)
    for i in range(1, V+1):
        if not visited[i]:
            ans = dfs(i,1)
            if not ans:
                break
    print("YES" if ans else "NO")
