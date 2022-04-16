# 2178번 미로 탐색
# 32분 해봤으나 잘 모르겠다. 만약 잘못된 길을 간 경우 등을 어떻게 고려하는지 모르겠다.
# 대충 로직은 맞았다. 값 갱신이나 return이 좀 미흡했다.
from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int,input().rstrip())) for _ in range(N)]
moves = [(1,0), (-1,0), (0,-1), (0,1)]

queue = deque([[0,0]])
while queue:
    x,y = queue.popleft()
    for (dx,dy) in moves:
        nx, ny = x+dx, y+dy
        if 0<= nx < M and 0<= ny < N and graph[ny][nx] == 1:
            queue.append([nx,ny])
            graph[ny][nx] = graph[y][x] + 1

print(graph[N-1][M-1])