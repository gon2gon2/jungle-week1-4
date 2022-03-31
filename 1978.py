# 2~N

import math
def check(n):
    if n == 1:
        return False
    elif n == 2:
        return True

    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False

    return True

N = int(input())
nums = filter(check,map(int,input().split()))
print(len(list(nums)))