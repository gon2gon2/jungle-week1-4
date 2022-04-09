# 뱀: 8
# 사과: 4


N = int(input()) # 보드의 크기
K = int(input()) # 사과의 개수

BOARD = [[0]*N for _ in range(N)]
# APPLE = [tuple(map(int, input().split())) for _ in range(K)]
for _ in range(K):
    x, y = map(int, input().split())
    BOARD[x-1][y-1] = 'a'

L = int(input()) # 방향전환 정보
XC = dict()
for _ in range(L):
    t, d = input().split()
    XC[int(t)] = d


direction_map = [
    (0,-1),
    (1,0),
    (0,1),
    (-1,0),
    ]

class Snake:
    def __init__(self, x=0, y=0):
        self.length = 1
        self.x = x
        self.y = y
        self.direction = 1

    def change_direction(self,D):
        # turn right
        if D == "D":
            if self.direction == 3:
                self.direction = 0
            else:
                self.direction += 1
            
        # turn left
        if D == "L":
            if self.direction == 0:
                self.direction = 3
            else:
                self.direction -= 1

    def next_move(self):
        (nx,ny) = direction_map[self.direction]
        return self.x+nx, self.y +ny

    def move(self):
        (nx,ny) = direction_map[self.direction]
        self.x += nx
        self.y += ny
        return self.x, self.y

# s = Snake()
# print(s.move())
# print(s.move())
# print(s.move())

from collections import deque
def game():
    snake = Snake()
    time = 1
    position = deque([[snake.y,snake.x]])
    BOARD[snake.y][snake.x] = 8

    while True:
        nx, ny = snake.move()
        if 0 <= ny < N and 0 <= nx < N and BOARD[ny][nx] != 8:
            # 이동한 곳이 빈칸이라면
            if BOARD[ny][nx] == 0:
                by, bx = position.popleft()
                BOARD[by][bx] = 0
            
            position.append([ny,nx])
            BOARD[ny][nx] = 8

            if time in XC.keys():
                snake.change_direction(XC[time])
            time += 1
        else:
            return time


print(game())