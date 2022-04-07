'''
1~49 중 K를 뽑고, 그 안에서 여섯개를 고른다
재귀는 됐는데 정렬에서 실패


pop만 하고 append를 하지 않아서 가지수를 줄임
한번 나온 애는 안 나오게
'''

def get_number(numbers, depth, my_number):
    if depth == 6:
        # 다 골랐으면
        print(*my_number)
        return

    temp = numbers[:]
    for _ in numbers:
        x = temp.pop(0)
        get_number(temp, depth+1, my_number + [x])


while True:      
    k_numbers = list(map(int,input().split()))
    if k_numbers[0] == 0:
        break
    number_list = sorted(k_numbers[1:])
    get_number(number_list, 0, [])
    print()
