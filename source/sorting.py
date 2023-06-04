from random import randrange
from typing import List, Callable
import datetime


FILENAME = "results.txt"


def make_a_list(n: int, limit: int):
    return [randrange(limit+1) for el in range(0, n)]


def bubble(arr: List[int]):
    n = len(arr)
    for i in range(1, n):
        for j in range(n-i):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]


def quicksort_partition(array: list, i: int, j: int) -> int:
    pivot = array[(i + j) // 2]
    while i <= j:
        while pivot > array[i]:
            i += 1
        while pivot < array[j]:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    return i


def quicksort_step(array: list, start: int, end: int):
    edge = quicksort_partition(array, i=start, j=end)
    if start < edge - 1:
        quicksort_step(array=array, start=start, end=edge-1)
    if end > edge:
        quicksort_step(array=array, start=edge, end=end)


def quicksort(array: list):
    quicksort_step(array, 0, len(array) - 1)


def insertion_sort(array: list):
    n = len(array)
    for i in range(1, n):
        sel = array[i]
        j = i - 1
        while j >= 0 and sel < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = sel


def measure_sorting(array: list, sort_function: Callable):
    array_copy = list(array)
    start = datetime.datetime.now()
    sort_function(array_copy)
    duration = datetime.datetime.now() - start
    return {sort_function.__name__: duration.microseconds}


def case(length, functions):
    unsorted = make_a_list(length, 1000)
    results = {}
    for function in functions:
        results.update(measure_sorting(unsorted, function))
    return results


def write_results(results: dict):
    with open(FILENAME, 'w') as file:
        for test_case in results.keys():
            file.write(f"array length: {test_case}\n")
            result = [f"{item[0]}: {item[1]}us" for item in results[test_case].items()]
            file.write(", ".join(result))
            file.write("\n")


if __name__ == "__main__":
    LENGTHS = [1000, 10000, 100000]
    FUNCTIONS = [bubble, insertion_sort, quicksort]

    results = {}
    for length in LENGTHS:
        results[length] = case(length, FUNCTIONS)
    write_results(results)
