"""
N-1개를 메인에서 보조로 옮긴다.
N을 타겟으로 옮긴다.
N-1을 보조에서 타겟으로 옮긴다.
"""
N = int(input())
def hanoi(x,y, n):

    if n == 1:
        print(f"{x} {y}")
        return

    hanoi(x, 6-x-y, n-1)
    print(f"{x} {y}")
    hanoi(6-x-y, y, n-1)
print(2**N -1)
hanoi(1,3,N)
