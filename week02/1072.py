X,Y = map(int,input().split())

def get_rate(x,y):
    '''
    x: 전체 게임 수
    y: 이긴 게임 수
    '''
    return y*100//x


# 문제의 이해도 부족
# 승률이 변하려면 올라야 하고 99나 100이면 더이상 올릴 수 없으므로 -1

start,end = 1, X
orig = get_rate(X,Y)
if orig >= 99:
    print(-1)
else:
    games = X

    while start <= end:
        mid = (start+end) // 2

        now = get_rate(X+mid,Y+mid)

        if now > orig:
            end = mid-1
            if games > mid:
                games = mid
        else:
            start = mid+1
    print(games)