n = int(input())

left = 1
right = n
count = 0

while left <= right:
    if left * right <= n:
        count += right - left + 1
        left += 1
    else:
        right -= 1
print(count)