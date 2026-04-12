def merge_sort(arr, counter):
    # tek veya boşsa direkt dön
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], counter)
    right = merge_sort(arr[mid:], counter)
    
    # merge olacak -> say
    counter[0] += 1
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result


# ---- input ----
n = int(input().strip())                                    
arr = list(map(int, input().split()))                       

counter = [0]
sorted_arr = merge_sort(arr, counter)

# ---- output ----
print(*sorted_arr)
print(counter[0])
