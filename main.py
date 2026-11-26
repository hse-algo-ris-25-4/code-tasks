def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель разложением по строке.

    :param matrix: квадратная целочисленная матрица порядка не меньше 1
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    if not isinstance(matrix, list) or not matrix:
        raise Exception("Некорректная матрица")

    n = len(matrix)

    # Проверки на ошиьочную матрицу
    for row in matrix:
        if not isinstance(row, list) or len(row) != n:
            raise Exception("Матрица должна быть квадратной")
        for element in row:
            if type(element) is not int:
                raise Exception("Элементы должны быть целыми числами")

    det = 0

    if n == 1:
        return matrix[0][0]

    for i in range(n):
        minor = []
        for row in matrix[1:]:
            minor.append(row[:i] + row[i + 1 :])

        det += (-1) ** i * matrix[0][i] * calculate_determinant(minor)

    return det


def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
