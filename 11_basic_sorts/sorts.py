def bubble_sort(array):
    for i in range(len(array)-1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

def selection_sort(array):
    for i in range(len(array) -1):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        if i != min_index:   
            temp = array[i]
            array[i] = array[min_index]
            array[min_index] = temp
    return array


def insertion_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while temp < array[j] and j > -1:
            array[j+1] = array[j]
            array[j] = temp
            j -= 1

    return array

