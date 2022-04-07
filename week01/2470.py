# 산성: 1 ~ 1000000000
# 알칼: -1 ~ -1000000000
# 수 2개를 더해 0에 가장 가깝게

N = int(input())
numbers = sorted(map(int, input().split()))

left, right = 0, N-1
gap = 100000000000
# 
while left < right :
    _sum = numbers[left] + numbers[right]
    if gap > abs(_sum):
        gap = abs(_sum)
        solution = [numbers[left], numbers[right]]
        if gap == 0:
            break

    # 음수인 경우
    if _sum < 0:
        left += 1
    # 양수인 경
    else:
        right -= 1

print(*solution)

'''
1. 음수 양수 0 세가지 경우를 나눔
2. 근데 그냥 작은 걸 


투포인터 알고리즘
연속해야 하는 경우 -> 같은 곳에서 시작
상관없는 경우 -> 좌우에서 시작


모자라 -> 더 가도 돼
커 -> 갈만큼 갔어 다른 애가 해
'''