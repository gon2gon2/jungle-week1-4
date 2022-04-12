# 총 소요시간 43분
# 큐 문제들은 원래 이렇게 더럽나
import sys
input = sys.stdin.readline

A, B, N = map(int,input().split())

blue = []
red = []
b_t = 0
r_t = 0


def calc_order(t, m, time_per_present, somone_time):
    if somone_time > t:
        t = somone_time
    return m*time_per_present+t, [t+i*time_per_present for i in range(m)]

preprocessing = lambda x: x if x in ["B", "R"] else int(x)
for _ in range(N):
    t, c, m = map(preprocessing, input().split())

    if c == "B":
        end_time, presents = calc_order(t, m, A, b_t)
        b_t = end_time
        blue += presents
    else:
        end_time, presents = calc_order(t, m, B, r_t)
        r_t = end_time
        red += presents

ans_1 = len(blue)
ans_2 = []
ans_3 = len(red)
ans_4 = []

for i in range(1, ans_1+ans_3+1):
    if not red and blue:
        ans_2.append(i)
        blue.pop(0)

    elif not blue and red:
        ans_4.append(i)
        red.pop(0)
    
    elif blue[0] <= red[0]:
        ans_2.append(i)
        blue.pop(0)
    else:
        ans_4.append(i)
        red.pop(0)
print(ans_1)
print(*ans_2)
print(ans_3)
print(*ans_4)