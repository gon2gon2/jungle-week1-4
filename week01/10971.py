# 도시 1~N

from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
minimum = sys.maxsize


def get_cost(p,):
    # print(p)
    total_cost = 0
    for i in range(N):
        cost = graph[p[i]][p[i+1]]
        total_cost += cost
        if not cost or total_cost > minimum:
            return False
    return total_cost


for p in permutations(range(N)):
    # p: 방문할 순서
    p = list(p)
    p.append(p[0])
    
    total_cost = get_cost(p)

    if total_cost < minimum and total_cost:
        minimum = total_cost
    
print(minimum)

