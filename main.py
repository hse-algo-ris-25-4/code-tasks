def fibonacci_rec(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


def fibonacci_iter(n: int) -> int:
    fibonacciArr = [1, 1]
    for i in range(n - 2):
        fibonacciArr.append(fibonacciArr[-1] + fibonacciArr[-2])
    return fibonacciArr[-1]


def fibonacci(n: int) -> int:
    first = 1
    second = 1
    for i in range(n - 2):
        temp = first
        first = second
        second = temp + first
    return second


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
