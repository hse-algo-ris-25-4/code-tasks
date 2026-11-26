def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель разложением по строке.
    :param matrix: квадратная целочисленная матрица порядка не меньше 1
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise Exception("Матрица должна быть непустым списков")

    n = len(matrix)
    for r in matrix:
        if not isinstance(r, list) or len(r) != n:
            raise Exception("Матрица должна быть квадратной")
        for el in r:
            if type(el) is not int:
                raise Exception("Все элементы матрицы должны быть целыми числами")

    def minor(matrix: list[list[int]], row_id: int, col_id: int) -> int:
        # Вычисляет минор, вычеркивая row_id и col_id
        mn = []
        for k in range(len(matrix)):
            if k == row_id: continue
            r = []
            for j in range(len(matrix)):
                if j != col_id: r.append(matrix[k][j])

            mn.append(r)
        
        return det(mn)

    def calc_alg_dop(matrix: list[list[int]], row_id: int, col_id: int) -> int:
        return ((-1)**(row_id + col_id)) * minor(matrix, row_id, col_id)

    def det(matrix: list[list[int]]) -> int:
        s = len(matrix)
        if s == 1: return matrix[0][0]
        if s == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        determinant = 0
        for i in range(s):
            determinant += matrix[0][i] * calc_alg_dop(matrix, 0, i)

        return determinant

    return det(matrix)


def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
# ананас