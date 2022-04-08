'''
1. 구분선을 긋고 최대의 직사각형을 찾는다
2. 왼쪽 오른쪽에도 똑같이 한다
3. 셋 중 가장 큰 값을 반환한다

'''
import sys  
sys.setrecursionlimit(10**8)

def divide_and_conquer(sub_blocks):
    num_of_blocks = len(sub_blocks)

    if num_of_blocks == 1:
        return sub_blocks[0]

    if num_of_blocks % 2 == 1:
        sub_blocks = [0] + sub_blocks

    div_idx = num_of_blocks//2
    left_block = sub_blocks[:div_idx]
    right_block = sub_blocks[div_idx:]

    cnt = 2
    temp_h = min(sub_blocks[div_idx],sub_blocks[div_idx-1])
    temp_area = temp_h*cnt
    go_left = 0
    go_right = 0
    for _ in range(num_of_blocks-2):
        if div_idx -1 -go_left == 0: # 틀림
            go_right += 1

        elif div_idx + go_right + 1 == num_of_blocks:
            go_left += 1
        
        else:
            if sub_blocks[div_idx-2-go_left] >= sub_blocks[div_idx + go_right + 1]: #등호 빠짐
                go_left += 1
            else:
                go_right += 1

        cnt += 1
        temp_h = min(temp_h,sub_blocks[div_idx-go_left-1],sub_blocks[div_idx+go_right])
        temp_area = max(temp_area, cnt*temp_h)
    Z = temp_area

    return max(divide_and_conquer(left_block), divide_and_conquer(right_block), Z)


while True:
    N, *blocks = list(map(int, input().split()))
    if N == 0:
        break
    max_value = divide_and_conquer(blocks)
    print(max_value)



