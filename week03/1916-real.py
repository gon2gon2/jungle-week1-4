import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
   u,v,c = map(int, input().split())
   graph[u].append((c,v))
start, target = map(int, input().split())
distance = [1e9] * (N+1)
distance[start] = 0
heap = [] 
heap.append((0,start))


while heap:

    cost, now = heapq.heappop(heap)
    if cost > distance[now]:
        continue

    for node in graph[now]:
        temp_cost = cost + node[0]
        if distance[node[1]] > temp_cost:
            distance[node[1]] = temp_cost
            heapq.heappush(heap, (temp_cost, node[1]))

print(distance[target])




