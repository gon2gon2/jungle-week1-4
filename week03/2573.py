import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


N, M = map(int, input().split())
ice_list = []
maps = []
for r in range(N):
    row = [*map(int,input().split())]
    for c in range(M):
        if row[c] != 0:
            ice_list.append((r,c))
    maps.append(row)
    
    
dx = [0,0,1,-1]
dy = [1,-1,0,0]

    
def dfs(r,c):

    visited[r][c] = True
    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]
        if maps[nr][nc] and not visited[nr][nc]:
            dfs(nr,nc)

year = 0
while ice_list:

    visited = [[False]*M for _ in range(N)]
    ice_be_removed = []

    for r, c in ice_list:
        zero_cnt = 0

        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < N and 0<= nc < M and maps[nr][nc] == 0:
                zero_cnt += 1

        if zero_cnt >= maps[r][c]:
            ice_be_removed.append((r,c))
        else:
            maps[r][c] -= zero_cnt

    for r,c in ice_be_removed:
        maps[r][c] = 0

    ice_list = list(set(ice_list) - set(ice_be_removed))
    cnt = 0
    for r,c in ice_list:
        if not visited[r][c]:    
            dfs(r,c)
            cnt += 1

    year += 1
    if cnt >= 2:
        break
if ice_list:
    print(year)
else:
    print(0)
