# 백준 2753번
'''
year => 1 or 0

4의 배수이지만 100의 배수가 아닐 때 
400의 배수일 때

1. 400의 배수?
2. 4의 배수이지만 100의 !배수 ? 
3. else 0
'''


def answer(year):
    if year%400 == 0:
        return 1

    elif year%4 == 0 and year%100 != 0:
        return 1

    return 0

n = int(input())
print(answer(n))