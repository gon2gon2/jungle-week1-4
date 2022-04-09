# import sys
# input = sys.stdin.readline

# class Queue:
#     def __init__(self):
#         self.data = []

#     def __add__(self,x):
#         self.data.append(x)

#     def pop(self,):
#         if self.data:
#             x = self.data.pop(0)
#             print(x)
#         else:
#             print(-1)

#     def size(self,):
#         print(len(self.data))

#     def empty(self):
#         if self.data:
#             print("0")
#         else:
#             print("1")

#     def front(self):
#         if self.data:
#             print(self.data[0])
#         else:
#             print("-1")

#     def back(self):
#         if self.data:
#             print(self.data[-1])
#         else:
#             print("-1")

# q = Queue()

# N = int(input())
# for _ in range(N):
#     cmd = input().split()
#     # print("실행 전:", q.data)
#     if cmd[0] == "push":
#         q+cmd[1]

#     elif cmd[0] == "front":
#         q.front()

#     elif cmd[0] == "back":
#         q.back()

#     elif cmd[0] == "size":
#         q.size()

#     elif cmd[0] == "pop":
#         q.pop()
#     elif cmd[0] == "empty":
#         q.empty()
#     # print("실행 후:", q.data)


from collections import deque
import sys
input = sys.stdin.readline



q = deque()

N = int(input())
for _ in range(N):
    cmd  = input().split()

    if cmd[0] == "push":
        q.append(cmd[1])

    elif cmd[0] == "pop":
        try:
            x = q.popleft()
            print(x)
        except:
            print(-1)

    elif cmd[0] == "size":
        print(len(q))

    elif cmd[0] == "empty":
        if len(q):
            print(0)
        else:
            print(1)

    elif cmd[0] == "front":
        if len(q):
            print(q[0])
        
        else:
            print(-1)

    else:
        if len(q):
            print(q[-1])
        else:
            print(-1)

