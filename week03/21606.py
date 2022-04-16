# 40분 60점 -> 설명봐도 모르겠어서 민성님이랑 얘기하고 이해완료
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
A = input().rstrip() # 1은 실내 0은 실외
path = 'n' + A
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문 안 했고 실외(0)라면 dfs 방문 안 했고 실내(1)라면 +1
def dfs(now):
    cnt = 0
    visited[now] = True

    for p in graph[now]:
        if path[p] == '1':
            cnt += 1
        else:
            if not visited[p]:
                cnt += dfs(p)
    return cnt

ans = 0
visited = [False] * (N+1)
for i in range(1,N+1):

    if path[i] == '1': # 실내실내 구하기
        for j in graph[i]:
            if path[j] == '1':
                ans +=1

    else: # 실외를 거치는 경우 구하기
        if not visited[i]:
            tmp = dfs(i)
            ans += tmp * (tmp-1)

print(ans)