from random import randrange
from typing import List, Callable
import math


def make_a_list(n: int, limit: int):
    return [randrange(limit+1) for el in range(0, n)]


def search_higher(arr: List[int], limit_val: int) -> List[int]:
    arr_sorted = sorted(arr)
    left = 0
    right = len(arr_sorted) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr_sorted[mid] <= limit_val:
            left = mid + 1
        else:
            right = mid - 1
    return arr_sorted[left:]


def count_higher(arr: List[int], limit_val: int, min_count: int) -> bool:
    return len(search_higher(arr, limit_val)) >= min_count


def find_x(p, q):
    if p >= q:  # q is at least p+1
        return None
    maximum = int(math.pow(q, 1/3))  # q ** (1/3)

    candidates = list(range(1, maximum+1))
    left = 0
    right = len(candidates)-1
    while left <= right:
        mid = (left+right) // 2
        x = candidates[mid]
        res = x ** 3 + p * x
        if res < q:
            left = mid + 1
        elif res > q:
            right = mid - 1
        else:
            return x
    return None


def generate_q_knowing_x(p, x):
    return x ** 3 + p * x


def find_x_game():
    z = int(input("count: "))
    for _ in range(z):
        p = int(input("p: "))
        q = int(input("q: "))
        p = 1012 if p > 1012 else p
        q = 1038 if q > 1038 else q
        res = find_x(p, q)
        print(res if res else "NIE")


if __name__ == "__main__":
    find_x_game()
