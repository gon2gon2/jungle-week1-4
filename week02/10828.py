class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)
    
    def pop(self):
        if not self.data:
            print(-1)
        else:
            x = self.data.pop()
            print(x)

    def size(self):
        print(len(self.data))

    def empty(self):
        if self.data:
            print(0)
        else:
            print(1)

    def top(self):
        if not self.data:
            print(-1)
        else:
            print(self.data[-1])


import sys
input = sys.stdin.readline
stack = Stack()
N = int(input())

for _ in range(N):
    cmd = input().split()
    if cmd[0] == "push":
        stack.push(cmd[1])
    elif cmd[0] == "pop":
        stack.pop()

    elif cmd[0] == "size":
        stack.size()

    elif cmd[0] == "empty":
        stack.empty()

    elif cmd[0] == "top":
        stack.top()
