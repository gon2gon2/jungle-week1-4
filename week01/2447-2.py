N = int(input())

def counting_star(n, star_in):
    star_out = []

    if n//3 == 1:
        return star_in

    for s in star_in:
        star_out.append(3*s)

    for s in star_in:
        star_out.append(s + " "*len(star_in) + s)

    for s in star_in:
        star_out.append(3*s)

    return counting_star(n//3, star_out)


first_star = ["***","* *","***"]
stars = counting_star(N,first_star)
for i in stars:
    print(i)