import sys
input = sys.stdin.readline

N, K = map(int, input().split())
LEVELS = sorted([int(input()) for _ in range(N)])

# 찾을 것 T: 팀 목표 레벨
# 팀 목표 레벨: 모든 캐릭터가 공통으로 맞출 수 있는 레벨

start, end = 0, max(LEVELS)

while start <= end:
    mid = (start+end)//2

    needed_level = [mid-l for l in LEVELS if mid>l]
    needed_level = sum(needed_level)
    if needed_level <= K:
        #목표 높이기
        start = mid+1

    else:
        end = mid-1

print(end)