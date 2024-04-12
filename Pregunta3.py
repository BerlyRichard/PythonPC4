import os
import requests
import zipfile

url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

directory = './downloads_pregunta3'
if not os.path.exists(directory):
    os.makedirs(directory)

filename = os.path.join(directory, 'imagen.jpg')

try:
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)
    print("Imagen descargada exitosamente:", filename)

    # creando un archivo zipeado
    zip_filename = os.path.join(directory, 'imagen_zip.zip')
    with zipfile.ZipFile(zip_filename, 'w') as zip_ref:
        zip_ref.write(filename, os.path.basename(filename))

    print("zipeada exitosamente:", zip_filename)

    # Extracción de archivos
    unzip_directory = os.path.join(directory, 'unzip')
    if not os.path.exists(unzip_directory):
        os.makedirs(unzip_directory)

    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall(path=unzip_directory)

    print("Ddescomprimido exitosamente en:", unzip_directory)

except Exception as e:
    print("Ocurrió un error:", e)