from __future__ import annotations
from random import paretovariate
from typing import Any

class Node:
    def __init__(self, k:any,v:any,l:Node=None,r:Node=None) -> None:
        self.k = k
        self.v = v
        self.l = l
        self.r = r

    def __str__(self) -> str:
        return f"키: {self.k}, 값:{self.v}, 왼쪽: {self.l}, 오른쪽 {self.r}"

class BinaryTree:

    def __init__(self, root:Node=None):
        self.root = None


    def search(self, key:Any) -> Any:
        '''임의의 key인 노드를 검색'''
        # 구현 소요시간: 5분 40초
        # cur = self.root
        # while cur:
        #     if cur.k == key:
        #         return cur
        #     elif cur.k < key:
        #         cur = cur.r

        #     elif cur.k > key:
        #         cur = cur.l

        # return "not found"
        current_node = self.root
        while True:
            if current_node == None:
                return "None"

            elif current_node.k == key:
                return current_node.v
                
            elif current_node.k < key:
                current_node = current_node.r

            else:
                current_node = current_node.l




    def add(self, key:Any, value:Any) -> bool:
        '''키가 key이고 값이 value인 노드 삽입'''
        ## try
        # 아무데나 넣는 중이고 왼쪽 갔을 떄 꽉차있는 경우를 고려하지 않음
        # 그냥 아무데나 넣으면 되나?
        # node = Node(key, value)
        # current_node = self.root
        # if not current_node:
        #     self.root = node
        #     return node
        # # none이 나올 떄 까지 탐색해서 none이면 거기다 추가
        # # 왔는데 공간이 없으면 돌아가는 로직이 없다.
        # while current_node:
        #     if current_node.l == None:
        #         current_node.l = node
        #         return node
        #     elif current_node.r == None:
        #         current_node.r = node
        #         return node
        #     else:
        #         # none이 나올 떄 까지 가는 로직
        #         if node.k < current_node.k: # 넣으려는 애가 왼쪽으로 가야 되면
        #             current_node = current_node.l
        #         else:
        #             current_node = current_node.r
        #         continue
        def add_node(node:Node, key:Any, value:Any) -> None:
            '''재귀적으로 빈 공간을 찾아가며 추가'''
            if node.k == key:
                return False
            elif node.k > key:
                if node.l == None:
                    node.left = Node(key, value)
                else:
                    add_node(node.l, key, value)
            elif node.k < key:
                if node.r == None:
                    node.right = Node(key, value)
                else:
                    add_node(node.r, key, value)
            return True

        if self.root == None:
            self.root = Node(key, value)
            return True
        else:
            return add_node(self.root, key, value)

    def remove(self, key:Any) -> bool:
        '''키가 key인 노드 삭제'''
        p = self.root
        parent = None
        is_left_child = True

        ############################################################################
        # 삭제할 key를 검색, p=찾은 노드, parent=p의부모
        while True:
            if p is None: # 검색 실패
                return False

            if key == p.key: # 검색 성공 = p에 값이 삭제하려는 노드가 저장되어 있음
                break
            else:
                parent = p
                if key < p.key:
                    is_left_child = True
                    p = p.left
                else:
                    is_left_child = False
                    p = p.right
        ############################################################################
        # 왼쪽에 자식이 없으면 -> 자식이 하나인 case 수행

        if p.left is None:
            if p is self.root:
                self.root = p.root
            elif is_left_child:
                parent.left = p.righ
            else:
                parent.right = p.right
        ############################################################################
        # 오른쪽에 자식이 없으면 -> 자식이 하나인 case 수행
        elif p.right in None:
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else:
                parent.right = p.left
        ############################################################################
        # 자식 노드가 2개인 노드를 삭제하는 case 수행
        # 
        else:
            parent = p      # 찾은 노드의 왼쪽 서브트리에서 가장 큰 값을 찾는다.
            left = p.left
            is_left_child = True
            while left.right is not None:
                parent = left
                left = left.right
                is_left_child = False

            p.key = left.key
            p.value = left.value
            if is_left_child:
                parent.left = left.left
            else:
                parent.right = left.right


        


    def dump(self):
        '''덤프(모든 노드를 키의 오름차순으로 출력)'''
        pass

    def min_key(self):
        '''최소 키 반환'''
        pass


    def max_key(self):
        '''최대 키 반환'''
        pass


# tree = BinaryTree()
# tree.add(1,10)
# tree.add(2,10)
# tree.add(3,10)
# tree.add(4,10)
# tree.add(5,10)
# tree.add(6,10)
# tree.add(7,10)