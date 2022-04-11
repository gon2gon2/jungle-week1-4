import sys
input = sys.stdin.readline

N = int(input())
LAYER = [[*map(int,input().split())] for _ in range(N)]


def pooling(input_layer):
    n = len(input_layer)
    if n == 1:
        return input_layer[0][0]

    else:
        base = n//2
        l1 = [l[:base] for l in input_layer[:base]]
        l2 = [l[base:] for l in input_layer[:base]]
        l3 = [l[:base] for l in input_layer[base:]]
        l4 = [l[base:] for l in input_layer[base:]]



        return sorted([pooling(l1),pooling(l2),pooling(l3),pooling(l4)])[2]

print(pooling(LAYER))