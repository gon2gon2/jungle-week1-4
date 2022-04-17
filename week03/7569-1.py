from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


M, N, H = map(int, input().split())
queue = deque()
all_tomato = []
for i in range(H):
    layer = []
    for j in range(N):
        row = [*map(int, list(input().strip().split()))]
        for k in range(M):
            if row[k] == 1:
                queue.append((i,j,k))
        layer.append(row)
    all_tomato.append(layer) 

dh = [1,-1,0,0,0,0]
dx = [0,0,1,-1,0,0]
dy = [0,0,0,0,1,-1]
while queue:
    h,y,x = queue.popleft()

    for i in range(6):
    
        nh = dh[i] + h
        ny = dy[i] + y
        nx = dx[i] + x
        if 0<= nh < H and 0 <= ny < N and 0 <= nx < M and all_tomato[nh][ny][nx] == 0:
            all_tomato[nh][ny][nx] = all_tomato[h][y][x] + 1
            queue.append((nh,ny,nx))

ans = 0
for i in all_tomato:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()
        ans = max(ans, max(j)) 
print(ans-1)
