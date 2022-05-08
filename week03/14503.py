# 시작: 20:51
# 종료: 22:00
# 평가: 괜히 OOP 흉내내보려다가 망쳤다. 
import sys
from collections import deque
input = sys.stdin.readline



class Cleaner:

    def __init__(self, r, c, d):
        self.r = r
        self.c = c
        self.d = d
        self.dr = [-1, 0, +1, 0]
        self.dc = [0, +1, 0, -1]
        self.status = 'on'
        self.score = 0
    
    def get_position(self):
        return self.r, self.c

    def turn(self):
        self.d = (self.d + 1) % 4
        return self.d


    def set_position(self, r, c):
        # TODO 배열 넘어가거나 예외처리 
        self.r = self.r + r
        self.c = self.c + c

        return self.r, self.c
    
    def go_backward(self):
        # TODO 예외처리
        self.r = self.r - self.dr[self.d]
        self.c = self.c - self.dc[self.d]

        if self.r > N or self.r < 0 or self.c > M or self.c <0 \
                or floor[self.r][self.c] == 1:
                    self.status = 'off'
                    return False

        return self.r, self.c


    def is_there_job(self):
        jobs = []
        for i in range(4):
            nr = self.r + self.dr[i]
            nc = self.c + self.dc[i]

            if floor[nr][nc] == 0 and not visited[nr][nc]:
                jobs.append((nr,nc))
        return jobs

    def clean(self):
        visited[self.r][self.c] = True
        self.score += 1

    
N, M = map(int, input().split())
r, c, d = map(int, input().split()) 

floor = [[*map(int,input().split())] for _ in range(N)]
visited = [[False]*M for _ in range(N)]    
cleaner = Cleaner(r,c,d)

q = deque([cleaner.get_position()])

while q and cleaner.status == 'on':

    cr, cc = q.popleft()
    cleaner.set_position(cr,cc)
    # 현재 위치를 청소한다
    cleaner.clean()

    # 인접 칸 탐색
    jobs = cleaner.is_there_job()
    
    if not jobs:
        cleaner.go_backward()
        q.append(cleaner.get_position())


print(cleaner.score)
