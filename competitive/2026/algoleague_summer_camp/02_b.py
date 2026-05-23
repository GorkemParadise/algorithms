N, M = map(int, input().split())
kenarlar = []

for _ in range(N):
    e1, e2 = map(int, input().split())
    pisagor = int((e1 * e1 + e2 * e2) ** 0.5)
    kenarlar.append(max(e1, e2, pisagor))

kenarlar.sort(reverse=True)

total = 0
for i, edge in enumerate(kenarlar):
    total += edge
    if total >= M:
        print(i + 1)
        break
else:
    print(-1)
