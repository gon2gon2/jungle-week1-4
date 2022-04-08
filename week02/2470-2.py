import math
import sys
input = sys.stdin.readline
N = int(input())
solution_list = sorted(map(int, input().split()))


best_score = math.inf
best_combination = [solution_list[0],solution_list[-1]]

for i in range(N-1):
    sol_1 = solution_list[i]
    start, end = i+1, N-1

    while start <= end:
        mid = (start + end) //2
        sol_2 = solution_list[mid]
        
        mix = sol_1 + sol_2

        if abs(mix) < best_score:
            best_combination = [sol_1, sol_2]
            best_score = abs(mix)

        if mix > 0:
            end = mid-1
        else:
            start = mid+1

print(*best_combination)
