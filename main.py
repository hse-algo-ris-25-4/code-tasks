def check_matrix(matrix: list[list[int]]):
    size = len(matrix)
    if size == 0:
        raise Exception("Матрица должна быть квадратной")

    for row in matrix:
        if len(row) != size:
            raise Exception("Матрица должна быть квадратной")

    main_el = matrix[0][0]
    upper_el = matrix[0][1] if size > 1 else 0
    lower_el = matrix[1][0] if size > 1 else 0

    for i in range(size):
        for j in range(size):
            if abs(i - j) > 1 and matrix[i][j] != 0:
                raise Exception("Матрица не трехдиагональная")

            if i == j and matrix[i][j] != main_el:
                raise Exception("Матрица не трехдиагональная")

            if j == i + 1 and matrix[i][j] != upper_el:
                raise Exception("Матрица не трехдиагональная")

            if i == j + 1 and matrix[i][j] != lower_el:
                raise Exception("Матрица не трехдиагональная")


# C901 `get_tridiagonal_determinant` is too complex (13 > 10) при ruff check .
def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Рекурсивное вычисление определителя трёхдиагональной матрицы разложением.
    :param matrix: квадратная целочисленная трёхдиагональная матрица
        порядка не меньше 1 с постоянными значениями на каждой
        из трёх диагоналей
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    size = len(matrix)

    check_matrix(matrix)

    main_el = matrix[0][0]
    upper_el = matrix[0][1] if size > 1 else 0
    lower_el = matrix[1][0] if size > 1 else 0

    def calculate(n):
        if n == 0:
            return 1
        if n == 1:
            return main_el

        return main_el * calculate(n - 1) - upper_el * lower_el * calculate(n - 2)

    return calculate(size)


def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
