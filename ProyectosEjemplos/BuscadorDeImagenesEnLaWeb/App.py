import requests
import json
import os
import shutil
from urllib.parse import urlsplit


def buscar_imagenes(query):
    url = "https://api.unsplash.com/search/photos"
    params = {
        "query": query,
        "per_page": 10,
        "client_id": "TU_CLIENT_ID"
    }

    response = requests.get(url, params=params)
    data = json.loads(response.text)

    imagenes = []
    for resultado in data["results"]:
        imagenes.append(resultado["urls"]["regular"])

    return imagenes


def descargar_imagen(imagen_url):
    response = requests.get(imagen_url, stream=True)

    if response.status_code == 200:
        filename = os.path.basename(urlsplit(imagen_url).path)
        with open(filename, 'wb') as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)


query = input("Ingrese una palabra clave para buscar imágenes: ")
imagenes = buscar_imagenes(query)

if len(imagenes) > 0:
    print(f"Se encontraron {len(imagenes)} imágenes:")
    for i, imagen_url in enumerate(imagenes, start=1):
        print(i, imagen_url)

    opcion = input("¿Desea descargar alguna de estas imágenes? (s/n): ")

    if opcion.lower() == "s":
        num_imagen = int(input("Ingrese el número de la imagen que desea descargar: "))
        imagen_url = imagenes[num_imagen - 1]
        descargar_imagen(imagen_url)
        print("Imagen descargada exitosamente")
else:
    print("No se encontraron imágenes para esa palabra clave")
