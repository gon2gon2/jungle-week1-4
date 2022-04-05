# 겹치면 안ㄷ ㅚㅁ
# 중단 X

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

# print(sorted(meetings, key=lambda x: (x[0],x[1])))
#####################################################
# from itertools import combinations
# maximum = 0
# for i in range(N):
#     for comb in combinations(meetings, i):
#         last_start = 0
#         for [start, end] in comb:
#             if last_start > start:
#                 break
#         else:
#             maximum = max(maximum, len(comb))
# print(maximum)
#####################################################
N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings = sorted(meetings, key=lambda x: (x[1], x[0]))
now = 0
cnt = 0
for [s,e] in meetings:
    if now <= s: # 같을 수도 있는 경우가 있기 때문에
        cnt += 1
        now = e
print(cnt)

    
        
'''
# 나의 접근
무엇을 선택할지는 어차피 combination(meetings, i)에서 전부 cover하므로 가능한 플랜인지만 체크하여 가능하면 미팅수 카운트 후 비교

1. 가능한 플랜은 2중 for문으로 전체에서 몇개 고를지까지 cover
2. 가능한 플랜이면 숫자 check

# 다른 접근
1. 빨리 끝나는 것부터
2. 더 일찍 시작하는 것부터

# 왜 생각을 못 했나?
- 이렇게 간단한 풀이인줄 몰랐음
- 이렇게 풀이가 가능한 이유
1. 단순히 갯수가 중요한 것이기 때문에
2. 회의에서 나오는 benefit이나 penalty가 없기 때문에
3. 그냥 최대한 빈칸 만들어서 풀면 된다.
'''

