def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Рекурсивное вычисление определителя трёхдиагональной матрицы разложением.

    :param matrix: квадратная целочисленная трёхдиагональная матрица
        порядка не меньше 1 с постоянными значениями на каждой
        из трёх диагоналей
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    if not matrix:
        raise Exception("Матрица заполнена неверно")
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise Exception("Матрица не квадратная")

    a = matrix[0][0]
    if n > 1:
        b = matrix[0][1]
        c = matrix[1][0]
    else:
        b = c = 0
    check_tridiagonal(matrix, n, a, b, c)
    return count_determ(n, a, b, c)


# проверка трехдиагональности матрицы
def check_tridiagonal(matrix, n, a, b, c):
    for i in range(n):
        for j in range(n):
            element = 0
            if i == j:  # главная диагональ
                element = a
            elif j == i + 1:  # над главной диагональю
                element = b
            elif i == j + 1:  # под главной диагональю
                element = c
            if matrix[i][j] != element:
                raise Exception("Матрица не трехдиагональная")


# расчет определителя
def count_determ(n, a, b, c):
    if n == 1:
        return a
    if n == 2:
        return a * a - b * c
    return a * count_determ(n - 1, a, b, c) - b * c * count_determ(n - 2, a, b, c)


def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
