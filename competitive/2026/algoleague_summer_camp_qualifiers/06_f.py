n = int(input())
prob = []

for _ in range(n):
    s, f = map(int, input().split())
    prob.append((f, s))

prob.sort()

counter = 0
last = -1

for final, start in prob:
    if start >= last:
        counter += 1
        last = final

print(counter)
