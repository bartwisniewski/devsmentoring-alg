from typing import List
from math import sqrt


def remove_multiplications(arr: List[int], val: int) -> List[int]:
    for el in arr:
        if not el % val and el // val >= 2:
            arr.remove(el)
    return arr


def get_n_primes(n: int) -> List[int]:
    if n <= 1:
        return []
    primes = list(range(3, n+1, 2))  # all odd numbers starting from 3
    for num in primes:
        primes = remove_multiplications(primes, num)
    primes = [2] + primes
    return primes


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if not n % i:
            return False
    return True


if __name__ == "__main__":
    print(get_n_primes(20))
