def menu():
    print("Bienvenido al cajero automático")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")

    opcion = int(input("Ingrese la opción deseada: "))
    return opcion

saldo = 1000  # saldo inicial del usuario

while True:
    opcion = menu()

    if opcion == 1:
        print("Su saldo actual es de $", saldo)
    elif opcion == 2:
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        if cantidad > saldo:
            print("Fondos insuficientes")
        else:
            saldo -= cantidad
            print("Retiraste $", cantidad, " y tu saldo actual es de $", saldo)
    elif opcion == 3:
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        saldo += cantidad
        print("Depositaste $", cantidad, " y tu saldo actual es de $", saldo)
    elif opcion == 4:
        print("Gracias por utilizar nuestro cajero automático")
        break
    else:
        print("Opción inválida. Por favor intente nuevamente.")
