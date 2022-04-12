# 18분

import sys
input = sys.stdin.readline

T = int(input())
for t in range(1,T+1):
    N = int(input())
    all_prices = list(map(int,input().split()))
    discount = []
    ans = []
    for _ in range(N*2):
        x = all_prices.pop(0)
        if not discount or discount[0]*4//3 != x:
            discount.append(x)
            continue
        else:
            ans.append(discount.pop(0))
    print(f"Case #{t}:", *ans)