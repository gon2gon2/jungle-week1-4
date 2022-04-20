# 시작: 19:30
# 종료: 20:40
# 평가: 확실히 좌표계를 만들어 구하는 건 너무 naive한 풀이고, 좌표들만 확인하는 것이 훨씬 빠르다.
import sys
from collections import deque
input = sys.stdin.readline

def bfs(home_x, home_y, convens, rock_x, rock_y):
    visited = [False] * (len(convens)+1)
    q = deque([[home_x, home_y]])

    while q:

        now_x, now_y = q.popleft()
        
        if abs(rock_x - now_x) + abs(rock_y - now_y) <= 1000:
            print("happy")
            return

        
        for idx, con_x, con_y in convens:
            if not visited[idx] and abs(con_x - now_x) + abs(con_y - now_y) <= 1000:
                q.append((con_x, con_y))
                visited[idx] = True
    

    print("sad")
    return






T = int(input())

for t in range(T):
    N = int(input())
    home_x, home_y = map(int,input().split())
    convens = [[i, *map(int,input().split())] for i in range(N)]
    rock_x, rock_y = map(int,input().split())

    
    bfs(home_x, home_y, convens, rock_x, rock_y)

