# 6 5 --> 7
# 6 6 --> 8 9
# 6 20 --> 2 3

n, k = list(map(int, input().strip().split()))   # rows - jump

döngü = 2*n - 2
pozisyon = k % döngü
if pozisyon == 0:
    pozisyon = döngü
if pozisyon <= n:
    satır = pozisyon
else:
    satır = n - (pozisyon - n)
    
sayı = 1
if satır % 2 == 1:
    sayı = (satır//2)*3 + 1
    print(sayı)
else:
    sayı1 = (satır//2 - 1)*3 + 2
    sayı2 = sayı1 + 1
    print(sayı1, sayı2)