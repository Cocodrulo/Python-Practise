def is_upper_triangled_matrix(matrix):
    if not is_squared(matrix):
        raise BadMatrix("matrix is not square")

    for row_index in range(len(matrix)):
        for el_index in range(len(matrix[row_index])):
            try:
                matrix[row_index][el_index] = int(matrix[row_index][el_index])
            except Exception:
                raise BadMatrix("there is a not integer value in matrix")
        
        if row_index != 0:
            for element in range(row_index):
                if matrix[row_index][element] != 0:
                    return False
    return True


def is_squared(matrix):
    lmatrix = len(matrix)
    for row in matrix:
        if len(row) != lmatrix:
            return False
    return True

class BadMatrix(Exception):
    pass