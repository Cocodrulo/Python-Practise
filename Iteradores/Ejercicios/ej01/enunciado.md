## Ejericio 1

Se debe crear una clase iterable que admita como parámetro una lista que contiene diferentes valores. La clase debe devolver en las iteraciones únicamente los valores de tipo `string` no vacías. Además, estas strings deben estar con la primera letra en mayúscula y se debe filtrar aquellos datos que aun siendo cadenas de caracteres, sus valores realmente representen otro tipo de dato. Los posibles tipos en formato string son int, float o None. EJ:

```python
for x in StringsPrinter(["2", 2, True, 9, "hola", "Adiós", 9.26, "4.74", "javier", "Sara", None]):
    print(f"Valor: {x}")
```

Output:
    Valor: Hola
    Valor: Adiós
    Valor: Javier
    Valor: Sara
