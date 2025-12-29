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

def modinv(a, p):
    return pow(a, p - 2, p)

def point_add(a, b, p, x1, y1, x2, y2):
    if x1 == x2 and (y1 + y2) % p == 0:
        return "POINT_AT_INFINITY"

    if x1 == x2 and y1 == y2:
        num = (3 * x1 * x1 + a) % p
        den = modinv(2 * y1 % p, p)
        lam = (num * den) % p
    else:
        num = (y2 - y1) % p
        den = modinv((x2 - x1) % p, p)
        lam = (num * den) % p

    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return f"{x3} {y3}"

# main
T = get_number()
for _ in range(T):
    a = get_number()
    b = get_number()
    p = get_number()
    x1 = get_number()
    y1 = get_number()
    x2 = get_number()
    y2 = get_number()

    result = point_add(a, b, p, x1, y1, x2, y2)
    print(result)