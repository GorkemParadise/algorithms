def asal_carpanlar(n):
    carpanlar = set()
    i = 2

    while i * i <= n:
        if n % i == 0:
            carpanlar.add(i)
            while n % i == 0:
                n //= i
        i += 1 if i == 2 else 2

    if n > 1:
        carpanlar.add(n)
        
    return carpanlar

a, b = map(int, input().split())
d = abs(b - a)

if d <= 1:
    print(-1)
else:
    ans = d
    for p in asal_carpanlar(d):
        k = (-a) % p
        if k < ans:
            ans = k
    print(ans)
