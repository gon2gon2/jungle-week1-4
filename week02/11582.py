# import sys 
# input = sys.stdin.readline
# N = int(input())
# score_list = [*map(int,input().split())]
# k = int(input())

# print(N)
# print(score_list)
# print(k)




def merge_sort(input_list, n):
    if n == 1:
        return input_list

    length = len(input_list)
    left = input_list[:length//2]
    right = input_list[length//2:]
    temp = []

    for _ in range(length):
        if not left:
            temp += right
            break
        elif not right:
            temp += left
            break

        if left and right:
            if left[0] > right[0]:
                x = right.pop(0)
                temp.append(x)

            else:
                x = left.pop(0)
                temp.append(x)

    return merge_sort(left, n//2) + merge_sort(right, n//2)


N = 8
score_list = [1, 5, 2, 4, 2, 9, 7, 3]
k =  2


print(merge_sort(score_list,k))