K, N = map(int, input().strip().split())  #7 5
rounds = input().strip()    #HSHSH

harun = rounds.count('H')
sami = rounds.count('S')

remaining = abs(N-K)

if harun > sami + remaining:
    print("Harun")
elif sami > harun + remaining:
    print("Sami")
else:
    print("Cilek")  #Cilek