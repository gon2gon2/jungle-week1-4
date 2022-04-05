# # 리스트의 그거로 표현
# # 
# import string
# word_book = {v:i for i, v in enumerate(string.ascii_uppercase)}
# print(word_book)

# Tree = [0] * 26

# class Tree:
#     def __init__(self):
#         self.data = ["A"] + [0] * 30

#     def insert_data(self, name, left, right):
#         idx = self.data.index(name)
#         self.data[2*idx + 1] = left
#         self.data[2*idx + 2] = right

#     def print_tree(self):
#         print(self.data)

#     # def preorder(self):
#     #     idx = 0

#     #     pass

#     # def inorder(self):
#     #     pass

#     # def postorder(self):
#     #     pass

# tree = Tree()
# N = int(input())
# for _ in range(N):
#     name, left, right = input().split()
#     left = 0 if left == '.' else left
#     right = 0 if right == '.' else right
#     tree.insert_data(name, left, right)

# def go_left(idx):
#     return idx*2 + 1
# def go_right(idx):
#     return idx*2 + 2

# def preorder(data,order):
#     root = data[0]

# tree.print_tree()

tree = dict()
N = int(input())
for _ in range(N):
    parent, left, right = input().split()
    tree[parent] = (left,right)

def preorder(x):
    if x == '.':
        return
    print(x,end='')
    preorder(tree[x][0])
    preorder(tree[x][1])

def inorder(x):
    if x == '.':
        return 
    inorder(tree[x][0])
    print(x,end='')
    inorder(tree[x][1])

def postorder(x):
    if x == '.':
        return
    postorder(tree[x][0])
    postorder(tree[x][1])
    print(x,end='')



preorder('A')
print()
inorder('A')
print()
postorder('A')