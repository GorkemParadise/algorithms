k = int(input()) # 6
divs = set()
extra = []
son = []

m = k

for i in range(2, k+1):
    if k % i == 0:
        divs.add(i)
divs = sorted(divs) # 2 3 6

kat = int(k / divs[0])

while kat > 1:
    for num in divs:
        if num*kat < k:
            extra.append(num*kat)
    kat -= 1

my_list = sorted(divs + extra)
new_list = []

while k > 1:
    for la in my_list:
        if la % k == 0 and la/k > 1:
            new_list.append(int(la/k))
    k -= 1

new_list = sorted(set(new_list))
last_list = new_list + my_list
last_list = sorted(set(last_list))

kat2 = int(m / last_list[0])

while kat2 > 1:
    for numm in last_list:
        if numm*kat2 < m:
            son.append(numm*kat2)
    kat2 -= 1

lala = sorted(set(last_list + son))
print(*lala) 



"""k = int(input())

divs = [i for i in range(1, k+1) if k % i == 0]

extra = {d * m for d in divs for m in range(1, k // d + 1) if d * m <= k}

result = sorted(extra)
print(*result)"""