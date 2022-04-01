from itertools import combinations

hops = [int(input()) for _ in range(9)]
for c in combinations(hops,7):
    if sum(c) == 100:
        print("\n".join(map(str,sorted(c))))
        break