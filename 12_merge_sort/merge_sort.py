def merge(arr1, arr2):
    combined = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            combined.append(arr1[i])
            i += 1
        else:  
            combined.append(arr2[j])
            j += 1
    while i < len(arr1):
        combined.append(arr1[i])
        i += 1
    while j < len(arr2):
        combined.append(arr2[j])
        j += 1
    return combined

def merge_sort(array):
    # Check list is lenght of one.
    if len(array) == 1:
        return array
    mid_index = int(len(array) // 2)
    # Recursion for list splitting.
    left = merge_sort(array[:mid_index])
    right = merge_sort(array[mid_index:])

    return merge(left, right)
