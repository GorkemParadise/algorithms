N = int(input())
A = list(map(int, input().split()))
A.sort()

danger = 0
for i in range(N // 2):
    danger += A[i] * A[N - 1 - i]

print(danger)