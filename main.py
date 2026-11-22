def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Рекурсивное вычисление определителя трёхдиагональной матрицы разложением.
    :param matrix: квадратная целочисленная трёхдиагональная матрица
        порядка не меньше 1 с постоянными значениями на каждой
        из трёх диагоналей
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """

    def determinant(order: int, a: int, b: int, c: int) -> int:
        if order == 0:
            return 1
        if order == 1:
            return a


        return (a * determinant(order - 1, a, b, c) - b * c * determinant(order - 2, a, b, c))

    rows = len(matrix)
    if not all([len(column) == rows for column in matrix]):
        raise ValueError("Матрица не квадратная")
    a = matrix[0][0]
    b = matrix[0][1] if rows > 1 else 0
    c = matrix[1][0] if rows > 1 else 0

    test = 1

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if j == i:
                chek = a
            elif j == i + 1:
                chek = b
            elif j == i - 1:
                chek = c
            else:
                chek = 0
            if value != chek:
                raise ValueError("Не трёхдиагональная")

    return determinant(rows, a, b, c)


def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
