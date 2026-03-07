## İlk input raf sayısı : 5
## İkinci input raflardaki kitap sayıları: 3 7 2 5 4
## Üçüncü input kaç kitabın yerini merak ediyoruz: 6
## Kalan inputlar ise kitapların yerini gösteriyor: 
## Örneğin 3. kitapın yerini merak ediyoruz: 1. raf 3. kitap yani output: 1 3
## Örneğin 12. kitabın yerini merak ediyoruz: 3. raf 2. kitap yani output: 3 2
## Örneğin 21. kitabın yerini merak ediyoruz: 5. raf 4. kitap yani output: 5 4

import bisect

raf = int(input())
books = list(map(int, input().split()))
q = int(input())

kitaplar = []
sum = 0

for i in books:
    sum += i
    kitaplar.append(sum)

for j in range(q):
    
    k = int(input())
    raf_index = bisect.bisect_left(kitaplar, k)

    if raf_index == 0:
        print(1, k)
    else:
        print(raf_index + 1, k - kitaplar[raf_index - 1])