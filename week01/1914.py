# '''
# N-1 -> middle로 옮김
# N을 target으로 옮김
# N-1을 middle어

# 횟수는 수식으로 구한다

# 1 -> 1
# 2 -> 3
# 3 -> 7
# 4 -> 15
# 5 -> 31
# '''


# n = int(input())
# def hanoi(current,middle,target,block):
#     if block == 1:
#         print(f"{current} {target}")
#         return 

#     hanoi(current,target,middle,block-1)
#     print(f"{current} {target}")
#     hanoi(middle,current,target,block-1)



# print(2**n -1)
# if (n <= 20):
#     # 20 이하인 경우에만 보여주면 되는 거였다
#     # 조건을 잘 읽자
#     hanoi(1,2,3,n)






n = int(input())

def hanoi(_from, _via, _to, n):
    if n == 1:
        print(f"{_from} {_to}")
        return

    # n-1개를 보조기둥으로 옮김
    hanoi(_from, _to,_via,n-1)
    print(f"{_from} {_to}")
    hanoi(_via,_from,_to, n-1)

print(2**n - 1)
if n <= 20:
    hanoi(1,2,3,n)




















