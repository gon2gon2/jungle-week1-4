# 1707 이분 그래프
# 이분그래프가 뭔지를 몰라서 검색해봤다
# 이웃한 정점을 다른 색으로 칠했을 떄 모든 점이 자신과 인접한 점과 서로 다른 색깔을 가져야 한다.

# DFS로 모든 점 탐색하면서 자식은 다른 색으로 칠한다.
# 색을 문자열로 넣어주려 했는데 1, -1로 하는게 ㅇ훨씬 좋은 것 같다.(-만 붙이면 알아서 반전)

# 31분 -> 틀렸습니다 -> 수정해서 43분 완료
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
def dfs(graph, now, c):

    visited[now] = c

    for p in graph[now]:
        if not visited[p]:
            if not dfs(graph, p, -c):
                return False
        elif visited[p] == visited[now]:
            return False
    return True

K = int(input().rstrip())

for k in range(K):
    V, E = map(int,input().rstrip().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().rstrip().split())
        graph[u].append(v)
        graph[v].append(u)
    
    
    visited = [False] * (V+1)
    for i in range(1, V+1):
        if not visited[i]:
            ans = dfs(graph, i, 1) # <- i가 아니라 1이 들어가 있었음 ㅡㅡ
            if not ans:
                break

    print("YES" if ans else "NO")