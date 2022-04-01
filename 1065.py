# 두자리수까지도 그냥 등차수열로 봐도 되는거였다 (100미만)
# 그 후엔 값의 범위가 정해져있어 1의자리 10의자리 100의 자리만 보면 됨

def is_hansu(n):
    
    if n < 10:
        return True
    n = str(n)
    gap = int(n[0]) - int(n[1])
    for i in range(1, len(n)-1):
        if int(n[i]) - int(n[i+1]) != gap:
            return False
    return True
        
n = int(input())
print(len([i for i in range(1,n+1,1) if is_hansu(i)]))
