from solution import Matriz
m = []

m.append([[1, 2, 5, 4], [5, 2, 5, 8], [2, 6, 1, 8], [5, 3, 8, 2]])
m.append([[1, 0, 0, 2], [0, 2, 3, 4], [0, 0, "hola", 4], [0, 0, 0, 1]])
m.append([[1, 0, 0, 2], [1, 2, 3, 4], [0, 0, 5, 4], [0, 0, 0, 1]])
m.append([[1, 0, 0], [1, 2, 3], [0, 5, 4], [0, 0, 0]])
m.append([[1, 0, 0, 2], [1, 2, 3, 4], [0, 0, 5, 4]])

if __name__ == "__main__":
    for matrix in range(len(m)):
        print("\n", f"=== Analizando Matriz {matrix+1} ===", "\n")
        real_m = Matriz(m[matrix])
        print("is_square: ", real_m.is_square())
        print("nrow: ", real_m.nrow())
        print("ncolumn: ", real_m.ncolumn())
        print("get_str: ", real_m.get_str())