import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())

# 1은 실내, 0은 실외
A = 'n'+input().strip()
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    '''실외에 맞닿아있는 점을 세주는 함수'''
    cnt = 0 
    visited[v] = True
    for i in graph[v]:
        if A[i] == "1":
            cnt += 1

        elif A[i]== "0" and not visited[i]:
            cnt += dfs(i)
    return cnt


visited = [False] * (N+1)
ans = 0
for i in range(1, N+1):
    if A[i] == '1':
        for j in graph[i]:
            if A[j] == '1':
                ans += 1
    else:
        if not visited[i]:
            temp = dfs(i)
            ans += temp * (temp-1)
print(ans)

