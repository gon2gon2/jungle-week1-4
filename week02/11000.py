# 강의실 배정
# 다른 사람들의 경우 heappush를 두번 쓰거나 heapq가 비어있는 경우를 처리해주던데 로직상 그럴 일이 없어 내 코드가 더 짧고 깔끔해졌다.

import heapq
import sys
input = sys.stdin.readline
N = int(input())
classes = [[*map(int, input().split())] for _ in range(N)]
classes.sort(key=lambda x: x[0])
heap = [classes[0][1]]

for c in classes[1:]:
    if c[0] >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, c[1])
print(len(heap))