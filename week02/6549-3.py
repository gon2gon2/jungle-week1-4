def dnc(sub_blocks):
    
    length = len(sub_blocks)

    if len(sub_blocks) == 1:
        return sub_blocks[0]

    # if length % 2 == 1:
    #     sub_blocks = [0] + sub

    div_idx = length//2
    left_blocks = sub_blocks[:div_idx]
    right_blocks = sub_blocks[div_idx:]

    # 하나씩 추가하면서 최대의 넓이를 찾는 기능
    # 하나짜리는 div하면서 되니까 2개로 시작
    block_cnt = 2
    temp_h = min(sub_blocks[div_idx], sub_blocks[div_idx-1])
    temp_area = temp_h * block_cnt

    # 이제 왼쪽 오른쪽 탐색 ㄱ
    go_left, go_right = 0,0
    for _ in range(length-2):
        if div_idx-1-go_left-1 == -1:
            go_right += 1
        elif div_idx+go_right+1 == length:
            go_left += 1
        
        else:
            if sub_blocks[div_idx-1-go_left-1] >= sub_blocks[div_idx+go_right+1]:
                go_left += 1
            else:
                go_right += 1
        cand_1 = sub_blocks[div_idx-1-go_left]
        cand_2 = sub_blocks[div_idx+go_right]
        temp_h = min(temp_h, cand_1, cand_2)
        block_cnt += 1
        temp_area = max(temp_h*block_cnt, temp_area)

    return max(dnc(left_blocks), dnc(right_blocks),temp_area)


while True:
    N, *blocks = list(map(int, input().split()))
    if N == 0:
        break
    max_value = dnc(blocks)
    print(max_value)
