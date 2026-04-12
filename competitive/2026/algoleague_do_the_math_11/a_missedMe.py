q = int(input())
MOD = 10**9 + 7

for i in range(q):
    l, r =  map(int, input().split())
    if l % 2 != 0:
        l += 1
    if r % 2 != 0:
        r -= 1
    
    result = (l + r) * ((r - l) // 2 + 1) // 2
    print(result % MOD)