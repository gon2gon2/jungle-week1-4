# 2시간은 한 것 같다. 답을 봐도 틀리니 어이가 없다.
import sys
import heapq
input = sys.stdin.readline

n = int(input())
maze = [[*map(int, list(input().rstrip()))] for _ in range(n)]

visited = [[False]*n for _ in range(n)]

def bfs():
    heap = [[0,0,0]]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    while heap:
        cnt, cx, cy = heapq.heappop(heap)

        if cx == n-1 and cy == n-1:
            return cnt

        if visited[cy][cx]:
            continue
        visited[cy][cx] = 1
        for i in range(4):
            nx = dx[i] + cx
            ny = dy[i] + cy
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                if maze[ny][nx] == 1:
                    heapq.heappush(heap, [cnt, nx, ny])
                elif maze[ny][nx] == 0:
                    heapq.heappush(heap, [cnt+1, nx,ny])

print(bfs())