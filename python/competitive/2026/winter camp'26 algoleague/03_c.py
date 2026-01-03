t = int(input())
for _ in range(t):
    a, b, x, y = map(int, input().split())
    max_area = max(x * b, (a - x - 1) * b, y * a, (b - y - 1) * a)
    print(max_area)