## [l, r] arasındaki sayılara bakıcaz. eğer sayının asal çarpanlarının hepsi en az 2 basamaklı ise o sayı güzel sayıdır
## 2 basamaklı tüm asal sayılar güzel sayıya örnektir.


l, r = map(int, input().split())

def solve(n):
    p = [2, 3, 5, 7]

    total = n

    birlesim = ( n // 2 + n // 3 + n // 5 + n // 7 ) - ( n // 6 + n // 10 + n // 14 + n // 15 + n // 21 + n // 35 ) + ( n // 30 + n // 42 + n // 70 + n // 105 ) - ( n // 210 )

    return total - birlesim

print(solve(r) - solve(l - 1))