from datetime import datetime


def bubble_sort(array):
    comp = 0
    swaps = 0
    start = datetime.now()
    for i in range(len(array) - 1):
        swapped = False
        for j in range(0, len(array) - i - 1):
            comp += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
                swaps += 1
        if not swapped:
            break
    end = datetime.now()
    time = end - start
    return time, comp, swaps


def shell_sort(array):
    comp = 0
    swaps = 0
    start = datetime.now()
    h = 1
    while h < len(array):
        h = h * 3 + 1
    while h > 1:
        h = (int)(h / 3)
        i = 0
        for i in range(h, len(array)):
            j = i
            comp += 1
            while j >= h and array[j] < array[j - h]:
                array[j - h], array[j] = array[j], array[j - h]
                swaps += 1
                j -= h
                comp += 1
    end = datetime.now()
    time = end - start
    return time, comp, swaps


def selection_sort(array):
    swaps = 0
    comp = 0
    start = datetime.now()
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            comp += 1
            if array[j] < array[min_index]:
                min_index = j
        if i != min_index:
            array[i], array[min_index] = array[min_index], array[i]
            swaps += 1
    end = datetime.now()
    time = end - start
    return time, comp, swaps


def insertion_sort(array):
    swaps = 0
    comp = 0
    start = datetime.now()
    for i in range(1, len(array)):
        j = i
        comp += 1
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
            swaps += 1
            comp += 1
    end = datetime.now()
    time = end - start
    return time, comp, swaps


def quick_sort(array):
    start = datetime.now()
    comp, swaps = quick_sort_sorting(array, 0, len(array))
    end = datetime.now()
    time = end - start
    return time, comp, swaps


def quick_sort_sorting(array, start, end, comp=0, swaps=0):
    if start != end:
        pivot = start + (int)((end - start) / 2)
        value_pivot = array[pivot]
        i = start
        j = end - 1
        while True:
            comp += 1
            while array[i] < value_pivot:
                i += 1
                comp += 1
            comp += 1
            while array[j] > value_pivot:
                j -= 1
                comp += 1
            if i == j:
                pivot = i
                break
            array[i], array[j] = array[j], array[i]
            swaps += 1

        comp, swaps = quick_sort_sorting(array, start, pivot, comp, swaps)
        comp, swaps = quick_sort_sorting(array, pivot + 1, end, comp, swaps)
    return comp, swaps


def merge_sort(array):
    start = datetime.now()
    comp, swaps = merge_sort_sorting(array)
    end = datetime.now()
    time = end - start
    return time, comp, swaps


def merge_sort_sorting(array, comp=0, swaps=0):
    if len(array) > 1:
        middle = (int)(len(array) / 2)
        left_array = array[:middle]
        right_array = array[middle:]

        comp, swaps = merge_sort_sorting(left_array, comp, swaps)
        comp, swaps = merge_sort_sorting(right_array, comp, swaps)

        i = 0
        j = 0
        k = 0

        while i < len(left_array) and j < len(right_array):
            comp += 1
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
                swaps += 1
            else:
                array[k] = right_array[j]
                swaps += 1
                j += 1
            k += 1

        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1
            swaps += 1

        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1
            swaps += 1
    return comp, swaps
