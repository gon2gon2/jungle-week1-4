# N 번째 수 -> heap으로 작은 거 N개

# K, N = 4, 19
# prime_numbers= [2, 3, 5, 7]
K, N = 3, 5
prime_numbers = [2,5,7]

import sys
import heapq
input = sys.stdin.readline
heap = []
# K, N = map(int, input().rstrip().split())
# prime_numbers = [*map(int, input().rstrip().split())]

# N개까지만 넣는다
# max_heap = [-i for i in prime_numbers]
# heapq.heapify(max_heap)
# i = 1
# while len(max_heap) < N:
#     x = -i*prime_numbers[0]
#     if x not in max_heap:
#         heapq.heappush(max_heap, x)
#         i += 1

# for p in prime_numbers:
#     for m in max_heap:
#         x = m*p
#         # 작은 경우만 넣는다. 실제론 반대
#         if x < max_heap[0]:
#             heapq.heappush(max_heap, x)
#         if len(max_heap) > N:
#         # len 넘었으면 pop한다.
#             heapq.heappop(max_heap)
# print(-max_heap[0])

# 인풋으로 받은 값들로 initialize
for p in prime_numbers:
    heapq.heappush(heap, p)

for i in range(N): # N번째 수가 target이니까 pop을 N번하면 된다.
    num = heapq.heappop(heap)
    for j in range(K): # input 개수
        new_num = num * prime_numbers[j] # heap에서 가장 작은 값으로 주어진 소수에 각각 곱해서
        heapq.heappush(heap, new_num)    # heap에 추가

        if num % prime_numbers[j] == 0:
            break
    else:
        print(num)
