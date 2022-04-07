N = int(input())


def counting_star(n, star_now):
    out = []
    if n == N:
        return star_now

    nn = 1+4*n # 2의 경우에는 5
    out.append("*"*nn)
    out.append("*" + " "*(nn-2) +"*")

    for s in star_now:
        out.append("* "+s+" *")

    out.append("*" + " "*(nn-2) +"*")
    out.append("*"*nn)
    

    return counting_star(n+1, out)
    
star = counting_star(1,['*'])
for s in star:
    print(s)