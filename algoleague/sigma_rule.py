T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    A.sort()
    invited = 0
    i = 0
    
    while i < N:
        if (i == 0 or A[i] - A[i-1] > 1) and (i == N-1 or A[i+1] - A[i] > 1):
            invited += 1
            if i < N-1 and A[i+1] - A[i] == 2:
                i += 1
        i += 1
    
    print(invited)
