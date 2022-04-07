
T = int(input())
for _ in range(T):
    R, S = input().split()
    print(''.join(map(lambda x: x*int(R), S)))