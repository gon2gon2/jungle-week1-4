N, K = map(int, input().split())
yose = [i for i in range(1, N+1)]
answer = []
cnt = 0
while yose:
    cnt += 1
    x = yose.pop(0)
    if cnt == K:
        cnt = 0
        answer.append(x)
    else:
        yose.append(x)

print("<", end='')
print(*answer, sep=', ',end='')
print(">")