# 16분 
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
numbers = []
while True:
    try:
        x = int(input())
        numbers.append(x)
    except:
        break


def postorder(left, right):
    if left > right:
        return

    root = numbers[left]
    for i in range(left+1, right+1):
        if numbers[left] < numbers[i]:
            div_idx = i
            break
    else:
        div_idx = right+1

    postorder(left+1, div_idx-1)
    postorder(div_idx, right)
    print(root)
postorder(0,len(numbers)-1)