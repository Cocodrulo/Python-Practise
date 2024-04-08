class Matriz:
    def __init__(self, matrix):
        self.matrix = matrix

    def is_square(self):
        lmatrix = self.nrow()
        for row in self.matrix:
            if len(row) != lmatrix:
                return False
        return True

    def nrow(self):
        return len(self.matrix)

    def ncolumn(self):
        max_col = 0
        for row in self.matrix:
            if len(row) > max_col:
                max_col = len(row)
        return max_col

    def get_str(self):
        return "\n".join([str(row) for row in self.matrix])
