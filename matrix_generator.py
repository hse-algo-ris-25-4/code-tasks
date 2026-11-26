from collections import namedtuple
import random
import copy


Case = namedtuple("Case", ["matrix", "det"])


def generate_matrix_and_det(order: int) -> Case:
    """Строит квадратную целочисленную матрицу заданного порядка
    с заранее известным определителем.

    Определитель получают из свойств, не вычисляя его разложением
    и не вызывая calculate_determinant.

    :param order: порядок матрицы, целое число не меньше 1
    :raises Exception: если order не является таким числом
    :return: Case с полями matrix и det
    """
    if not isinstance(order, int) or isinstance(order, bool) or order < 1:
        raise Exception("Порядок матрицы должен быть целым числом >= 1")

    diag_values = [-3, -2, -1, 1, 2, 3]
    matrix = []
    for i in range(order):
        row = []
        for j in range(order):
            if j < i:
                row.append(0)
            elif j == i:
                row.append(random.choice(diag_values))
            else:
                row.append(random.randint(-3, 3))
        matrix.append(row)
    
    det = 1
    for i in range(order):
        det *= matrix[i][i]

    for i in range(order):
        for k in range(i + 1, order):
            factor = random.choice([-1, 1])
            for j in range(order):
                matrix[k][j] += factor * matrix[i][j]

    for i in range(order - 1, -1, -1):
        for k in range(i - 1, -1, -1):
            factor = random.choice([-1, 1])
            for j in range(order):
                matrix[k][j] += factor * matrix[i][j]
 
    return Case(matrix, det)



def main():
    n = 3
    print(f"Генерация матрицы порядка {n}")
    result = generate_matrix_and_det(n)
    print("\nОпределитель сгенерированной матрицы равен", result.det)
    print("\n".join(["\t".join([str(cell) for cell in row]) for row in result.matrix]))


if __name__ == "__main__":
    main()