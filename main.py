def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель разложением по строке.

    :param matrix: квадратная целочисленная матрица порядка не меньше 1
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise ValueError("Матрица должна быть непустым списком списков.")

    n = len(matrix)
    for row in matrix:
        if not isinstance(row, list) or len(row) != n:
            raise ValueError("Матрица должна быть квадратной.")
        for element in row:
            if type(element) is not int:
                raise ValueError("Все элементы матрицы должны быть целыми числами.")

    def get_minor(sub_matrix: list[list[int]], row_idx: int, col_idx: int) -> int:
        """Вычисляет минор элемента, вычеркивая строку row_idx и столбец col_idx."""
        minor_matrix = []
        for k in range(len(sub_matrix)):
            if k == row_idx:
                continue
            r = []
            for j in range(len(sub_matrix)):
                if j != col_idx:
                    r.append(sub_matrix[k][j])
            minor_matrix.append(r)
        return det_recursive(minor_matrix)

    def get_cofactor(sub_matrix: list[list[int]], row_idx: int, col_idx: int) -> int:
        """Вычисляет алгебраическое дополнение элемента."""
        return ((-1) ** (row_idx + col_idx)) * get_minor(sub_matrix, row_idx, col_idx)

    def det_recursive(sub_matrix: list[list[int]]) -> int:
        size = len(sub_matrix)
        if size == 1:
            return sub_matrix[0][0]
        if size == 2:
            return sub_matrix[0][0] * sub_matrix[1][1] - sub_matrix[0][1] * sub_matrix[1][0]

        determinant = 0
        for i in range(size):
            determinant += sub_matrix[0][i] * get_cofactor(sub_matrix, 0, i)
        return determinant

    return det_recursive(matrix)


def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
# ананас