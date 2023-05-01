def mergesort(productos):
    length = len(productos)

    if length == 1:
        return list
    
    mid = length // 2

    left = mergesort(list[:mid])
    right = mergesort(list[mid:])

    return merge(left, right)

def merge(left, right):
    output = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])

    return output