N = int(input())
dots = sorted([tuple(map(int,input().split())) for _ in range(N)], 
key=lambda x:(x[0]-x[1]))

# dots = []
# for _ in range(N):
#     x, r = map(int, input().split())
#     dots.append((x-r,'l',x,r))
#     dots.append((x+r,'r',x,r))
# dots.sort(key=lambda x:x[0])

# for d in dots:
#     print(d)

stack = []

# '''
# 1. 점을 꺼낸다
# 2. stack이 비어있으면 append
# 3. stack[-1]이랑 점 비교해서 범위 안에 있는 애면 append
# 4. 범위 밖이면 pop하면서 


# '''


## 오른쪽 좌표: dot[-1] + dot[-2]
## 왼쪽 좌표: dot[-2] - dot[-1]

ans = 0
# # 뽑았을 때, 
for i in range(N):

    now = dots[i]
    
    connected = []
    while stack:
        top = stack[-1]

        # 만약 안에 있다면 -> push
        if top[-1] + top[-2] >= now[-2] + now[-1]:
            stack.append(now)
            break
        else:
            # l 만날 떄 까지 이어지면 ok
            x = stack.pop()
            ans += 1
            
            # 뽑고나서  마지막인 경우
            if not stack:
                if connected:
                    ans += 1
                if all(connected):
                    ans +=1
                break
            else:
                top = stack[-1]
                # 뽑은 애의 좌좌표가 stack-1의 우좌표랑 일치?
                if x[-2] - x[-1] == top[-1] + top[-2]:
                    connected.append(True)
                else:
                    connected.append(False)
    # if :
    #     # 전부 이어졌다는 뜻, +2 or *2
    #     ans += 2
        
        

    if not stack and i != N-1:
        stack.append(now)

print("stack:", stack)
print("ans:", ans+1)
# 자꾸 스택에 뭐가 남아있다. 다 없어져야 할텐데
