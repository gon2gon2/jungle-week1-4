# 4월 19일 20:05 ~ 21:12
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N = int(input())

graph = [list(map(int,list(input().strip()))) for _ in range(N)]


dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(x,y,c):
    graph[y][x] = c
    ans[c] += 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and graph[ny][nx] == 1:
            dfs(nx, ny, c)
            
c = 1 
ans = dict()
for i in range(N):
    for j in range(N):
        if graph[j][i] == 1:
            c += 1
            ans[c] = 0
            dfs(i,j,c)

print(c-1)
for a in sorted(ans.values()):
    print(a)
