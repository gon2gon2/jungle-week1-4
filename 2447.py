


def counting_star(n:int, stars:list):
    added_stars = []
    if n == 3:
        return stars

    # input 리스트의 원소가 점점 늘어나면서 append가 많아짐
    # 그럼에도 nested가 안 생기는 건 꺼내서 넣기 때문
    for s in stars:
        added_stars.append(s*3)

    for s in stars:
        added_stars.append(s + " " * len(stars) + s)

    for s in stars:
        added_stars.append(s*3)


    return counting_star(n//3, added_stars)

n = int(input())
first = ['***','* *','***']

result = counting_star(n,first)
for i in result:
    print(i)
