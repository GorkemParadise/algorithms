# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
import scipy

N = get_number()
M = get_number()
grid = [list(get_word().strip()) for _ in range(N)]

nm = N * M
parent = list(range(nm))
size = [1]*nm

def idxy(i,j): return i*M + j

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a,b):
    ra = find(a); rb = find(b)
    if ra == rb: return
    if size[ra] < size[rb]:
        ra,rb = rb,ra
    parent[rb] = ra
    size[ra] += size[rb]

for i in range(N):
    j = 0
    while j < M:
        if grid[i][j] == '.':
            j += 1
            continue
        # start segment
        l = j
        while j < M and grid[i][j] != '.':
            j += 1
        r = j-1
        # pair symmetric
        a=l; b=r
        while a < b:
            union(idxy(i,a), idxy(i,b))
            a += 1; b -= 1

for j in range(M):
    i = 0
    while i < N:
        if grid[i][j] == '.':
            i += 1
            continue
        l = i
        while i < N and grid[i][j] != '.':
            i += 1
        r = i-1
        a=l; b=r
        while a < b:
            union(idxy(a,j), idxy(b,j))
            a += 1; b -= 1

comp_pos = {}
for i in range(N):
    for j in range(M):
        if grid[i][j] == '.': continue
        idx = idxy(i,j)
        root = find(idx)
        comp_pos.setdefault(root, []).append((i,j,int(grid[i][j])))

for root, lst in comp_pos.items():
    vals = sorted(x[2] for x in lst)
    median = vals[(len(vals)-1)//2]  # lower median
    ch = str(median)
    for (i,j,_) in lst:
        grid[i][j] = ch

for i in range(N):
    print(''.join(grid[i]))