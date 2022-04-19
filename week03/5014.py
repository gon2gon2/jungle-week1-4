# 시작: 22:05
# 종료: 22:53
# 평가: U나 D가 0인 경우를 생각 못했다.
import sys
from collections import deque
input = sys.stdin.readline


F, S, G, U, D = map(int,input().strip().split())
if S == G:
    print(0)
else:
    floors = [False] * (F+1)
    q = deque([S])
    buttons = [U, -D]
    while q:

        now = q.popleft()
            
        for btn in buttons:
            next_floor = now + btn
            if 0 < next_floor <= F and not floors[next_floor] and now != next_floor:
                floors[next_floor] = floors[now] + 1 
                q.append(next_floor)


    if floors[G]:
        print(floors[G])
    else:
        print('use the stairs')
