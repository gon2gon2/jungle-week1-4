# 확실히 문제 퀄리티가 좋아서 풀이도 좋은 풀이가 있었다.
# 누가 볼 일은 없겠지만 링크를 아래에 적어둡니다.
# https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%ED%83%80%EA%B2%9F%EB%84%98%EB%B2%84-BFSDFS




def solution(numbers, target):
    answer = 0

    # 방법 1: BFS
    from collections import deque
    n = len(numbers)
    q = deque()

    q.append((numbers[0], 0))
    q.append((-1 * numbers[0], 0))

    while q:

        num, idx = q.popleft()
        idx += 1

        if idx < n:
            q.append((num + numbers[idx], idx))
            q.append((num - numbers[idx], idx))

        else:
            if num == target:
                answer += 1

    # 방법 2: stack DFS
    answer = 0
    stack = [[numbers[0],0], [-1 * numbers[0],0]]
    n = len(numbers)

    while stack:
        num, idx = stack.pop()

        idx += 1
        if idx < n:
            stack.append([num + numbers[idx], idx])
            stack.append([num - numbers[idx], idx])
        else:
            if num == target:
                answer += 1
    
    # 방법 3: 재귀함수 DFS
    answer = 0

    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1 
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    
    dfs(0,0)
    return answer



tc_1 = [[1,1,1,1,1], 3,5]
tc_2 = [[4,1,2,1],4,2]

for a,b,c in [tc_1, tc_2]:
    print(c == solution(a,b))
