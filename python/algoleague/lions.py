def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))

for _ in range(Q):
    L, R = map(int, input().split())

    left_index = lower_bound(A, L)
    right_index = upper_bound(A, R)

    print(right_index - left_index)