N = int(input())

A = list(map(int, input().split()))
A.sort()
s = sum(A)
min = abs(s - A[0])

for i in range(N):
    n_sum = s - A[i]
    if abs(n_sum) < min:
        min = abs(n_sum)

print(min)

