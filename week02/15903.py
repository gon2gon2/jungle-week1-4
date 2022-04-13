# 우선순위 큐라는 걸 아니까 쉬워졌다
import heapq
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a_ = [*map(int,input().split())]

heapq.heapify(a_)

for _ in range(m):
    a = heapq.heappop(a_)
    b = heapq.heappop(a_)
    x = a+b
    heapq.heappush(a_,x)
    heapq.heappush(a_,x)
print(sum(a_))