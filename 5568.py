# from itertools import permutations
# n = int(input())
# k = int(input())

# cards = [int(input())for _ in range(n)]
# cards = {''.join(map(str,i)) for i in permutations(cards,k)}
# print(len(cards))


# 재귀로 풀기

# 1. 후보군과, k를 넘겨준다
# 2. 안에서 카드 한장을 뽑고 k-1을 넘겨준다
from typing import List


n = int(input())
k = int(input())
cards = [int(input()) for _ in range(n)]

nums = []
def make_number(cards: List, k:int, word:str) -> str:
    # k-1, 현재 단어, 남은 카드를 넘겨준다
    if k == 0:
        nums.append(word)
        return

    for n in cards:
        temp_card = list(cards).copy()
        # 여기서 쓸 카드를 빼고 나머지 카드로 집합 생성 후 넣어준다.
        temp_card.remove(n)
        make_number(temp_card, k-1, str(n)+word)


make_number(cards, k, '')
# print(set(nums))
print(len(set(nums)))




    # for card in permutations(cards, k-1):
    #     # card: 후보카드들
    #     # print("permutation", card)
    #     # for n in set(cards).difference(set(c)):
    #     # # set처리를 해서 중복된 숫자를 뽑는 경우가 사라짐 -> 차집합 대신 하나씩 remove
    #     temp_card = list(card).copy()
    #     # print('temp_card')
    #     for n in card:
    #         make_number(temp_card.remove(n), k-1, str(n)+word)