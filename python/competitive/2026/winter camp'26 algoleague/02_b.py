# x, y = map(int, input().split())
# k = y - x + 1
# b = 0
# while k > 1:
#    k = (k + 1) // 2
#     b += 1
# print(b)


X, Y = map(int, input().split())

N = Y - X + 1
print(N.bit_length())