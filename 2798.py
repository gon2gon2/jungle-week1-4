from itertools import combinations


N, M = map(int, input().split())
cards = map(int, input().split())

# optim = 0
# for comb in combinations(cards, 3):
#     x = sum(comb)
#     if x<=M and x > optim:
#         optim = x

# print(optim)

N, M = map(int, input().split())
cards = map(int, input().split())

cards = list(cards)
optim = 0
combs = [(i,j,k) for i in range(len(cards)-2) for j in range(i+1,len(cards)-1) for k in range(j+1,len(cards))]

for (i,j,k) in combs:
    x = cards[i] + cards[j] + cards[k]
    if x == M:
        optim = x
        break

    if x <= M and x > optim:
        optim = x

print(optim)


