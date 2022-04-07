# 틀린 이유
# start를 0이 아니라 budget_list의 min값으로 설정해서.

def get_limit(budget_list, start, end):
    while start <= end:
        mid = (start+end)//2
        total = sum([mid if x > mid else x for x in budget_list]) 

        if total <= M:
            start = mid+1
        
        else:
            end = mid-1
    return end


N = int(input()) #지방의 수
budget = sorted(map(int, input().split()))
M = int(input()) # 총 예산

if sum(budget) <= M:
    print(budget[-1])

else:
    print(get_limit(budget, 0, budget[-1]))