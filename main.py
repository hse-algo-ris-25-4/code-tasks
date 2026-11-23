def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Итеративное вычисление определителя трёхдиагональной матрицы.

    :param matrix: квадратная целочисленная трёхдиагональная матрица
        порядка не меньше 1 с постоянными значениями на каждой
        из трёх диагоналей
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    n = len(matrix)

    if n == 0:
        raise Exception("Пустая матрица")

    for row in matrix:
        if len(row) != n:
            raise Exception("Неквадратная матрица")

    a = matrix[0][0]
    b = matrix[0][1] if n > 1 else 0
    c = matrix[1][0] if n > 1 else 0

    for i in range(n):
        for j in range(n):
            if i == j:
                x = a
            elif j == i + 1:
                x = b
            elif i == j + 1:
                x = c
            else:
                x = 0

            if matrix[i][j] != x:
                raise Exception("Неверная матрица")

    d0 = 1
    d1 = a

    for i in range(2, n + 1):
        d0, d1 = d1, a * d1 - b * c * d0

    return d1

def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
