# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 çıkan 6
# 1 2 4 5 7 8 10 11 13 14 16 17 19 20 çıkan 4
# 1 2 5 7 10 11 14 16 19 20 çıkan 3
# 1 2 7 10 14 19 20 çıkan 2
# 1 2 10 14 20 çıkan 1
# 1 2 14 20 çıkan 1
# 1 2 20 çıkan 1
# 1 2

N, K = map(int, input().split())

count = 1
if K > N:
    print(0)
else:
    while N > K:
        N -= N // K
        count += 1
    print(count)
