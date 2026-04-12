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
import sys

T = get_number()
for _ in range(T):
    n = get_number()
    k = get_number()
    s = get_word()
    s = list(s)
    flips = 0
    for i in range(n - k + 1):
        if s[i] == 'S':
            flips += 1
            for j in range(k):
                s[i+j] = 'H' if s[i+j]=='S' else 'S'
    if all(c=='H' for c in s):
        print(flips)
    else:
        print(-1)