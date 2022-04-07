# N, M = 4, 6
# trees = [15,15,15,15]
N, M = map(int,input().split())
trees = tuple(map(int,input().split()))

bottom, top = 0, max(trees)

# 높이의 최댓값 -> 나무를 최대한 덜
while bottom <= top:
    h = (bottom+top) // 2
    cutted_tree = [t-h for t in trees if t>h] 
    logs = sum(cutted_tree)

    if logs >= M:
        bottom = h + 1

    else:
        top = h - 1

print(top)
