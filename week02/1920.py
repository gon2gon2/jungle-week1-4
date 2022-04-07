# left, right 의 등호, N-1이 아니라 M-1에서 인덱스 에러 발생
N = int(input())
Ns = sorted(map(int,input().split()))
M = int(input())
Ms = tuple(map(int,input().split()))


def binary_search(x):
    left = 0
    right = N - 1
    while left <= right:
        mid = (left+right) // 2
        if Ns[mid] == x:
            return True
        elif Ns[mid] < x:
            left = mid+1
        elif Ns[mid] > x:
            right = mid-1
    return False

for m in Ms:
    print(1 if binary_search(m) else 0)