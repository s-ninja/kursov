a = []
b = []
d = []*18
for k in range (18):
    a.append(list(map(int,input().split())))
for _ in range(18):
    b.append(list(map(int, input().split())))
for i in range (18):
    for j in range (18):
        a[i][j]=(a[i][j]+b[i][j])
for q in a:
    print(*q , sum(q))

