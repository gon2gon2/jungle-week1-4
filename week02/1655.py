# N = int(input())


# class Heap:
#     def __init__(self):
#         self.length = 1
#         self.heapsize = 0
#         self.heap = [0]

#     def __add__(self, x):
#         self.heap.append(x)
#         self.heapsize += 1
#         self.length += 1
#         self.max_heapify()

#     def __str__(self):
#         return f"힙사이즈: {self.heapsize}, 힙:{self.heap[1:]}"

#     def heapify(self, i):
#         l = 2*i
#         r = 2*i+1

#         if l<=self.heapsize and self.heap[l] > self.heap[i]:
#             largest = l
#         else:
#             largest = i
        
#         if r<=self.heapsize and self.heap[largest] < self.heap[i]:
#             largest = r

#         if largest != i:
#             self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
#             self.heapify(largest)

#     def max_heapify(self):

#         for i in range(self.heapsize//2, 0, -1):
#             self.heapify(i)

#     def extract_max(self):
#         '''idx 1을 빼서 맨 뒤로 붙인다.
#         heap의 맨뒤를 root로
#         '''
#         if self.heapsize == 0:
#             return 0
#         extracted = self.heap[1]
#         self.heap[1],self.heap[self.heapsize] = self.heap[self.heapsize], self.heap[1]
#         self.heapsize -= 1
#         self.max_heapify()
#         return extracted

import heapq
import sys
input = sys.stdin.readline
N = int(input())
numbers = []
# default heap은 최소힙
# 최대힙을 쓰려면? -를 붙이자
left = []
right = []
for _ in range(N):
    x = int(input())

    if len(left) == len(right):
        heapq.heappush(left, (-x))
    else:
        heapq.heappush(right,(x))

    if right and -left[0] > right[0]:
        left_root = heapq.heappop(left)
        right_root = heapq.heappop(right)
        heapq.heappush(left, -right_root)
        heapq.heappush(right, -left_root)

    
    print(-left[0])