def contador_lineas(archivo):
    try:
        with open(archivo, 'r') as file:
            lineas = file.readlines()
            lineas_limpias = [linea.strip() for linea in lineas if linea.strip() and not linea.strip().startswith('#')]
            return len(lineas_limpias)
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return None


def main():
    ruta_archivo = input("Introduce la ruta del archivo .py: ")
    if ruta_archivo.endswith('.py'):
        num_lineas = contador_lineas(ruta_archivo)
        if num_lineas is not None:
            print(f"Número de líneas de código en {ruta_archivo}: {num_lineas}")
    else:
        print("La ruta no corresponde a un archivo .py.")


if __name__ == "__main__":
    main()