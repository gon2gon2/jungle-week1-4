# 한번의 순회에서 토마토가 있는 곳을 미리 큐에 넣어놓고 bfs를 나중에 실행시켜준다.
# 40분 해봤는데 최종 결과물 출력하는 방법이나 일수 측정하는 방법을 몰랐다.
import sys
from collections import deque
input = sys.stdin.readline


M,N,H = map(int,input().split())

tomato = []
queue = deque()
for i in range(H):
    layer = []
    for j in range(N):
        layer.append(list(map(int, input().split())))
        for k in range(M):
            if layer[j][k] == 1:
                queue.append([k,j,i])
    tomato.append(layer)
dh = [1,-1,0,0,0,0]
dx = [0,0,1,-1,0,0]
dy = [0,0,0,0,1,-1]

while queue:
    cx,cy,ch = queue.popleft()

    for i in range(6):
        nx = cx + dx[i]
        ny = cy + dy[i]
        nh = ch + dh[i]
        if 0<= nx < M and 0<= ny < N and 0 <= nh < H and not tomato[nh][ny][nx]:
            queue.append([nx,ny,nh])
            tomato[nh][ny][nx] = tomato[ch][cy][cx]+1
# 아하 위에서 오버 숙성 되게 해놔서 max만 써도 최대 일 수를 알 수 있군.+1
day = 0
for i in tomato:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()
        day = max(day,max(j))
print(day-1)
     