import sys
input = sys.stdin.readline


input_string = input().strip()
explode_string = input().strip()
ex_len = len(explode_string)
stack = []


# 문자열을 하나씩 추가한다.
# if 마지막 n개가 폭발문자열이면 그만큼 pop
# 다시 체크

for i in input_string:
    # 하나씩 추가한다
    stack.append(i)
    while len(stack) >= ex_len and "".join(stack[-ex_len:]) == explode_string:
        for _ in range(ex_len):
            stack.pop()
ans = ''.join(stack)
print(ans if ans else "FRULA")