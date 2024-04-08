from solution import is_upper_triangled_matrix
from solution import BadMatrix

m1 = [[1, 0, 0, 2], [0, 2, 3, 4], [0, 0, 6, 4], [0, 0, 0, 1]]
m2 = [[1, 0, 0, 2], [0, 2, 3, 4], [0, 0, "hola", 4], [0, 0, 0, 1]]
m3 = [[1, 0, 0, 2], [1, 2, 3, 4], [0, 0, 5, 4], [0, 0, 0, 1]]
m4 = [[1, 0, 0, 2], [1, 2, 3, 4], [0, 5, 4], [0, 0, 0, 1]]

if __name__ == "__main__":
    for m in [m1, m2, m3, m4]:
        print(f"=== Analizando Matriz ===")
        print(str(m))
        try:
            print(is_upper_triangled_matrix(m))
        except BadMatrix as err:
            print("Error en matriz", err)
        finally:
            print()