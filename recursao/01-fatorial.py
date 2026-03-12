def recursive_factorial(n):
    if n <= 1:
        return 1
    return n * recursive_factorial(n - 1)


print(recursive_factorial(5))


def iterative_factorial(n):
    if n <= 1:
        return 1
    for i in range(n - 1, 1, -1):
        n = n * i
    return n


print(iterative_factorial(5))
