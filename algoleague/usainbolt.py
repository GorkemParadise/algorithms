a = int(input().strip())  #rekor sayısı - 5
b = list(map(int, input().split()))  #rekorlar - 3 7 2 6 8 

high = b[0]
high_breaks = 0

for i in range(1, a):
    if b[i] > high:
        high = b[i] # rekor güncelleniyor
        high_breaks += 1

print(high_breaks)  #output - 2