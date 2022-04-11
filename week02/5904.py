# 메모리 초과 ㅜ
# N = int(input())
# n = 1
# length = 3
# while N > length:
#     length = length*2 + n + 3
#     n +=1



# def moo_game(k):
#     if k == 0:
#         return "moo"
#     temp = moo_game(k-1)
#     return temp + "m" + "o"*(k+2) + temp

# print(moo_game(n)[N-1])
############################# 인터넷에서 찾은 풀이 #############################
N = int(input())


'''
k번째 moo수열은 (k-1의 수열) + (k+3개) + (k-1의 수열)로 이루어져 있다.

k-1의 길이를 구하는 법은 전체 문자열에서 (k+3)을 뺀 뒤 2로 나눠주는 것.

prev보다 짧다는 건 왼쪽에 있다는 것이고 prev+cur보다 크다는 건 오른쪽에 있다는 것이고 가운데면 k+3의 안에 있으므로 첫번째만 아니면 o를 return해주면 됨.

첫번째면 cur-prev-1에서 0이 나오므로 m return


'''

def moo(acc, cur, N):
    prev = (acc-cur)//2

    if N <= prev: 
        return moo(prev, cur-1, N)
    elif N > prev+cur: 
        return moo(prev, cur-1, N-prev-cur)
    else: 
        return "o" if N-prev-1 else "m"

acc, n = 3, 0
while N > acc:
    n += 1
    acc = acc*2+n+3

print(moo(acc, n+3, N))

# 출처: https://tesseractjh.tistory.com/101