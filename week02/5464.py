# N,M = 3, 4
# price_per_weight = [0] + [2, 3, 5]
# cars = [0] + [200, 100, 300, 800]
# order = [0] +  [3, 2, -3, 1, 4, -4, -2, -1]


# 주차공간 N, M대의 차량
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
price_per_weight = [0] + [int(input().rstrip()) for _ in range(N)]
cars = [0] + [int(input().rstrip()) for _ in range(M)]
order = [0] + [int(input().rstrip()) for _ in range(M*2)]

def find_vacant_space():
    for i in range(1,N+1):
            if not space[i]:
                return i
    return False

def find_car(car_num):
    for i in range(1, N+1):
        if space[i] == car_num:
            return i

ans = 0
space = [0] * (N+1)

waiting = []
for o in order:
    if o > 0: # 들어오는 케이스
        available = find_vacant_space()
        if available:
            space[available] = o
            
        else:
            waiting.append(o)

    else: # 나가는 case
        parking = find_car(-o)
        ans += price_per_weight[parking] * cars[-o]
        space[parking] = 0
        
        if waiting:
            parkable = find_vacant_space()
            space[parkable] = waiting.pop(0)



print(ans)