
N, M = map(int, input().split())
A = list(map(int, input().split()))

pos = {0}

for x in A:
    new = set()
    for s in pos:
        new.add(s ^ x)
    pos = pos | new

if M in pos:
    print("yes")
else:
    print("no")
