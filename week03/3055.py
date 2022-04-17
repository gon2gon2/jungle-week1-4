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
# import sys
# from collections import deque
# r,c=map(int,input().split())
# maps=[list(p for p in sys.stdin.readline().strip()) for _ in range(r)]
# visit=[[0]*c for _ in range(r)]
# dr=[1,0,-1,0]
# dc=[0,-1,0,1]
# queue=deque()

# #물,고슴도치 위치 queue에 담기
# #굴의 위치는 target에 저장
# for i in range(r):
#     for j in range(c):
#         if maps[i][j]=='*':
#             queue.append([i,j])
#         elif maps[i][j]=='S':
#             queue.appendleft([i,j])
#         elif maps[i][j]=='D':
#             target_r=i
#             target_c=j

# flag=False
# #물과 고슴도치 위치에서 BFS탐색
# while queue:
#     # 굴에 도착하고 나면 while문 탈출
#     if flag:
#         break
#     pr, pc = queue.popleft()
#     for i in range(4):
#         nr,nc=pr+dr[i],pc+dc[i]
#         if nr<0 or nr>=r or nc<0 or nc>=c:
#             continue

#         #물
#         if maps[pr][pc]=='*':
#             if maps[nr][nc]=='.' or maps[nr][nc]=='S':
#                 maps[nr][nc]='*'
#                 queue.append([nr,nc])

#         #고슴도치
#         elif maps[pr][pc] == 'S':
#             if maps[nr][nc] == '.':
#                 maps[nr][nc] = 'S'
#                 visit[nr][nc] = visit[pr][pc] + 1
#                 queue.append([nr,nc])
#             #굴에 도착하면 탈출
#             elif maps[nr][nc] == 'D':
#                 flag=True
#                 visit[nr][nc]=visit[pr][pc]+1
#                 break

# #굴에 도착하지 못하면 visit[굴]이 0이므로
# if visit[target_r][target_c]==0:
#     print('KAKTUS')
# else: print(visit[target_r][target_c])