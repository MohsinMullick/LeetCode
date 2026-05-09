from typing import TypeVar, Tuple

T = TypeVar('T')  # T can be any type


def swap(a: T, b: T) -> Tuple[T, T]:
    return b, a


# Same function works for all types:
print(swap(3, 7))  # (7, 3)      — integers
print(swap("hi", "bye"))  # ("bye","hi") — strings
print(swap(1.5, 2.5))  # (2.5, 1.5)  — floats
