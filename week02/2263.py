# l은 div_idx 왼쪽으로 얼마나 갈지
# r은 div_idx 오른쪼그로 얼마나 갈지

import sys
input = sys.stdin.readline

def divide_and_conquer(sub_block):
    if len(sub_block) == 1:
        return sub_block[0]

    if len(sub_block)%2 == 1:
        sub_block = [0] + sub_block


    div_idx = len(sub_block)//2

    left_block = sub_block[:div_idx]
    right_block = sub_block[div_idx:]

    block_cnt = 2
    temp_h = min(sub_block[div_idx], sub_block[div_idx-1])
    temp_area = temp_h * block_cnt

    left_idx, right_idx = 0, 0

    for _ in range(len(sub_block) - 2):
        if div_idx -1 -left_idx == 0:
            right_idx += 1

        elif div_idx + right_idx == len(sub_block)-1:
            left_idx += 1

        else:
            if sub_block[div_idx -2 -left_idx] >= sub_block[div_idx + right_idx + 1]:
                left_idx+=1
            else:
                right_idx+=1
        temp_h = min(temp_h, sub_block[div_idx -1 -left_idx], sub_block[div_idx + right_idx])
        block_cnt += 1
        temp_area = max(temp_area, temp_h*block_cnt)
    best_block = temp_area

    return max(best_block, divide_and_conquer(left_block), divide_and_conquer(right_block))

while True:
    N, *blocks = list(map(int, input().split()))
    if N == 0:
        break
    max_area = divide_and_conquer(blocks)
    print(max_area)