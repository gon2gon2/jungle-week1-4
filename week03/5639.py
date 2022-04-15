# 33분 시도
# input은 참고했는데 인덱스 에러 -< 해결했으나 틀림
import sys
input = sys.stdin.readline

preorder = []
while True:
    try:
        num = int(input())
        preorder.append(num)
    except:
        break

############ 내풀이
# 내가 생각해도 직접 트리를 만들어 낸 다음 거기서 순회하는 건 별로같다
# MAX_SIZE= 10002
# tree = [0] * MAX_SIZE

# def make_tree(idx, array):
#     if not array or idx > MAX_SIZE:
#         return 
#     root = array.pop(0)
#     tree[idx] = root

#     div_idx = 0
#     for i in range(len(array)):
#         if array[i] > root:
#             div_idx = i
#             break

#     left = array[:div_idx]
#     right = array[div_idx:]

#     make_tree(idx*2, left)
#     make_tree(idx*2+1, right)

# make_tree(1,preorder)

# def postorder(idx):
#     if idx > MAX_SIZE or not tree[idx]:
#         return
#     postorder(idx*2)
#     postorder(idx*2+1)
#     print(tree[idx])

# postorder(1)

# 다른 사람풀이
sys.setrecursionlimit(10**9)
def postorder(start, end):
    if start > end:
        return
    mid = end + 1

    for i in range(start+1, end+1):
        if preorder[start] < preorder[i]:
            mid = i
            break

    postorder(start+1, mid-1)
    postorder(mid, end)
    print(preorder[start])

postorder(0, len(preorder)-1)