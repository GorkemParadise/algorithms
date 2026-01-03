n = int(input())
a = list(map(int, input().split()))

c = 0

curr_sum = a[0] + a[1] + a[2]

if curr_sum < 0:
    add = -curr_sum
    c += add
    a[2] += add
    curr_sum = 0

for i in range(3, n):
    curr_sum = curr_sum - a[i - 3] + a[i]

    if curr_sum < 0:
        add = -curr_sum
        c += add
        a[i] += add
        curr_sum = 0

print(c)