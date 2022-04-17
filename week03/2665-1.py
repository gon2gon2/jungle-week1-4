# 25분, 방문 처리 없이 할 수 있을 거 같은디
import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
maze = [list(map(int,list(input().strip()))) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
# print(maze)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

heap = [(0,0,0)]
while heap:
    (cnt, cx, cy) = heapq.heappop(heap)

    if cx == n-1 and cy == n-1:
        print(cnt)
        break  
    maze[cy][cx] = cnt
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            # 흰색인 경우
            if maze[ny][nx] == 1 and not visited[ny][nx]:
                heapq.heappush(heap, (cnt, nx, ny))

            # 회색인 경우
            elif maze[ny][nx] == 0 and not visited[ny][nx]:
                heapq.heappush(heap, (cnt+1, nx, ny))

            visited[ny][nx] = True


