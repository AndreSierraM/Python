import numpy as np
import math


# Programa 1
def __ProgramaFor__(n):  # definimos la funcion que recibe el numero de elementos que queremos imprimir de la serie de fibonacci
    a = np.ones((n))  # creamos un arreglo de unos de longitud n
    for i in range(2, n):  # corremos el ciclo for desde el elemento 2 hasta el elemento n
        # definimos la serie de fibonacci con el elemento a[i] que es igual a la suma del elemento anterior y el elemento anterior al anterior
        a[i] = a[i-1]+a[i-2]
    print(a)  # imprimimos el arreglo
    return  # regresamos el arreglo

 # Programa 2
def __ProgramaIf__(a):  # Definimos la funcion que recibe el valor de a
    b = a**2  # Elevar a a la 2
    if b == 0:  # Si b es igual a 0
        print("Es 0")  # Imprimir Es 0
    else:  # Si no
        print("Es Distinto a 0")  # Imprimir Es Distinto a 0


# Programa 3
def __ProgramaCondicional__(a):  # Definimos la funcion con un parametro
    if a == 0 or a == 90 or a == 180 or a == 270 or a == 360:  # Condicion para que el numero este en los ejes
        print("Esta en el eje")
    elif a > 0 and a < 90:  # Condicion para que el numero este en el primer cuadrante
        print("Esta en el primer cuadrante")
    elif a > 90 and a < 180:  # Condicion para que el numero este en el segundo cuadrante
        print("Esta en el segundo cuadrante")
    elif a > 180 and a < 270:  # Condicion para que el numero este en el tercer cuadrante
        print("Esta en el tercer cuadrante")
    elif a > 270 and a < 360:  # Condicion para que el numero este en el cuarto cuadrante
        print("Esta en el cuarto cuadrante")
    else:  # Si no esta en ningun cuadrante
        print("No esta en ningun cuadrante")
    return  # Regresamos el valor


# programa 4
def __ProgramaWhile__(a, b):
    while (a*b > 0):  # ejecuta el bucle siempre que la multiplicación entre a y b sea mayor que cero
        Na = math.sin(a)  # asigna el valor del seno de a a la variable Na
        Nb = math.sin(b)  # asigna el valor del seno de b a la variable Nb
        a = Na-0.5  # asigna el valor de resta entre el seno de a y 0,5 a la variable a
        b = Nb-0.5  # asigna el valor de resta entre el seno de b y 0,5 a la variable b
        print(a*b, ' Na= ', Na)  # imprime los valores de a*b, Na y Nb
    print(a*b, ' Nb= ', Nb)  # imprime los valores de a*b, Na y Nb
    return


# Programa 5
def __ProgramaSeleccionMenu__():  # Definicion de la funcion

    print("--------  CALCULADORA  --------")  # Imprimir texto
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")


def __suma__(a, b):
    return a+b


def __resta__(a, b):
    return a-b


def __multiplicacion__(a, b):
    return a*b


def __switch__(case, a, b):
    # Definimos un diccionario con las opciones a elegir
    sw = {
        1: __suma__(a, b),
        2: __resta__(a, b),
        3: __multiplicacion__(a, b)

    }

    # Retornamos el valor correspondiente a la opcion elegida
    return sw.get(case, "Opcion no valida")


# Programa 6
def __Factorial__(n):
    # Realice una función para hallar el factorial de un número utilizando un ciclo for, se debe
    # enviar el parámetro n y debe entregar n! con:
    # 𝑛! = 𝑛 ∗ (𝑛 − 1) ∗ (𝑛 − 2) ∗ … ∗ 2 ∗ 1

    # Definimos la variable factorial, la cual almacenará el resultado del factorial
    factorial = 1
    # Iniciamos ciclo for, el cual se repetirá n veces, donde n es el número enviado como parámetro
    for i in range(1, n+1):
        # En cada iteración, multiplicamos el valor de la variable factorial por el valor de i
        factorial = factorial*i
    # Imprimimos el resultado del factorial
    print("El factorial de ", n, " es: ", factorial)
    # Retornamos el valor de la variable factorial
    return factorial

#programa 7
def __exponencial__(x, error):
    __Factorial__(x)  # Calcula el factorial de x
    e = 1  # Inicializa e
    i = 1  # Inicializa i
    while (error < e):  # Mientras el error sea menor que el valor de e
        e = e + (x**i)/__Factorial__(i)  # Calcula el valor de e
        i = i + 1  # Incrementa i
    print("El valor de e^x es: ", e)
    return


def __main__():
    print("""
        LABORAORIO 1
    1. Programa con For 
    2. Programa con If
    3. Programa con condicionales Anidados
    4. Programa con While
    5. Programa con selección
    6. Programa con Adicional 1 
    7. Programa con Adicional 2
    """)
    return


if __name__ == "__main__":
    __main__()

    op = int(input("Elige una opción: "))

    if op == 1:
        print("Programa con For(Sucesion de Fibonacci)")
        n = int(input("Hasta donde quiere ver la serie: "))
        __ProgramaFor__(n)

    elif op == 2:
        print("Programa con If")
        a = int(input("ingrese el valor de a: "))
        __ProgramaIf__(a)
    elif op == 3:
        print("Programa con condicionales Anidados")
        a = int(input("Ingrese el valor del angulo: "))
        __ProgramaCondicional__(a)

    elif op == 4:
        print("Programa con While")
        a = int(input("primer numero es a= "))
        b = int(input("segundo numero es b= "))
        __ProgramaWhile__(a, b)

    elif op == 5:
        print("Programa con selección")
        __ProgramaSeleccionMenu__()
        a = int(input("ingrese el valor de a: "))
        b = int(input("ingrese el valor de b: "))
        case = int(input("Ingrese la opcion: "))
        print(__switch__(case, a, b))
    elif op == 6:
        print("""
        Realice una función para hallar el factorial de un número utilizando un ciclo for, se debe
        enviar el parámetro n y debe entregar n! con:
        𝑛! = 𝑛 ∗ (𝑛 − 1) ∗ (𝑛 − 2) ∗ … ∗ 2 ∗ 1
        """)
        n = int(input("Ingrese el valor de n: "))
        __Factorial__(n)

    elif op == 7:
        print(""" 
        Utilice la función del factorial y la siguiente serie para calcular la exponencial. Se debe
        enviar a la función el parámetro x y la precisión deseada como error total. Debe utilizarse
        un ciclo while hasta encontrar la precisión solicitada. La función debe devolver el cálculo
        realizado y el número de iteraciones que le tomó llegar a la precisión.
        Error total = (Valor Verdadero ) –- (Valor aproximado)
        """)
        x = int(input("Ingrese el valor de x: "))
        error = int(input("Ingrese el valor del error: "))
        __exponencial__(x, error)

    else:
        print("Opcion no valida")



#Autor: Andres Sierra
#Desierrandre
