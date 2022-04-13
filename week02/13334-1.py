import heapq
import sys
input = sys.stdin.readline
N = int(input())
dots = [sorted(map(int, input().split()))for _ in range(N)]
L = int(input())
dots = [d for d in dots if d[1]-d[0] <=L]
# print(dots)
dots.sort(key=lambda x:x[0])
print(dots)

available = []
ans = 0
for d in dots:
    while available and available[0][0]+L < d[1]:
        heapq.heappop(available)
    heapq.heappush(available, d)
    ans = max(ans, len(available))
print(ans)