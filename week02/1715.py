import heapq
import sys
input = sys.stdin.readline
N = int(input())

cards = [int(input()) for _ in range(N)]
if N == 1:
    print(0)

else:
    ans = 0
    heapq.heapify(cards)
    while len(cards) > 1:
        x = heapq.heappop(cards)
        y = heapq.heappop(cards)
        new_card = x+y
        ans += new_card
        heapq.heappush(cards, new_card)

    print(ans)