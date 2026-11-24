from profilehooks import profile


def fibonacci_rec(n: int) -> int:
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)
    pass


def fibonacci_iter(n: int) -> int:
    lst = list()
    lst.append(0)
    lst.append(1)
    for i in range(1, n):
        lst.append(lst[i - 1] + lst[i])
    return lst[-1]
    pass


def fibonacci(n: int) -> int:
    a = 0
    b = 1
    for i in range(1, n):
        a, b = b, a + b
    return b
    pass


def main():
    n = 35
    print(f"Вычисление {n} числа Фибоначчи рекурсивно:")
    print(fibonacci_rec(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно:")
    print(fibonacci_iter(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно без использования массива:")
    print(fibonacci(n))


if __name__ == "__main__":
    main()