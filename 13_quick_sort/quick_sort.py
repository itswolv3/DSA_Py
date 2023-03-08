def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

def pivot(array, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index + 1, end_index + 1):
        if array[i] < array[pivot_index]:
            swap_index += 1
            swap(array, swap_index, i)
    swap(array, pivot_index, swap_index)
    return swap_index

def quick_sort_helper(array, left, right):
    if left < right:
        pivot_index = pivot(array, left, right)
        quick_sort_helper(array, left, pivot_index - 1)
        quick_sort_helper(array, pivot_index + 1, right)
    return array

def quick_sort(array):
    return quick_sort_helper(array, 0, len(array)-1)
