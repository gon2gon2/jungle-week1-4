# 시작: 18:12
# 종료: 19:22
# 평가: 풀다 잠들어서 오래 걸렸다. -로 split했기 때문에 뒤에 나오는 애들은 빼기만 하면 된다
import sys

input = sys.stdin.readline

opers = input().strip().split('-')

get_sum = lambda x: sum(map(int, x.split('+')))
ans = get_sum(opers[0])
if len(opers) > 1:
    for i in range(1, len(opers)):
        ans -= get_sum(opers[i])


print(ans)

