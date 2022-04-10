import heapq
import sys
input = sys.stdin.readline

left = []
right = []

N = int(input())
for _ in range(N):
    x = int(input())
    if len(left) == len(right):
        heapq.heappush(left, -x)

    else:
        heapq.heappush(right, x)

    if right and -left[0] > right[0]:
        l,r = heapq.heappop(left),heapq.heappop(right)
        heapq.heappush(left, -r)
        heapq.heappush(right, -l)

    print(-left[0])
