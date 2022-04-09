# N = 7
# block = [2, 1, 4, 5, 1, 3, 3]
import sys  
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def go_left(i,h):
    if i == -1 or block[i]<h:
        return 0

    return go_left(i-1,h) + h

def go_right(i,h):
    if i == N or block[i]<h:
        return 0
    return go_right(i+1,h) + h

def check(i):
    h = block[i]
    return go_left(i,h) + go_right(i,h) - h

# 만약 정답 아니면 h도 전체 탐색 돌려줘야 될듯 -> python 시간초과 -> pypy 메모리초과
while True:
    input_numbers = list(map(int,input().split()))
    N = input_numbers[0]
    if N == 0:
        break

    block = input_numbers[1:]
    ans = 0
    for i in range(N):
        value = check(i)
        ans = max(value, ans)
    print(ans)



    
import sys
def divdeandconquer(a):
    if len(a) == 1:
        return a[0]
    if len(a) % 2 == 1: # 홀수면 왼쪽에 0 하나 붙여서 균형 맞춰줌
        a = [0] + a
    d = len(a) // 2 #기준선
    x = a[:d] # 기준선 왼쪽 부분
    y = a[d:] # 기준선 오른쪽 부분
    cnt = 2   # 사각형 개수
    tmpmax = min(a[d - 1], a[d]) # 높이를 확인해서 더 작은 쪽으로
    tmparea = tmpmax * cnt  # 기준선이 있는 곳의 넓이
    i = 0
    j = 0
    for _ in range(0, len(a) - 2):
        if d - 1 - i == 0:
            # 왼쪽끝까지 가면 오른쪽으로 한번
            j += 1
        elif d + j == len(a) - 1:
            # 오른쪽 끝까지 가면 왼쪽으로 한번
            i += 1
        else:
            if a[d - 2 - i] >= a[d + 1 + j]: # 왼쪽 오른쪽 둘 중 어디로 가야 이득일까 확인
                i += 1
            else:
                j += 1
        tmpmax = min(tmpmax, a[d - 1 - i], a[d + j]) # 가운데, 왼추,우추 중 하나 골라서 넓이
        cnt += 1
        tmparea = max(tmparea, tmpmax * cnt) # 추가한거랑 이전 비교
    z = tmparea
    return max(divdeandconquer(x), divdeandconquer(y), z)


while 1:
    n, *histogram = list(map(int, sys.stdin.readline().split()))
    if n == 0:
        break
    maxarea = divdeandconquer(histogram)
    print(maxarea)
