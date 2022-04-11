# 56분 걸려서 얼추 짰으나 최종 구현 실패
# 왼쪽 안내사항 보면서 침착하게 했으면 됐을 거 같은데 아쉽다.
import sys
sys.setrecursionlimit(10000)
def split_u_v(p):
    n = len(p)
    if n == 2:
        return 2
    
    for i in range(2,n,2):
        if p[:i].count('(') == i//2:
            return i
    return n

def is_right(p):
    stack = []
    for s in p:
        if s == "(":
            stack.append("(")
        else:
            if not stack:
                return False
            x = stack.pop()
            if x != "(":
                return False
    return True if not stack else False

def solution(p):
    '''
    개수는 항상 같다. 짝만 맞추면 된다.
    '''
    answer = ''
    if p == '':
        return p
    if is_right(p):
        return p
    
    
    idx = split_u_v(p)
    u,v = p[:idx], p[idx:]
    
    if is_right(u):
        return u + solution(v)
    else:
        # 4-1
        answer += "("
        answer += solution(v)
        answer += ')'
        
        # 4-2    
        return answer + u[1:-1].replace("(","[").replace(')',"(").replace("[",')')