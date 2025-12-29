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
import heapq
import sys

T = get_number()
for _ in range(T):
    N = get_number()
    M = get_number()
    adj = [[] for _ in range(N)]
    for _ in range(M):
        u = get_number()-1
        v = get_number()-1
        W = get_number()
        R = get_number()
        adj[u].append((v, W, R))
        adj[v].append((u, W, R))
        
    INF = 10**18
    dist = [(INF, INF)] * N 
    dist[0] = (0, 0)
    pq = [(0, 0, 0)]

    while pq:
        maxR_so_far, totalT_so_far, u = heapq.heappop(pq)
        if (maxR_so_far, totalT_so_far) > dist[u]:
            continue
        for v, W, R in adj[u]:
            new_maxR = max(maxR_so_far, R)
            new_totalT = totalT_so_far + W
            if (new_maxR, new_totalT) < dist[v]:
                dist[v] = (new_maxR, new_totalT)
                heapq.heappush(pq, (new_maxR, new_totalT, v))

    if dist[N-1][0] == INF:
        print(-1)
    else:
        print(dist[N-1][0], dist[N-1][1])
