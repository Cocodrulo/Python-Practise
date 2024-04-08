from solucion import Solution
from template import StringsPrinter

if __name__ == "__main__":
    test = []
    test.append(["2", 2, True, 9, "hola", "Adiós", 9.26, "4.74", "javier", "Sara", None])
    test.append(["2", 2, True, 9, "chao", "Cuandp", 9.26, "4.74", "None", "", None])
    results = []

    for i, x in enumerate(test):
        print("============================")
        print(f"Realizando test {i}")
        print("============================")
        print(x)
        print()
        res = []
        index = 0
        try:
            for s in Solution(x):
                res.append(s)
            for s in StringsPrinter(x):
                print(s)
                results.append(s == res[index])
                index += 1
        except Exception as excp:
            print(excp)
            results.append(False)

    print()
    resultados = results.count(True)
    print(f"Resultados: {resultados}/{len(results)}")
    print(f"Nota: {resultados*10/len(results)}")