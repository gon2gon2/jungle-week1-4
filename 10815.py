N = int(input())
card_A = set(map(int, input().split()))

M = int(input())
card_B = list(map(int, input().split()))


# card_B에서 한장씩 꺼내 A에 있나 확인
# in 을 쓰면 간단하지만 오래 걸릴 것 같으니 인덱싱을 활용해보장

# is_in_A = [False] * 20000000

# for a in card_A:
#     is_in_A[a+10000000] = True

# for b in card_B:
#     if is_in_A[b+10000000]:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')



for b in card_B:
    if b in card_A:
        print('1', end=' ')
    else:
        print('0', end=' ')