import sys

N = int(input().strip())
x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())
x3,y3 = map(int, input().split())
x4,y4 = map(int, input().split())
x5,y5 = map(int, input().split())
x6,y6 = map(int, input().split())

def power(x1,y1,x2,y2,x3,y3):
    return (x2 + x3 - 2*x1) + (y2 + y3 - 2*y1)

p1 = power(x1,y1,x2,y2,x3,y3)
p2 = power(x4,y4,x5,y5,x6,y6)

if N == 1:
    print(p1)
    sys.exit(0)
if N == 2:
    print(p2)
    sys.exit(0)

K = (x2 + y2 + x3 + y3) - 2*(x1 + y1)

pw2 = p1
pw1 = p2
pw = None

for i in range(3, N+1):
    pw = 2*pw1 + 2*pw2 + K
    pw2, pw1 = pw1, pw

print(pw)

