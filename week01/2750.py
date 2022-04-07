N = int(input())

ns = [int(input()) for _ in range(N)]
print("\n".join(map(str,sorted(ns))))