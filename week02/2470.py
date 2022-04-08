# N = int(input())
# solutions = sorted(map(int, input().split()))

# def find_minimal(v, ac):
#     # 알칼값 1개, 산성 여러개
#     start, end = 0, len(ac)-1
#     minimum = ac[-1]
#     while start < end:
#         mid = (start+end)//2

#         if v+ac[mid] == 0:
#             return (v, ac[mid])

#         elif v+ac[mid] <= minimum:
#             # 더 줄여볼 수 있나 확인
#             end = mid-1
#         else:
#             start = mid+1

#     return [ac[end]]


# # print(find_minimal(-7,[1,3,4]))


# def two_solution(alk, ac):
#     '''알칼리성, 산성 하나씩 받고 alk에서 하나 뽑은 뒤 이진탐색 수행'''

#     best = (alk[0], ac[-1])

#     for a in alk:
#         best_combination = find_minimal(a, ac)
#         if len(best_combination) == 2:
#             return best_combination

#         best_combination = best_combination[0]
#         if abs(a+best_combination) < abs(sum(best)):
#             best = (a,best_combination)

#     return best


# if solutions[0] < 0 and solutions[-1] < 0:
#     print(solutions[-2], solutions[-1])

# elif solutions[0] > 0 and solutions[-1] > 0:
#     print(solutions[0], solutions[1])

# else:
#     # 두 종류의 용액이 있는 경우
#     acid = []
#     alkaline = []
#     for sol in solutions:
#         if sol > 0:
#             acid.append(sol)
#         else:
#             alkaline.append(sol)

#     # print(*two_solution(alkaline, acid))

#     print(*min((solutions[-2], solutions[-1]), (solutions[0], solutions[1]), two_solution(alkaline, acid), key=lambda x:abs(sum(x))))

    
# 갱신할 값이 여러개면 한번에 묶어버리든가 하자 계산으로 얻어내던가

N = int(input())
solutions = sorted(map(int, input().split()))

best_val = abs(sum([solutions[0], solutions[-1]]))
best_sols = [solutions[0], solutions[-1]]

for i in range(N-1):
    sol_1 = solutions[i]
    start,end = i+1, N-1

    while start <= end:
        mid = (start+end)//2
        sol_2 = solutions[mid]

        mix = sol_1 + sol_2

        if abs(mix) < best_val:
            # 기록
            best_sols = [sol_1, sol_2]
            best_val = abs(mix)

        if mix < 0:
            start = mid + 1
        else:
            end = mid-1

print(*best_sols)




## 위 풀이는 -1,-2,6가 있으면 -1과 6만 나올 케이스.
# 같은 부호더라도 

'''
5
-2 4 -99 -1 98
'''