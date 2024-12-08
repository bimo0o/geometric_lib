def is_valid_triangle(a, b, c):
    return (a + b > c) and (b + c > a) and (a + c > b)


def area(a, b, c):
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        raise TypeError("All sides must be numbers")
    if any(x <= 0 for x in (a, b, c)):
        raise ValueError("Sides must be positive")
    if not is_valid_triangle(a, b, c):
        raise ValueError("Invalid triangle sides")
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def perimeter(a, b, c):
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        raise TypeError("All sides must be numbers")
    if any(x <= 0 for x in (a, b, c)):
        raise ValueError("Sides must be positive")
    if not is_valid_triangle(a, b, c):
        raise ValueError("Invalid triangle sides")
    return a + b + c
