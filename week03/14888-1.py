import sys
from copy import deepcopy
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
A_ = [*map(int, input().split())]
operators = [*map(int, input().split())]
ans = [1e9, -1e9]
def dfs(idx, value, used_oper ):

    if idx == N:
        if value < ans[0] :
            ans[0] = value
        if value > ans[1]:
            ans[1] = value

        return 
        

    for i in range(4):
        if operators[i] > used_oper[i]:
            temp = deepcopy(used_oper)
            temp[i] += 1
            if i == 0:
                dfs(idx+1, value+A_[idx],temp)

            elif i == 1:
                dfs(idx+1, value-A_[idx],temp)

            elif i == 2:
                dfs(idx+1, value*A_[idx],temp)

            elif i == 3:
                temp_value = abs(value) // A_[idx]
                if value < 0:
                    temp_value *= -1
                dfs(idx+1,temp_value,temp)

dfs(1,A_[0],[0,0,0,0])
print(ans[1])
print(ans[0])
