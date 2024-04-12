def guardar_tabla_multiplicar():
    while True:
        try:
            numero = int(input("Introduce un número entero entre 1 y 10: "))
            if numero < 1 or numero > 10:
                print("El número debe estar entre 1 y 10. Inténtalo de nuevo.")
                continue
            else:
                break
        except ValueError:
            print("Por favor, introduce un número entero válido.")

    nombre_fichero = f"tabla-{numero}.txt"

    with open(nombre_fichero, 'w') as archivo:
        for i in range(1, 13):
            resultado = numero * i
            archivo.write(f"{numero} x {i} = {resultado}\n")

    print(f"La tabla de multiplicar del número {numero} ha sido guardada en el archivo '{nombre_fichero}'.")


def mostrar_tabla_multiplicar():
    try:
        numero = int(input("Introduce un número entero entre 1 y 10: "))
        nombre_fichero = f"tabla-{numero}.txt"
        with open(nombre_fichero, 'r') as archivo:
            data = archivo.read()
            print(data)
    except FileNotFoundError:
        print("El archivo no existe.")


def mostrar_linea_tabla():
    try:
        n = int(input("Introduce el primer número entero entre 1 y 10: "))
        m = int(input("Introduce el segundo número entero entre 1 y 10: "))
        nombre_fichero = f"tabla-{n}.txt"
        with open(nombre_fichero, 'r') as archivo:
            lineas = archivo.readlines()
            if m <= len(lineas):
                print(lineas[m - 1])
            else:
                print(f"La línea {m} no existe en el archivo.")
    except FileNotFoundError:
        print("El archivo no existe.")


def menu():
    while True:
        print("\nMENU:")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de tabla de multiplicar")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            guardar_tabla_multiplicar()
        elif opcion == '2':
            mostrar_tabla_multiplicar()
        elif opcion == '3':
            mostrar_linea_tabla()
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    menu()