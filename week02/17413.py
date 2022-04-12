# 20
S = input()
ans = ''
stack = []
is_tag = False
for s in S:
    if s.isalpha() or s.isnumeric():
        if is_tag:
            ans += s
        else:
            stack.append(s)
    elif s == '<' or s == '>':
        while stack and not is_tag:
            ans += stack.pop()
        ans += s
        is_tag = False if is_tag else True
    else:
        while stack and not is_tag:
            ans += stack.pop()
        ans += s
while stack:
    ans += stack.pop()
print(ans)
