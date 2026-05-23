# xs'den xf'e min enerji
# yurume: 2 enerji/birim, otobus: 1 enerji/birim (sadece duraktan duraga)
# optimal: xs'e en yakin duraga yuru, otobus, xf'e en yakin durakta in

def ara(durak, x):
    s = 0
    f = len(durak)
    while s < f:
        mid = (s + f) // 2
        if durak[mid] < x:
            s = mid + 1
        else:
            f = mid
    return s

N, Q = map(int, input().split())
distances = list(map(int, input().split()))

durak = [0]
for d in distances:
    durak.append(durak[-1] + d)

for _ in range(Q):
    xs, xf = map(int, input().split())

    ans = 2 * abs(xf - xs)

    # xs ve xf'e en yakin 2ser durak
    yyy = ara(durak, xs)
    cs = []
    if yyy < N:
        cs.append(yyy)
    if yyy > 0:
        cs.append(yyy - 1)

    zzz = ara(durak, xf)
    cf = []
    if zzz < N:
        cf.append(zzz)
    if zzz > 0:
        cf.append(zzz - 1)

    for i in cs:
        for j in cf:
            cost = 2 * abs(xs - durak[i]) + abs(durak[i] - durak[j]) + 2 * abs(xf - durak[j])
            if cost < ans:
                ans = cost

    print(ans)
