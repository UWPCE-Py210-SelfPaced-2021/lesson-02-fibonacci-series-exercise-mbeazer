def fibonacci(n):
    """returns the nth value in a fibonacci series"""
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """returns the nth value in a lucas series"""
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)


def sum_series(n, n0=0, n1=1):
    """returns the nth value in a sum series"""
    if n == 0:
        return n0
    if n == 1:
        return n1
    return sum_series(n - 1) + sum_series(n - 2)


print(fibonacci(7))
print(lucas(7))
print(sum_series(7, n0=2, n1=1))
