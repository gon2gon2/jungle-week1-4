# N = int(input())
# A_i = list(map(int, input().split()))

import sys
N = 6
A_i = [10, 20, 10, 30, 20, 50]



# 정렬하고 오른쪽에서 나보단 큰데 가장 작은 값 찾는다
# 인덱스 꼬여서 안 된다.

# 1. 맨 왼쪽 값과 오른쪽값을 분리한다.
# 2. 오른쪽을 정렬하고 나보다 크지만 가장 작은 값을 찾는다
# 3. cnt를 세고 1 수행
# 문제: 순서가 바뀐다. n에 대해 정렬(logN)하고 탐색(logN)을 수행한다. n * logN^2
# 28분


# ans = 0
# for i in range(N):
#     now = A_i[i]
#     right = sorted(A_i[i+1:])
#     temp = sys.maxsize
#     while right:
#         start, end = 0, len(right) - 1
#         while start<=end:
#             mid = (start+end) // 2
#             v = right[mid]

#             if v < now:
#                 start = mid+1
#             else:
#                 end = mid-1
#                 if 



import sys
input = sys.stdin.readline
N = int(input())
A_i = [*map(int,input().split())]

def find_lowerbound(x):

    start,end = 0, len(LIS) -1

    while start <= end:
        mid = (start+end) // 2

        if LIS[mid] == x:
            return mid
        elif LIS[mid] > x:
            end = mid - 1
        else:
            start = mid + 1

    return start


LIS = [A_i[0]]

for i in range(1,N):
    if LIS[-1] < A_i[i]:
        LIS.append(A_i[i])

    else:
        x = find_lowerbound(A_i[i])
        LIS[x] = A_i[i]

print(len(LIS))