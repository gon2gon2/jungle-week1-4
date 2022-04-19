from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

R, C = map(int, input().split())
queue = deque()
tmap = []
visited = [[0]*C for _ in range(R)]
for r in range(R):
    row = list(input().strip())
    for c in range(C):
        if row[c] == "D":
            D_x, D_y = c,r
        elif row[c] == "*":
            queue.append((c,r))
        elif row[c] == "S":
            visited[r][c] = True
            queue.appendleft((c,r))
    tmap.append(row)
dx = [0,0,1,-1]
dy = [1,-1,0,0]
flag = False
while queue:

    if flag:
        break

    x, y = queue.popleft()

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 > nx or nx >= C or ny < 0 or ny >= R:
            continue

        if tmap[y][x] == 'S':
            if tmap[ny][nx] == ".":
                tmap[ny][nx] = 'S'
                queue.append((nx, ny))
                visited[ny][nx] = visited[y][x]+1

            elif tmap[ny][nx] == "D":
                flag = True
                visited[ny][nx] = visited[y][x]+1
                break


        elif tmap[y][x] == "*":
            if tmap[ny][nx] == "." or tmap[ny][nx] == "S":
                tmap[ny][nx] = '*'
                queue.append((nx, ny))

if visited[D_y][D_x] == 0:
    print("KAKTUS")
else: print(visited[D_y][D_x]-1)