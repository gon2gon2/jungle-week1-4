stack = []

pipes = list(input().replace('()','l'))
ans = 0
for i in range(len(pipes)):
    if pipes[i] == '(':
        stack.append('(')

    elif pipes[i] == "l":
        ans += len(stack)
    else:
        ans += 1
        stack.pop()
        
print(ans)