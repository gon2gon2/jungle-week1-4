import sys
import heapq
input = sys.stdin.readline

N = int(input())
my_heap = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if not my_heap:
            print(0)
            continue
        print(heapq.heappop(my_heap)[1])
    else:
        heapq.heappush(my_heap, [abs(x),x])