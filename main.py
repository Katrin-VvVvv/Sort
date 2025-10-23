import time
import random

def bubble_sort(array):
    l = len(array)
    compare = 0
    permutation = 0

    for i in range(l - 1):
        for j in range(l - 1 - i):
            compare += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                permutation += 1
    return array, compare, permutation

def selection_sort(array):
    l = len(array)
    compare = 0
    permutation = 0

    for i in range(l):
        min_idx = i
        for j in range(i + 1, l):
            compare += 1
            if array[j] < array[min_idx]:
                min_idx = j
        if min_idx != i:
            array[i], array[min_idx] = array[min_idx], array[i]
            permutation += 1
    return array, compare, permutation

def insertion_sort(array):
    l = len(array)
    compare = 0
    permutation = 0

    for i in range(1, l):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            compare += 1
            array[j + 1] = array[j]
            j -= 1
            permutation += 1
        if j >= 0:
            compare += 1
        array[j + 1] = key
    return array, compare, permutation

def main():
    size = 50

    ascend = list(range(size))
    descend = list(range(size - 1, -1, -1))
    random_list = random.sample(range(size * 2), size)

    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort)
    ]

    test = [
        ("По возрастанию: ", ascend),
        ("По убыванию: ", descend),
        ("случайный: ", random_list)
    ]

    for description, array in test:
        start_time = time.time()
        sorted_array, comps, perms = bubble_sort(array.copy())
        end_time = time.time()
        print(f"{description:<15} {'Bubble':<15} {comps:<12} {perms:<12} {end_time - start_time:.6f}")

        start_time = time.time()
        sorted_array, comps, perms = selection_sort(array.copy())
        end_time = time.time()
        print(f"{description:<15} {'Selection':<15} {comps:<12} {perms:<12} {end_time - start_time:.6f}")

        start_time = time.time()
        sorted_array, comps, perms = insertion_sort(array.copy())
        end_time = time.time()
        print(f"{description:<15} {'Insertion':<15} {comps:<12} {perms:<12} {end_time - start_time:.6f}")

if __name__ == "__main__":
    main()
