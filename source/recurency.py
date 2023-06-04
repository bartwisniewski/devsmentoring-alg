from typing import List, Dict


def print_recurrent(arr: List[str]) -> None:
    if len(arr) == 0:
        return
    if len(arr) == 1:
        print(arr[0])
        return
    print(arr[0], end=' ')
    print_recurrent(arr[1:])


def is_vowel(x: str) -> bool:
    return x in ('a', 'e', 'i', 'o', 'u')


#  REKURENCJA!!
def count_vowels(text: str) -> Dict:
    freq = {}
    for char in text:
        if is_vowel(char):
            if char in freq.keys():
                freq[char] += 1
            else:
                freq[char] = 1
    return freq


def count_vowels_iter(text: str) -> Dict:
    freq = {}
    for char in text:
        if is_vowel(char):
            if char in freq.keys():
                freq[char] += 1
            else:
                freq[char] = 1
    return freq


def crash_me():
    return crash_me()


def print_numbers(n: int) -> None:
    if n == 0:
        print(n)
        return
    print(n, end=' ')
    print_numbers(n-1)


def nwd(a: int, b: int) -> int:
    if b > a:
        a, b = b, a

    if b == 0:
        return a

    return nwd(b, a % b)


def nww(a: int, b: int) -> int:
    return a * b // nwd(a, b)


def get_a_number(symbol: str):
    a = 0
    while True:
        try:
            a = int(input(f'{symbol}: '))
        except ValueError:
            print("please enter positive integer")
        else:
            if a < 1:
                print("please enter positive integer")
            else:
                break
    return a


def nww_user():
    a = get_a_number('a')
    if not a:
        return
    b = get_a_number('b')
    if not b:
        return
    print(nww(a, b))


if __name__ == "__main__":
    nww_user()
