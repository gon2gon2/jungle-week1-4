
# def dfs(idx, value, num_of_add, num_of_sub, num_of_mul, num_of_div, operator):

#     if num_of_add<0 or num_of_add<0 or num_of_add<0 or num_of_add<0:
#         return

#     a = dfs(idx+1, value, num_of_add-1, num_of_sub, num_of_mul, num_of_div, '+')
#     b = dfs(idx+1, value, num_of_add, num_of_sub-1, num_of_mul, num_of_div, '-')
#     c = dfs(idx+1, value, num_of_add, num_of_sub, num_of_mul-1, num_of_div, '*')
#     d = dfs(idx+1, value, num_of_add, num_of_sub, num_of_mul, num_of_div-1, '/')

#     value = eval(f"{value}{operator}{A_[idx]}")


#     if idx == N-1:
#         return value

from copy import deepcopy
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
A_ = [*map(int, input().split())]
operators = [*map(int, input().split())]
answer = [-sys.maxsize, sys.maxsize]

def dfs(operand, used, index):
    if index == N:
        if operand > answer[0]:
            answer[0] = operand
        if operand < answer[1]:
            answer[1] = operand
        return

    for i in range(4):
        if used[i] < operators[i]:
            tmp_used = deepcopy(used)
            tmp_used[i] += 1

            if i == 0:
                dfs(operand + A_[index], tmp_used, index+1)
            elif i == 1:
                dfs(operand - A_[index], tmp_used, index+1)
            elif i == 2:
                dfs(operand * A_[index], tmp_used, index+1)
            else:
                num = abs(operand) // A_[index]
                if operand < 0:
                    num *= -1
                dfs(num, tmp_used, index+1)
dfs(A_[0], [0,0,0,0], 1)
print(answer[0])
print(answer[1])