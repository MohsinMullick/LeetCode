# Method 1: Using type checks (Pythonic overloading simulation)
def swap(a, b):
    if isinstance(a, int) and isinstance(b, int):
        print(f"Swapping integers: {a}, {b}")
        return b, a
    elif isinstance(a, str) and isinstance(b, str):
        print(f"Swapping strings: {a}, {b}")
        return b, a
    elif isinstance(a, float) and isinstance(b, float):
        print(f"Swapping floats: {a}, {b}")
        return b, a
    else:
        raise TypeError("Unsupported types for swap")


# Usage:
x, y = swap(3, 7)  # Swapping integers: 3, 7   -> (7, 3)
a, b = swap("hi", "bye")  # Swapping strings          -> ("bye", "hi")
p, q = swap(1.5, 2.5)  # Swapping floats           -> (2.5, 1.5)
