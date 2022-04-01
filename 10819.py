from itertools import permutations

N = int(input())
numbers = list(map(int, input().split()))

ans = 0
for p in permutations(numbers):
    hap = 0

    for i in range(N-1):
        hap += abs(p[i] - p[i+1])

    if ans < hap:
        ans = hap
print(ans)