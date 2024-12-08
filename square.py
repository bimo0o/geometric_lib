def area(a):
    if not isinstance(a, (int, float)):
        raise TypeError("Side must be a number")
    if a < 0:
        raise ValueError("Side cannot be negative")
    return a * a


def perimeter(a):
    if not isinstance(a, (int, float)):
        raise TypeError("Side must be a number")
    if a < 0:
        raise ValueError("Side cannot be negative")
    return 4 * a
