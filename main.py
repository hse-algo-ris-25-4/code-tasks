def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Рекурсивное вычисление определителя трёхдиагональной матрицы разложением.

    :param matrix: квадратная целочисленная трёхдиагональная матрица
        порядка не меньше 1 с постоянными значениями на каждой
        из трёх диагоналей
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    # Матрица не нон и не пустая
    if matrix is None or len(matrix) == 0:
        raise Exception("Матрица не должна быть пустой")
    # Матрица квадратная
    for i in range(0, len(matrix)):
        if len(matrix) != len(matrix[i]):
            raise Exception("Матрица должна быть квадратной")
    # Элементы за пределами трех диагоналей равны 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if abs(i - j) > 1:
                if matrix[i][j] != 0:
                    raise Exception("Матрица не трехдиагональная")
    # Элементы в трех диагоналях одинаковые
    for i in range(0, len(matrix)):
        if matrix[0][0] != matrix[i][i]:
            raise Exception("Матрица не трехдиагональная")
    for i in range(0, len(matrix) - 1):
        if matrix[0][1] != matrix[i][i + 1]:
            raise Exception("Матрица не трехдиагональная")
    for i in range(1, len(matrix)):
        if matrix[1][0] != matrix[i][i - 1]:
            raise Exception("Матрица не трехдиагональная")

    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]

    def determination(n):
        if n == 0:
            return 1
        if n == 1:
            return a
        else:
            return a * determination(n - 1) - b * c * determination(n - 2)

    return determination(n)


def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
