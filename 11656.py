# i부터 문자열[i:]로 하나씩 생성 후, 이걸 정렬해서 "\n".join(list)로 print

S = input()
names = [S[i:] for i in range(len(S))]
for n in sorted(names):
    print(n)