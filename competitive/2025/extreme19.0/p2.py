#The Twin Occurrence Quest

# a simple parser for python. use get_number() and get_word() to read
def parser():
    while True:
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

import numpy
import scipy
import bisect

N = get_number()
Q = get_number()

A = [get_number() for _ in range(N)]

for _ in range(Q):
    x = get_number()
    l = bisect.bisect_left(A, x)
    if l == N or A[l] != x:
        print("-1 -1")
    else:
        r = bisect.bisect_right(A, x) 
        print(l + 1, r)