from itertools import permutations
import sys
import math

mx = 0
mn = math.inf
input = sys.stdin.readline


N = int(input())
An = list(map(int, input().split()))

a,s,m,d = map(int, input().split())
# operators = list(
#       '+' * a 
#     + '-' * s 
#     + '*' * m 
#     + '/' * d
#     )

operators = []
for o,n in zip (['+','-','*','/'],[a,s,m,d]):
    for _ in range(n):
        operators.append(o)

def operate(front,operater,back):
    if operater == '+':
        return front + back
    elif operater == '-':
        return front - back
    elif operater == '*':
        return front * back
    elif operater == '/':
        # return int(front/back)

        if front < 0:
           return -(-front//back)
        else:
           return front//back


for p in permutations(operators):
    value = An[0]

    for o,a in zip(p,An[1:]):
        if o == '+':
            value = value + a
        elif o == '-':
            value = value - a
        elif o == '*':
            value = value * a
        elif o == '/':
            value = -(-value//a) if value < 0 else value//a


    if value > mx:
        mx = value
    if value < mn:
        mn = value

print(mx)
print(mn)

    

# print(operate(3,'+',3) == 6)
# print(operate(3,'-',3) == 0)
# print(operate(3,'*',3) == 9)
# print(operate(3,'/',3) == 1)

# print(operate(-3,'/',2) == -1)
# print(operate(-5,'/',6) == 0)
# print(operate(-4,'/',2) == -2)


