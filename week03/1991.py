# 5분, 전에 푼 기억이 있어서 쉬웠다.
tree = dict()
N = int(input())
for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]


def preorder(idx):
    if idx=='.':
        return
    print(idx,end='')
    preorder(tree[idx][0])
    preorder(tree[idx][1])

def inorder(idx):
    if idx=='.':
        return
    inorder(tree[idx][0])
    print(idx, end='')
    inorder(tree[idx][1])

def postorder(idx):
    if idx=='.':
        return
    postorder(tree[idx][0])
    postorder(tree[idx][1])
    print(idx,end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')