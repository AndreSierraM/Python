def menu():
    print("Bienvenido al programa de gestión de tareas")
    print("1. Ver tareas pendientes")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = int(input("Ingrese la opción deseada: "))
    return opcion

tareas = []  # lista de tareas pendientes

while True:
    opcion = menu()

    if opcion == 1:
        if len(tareas) == 0:
            print("No hay tareas pendientes")
        else:
            print("Tareas pendientes:")
            for i, tarea in enumerate(tareas, start=1):
                print(i, ".", tarea)
    elif opcion == 2:
        tarea = input("Ingrese la tarea que desea agregar: ")
        tareas.append(tarea)
        print("Tarea agregada exitosamente")
    elif opcion == 3:
        if len(tareas) == 0:
            print("No hay tareas pendientes")
        else:
            tarea_eliminar = int(input("Ingrese el número de la tarea que desea eliminar: "))
            if tarea_eliminar < 1 or tarea_eliminar > len(tareas):
                print("Número de tarea inválido")
            else:
                tareas.pop(tarea_eliminar - 1)
                print("Tarea eliminada exitosamente")
    elif opcion == 4:
        print("Gracias por utilizar nuestro programa de gestión de tareas")
        break
    else:
        print("Opción inválida. Por favor intente nuevamente.")
