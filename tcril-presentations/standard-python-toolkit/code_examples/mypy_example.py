from typing import Iterator

def before_fib(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

def after_fib(n: int) -> Iterator[int]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
