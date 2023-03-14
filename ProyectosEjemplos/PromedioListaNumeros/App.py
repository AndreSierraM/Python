def calcular_promedio(numeros):
    suma = sum(numeros)
    cantidad = len(numeros)
    promedio = suma / cantidad
    return promedio

numeros = [1, 2, 3, 4, 5]
promedio = calcular_promedio(numeros)

print("La lista de números es:", numeros)
print("El promedio de la lista es:", promedio)
