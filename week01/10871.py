N, X = map(int, input().split())
A = input().split()

answer = [a for a in A if int(a) < X]

print(" ".join(answer))