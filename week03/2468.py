# 시작: 13:12
# 종료: 14:07
# 평가: 굳이 일일이 빼주지 않아도 로직 안에 h보다 클 때만 함수가 실행되게 할 수 있군
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
max_h = 0
min_h = 101
area = []
for _ in range(N):
    row = [*map(int,input().split())]
    area.append(row)
    max_h = max(max(row), max_h)
    min_h = min(min(row), min_h)


dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(r,c,h):
    visited[r][c] = True
   
    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]

        if 0 <= nr < N and 0<= nc < N and not visited[nr][nc] and area[nr][nc] > h:
            dfs(nr,nc,h)



ans = 1
for h in range(min_h-1, max_h+1):
    visited = [[False]*N for _ in range(N)]
    cnt = 0 
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and area[r][c] > h:
                dfs(r,c,h)
                cnt += 1

    ans = max(ans, cnt)

print(ans)


