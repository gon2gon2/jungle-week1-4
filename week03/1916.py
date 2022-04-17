# # 40분동안 해봤지만 실패 -> 다익스트라로 구하는 거였다.
# from collections import deque
# import sys
# input = sys.stdin.readline


# N = int(input())
# M = int(input())
# graph = [[0]*(N+1) for _ in range(N+1)]
# for _ in range(M):
#     s, e, c = map(int, input().split())
#     graph[s][e] = c

# start, target = map(int,input().split())


# visited = [False] * (N+1)
# minimal_cost = [100000] * (N+1)
# queue = deque([start])
# while queue:
#     departure = queue.popleft()
#     for arrival in range(1,N+1):
#         if graph[departure][arrival]:
#             if not visited[arrival]:
#                 minimal_cost[arrival] = graph[departure][arrival]
#                 visited[arrival] = True
#                 queue.append(arrival)
#             else:
#                 minimal_cost[arrival] = min(minimal_cost[arrival], minimal_cost[departure]+graph[departure][arrival])

# print(minimal_cost[target])
###################################### 다시 짠 코드############################## 
import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(M+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B,C))

start, target = map(int,input().split())

distance = [1000000] * (N+1)

def djikstra(start):
    heap = []
    heapq.heappush(heap,(0,start))
    while heap:
        dist, departure = heapq.heappop(heap)

        if distance[departure] < dist:
            continue
        
        for node in graph[departure]:
            cost = dist + node[1] # 여기까지의 비용 + node까지의 비용
            if distance[node[0]] > cost:
                distance[node[0]] = cost
                heapq.heappush(heap, (cost,node[0]))
djikstra(start)
print(distance[target])